# Radial Vortex BPS Coupling Sweep Results

Purpose: check the critical coupling identified in `analysis/field01_bps_coupling_convention_note.md` by solving the radial vortex boundary-value problem for several values of `lambda`.

Status: numerical standard-math check. No Field 01 interpretation is used here.

## 1. Script And Outputs

Script:

```text
analysis/numerics/sweep_radial_vortex_coupling.py
```

Outputs:

```text
analysis/numerics/radial_vortex_coupling_sweep.json
analysis/numerics/radial_vortex_coupling_sweep.csv
analysis/numerics/radial_vortex_coupling_sweep.png
```

## 2. Normalization

The energy normalization is:

```math
E=\int d^2x\left[
\frac{1}{2}|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right].
```

In this normalization:

```math
\lambda_{\mathrm{BPS}}=\frac{g^2}{2},
\qquad
\beta=\frac{2\lambda}{g^2},
\qquad
\beta_{\mathrm{BPS}}=1.
```

For this run:

```text
g = 1
N0 = 1
n = 1
R = 20
```

Therefore:

```math
\lambda_{\mathrm{BPS}}=0.5,
\qquad
E_{\mathrm{BPS}}=\pi.
```

## 3. Numerical Results

| lambda | beta | energy | energy / pi | energy - pi | flux / 2pi |
|---:|---:|---:|---:|---:|---:|
| 0.25 | 0.5 | 2.726605263809252 | 0.8679054111912475 | -0.41498738978054117 | 1.0 |
| 0.50 | 1.0 | 3.1415667978875335 | 0.9999917698743566 | -0.000025855702259658386 | 1.0 |
| 1.00 | 2.0 | 3.634026939952255 | 1.1567467016450315 | 0.492434286362462 | 1.0 |
| 2.00 | 4.0 | 4.211522775540257 | 1.3405693353426615 | 1.0699301219504642 | 1.0 |

## 4. BPS Residual Check

At the BPS value `lambda = 0.5`, the first-order residuals are small compared with the non-BPS cases:

```text
lambda = 0.5
max_abs_bps_N_residual_excluding_core = 3.770010223378417e-04
max_abs_bps_a_residual_excluding_core = 2.6530219790488196e-06
```

The finite-disk energy differs from `pi` by:

```text
E - pi = -2.5855702259658386e-05
```

This confirms that, in the current normalization, the critical coupling is correctly identified as:

```math
\lambda=\frac{g^2}{2}.
```

## 5. Important Caution

The comparison with `pi` is meaningful as the BPS target only at:

```math
\beta=1.
```

The `beta != 1` energies should not be read as violating or satisfying the BPS bound. They are simply non-critical coupling solutions of the same finite-disk boundary-value problem.

## 6. Main Technical Conclusion

The radial solver now passes a standard consistency check:

```text
At lambda = g^2 / 2, n = 1, N0 = 1, the energy is numerically pi and the BPS first-order residuals are small.
```

Therefore the current normalization, radial functional, field-strength term, and boundary conventions are internally consistent with the Abelian-Higgs / Nielsen-Olesen BPS convention up to the stated normalization factors.

## 7. Next Step

The next technical step is to compare this convention against a standard reference notation and create a dictionary such as:

```text
our N(r)      <-> reference f(r) or v f(r)
our a(r)      <-> reference n P(r), n[1-P(r)], or e A_theta
our lambda    <-> reference scalar coupling
our g or e    <-> reference gauge coupling
our beta      <-> reference Ginzburg-Landau / type-I/type-II parameter
```

This should be done before making any interpretive claims.