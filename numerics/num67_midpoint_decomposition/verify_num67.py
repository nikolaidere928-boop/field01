"""Replay NUM67 from frozen states using only the Python standard library."""
import argparse
import ast
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


REFERENCE_SHA = "c82ecbd78359281a3fdab4f244cae83ebcd6a6266d07854c034c223fb208fad4"
COEFFICIENTS = ((1, 2, 1), (-1, 2, 2), (-1, 5, 2), (2, 5, 3))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()).hexdigest()


def record(value):
    with localcontext() as context:
        context.prec = 40
        decimal = str(Decimal(value.numerator) / Decimal(value.denominator))
    return {"exact": str(value), "decimal": decimal}


def decode(value):
    sign, mantissa, exponent, bits = value
    require(sign in (0, 1), "Invalid MP sign")
    require(int(mantissa).bit_length() == bits, "Invalid MP mantissa")
    return (-1)**sign * Fraction(int(mantissa)) * Fraction(2)**exponent


def load(directory, filename):
    if directory.is_file():
        with ZipFile(directory) as archive:
            member = "Universe_Memory_Working/" + filename
            require(archive.namelist().count(member) == 1, "Missing or duplicate ZIP member")
            require(archive.getinfo(member).file_size <= 180000, "Oversized input JSON")
            raw = archive.read(member)
    else:
        raw = (directory / filename).read_bytes()
    wrapper = json.loads(raw)
    require(digest(wrapper["payload"]) == wrapper["payload_sha256"], filename)
    return raw, wrapper


def verify_coefficient_source(directory, reference_payload):
    source_paths = [path for path in reference_payload["source_hashes"]
                    if path.endswith("__qw_state_extrema_01.py")]
    require(len(source_paths) == 1, "Ambiguous coefficient source hash")
    source_path = source_paths[0]
    if directory.is_file():
        with ZipFile(directory) as archive:
            member = "Universe_Memory_Working/" + source_path
            require(archive.namelist().count(member) == 1,
                    "Missing or duplicate coefficient source")
            raw = archive.read(member)
    else:
        raw = (directory / "qw_state_extrema_01.py").read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    hash_with_final_lf = hashlib.sha256(raw + b"\n").hexdigest()
    require(reference_payload["source_hashes"][source_path]
            in (source_hash, hash_with_final_lf), "Coefficient source hash")
    tree = ast.parse(raw.decode("utf-8"))
    values = [ast.literal_eval(node.value) for node in ast.walk(tree)
              if isinstance(node, ast.Assign)
              and any(isinstance(target, ast.Name)
                      and target.id == "COEFFICIENTS" for target in node.targets)]
    require(values == [COEFFICIENTS], "Coefficient source values")


def raw_rhs(radius, fields, gamma):
    charge, charge_slope, field, field_slope = fields
    return [
        charge_slope,
        -4 * charge_slope / radius + 4 * field * charge
        + 2 * radius**2 * field**2 * charge
        + gamma * (radius**2 * charge**2 - 1) * charge / 2,
        field_slope,
        -4 * field_slope / radius + 3 * field**2 + radius**2 * field**3
        + charge**2 + radius**2 * field * charge**2,
    ]


def rhs(radius, fields, gamma):
    profile = [Fraction(num, den) / (1 + radius)**power
               for num, den, power in COEFFICIENTS]
    slopes = [-Fraction(num * power, den) / (1 + radius)**(power + 1)
              for num, den, power in COEFFICIENTS]
    require(slopes[0] == profile[1] and slopes[2] == profile[3],
            "Kinematic profile identities")
    return [value - star + slope for value, star, slope in zip(
        raw_rhs(radius, fields, gamma), raw_rhs(radius, profile, gamma), slopes
    )]


def calculate(directory):
    reference_raw, wrapper = load(directory, "NUM66_FIRST_CELL_BALANCE_01.json")
    require(wrapper["payload_sha256"] == REFERENCE_SHA, "Wrong NUM66")
    reference_payload = wrapper["payload"]
    verify_coefficient_source(directory, reference_payload)
    reference = reference_payload["result"]
    left = Fraction(reference["left"]["exact"])
    right = Fraction(reference["right"]["exact"])
    width = right - left
    require(width > 0 and left > 0, "Invalid cell")
    radius = (left + right) / 2
    weight = 2 * width / 3
    gamma = Fraction(reference["gamma_exact"])
    inputs = {"NUM66_FIRST_CELL_BALANCE_01.json": {
        "raw_sha256": hashlib.sha256(reference_raw).hexdigest(),
        "payload_sha256": REFERENCE_SHA,
    }}
    cases = []
    midpoints = []
    middle_rhs = []
    for filename, variant, name in (
        ("NUM53_TERMINALS_01.json", "full", "baseline17"),
        ("NUM62_LOCAL_MESH_TERMINALS_01.json", "split9", "split9"),
    ):
        raw, terminal_wrapper = load(directory, filename)
        expected = reference_payload["source_hashes"][filename]
        raw_hash = hashlib.sha256(raw).hexdigest()
        restored_hash = hashlib.sha256(raw + b"\n").hexdigest()
        require(expected in (raw_hash, restored_hash), "Source file hash")
        rows = terminal_wrapper["payload"]["result"]["cases"]
        matches = [row for row in rows if row["variant"] == variant]
        require(len(matches) == 1, "Ambiguous variant")
        row = matches[0]
        saved = next(case for case in reference["cases"] if case["name"] == name)
        state = row["result"]["state"]
        mesh = row["input"]["mesh"]
        require(digest(state) == saved["source_state_sha256"], "State hash")
        require(digest(mesh) == saved["source_mesh_sha256"], "Mesh hash")
        require([Fraction.from_float(float.fromhex(value)) for value in mesh[:2]]
                == [left, right], "Cell endpoints")
        require(state["encoding"] == "mpf-sign-man-exp-bc-v1", "State encoding")
        values = [decode(value) for value in state["values"][:8]]
        left_values, right_values = values[:4], values[4:]
        left_rhs = rhs(left, left_values, gamma)
        right_rhs = rhs(right, right_values, gamma)
        midpoint = [(start + end) / 2 + width * (start_rhs - end_rhs) / 8
                    for start, end, start_rhs, end_rhs in zip(
                        left_values, right_values, left_rhs, right_rhs)]
        midpoint_rhs = rhs(radius, midpoint, gamma)
        parts = {"left": width * left_rhs[3] / 6,
                 "mid": weight * midpoint_rhs[3],
                 "right": width * right_rhs[3] / 6}
        for key, value in parts.items():
            require(value == Fraction(saved["rhs_parts"][key]["exact"]),
                    name + " RHS " + key)
        balance = {"left_value": left_values[3], "right_value": right_values[3],
                   "discrete_rhs": sum(parts.values()),
                   "residual": right_values[3] - left_values[3] - sum(parts.values())}
        for key, value in balance.items():
            require(value == Fraction(saved["balance"][key]["exact"]),
                    name + " balance " + key)
        inputs[filename] = {
            "raw_sha256": raw_hash, "original_sha256": expected,
            "original_matches_after_appending_lf": raw_hash != expected,
            "payload_sha256": terminal_wrapper["payload_sha256"],
            "state_sha256": digest(state), "mesh_sha256": digest(mesh),
            "variant": variant,
        }
        cases.append({"name": name, "midpoint": [record(value) for value in midpoint]})
        midpoints.append(midpoint)
        middle_rhs.append(midpoint_rhs[3])
    baseline, changed = midpoints
    delta_charge = changed[0] - baseline[0]
    delta_field = changed[2] - baseline[2]
    delta_slope = changed[3] - baseline[3]
    delta_charge_squared = changed[0]**2 - baseline[0]**2
    mean_field = (changed[2] + baseline[2]) / 2
    mean_charge_squared = (changed[0]**2 + baseline[0]**2) / 2
    mixed = changed[2] * changed[0]**2 - baseline[2] * baseline[0]**2
    require(mixed == mean_charge_squared * delta_field
            + mean_field * delta_charge_squared, "Symmetric product identity")
    terms = {
        "minus_4_delta_v_over_r": -4 * delta_slope / radius,
        "3_delta_w_squared": 3 * (changed[2]**2 - baseline[2]**2),
        "r_squared_delta_w_cubed": radius**2 * (changed[2]**3 - baseline[2]**3),
        "delta_q_squared": delta_charge_squared,
        "r_squared_delta_w_q_squared": radius**2 * mixed,
    }
    variable_terms = {
        "q": (1 + radius**2 * mean_field) * (changed[0] + baseline[0]) * delta_charge,
        "w": (3 * (changed[2] + baseline[2])
              + radius**2 * (changed[2]**2 + changed[2] * baseline[2] + baseline[2]**2)
              + radius**2 * mean_charge_squared) * delta_field,
        "v": -4 * delta_slope / radius,
    }
    total = sum(terms.values())
    require(total == sum(variable_terms.values()), "Variable decomposition")
    require(total == middle_rhs[1] - middle_rhs[0], "Direct forced RHS difference")
    require(weight * total == Fraction(reference["delta_rhs_parts"]["mid"]["exact"]),
            "NUM66 midpoint contribution")
    return {
        "kind": "NUM67-exact-midpoint-algebra-v1", "date": "2026-09-10",
        "inputs": inputs, "coefficients": COEFFICIENTS,
        "coefficient_provenance": "Transcribed from uploaded screenshot 2026-09-10 045842; source file qw_state_extrema_01.py line 15 not independently file-hash-verified",
        "radius": record(radius), "width": record(width), "simpson_weight": record(weight),
        "cases": cases, "five_terms": {key: record(value) for key, value in terms.items()},
        "variable_terms": {key: record(value) for key, value in variable_terms.items()},
        "weighted_variable_terms": {key: record(weight * value) for key, value in variable_terms.items()},
        "total_rhs_change": record(total), "weighted_total": record(weight * total),
        "checks": "Exact hashes, endpoints, six RHS parts, eight balance fields, symmetric product and both decompositions passed",
        "new_solves": 0, "new_meshes": 0, "new_extrema_searches": 0,
        "limitations": "Local algebra only; no full ancestor audit, causal attribution, stability proof or physical validation",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sources = parser.add_mutually_exclusive_group()
    sources.add_argument("--inputs", type=Path,
                         help="Directory containing the input JSON files and coefficient source")
    sources.add_argument("--archive", type=Path,
                         help="Read the source inputs directly from the working ZIP")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    default_inputs = Path(__file__).resolve().parent / "inputs"
    result = calculate(arguments.archive or arguments.inputs or default_inputs)
    artifact = {"payload_sha256": digest(result), "payload": result}
    if arguments.check:
        saved = json.loads(arguments.check.read_text(encoding="utf-8"))
        require(digest(saved["payload"]) == saved["payload_sha256"], "Output payload hash")
        require(json.loads(json.dumps(artifact)) == saved, "Saved result differs from replay")
    if arguments.output:
        with arguments.output.open("x", encoding="utf-8") as output:
            json.dump(artifact, output, ensure_ascii=False, indent=2)
            output.write("\n")
    print("Exact replay and coefficient provenance: PASS")
    for key, value in result["variable_terms"].items():
        print(key, value["decimal"])
    print("Total:", result["total_rhs_change"]["decimal"])


if __name__ == "__main__":
    main()