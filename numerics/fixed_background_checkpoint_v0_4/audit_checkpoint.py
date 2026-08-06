import csv
import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
EXPECTED_FOLD = 2.0934591793773114e-3
EXPECTED_PREVIOUS_FOLD = 2.0682495692869894e-3
EXPECTED_FAMILY_COUNT = 9
DIRECT_FOLD_THRESHOLD = 0.01


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as input_file:
        return list(csv.DictReader(input_file))


def read_one(path):
    rows = read_rows(path)
    if len(rows) != 1:
        raise ValueError(f"expected one data row in {path}, found {len(rows)}")
    return rows[0]


def require(condition, message, failures):
    if not condition:
        failures.append(message)


def main():
    failures = []
    closures = read_rows(BASE_DIR / "coordinate_closures.csv")
    direct = read_one(BASE_DIR / "retained_direct_fold.csv")
    summary = read_one(BASE_DIR / "checkpoint_summary.csv")

    require(
        len(closures) == EXPECTED_FAMILY_COUNT,
        "wrong coordinate-family count",
        failures,
    )

    gains = {}
    for row in closures:
        family = row["coordinate_family"]
        require(
            row["coordinate_closed"] == "True",
            f"{family}: coordinate is not closed",
            failures,
        )
        require(
            row["further_direct_fold_authorized"] == "False",
            f"{family}: unexpected direct-fold authorization",
            failures,
        )
        require(
            row["full_static_backreaction_authorized"] == "False",
            f"{family}: unexpected static-backreaction authorization",
            failures,
        )
        require(
            row["dynamic_root_audit_authorized"] == "False",
            f"{family}: unexpected dynamic-root authorization",
            failures,
        )
        require(
            math.isclose(
                float(row["confirmed_record"]),
                EXPECTED_FOLD,
                rel_tol=1e-12,
                abs_tol=1e-15,
            ),
            f"{family}: confirmed record is inconsistent",
            failures,
        )
        gain = float(row["maximum_unresolved_gain"])
        threshold = float(row["direct_gain_threshold"])
        gains[family] = gain
        require(
            gain < threshold,
            f"{family}: unresolved gain reaches direct-fold threshold",
            failures,
        )

    maximum_sector = max(gains, key=gains.get)
    maximum_gain = gains[maximum_sector]

    require(
        math.isclose(
            float(direct["previous_confirmed_record"]),
            EXPECTED_PREVIOUS_FOLD,
            rel_tol=1e-12,
            abs_tol=1e-15,
        ),
        "direct record: previous fold is inconsistent",
        failures,
    )
    require(
        math.isclose(
            float(direct["measured_fold_backreaction"]),
            EXPECTED_FOLD,
            rel_tol=1e-12,
            abs_tol=1e-15,
        ),
        "direct record: retained fold is inconsistent",
        failures,
    )
    for field in (
        "all_radius_turning_points_detected",
        "direct_predictor_validation_pass",
        "matching_radius_fold_gate_pass",
        "sign_changing_fold_gate_pass",
        "new_record_confirmed",
    ):
        require(
            direct[field] == "True",
            f"direct record: {field} is not True",
            failures,
        )
    require(
        direct["full_static_backreaction_authorized"] == "False",
        "direct record: unexpected static-backreaction authorization",
        failures,
    )
    require(
        direct["dynamic_root_audit_authorized"] == "False",
        "direct record: unexpected dynamic-root authorization",
        failures,
    )

    require(
        summary["coordinate_family_count"] == str(EXPECTED_FAMILY_COUNT),
        "summary: wrong coordinate-family count",
        failures,
    )
    require(
        summary["closed_coordinate_family_count"]
        == str(EXPECTED_FAMILY_COUNT),
        "summary: wrong closed-coordinate count",
        failures,
    )
    require(
        summary["all_coordinate_families_closed"] == "True",
        "summary: all-coordinate closure flag is not True",
        failures,
    )
    require(
        summary["maximum_unresolved_gain_sector"] == maximum_sector,
        "summary: maximum-gain sector is inconsistent",
        failures,
    )
    require(
        math.isclose(
            float(summary["maximum_unresolved_predictor_gain"]),
            maximum_gain,
            rel_tol=1e-12,
            abs_tol=1e-15,
        ),
        "summary: maximum unresolved gain is inconsistent",
        failures,
    )
    require(
        maximum_gain < DIRECT_FOLD_THRESHOLD,
        "maximum unresolved gain reaches the direct-fold threshold",
        failures,
    )
    require(
        summary["retained_direct_fold_validated"] == "True",
        "summary: retained direct fold is not validated",
        failures,
    )
    require(
        summary["fixed_background_optimization_contour_closed"] == "True",
        "summary: fixed-background contour is not closed",
        failures,
    )
    require(
        summary["full_static_backreaction_authorized"] == "False",
        "summary: unexpected static-backreaction authorization",
        failures,
    )
    require(
        summary["dynamic_root_audit_authorized"] == "False",
        "summary: unexpected dynamic-root authorization",
        failures,
    )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)

    print(
        f"PASS: {EXPECTED_FAMILY_COUNT}/{EXPECTED_FAMILY_COUNT} "
        "audited coordinates closed; "
        f"retained direct fold={EXPECTED_FOLD:.12e}; "
        f"maximum unresolved predictor gain={maximum_gain:.6%}; "
        f"threshold={DIRECT_FOLD_THRESHOLD:.6%}"
    )


if __name__ == "__main__":
    main()