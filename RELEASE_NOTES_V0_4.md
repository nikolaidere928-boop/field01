# Field 01 Release Notes — v0.4 Fixed-Background Handoff

Date: 2026-08-06.

Status: public staging package for technical criticism.

## Main Result

This release updates the retained fixed-background fold diagnostic from

```text
2.0682495692869894e-3
```

to

```text
2.0934591793773114e-3.
```

The measured improvement over the `v0.3` benchmark is `1.218886%`.

## Retained Shape

```text
difference profile:
q=16, d=4, zeta=1.810582828929,
c1=1.20, c2=0, lambda=-0.35;

aligned profile:
p=1, c1=-3.260, c2=3.041, rho=0.
```

## Audit Scope

The release records nine closed coordinates:

1. difference cubic-exponential tilt;
2. difference core power;
3. difference shoulder coefficient;
4. difference linear width;
5. difference quadratic width;
6. aligned shell power;
7. aligned linear width;
8. aligned quadratic width;
9. aligned cubic-exponential tilt.

The last coordinate reaches a maximum unresolved connected-branch predictor gain of `0.917518%`, below the internal `1%` threshold for authorizing another direct fold.

## Direct-Fold Validation

The retained direct fold passes:

- predictor validation;
- sign-changing fold gate;
- matching-radius fold gate;
- turning-point detection at all audited radii.

The maximum relative matching-radius spread is `0.074515%`. The predictor relative error at the retained fold is `0.057938%`.

## Reproducibility Boundary

The compact public package reproduces the final closure logic from derived CSV records. It does not include the complete exploratory workspace or rerun every primary boundary-value solve.

## Explicit Non-Claims

This release does not establish a completed theory, experimental evidence, a fundamental action, full static backreaction, dynamic stability, or physical particle spectra.

## Next Stage

The selected profile optimization contour is frozen. The next numerical branch should address an independent physical sector rather than another adjacent profile-shape coordinate.

## License Status

`LICENSE_NOTE.md` remains a temporary usage notice. A formal long-term text and code license has not yet been selected.