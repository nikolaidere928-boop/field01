import csv
import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SUMMARY_DIR = BASE_DIR / "closure_summaries"
EXPECTED_FOLD = 2.0682495692869894e-3
DIRECT_FOLD_THRESHOLD = 0.01

INPUTS = {
    "aligned_polynomial_widths": {
        "path": SUMMARY_DIR / "aligned_polynomial_widths.csv",
        "closure": "alternating_width_audit_closed",
        "fold": "discrete_winner_fold_backreaction",
        "headrooms": {
            "aligned_linear_width": "fitted_residual_gain_over_discrete_winner",
            "aligned_quadratic_width": "previous_quadratic_residual_gain",
        },
    },
    "aligned_shell_power": {
        "path": SUMMARY_DIR / "aligned_shell_power.csv",
        "closure": "post_width_shell_power_coordinate_closed",
        "fold": "retained_fold_backreaction",
        "headrooms": {},
    },
    "difference_core_power": {
        "path": SUMMARY_DIR / "difference_core_power.csv",
        "closure": "post_aligned_core_power_coordinate_closed",
        "fold": "retained_fold_backreaction",
        "headrooms": {
            "difference_core_power": "combined_core_power_headroom",
        },
    },
    "difference_shoulder_coefficient": {
        "path": SUMMARY_DIR / "difference_shoulder_coefficient.csv",
        "closure": "post_aligned_shoulder_coefficient_closed",
        "fold": "retained_fold_backreaction",
        "headrooms": {
            "difference_shoulder_coefficient": "combined_shoulder_headroom",
        },
    },
    "difference_linear_width": {
        "path": SUMMARY_DIR / "difference_linear_width.csv",
        "closure": "post_aligned_linear_width_closed",
        "fold": "retained_fold_backreaction",
        "headrooms": {
            "difference_linear_width": "fitted_residual_gain",
        },
    },
    "difference_quadratic_width": {
        "path": SUMMARY_DIR / "difference_quadratic_width.csv",
        "closure": "post_aligned_quadratic_width_closed",
        "fold": "retained_fold_backreaction",
        "headrooms": {
            "difference_quadratic_width": "fitted_residual_gain",
        },
    },
}


def read_row(path):
    with path.open(newline="", encoding="utf-8") as input_file:
        rows = list(csv.DictReader(input_file))
    if len(rows) != 1:
        raise ValueError(f"expected one data row in {path}, found {len(rows)}")
    return rows[0]


def require(condition, message, failures):
    if not condition:
        failures.append(message)


def main():
    failures = []
    rows = {}
    headrooms = {}

    for family, specification in INPUTS.items():
        row = read_row(specification["path"])
        rows[family] = row
        require(
            row[specification["closure"]] == "True",
            f"{family}: closure flag is not True",
            failures,
        )
        require(
            math.isclose(
                float(row[specification["fold"]]),
                EXPECTED_FOLD,
                rel_tol=1e-12,
                abs_tol=1e-15,
            ),
            f"{family}: retained fold is inconsistent",
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
        for sector, column in specification["headrooms"].items():
            headrooms[sector] = float(row[column])

    maximum_sector = max(headrooms, key=headrooms.get)
    maximum_headroom = headrooms[maximum_sector]
    require(
        maximum_headroom < DIRECT_FOLD_THRESHOLD,
        "maximum one-coordinate headroom reaches the direct-fold threshold",
        failures,
    )

    unified = read_row(BASE_DIR / "checkpoint_summary.csv")
    require(unified["coordinate_family_count"] == "6", "wrong family count", failures)
    require(
        unified["closed_coordinate_family_count"] == "6",
        "wrong closed-family count",
        failures,
    )
    require(
        unified["unified_post_aligned_shape_audit_closed"] == "True",
        "unified checkpoint is not closed",
        failures,
    )
    require(
        unified["maximum_one_coordinate_headroom_sector"] == maximum_sector,
        "unified maximum-headroom sector is inconsistent",
        failures,
    )
    require(
        math.isclose(
            float(unified["maximum_one_coordinate_headroom"]),
            maximum_headroom,
            rel_tol=1e-12,
            abs_tol=1e-15,
        ),
        "unified maximum headroom is inconsistent",
        failures,
    )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)

    print(
        "PASS: 6/6 coordinate families closed; "
        f"maximum headroom={maximum_headroom:.6%}; "
        "unified checkpoint closed=True"
    )


if __name__ == "__main__":
    main()