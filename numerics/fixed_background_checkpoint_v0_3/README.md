# Fixed-Background Numerical Checkpoint v0.3

Date: 2026-08-05.

This directory is a compact public audit package for one fixed-background profile-search checkpoint. It is designed to make the final closure decision inspectable without publishing the complete exploratory workspace.

## Quick Check

From the repository root, run:

```sh
python numerics/fixed_background_checkpoint_v0_3/audit_checkpoint.py
```

Expected final line:

```text
PASS: 6/6 coordinate families closed; maximum headroom=0.332421%; unified checkpoint closed=True
```

The script uses only the Python standard library.

## Included Files

- `CHECKPOINT_REPORT.md` — scientific scope, retained shape, result, and non-claims.
- `audit_checkpoint.py` — standalone consistency audit.
- `checkpoint_summary.csv` — unified one-row checkpoint record.
- `closure_summaries/*.csv` — six one-row coordinate-closure records.

## What Is Reproduced

The audit verifies:

1. all six coordinate families report closure;
2. every family retains the same fold measure;
3. the maximum conservative one-coordinate headroom is below `1%`;
4. no direct fold, full static backreaction, or dynamic-root analysis is authorized by these records;
5. the unified summary is consistent with the six source summaries.

## What Is Not Reproduced

This compact release does not rerun the complete primary boundary-value solver campaign. The CSV files are derived closure records from that internal campaign. They are published to make the final checkpoint logic auditable, not to claim full end-to-end solver reproduction.