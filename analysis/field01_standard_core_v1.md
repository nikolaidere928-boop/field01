# Field 01 Standard Core v1

Purpose: state the clean standard-math core of the current radial vortex toy model, separated from all Field 01 interpretation.

Status: standard Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex comparison note. This is not a physical theory, not a novelty claim, and not an interpretive model.

Date: 2026-06-14.

## 1. Scope

This file contains only the technical layer:

- complex scalar in polar form;
- phase winding;
- scalar radial modulus;
- `U(1)` covariant derivative;
- radial vortex ansatz;
- finite-energy boundary conditions;
- magnetic flux;
- radial energy functional;
- Euler-Lagrange equations;
- BPS / Bogomolny normalization.

It deliberately excludes interpretive language. Any later interpretation must cite this file as a standard mathematical substrate, not as a proof of interpretation.

## 2. Fields And Conventions

Work on a two-dimensional spatial slice with polar coordinates:

```math
(r,\theta).
```

Use a complex scalar:

```math
\Psi=N(r)e^{i\varphi(r,\theta)},
```

with vortex phase:

```math
\varphi(r,\theta)=n\theta,
\qquad
n\in\mathbb Z.
```

Use an Abelian gauge field in the convention:

```math
D_i=\partial_i-iA_i.
```

The coupling is not placed in `D_i`; it is placed in the gauge-field kinetic term.

## 3. Winding Number

Definition:

```math
Q_{\mathrm{wind}}
=\frac{1}{2\pi}\oint_C d\varphi.
```

For:

```math
\varphi=n\theta,
```

one obtains:

```math
Q_{\mathrm{wind}}=n.
```

This is the standard integer phase winding around the vortex core.

## 4. Radial Vortex Ansatz

Use the radial ansatz:

```math
\Psi=N(r)e^{in\theta},
\qquad
A_r=0,
\qquad
A_\theta=a(r).
```

In this convention, the angular covariant derivative contributes the factor:

```math
D_\theta\Psi
\propto i[n-a(r)]N(r)e^{in\theta}.
```

Equivalently, the angular mismatch is:

```math
D_\theta\varphi=n-a(r).
```

The public-safe wording is:

```text
The angular component of the covariant derivative tends to zero at infinity.
```

Avoid using `angular screening` as the primary technical phrase.

## 5. Boundary Conditions

For the standard finite-energy vortex-like configuration:

```math
N(0)=0,
\qquad
a(0)=0,
```

and:

```math
N(\infty)=N_0,
\qquad
a(\infty)=n.
```

Therefore:

```math
D_\theta\Psi\to0
\quad(r\to\infty).
```

These boundary conditions match the normalized reference convention where the gauge profile tends to `1`, after the map:

```math
a_{ours}(r)=n\,a_{ref}(r),
\qquad
a_{ref}(\infty)=1.
```

## 6. Magnetic Field And Flux

In the current polar-coordinate convention:

```math
B=F_{12}=\frac{a'(r)}{r}.
```

The total flux is:

```math
\Phi_B
=\int B\,d^2x
=\int_0^{2\pi}\int_0^\infty \frac{a'}{r}r\,dr\,d\theta
=2\pi[a(\infty)-a(0)].
```

With the standard boundary conditions:

```math
\Phi_B=2\pi n.
```

If the gauge coupling is placed inside the covariant derivative instead, the physical flux is commonly written as:

```math
\Phi_B^{ref}=\frac{2\pi n}{e}.
```

## 7. Energy Functional

Current convention:

```math
E=\int d^2x\left[
\frac12|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right].
```

Substituting the radial ansatz gives:

```math
E
=2\pi\int_0^R dr\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right].
```

For an infinite plane, take the formal limit:

```math
R\to\infty,
```

with the finite-energy boundary conditions stated above.

## 8. Euler-Lagrange Equations

For the radial integrand:

```math
L_r
=\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2,
```

the scalar profile equation is:

```math
N''+\frac{1}{r}N'
-\frac{(n-a)^2}{r^2}N
-\lambda N(N^2-N_0^2)=0.
```

The gauge profile equation is:

```math
a''-\frac{1}{r}a'
+g^2(n-a)N^2=0.
```

Equivalently:

```math
a''-\frac{1}{r}a'
=g^2(a-n)N^2.
```

## 9. BPS / Critical Coupling

Completing the square in the current normalization gives the critical coupling:

```math
\lambda_{\mathrm{BPS}}=\frac{g^2}{2}.
```

Equivalently:

```math
\beta=\frac{2\lambda}{g^2},
\qquad
\beta_{\mathrm{BPS}}=1.
```

At the BPS point, the first-order radial equations can be written as:

```math
N'=\frac{n-a}{r}N,
```

and:

```math
\frac{a'}{r}=\frac{g^2}{2}(N_0^2-N^2).
```

The BPS energy bound in this normalization is:

```math
E_{\mathrm{BPS}}=\pi N_0^2|n|.
```

For:

```math
N_0=1,
\qquad
|n|=1,
```

this gives:

```math
E_{\mathrm{BPS}}=\pi.
```

## 10. Schaposnik Convention Map

Reference:

```text
F.A. Schaposnik, Vortices, arXiv:hep-th/0611028v1.
```

Schaposnik's Abelian-Higgs energy per unit length is:

```math
E_S=\int d^2x\left[
\frac14F_{ij}^2
+\frac12|D_i\phi|^2
+\lambda_S(|\phi|^2-\phi_0^2)^2
\right],
```

with:

```math
D_\mu=\partial_\mu+i e A_\mu.
```

The useful coefficient map is:

```math
N_0\leftrightarrow\phi_0,
\qquad
n\leftrightarrow N,
\qquad
g\leftrightarrow e,
\qquad
\lambda_{ours}=4\lambda_S.
```

Schaposnik's critical point:

```math
e^2=8\lambda_S
```

maps to:

```math
\lambda_{ours}=\frac{g^2}{2}.
```

Schaposnik's BPS bound:

```math
E_S\ge\pi\phi_0^2|N|
```

maps to:

```math
E_{ours,\mathrm{BPS}}=\pi N_0^2|n|.
```

This is consistent with using the `pi` target in the explicit `1/2 |D_i\Psi|^2` scalar-kinetic normalization.

## 11. Standard Names

The standard mathematical construction may be described as:

- Abelian-Higgs vortex;
- Nielsen-Olesen vortex;
- Abrikosov vortex;
- Ginzburg-Landau vortex;
- radial vortex ansatz;
- `U(1)` scalar-gauge vortex ansatz.

Use `structurally the same radial vortex machinery as` when comparing conventions.

Do not claim novelty for this standard layer.

## 12. Non-Claims

This file does not claim:

- a new field theory;
- a particle model;
- a cosmological model;
- a new physical observable;
- any nonstandard interpretation.

This file only fixes a clean standard mathematical core and its convention map.

## 13. Public-Safe Summary

```text
The standard core is a two-dimensional radial Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex ansatz: a winding complex scalar, a radial scalar modulus, and a U(1) covariant derivative whose angular component vanishes at infinity. In the current normalization the energy has an explicit 1/2 scalar kinetic term, the BPS point is lambda=g^2/2, and the unit-winding BPS target is E=pi for N0=1. This is standard vortex machinery, not a novelty claim.
```

## 14. Next Use

Use this file as the base technical reference before writing any interpretive Field 01 note. Any nonstandard interpretation should cite this file only for the standard vortex substrate and must state its own definitions, hypotheses, and open problems separately.