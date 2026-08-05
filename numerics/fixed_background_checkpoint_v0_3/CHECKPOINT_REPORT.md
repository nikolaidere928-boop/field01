# Field 01 Fixed-Background Profile Checkpoint

Date: 2026-08-05.

## Scope

This checkpoint concerns a restricted fixed-background two-profile search. The search varied one profile coordinate at a time and required structural, fixed-background, predictor, matching-radius, and direct-fold authorization gates before accepting any new fold calculation.

The reported quantity `xi_br,max` is an internal fold/backreaction diagnostic within this restricted model. It is not an experimentally measured observable.

## Closed Coordinate Families

Six coordinate families are closed:

1. aligned polynomial widths;
2. aligned shell power;
3. difference core power;
4. difference shoulder coefficient;
5. difference linear width;
6. difference quadratic width.

## Retained Discrete Shape

```text
difference profile:
    core power q = 16
    shoulder coefficient d = 4
    node parameter zeta = 1.859155130556
    linear width coefficient c1 = 1.20
    quadratic width coefficient c2 = 0

aligned profile:
    shell power p = 1
    linear width coefficient c1 = -3.260
    quadratic width coefficient c2 = 3.041

retained fold measure:
    xi_br,max = 2.0682495692869894e-3
```

## Closure Result

All six source summaries retain the same fold measure. The largest conservative unresolved one-coordinate headroom is:

```text
sector: difference shoulder coefficient
headroom: 0.0033242123537000623 = 0.332421%
direct-fold threshold: 0.01 = 1%
```

The maximum headroom is below the direct-fold threshold. The unified checkpoint is therefore closed within the tested separable polynomial profile family.

## Interpretation Boundary

Closure means that the tested one-coordinate extensions do not justify another direct fold under the stated internal gates. It does not prove that the retained shape is globally optimal over all possible functions or bases.

## Explicit Non-Claims

This checkpoint does not provide:

- experimental evidence;
- a physical parameter fit;
- a complete action or fundamental theory;
- full static backreaction;
- dynamic-root or stability analysis;
- proof of a new particle, force, or field;
- validation of the Field 01 interpretation layer.

## Next Authorized Direction

Further fixed-background work may introduce a genuinely new basis family, for example a noninteger or mixed shoulder-exponent profile. Such work is a new research branch and is not part of this frozen checkpoint.