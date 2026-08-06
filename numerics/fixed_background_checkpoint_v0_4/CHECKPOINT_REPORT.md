# Field 01 Fixed-Background Optimization Handoff

Date: 2026-08-06.

## Scope

This checkpoint concerns a restricted two-component fixed-background profile search. Candidate changes were required to pass structural, fixed-background, predictor-gain, matching-radius, and direct-fold authorization gates.

The quantity `xi_br,max` is an internal fold/backreaction diagnostic of this restricted numerical model. It is not an experimentally measured observable.

## Retained Direct Fold

```text
difference profile:
    q = 16
    d = 4
    zeta = 1.810582828929
    c1 = 1.20
    c2 = 0
    lambda = -0.35

aligned profile:
    p = 1
    c1 = -3.260
    c2 = 3.041
    rho = 0

xi_br,max = 2.0934591793773114e-3
```

The retained fold improves the `v0.3` value by `1.218886%`.

## Direct Validation

The compact retained record reports:

```text
predictor relative error: 0.057938%
maximum matching-radius spread: 0.074515%
all radius turning points detected: True
predictor validation: True
matching-radius gate: True
sign-changing fold gate: True
```

## Closed Coordinates

Nine coordinates are closed under the current rules:

1. difference cubic-exponential tilt `lambda`;
2. difference core power `q`;
3. difference shoulder coefficient `d`;
4. difference linear width `c1`;
5. difference quadratic width `c2`;
6. aligned shell power `p`;
7. aligned linear width `c1`;
8. aligned quadratic width `c2`;
9. aligned cubic-exponential tilt `rho`.

The largest unresolved connected-coordinate predictor gain is associated with the aligned cubic-exponential extension:

```text
rho_vertex = 0.269251036968
predicted gain = 0.917518%
direct-fold threshold = 1.000000%
remaining gap = 0.082482%
```

The connected physical branch ends between `rho=0.29` and `rho=0.30`. A separate passing point at `rho=1.00` is not included because it is separated from the control by a failed physical region.

## Meaning of Closure

Closure means that the audited coordinates do not authorize another direct fold under the stated rules. It freezes the selected fixed-background ansatz as a benchmark.

It does not prove global optimality over arbitrary functions, different actions, additional fields, disconnected branches, or different physical sectors.

## Explicit Non-Claims

This checkpoint does not provide:

- experimental evidence;
- a fundamental action;
- a complete physical theory;
- full static backreaction;
- dynamic-root or nonlinear stability analysis;
- physical particle masses or spectra;
- proof of a new particle, force, or field;
- validation of the Field 01 interpretation layer.

## Next Authorized Direction

The next research stage should test an independent physical sector with its own predeclared gates. Full static backreaction and dynamic-root analysis remain separate, unauthorized stages.