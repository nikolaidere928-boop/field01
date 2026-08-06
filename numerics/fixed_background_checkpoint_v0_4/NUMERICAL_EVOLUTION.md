# Selected Numerical Evolution Milestones

Date: 2026-08-06.

This table summarizes selected retained milestones from the internal fixed-background search. It is not a claim that every intermediate slice is reproduced in this compact package.

| Stage | Retained `xi_br,max` | Model-level role |
|---|---:|---|
| One-component core basis | approximately `7.624e-4` | Baseline localization limit of the preceding single-basis sector |
| Coupled two-component boundary | `1.278178674e-3` | Introduction of a connected compensating shoulder component |
| Node and difference-width closure | `1.307068707e-3` | Node placement and sign-changing core/shoulder profile closure |
| Aligned linear-width milestone | `1.996071538e-3` | Fine aligned-profile shaping |
| `2e-3` benchmark crossing | `2.002226282e-3` | First retained fold above the internal `2e-3` benchmark |
| Aligned polynomial closure (`v0.3`) | `2.068249569287e-3` | Final retained polynomial aligned profile |
| Difference cubic-exponential record (`v0.4`) | `2.093459179377e-3` | Confirmed direct fold after a genuinely non-polynomial difference-profile extension |

## Near-Threshold Non-Record

The aligned multiplier

```text
exp[rho (1-H^2)^3]
```

produces a fitted predictor maximum near

```text
rho = 0.269251036968
predicted xi_br = 2.112667042958e-3
raw predicted gain = 0.917518%
```

This is not a retained record because the gain remains below the predeclared `1%` threshold for authorizing a direct fold.

## Interpretation Rule

The table describes numerical development inside the selected fixed-background ansatz. Terms such as core, shoulder, node, and aligned profile are model-level labels. The sequence is not experimental evidence and does not establish a globally optimal particle solution.