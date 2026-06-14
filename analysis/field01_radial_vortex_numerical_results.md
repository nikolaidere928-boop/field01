# Radial Vortex Numerical Results

Purpose: record the first numerical solve using the explicit radial vortex functional derived in `analysis/field01_radial_vortex_functional_derivation.md`.

Status: standard-math toy result. No Field 01 interpretation is used here.

## 1. Script And Outputs

Script:

```text
analysis/numerics/solve_radial_vortex_profile.py
```

Primary JSON output:

```text
analysis/numerics/radial_vortex_results.json
```

Profile CSV outputs:

```text
analysis/numerics/standard_vortex_boundary_radial_vortex_profile.csv
analysis/numerics/forced_outer_zero_boundary_radial_vortex_profile.csv
```

Plot:

```text
analysis/numerics/radial_vortex_profiles.png
```

## 2. Functional Used

The numerical solve used:

```math
E
=2\pi\int_0^R dr\,
\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right].
```

with parameters:

```text
lambda = 1
 g     = 1
 N0    = 1
 n     = 1
 R     = 12
 r_min = 1e-3
```

The radial equations were:

```math
N''+\frac{1}{r}N'
-\frac{(n-a)^2}{r^2}N
-\lambda N(N^2-N_0^2)=0,
```

```math
a''-\frac{1}{r}a'
+g^2(n-a)N^2=0.
```

## 3. Case A — Standard Vortex Boundary

Boundary conditions:

```math
N(r_{min})=0,
\qquad
a(r_{min})=0,
\qquad
N(R)=N_0,
\qquad
a(R)=n.
```

Numerical result:

```text
success: true
energy_finite_disk: 3.6340494886492563
flux_finite_disk: 6.283185307179586
flux_over_2pi: 1.0
screened_phase_mismatch_right: 0.0
max_abs_ode_residual_excluding_core: 1.2333991380314435e-07
```

Interpretation in standard terms:

```text
The phase winding remains Q_wind = 1, while the covariant angular mismatch is screened at the outer boundary.
```

## 4. Case B — Forced Outer-Zero Boundary

Boundary conditions:

```math
N(r_{min})=0,
\qquad
a(r_{min})=0,
\qquad
N(R)=0,
\qquad
a(R)=n.
```

Numerical result:

```text
success: true
energy_finite_disk: 37.263888601274736
flux_finite_disk: 6.283185307179586
flux_over_2pi: 1.0
screened_phase_mismatch_right: 0.0
max_abs_ode_residual_excluding_core: 1.2333935673486396e-07
```

Caution:

```text
This is not a standard infinite-domain vortex boundary condition. It is a forced finite-disk boundary test where the scalar modulus is required to return to zero at R.
```

## 5. Relation To The Previous Screened Toy Solver

For the parameter choice:

```text
A = B = C = lambda = N0 = g = 1
```

the previous screened toy solver and the explicit radial vortex solver produce the same finite-disk energies:

```text
screened_particle_boundary / standard_vortex_boundary:
3.634049488649256  vs  3.6340494886492563

screened_horizon_boundary / forced_outer_zero_boundary:
37.26388860127473  vs  37.263888601274736
```

This means the older screened model was already using the same radial structure, but the new derivation makes the polar-coordinate origin of the terms explicit and renames the objects in standard vortex language.

## 6. Main Technical Conclusion

The screened radial toy model is mathematically an Abelian-Higgs / Nielsen-Olesen-like vortex ansatz under the convention:

```math
\Psi=N e^{i\varphi},
\qquad
\varphi=n\theta,
\qquad
A_\theta=a(r),
\qquad
D_\theta\varphi=n-a(r).
```

The correct technical next step is not to add interpretation, but to compare conventions and equations directly with standard Abelian-Higgs vortex references.

## 7. Next Checks

1. Compare the exact radial equations with a textbook Nielsen-Olesen convention.
2. Track how the coupling `e` or `g` is placed in different conventions.
3. Check the critical/BPS coupling convention for this normalization.
4. Repeat the solve for several `lambda/g^2` values.
5. Decide whether any part of the toy model remains after subtracting standard Abelian-Higgs content.