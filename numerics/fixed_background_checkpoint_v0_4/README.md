# Fixed-Background Numerical Checkpoint v0.4

Date: 2026-08-06.

This directory is a compact public audit package for the final selected fixed-background profile-optimization handoff.

## Quick Check

From the repository root, run:

```sh
python numerics/fixed_background_checkpoint_v0_4/audit_checkpoint.py
```

Expected final line:

```text
PASS: 9/9 audited coordinates closed; retained direct fold=2.093459179377e-03; maximum unresolved predictor gain=0.917518%; threshold=1.000000%
```

The audit uses only the Python standard library.

## Included Files

- `CHECKPOINT_REPORT.md` — scope, retained shape, gates, and non-claims.
- `NUMERICAL_EVOLUTION.md` — selected optimization milestones.
- `audit_checkpoint.py` — standalone consistency audit.
- `checkpoint_summary.csv` — unified checkpoint record.
- `coordinate_closures.csv` — normalized records for nine audited coordinates.
- `retained_direct_fold.csv` — compact direct-fold validation record.

## Reproduced Checks

The audit verifies:

1. all nine coordinate records report closure;
2. all coordinate records retain the same confirmed fold;
3. no coordinate authorizes another direct fold;
4. the maximum unresolved connected-coordinate predictor gain remains below `1%`;
5. the retained direct fold passes predictor, sign-changing, matching-radius, and turning-point gates;
6. full static backreaction and dynamic-root analysis remain unauthorized.

## Boundary

The package audits compact derived records. It does not rerun the complete internal boundary-value solver campaign and is not an end-to-end primary-solver release.