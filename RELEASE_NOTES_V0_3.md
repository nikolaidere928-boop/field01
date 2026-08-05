# Field 01 Release Notes — v0.3 Fixed-Background Checkpoint

Date: 2026-08-05.

Status: public staging package for technical criticism.

## Main Addition

This release adds a compact numerical checkpoint under:

```text
numerics/fixed_background_checkpoint_v0_3/
```

The package records the closure of six independently gated one-coordinate profile families around one retained discrete fixed-background shape. A standalone audit script verifies the closure flags, retained fold consistency, authorization boundaries, and the maximum conservative unresolved one-coordinate headroom.

## Retained Checkpoint

```text
difference profile: q=16, d=4, zeta=1.859155130556, c1=1.20, c2=0;
aligned profile: p=1, c1=-3.260, c2=3.041;
retained fold measure: xi_br,max=2.068249569e-3.
```

The largest conservative unresolved one-coordinate headroom is `0.332421%`, below the internal `1%` direct-fold threshold.

## Reproducibility Boundary

This release reproduces the final closure audit from compact derived CSV records. It does not include the full exploratory workspace or rerun every primary boundary-value solve that generated those records.

## Explicit Non-Claims

This release does not establish:

- a new physical theory;
- experimental evidence;
- a full nonlinear static solution;
- dynamic stability;
- physical particle masses or spectra;
- a solution to any black-hole information problem.

Full static backreaction and dynamic-root analysis remain outside the release boundary.

## Next Research Branch

The closed separable polynomial profile family is retained as a benchmark. Further fixed-background work must use an explicitly new basis family rather than reopen a closed coordinate.

## Remaining Publication Gate

`LICENSE_NOTE.md` remains a temporary usage notice. A formal text and code license must be selected before treating this staging directory as a finalized long-term public release.