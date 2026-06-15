# BPS / Critical Coupling Convention Note

Purpose: identify the critical coupling for the explicit radial vortex functional used in `analysis/field01_radial_vortex_functional_derivation.md`.

Status: standard Abelian-Higgs convention check. No Field 01 interpretation is used here.

## 1. Energy Normalization Used Here

The static two-dimensional energy is written as:

```math
E=\int d^2x\left[
\frac{1}{2}|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right],
```

where:

```math
D_i\Psi=(\partial_i-iA_i)\Psi,
\qquad
B=F_{12},
\qquad
\Psi=N e^{i\varphi}.
```

In this convention the gauge coupling is placed in the Maxwell term, not inside the covariant derivative.

## 2. Critical Coupling In This Normalization

Completing the square gives a critical, or Bogomolny, coupling when the scalar potential coefficient matches the gauge square coefficient:

```math
\frac{\lambda}{4}=\frac{g^2}{8}.
```

Therefore:

```math
\boxed{\lambda_{\mathrm{BPS}}=\frac{g^2}{2}}.
```

Equivalently, the dimensionless ratio is:

```math
\boxed{\beta=\frac{2\lambda}{g^2}},
\qquad
\beta_{\mathrm{BPS}}=1.
```

This is the safest way to compare conventions, because many references place factors of `2`, `e`, or `1/2` differently. It is also only a statement about the ordinary Abelian-Higgs energy written above; Chern-Simons terms, dielectric functions, or other modified gauge sectors require a separate self-duality analysis.

## 3. BPS Energy Bound In This Normalization

At critical coupling, the energy can be written schematically as a sum of positive squares plus a flux term:

```math
E
=\int d^2x\left[
\frac{1}{2}|(D_1\pm iD_2)\Psi|^2
+\frac{1}{2g^2}\left(B\mp\frac{g^2}{2}(N_0^2-|\Psi|^2)\right)^2
\right]
\pm\frac{N_0^2}{2}\int B\,d^2x.
```

The sign is chosen to make the flux contribution positive.

With flux:

```math
\Phi_B=\int B\,d^2x=2\pi n,
```

the BPS bound is:

```math
\boxed{E_{\mathrm{BPS}}=\pi N_0^2 |n|}.
```

This bound corresponds to the present `1/2 |D_i Psi|^2` normalization. Other common normalizations may give `2 pi v^2 |n|` instead.

## 4. Schaposnik Reference Check

F.A. Schaposnik, *Vortices*, arXiv:hep-th/0611028v1, uses an Abelian-Higgs energy per unit length with:

```math
\frac14F_{ij}^2
+\frac12|D_i\phi|^2
+\lambda_S(|\phi|^2-\phi_0^2)^2,
```

and covariant derivative:

```math
D_\mu=\partial_\mu+i e A_\mu.
```

In that convention the critical point is:

```math
e^2=8\lambda_S.
```

Using the coefficient map:

```math
g=e,
\qquad
\lambda_{ours}=4\lambda_S,
```

this becomes:

```math
\lambda_{ours}=\frac{g^2}{2}.
```

Schaposnik's Bogomolny bound is:

```math
E\ge\pi\phi_0^2|N|,
```

which maps directly to:

```math
E_{\mathrm{BPS}}=\pi N_0^2|n|.
```

This is consistent with using the `pi` target in the present explicit `1/2 |D_i\Psi|^2` scalar-kinetic normalization.

Broader soliton/vortex background references for this standard layer include Rajaraman's textbook and Tong's TASI soliton lectures:

```text
R. Rajaraman, Solitons and Instantons: An Introduction to Solitons and Instantons in Quantum Field Theory, North-Holland, 1982.
D. Tong, TASI Lectures on Solitons, arXiv:hep-th/0509216.
```

## 5. Radial BPS Equations

For positive winding with the charge-absorbed coordinate one-form convention:

```math
\varphi=n\theta,
\qquad
A=a(r)\,d\theta,
\qquad
B=\frac{a'}{r},
```

or equivalently `\mathcal A=(a/g)d\theta` and `B_{\mathrm{phys}}=a'/(g r)`, one convenient sign choice gives:

```math
N'=\frac{n-a}{r}N,
```

```math
\frac{a'}{r}=\frac{g^2}{2}(N_0^2-N^2).
```

These first-order equations imply the second-order radial equations at:

```math
\lambda=\frac{g^2}{2}.
```

## 6. Relation To The Existing Numerical Parameters

The existing numerical solve used:

```text
g = 1
lambda = 1
```

Therefore:

```math
\beta=\frac{2\lambda}{g^2}=2.
```

So the previous run is not at critical coupling in this normalization. The BPS value for `g=1` is:

```math
\lambda_{\mathrm{BPS}}=0.5.
```

At `N0=1` and `n=1`, the BPS energy target is:

```math
E_{\mathrm{BPS}}=\pi\approx3.141592653589793.
```

## 7. Next Numerical Check

Run the radial solver at several values of:

```math
\beta=\frac{2\lambda}{g^2},
```

especially:

```text
lambda = 0.25  -> beta = 0.5
lambda = 0.50  -> beta = 1.0  (BPS)
lambda = 1.00  -> beta = 2.0
lambda = 2.00  -> beta = 4.0
```

The `lambda = 0.50` result should be close to `E = pi` for a sufficiently large outer radius and accurate boundary solve.