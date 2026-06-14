# Vortex Convention Dictionary

Purpose: translate the current radial vortex notation into common Abelian-Higgs / Nielsen-Olesen-style conventions, and mark where factors of `e`, `g`, `2`, and `r` can move.

Status: standard-math comparison aid. No Field 01 interpretation is used here.

External feedback update: use the broader standard label set `Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau vortex`, and prefer covariant-derivative language over informal `angular screening` language. Also, do not present the ansatz as physics without an explicit action, Lagrangian, Hamiltonian, or energy functional.

## 1. Our Current Convention

The current technical core uses:

```math
\Psi=N(r)e^{in\theta},
\qquad
A_r=0,
\qquad
A_\theta=a(r),
```

with:

```math
D_i\Psi=(\partial_i-iA_i)\Psi,
\qquad
B=\frac{a'(r)}{r}.
```

The energy is:

```math
E=\int d^2x\left[
\frac{1}{2}|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right].
```

The radial energy is:

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

Boundary conditions for the standard finite-energy vortex-like case:

```math
N(0)=0,
\qquad
N(\infty)=N_0,
\qquad
a(0)=0,
\qquad
a(\infty)=n.
```

Flux in this convention:

```math
\Phi_B=2\pi n.
```

Critical coupling in this convention:

```math
\lambda_{\mathrm{BPS}}=\frac{g^2}{2},
\qquad
\beta=\frac{2\lambda}{g^2},
\qquad
\beta_{\mathrm{BPS}}=1.
```

## 1.1 Standard Names And Scope

The same radial vortex machinery appears under several closely related names:

- Abelian-Higgs vortex;
- Nielsen-Olesen vortex;
- Abrikosov vortex;
- Ginzburg-Landau vortex.

Scope warning:

```text
These names identify the standard mathematical construction only. They do not validate any Field 01 interpretation of memory, normal retention, horizon behavior, or charge-like meaning.
```

Terminology preference:

```text
Use "the angular component of the covariant derivative tends to zero at infinity" rather than "angular screening" as the main technical phrase.
```

## 2. Mapping To A Common `e A_i` Convention

A common reference convention places the gauge coupling inside the covariant derivative:

```math
D_i^{\mathrm{ref}}=\partial_i-ieA_i^{\mathrm{ref}},
```

and uses a canonical Maxwell term:

```math
E_{\mathrm{ref}}=\int d^2x\left[
\frac{1}{2}|D_i^{\mathrm{ref}}\Phi|^2
+\frac{1}{2}(B^{\mathrm{ref}})^2
+\frac{\lambda_{\mathrm{ref}}}{4}(|\Phi|^2-v^2)^2
\right].
```

The dictionary is:

| Our notation | Reference notation | Comment |
|---|---|---|
| `Psi` | `Phi` | complex scalar |
| `N(r)` | `|Phi|` or `v h(r)` | scalar modulus |
| `N0` | `v` | vacuum modulus |
| `A_i` | `e A_i^ref` | our gauge field absorbs charge |
| `g` | `e` | if matching canonical Maxwell term |
| `B` | `e B^ref` | because `A=e A_ref` |
| `lambda` | `lambda_ref` | same potential coefficient in this normalization |
| `Phi_B = 2pi n` | `Phi_B^ref = 2pi n/e` | physical flux if using `A_ref` |
| `beta = 2 lambda / g^2` | `beta = 2 lambda_ref / e^2` | BPS at `beta=1` |

Thus:

```math
A_i=eA_i^{\mathrm{ref}},
\qquad
B=eB^{\mathrm{ref}},
\qquad
g=e.
```

## 2.1 Mapping To Schaposnik's `Vortices` Convention

Schaposnik's Abelian-Higgs energy per unit length is written as:

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

Schaposnik's critical condition:

```math
e^2=8\lambda_S
```

therefore maps to:

```math
\lambda_{ours}=\frac{g^2}{2}.
```

Schaposnik's BPS bound:

```math
E_S\ge\pi\phi_0^2|N|
```

maps to the current normalization target:

```math
E_{ours,\mathrm{BPS}}=\pi N_0^2|n|.
```

This is consistent with using the `pi` target in the explicit `1/2 |D_i\Psi|^2` scalar-kinetic normalization.

## 3. Radial Gauge Profile Conventions

Different references define the radial gauge profile differently. The same configuration may appear in at least three forms.

### 3.1 Coordinate One-Form Convention

This is the current convention:

```math
A_\theta=a(r),
\qquad
D_\theta\varphi=n-a(r),
\qquad
B=\frac{a'}{r}.
```

Boundary conditions:

```math
a(0)=0,
\qquad
a(\infty)=n.
```

### 3.2 Normalized Increasing Profile `alpha(r)`

Many references use a dimensionless increasing profile:

```math
a(r)=n\alpha(r).
```

Then:

```math
\alpha(0)=0,
\qquad
\alpha(\infty)=1.
```

The screened angular mismatch becomes:

```math
n-a(r)=n[1-\alpha(r)].
```

### 3.3 Decreasing Profile `P(r)`

Some references instead use a decreasing profile:

```math
P(r)=1-\alpha(r),
\qquad
a(r)=n[1-P(r)].
```

Then:

```math
P(0)=1,
\qquad
P(\infty)=0.
```

The screened angular mismatch becomes:

```math
n-a(r)=nP(r).
```

This convention is common because the scalar angular-gradient term becomes proportional to:

```math
\frac{n^2P(r)^2N(r)^2}{r^2}.
```

## 4. Scalar Profile Conventions

The scalar modulus may be written in dimensional or dimensionless form.

Our convention:

```math
N(r).
```

Dimensionless scalar profile:

```math
h(r)=\frac{N(r)}{N_0}.
```

Then:

```math
h(0)=0,
\qquad
h(\infty)=1.
```

If a reference writes:

```math
\Phi=v f(r)e^{in\theta},
```

then the mapping is:

```math
v=N_0,
\qquad
f(r)=h(r)=\frac{N(r)}{N_0}.
```

## 5. BPS Equations In Different Profiles

Our BPS equations for positive `n` are:

```math
N'=\frac{n-a}{r}N,
```

```math
\frac{a'}{r}=\frac{g^2}{2}(N_0^2-N^2).
```

Using:

```math
N=N_0h,
\qquad
a=n\alpha=n(1-P),
```

these become:

```math
h'=\frac{n(1-\alpha)}{r}h
=\frac{nP}{r}h,
```

```math
\frac{n\alpha'}{r}
=-\frac{nP'}{r}
=\frac{g^2N_0^2}{2}(1-h^2).
```

A dimensionless radius can be chosen as:

```math
\rho=\frac{gN_0}{\sqrt{2}}r.
```

Then the BPS equations become:

```math
\frac{dh}{d\rho}=\frac{nP}{\rho}h,
```

```math
-\frac{n}{\rho}\frac{dP}{d\rho}=1-h^2.
```

or equivalently:

```math
\frac{n}{\rho}\frac{d\alpha}{d\rho}=1-h^2.
```

## 6. Energy Normalization Warnings

References may differ by factors of `1/2` in the scalar kinetic term, Maxwell term, and potential. Therefore the following quantities are convention-sensitive:

- the numerical value of `lambda_BPS`;
- whether the BPS energy is written as `pi N0^2 n` or `2 pi v^2 n`;
- whether the flux is `2 pi n` or `2 pi n/e`;
- whether `A_theta` denotes a coordinate component or a physical angular component;
- whether `a(r)` tends to `n`, `1`, or `0` at infinity.

The safest comparison procedure is:

1. write the reference energy functional;
2. identify where the gauge coupling appears;
3. identify whether the radial gauge profile is increasing or decreasing;
4. map the boundary conditions;
5. only then compare BPS coupling and energy.

## 7. Minimal Dictionary Table

| Concept | Our symbol | Common alternatives |
|---|---|---|
| standard names | Abelian-Higgs / Nielsen-Olesen | Abrikosov, Ginzburg-Landau |
| complex scalar | `Psi` | `Phi`, `phi` |
| scalar modulus | `N(r)` | `f(r)`, `v f(r)`, `h(r)` |
| vacuum modulus | `N0` | `v`, `eta` |
| phase | `varphi=n theta` | `arg Phi = n theta` |
| winding | `n` | `m`, `N`, vortex number |
| gauge field | `A_i` | `e A_i`, `A_i^ref` |
| angular gauge profile | `a(r)` | `n alpha(r)`, `n[1-P(r)]` |
| increasing gauge profile | `alpha=a/n` | `a_ref`, `A(r)` |
| decreasing gauge profile | `P=1-a/n` | `P(r)`, `1-alpha` |
| magnetic field | `B=a'/r` | `F12`, `B_z` |
| flux | `2 pi n` | `2 pi n/e` |
| coupling ratio | `beta=2 lambda/g^2` | GL parameter, type-I/type-II parameter |
| BPS point | `beta=1` | critical coupling |

## 8. Physics Threshold

A radial ansatz plus boundary conditions is not, by itself, a complete physical theory. Before making physics claims, state at least one of:

- an action;
- a Lagrangian density;
- a Hamiltonian;
- an energy functional;
- equations of motion derived from one of the above.

Practical wording rule:

```text
Before the energy/action is explicit, say "toy ansatz" or "standard vortex-like mathematical structure", not "new physical model".
```

## 9. Public-Safe Summary

```text
My notation uses A_theta=a(r), so the angular covariant-derivative term is (n-a)^2 N^2/r^2. Many references instead write a(r)=n alpha(r) or a(r)=n[1-P(r)]. In those conventions the same term becomes n^2(1-alpha)^2N^2/r^2 or n^2P^2N^2/r^2. The coupling convention also differs: I put the gauge coupling in the Maxwell term, so the BPS point is lambda=g^2/2, equivalently beta=2lambda/g^2=1. BPS energy comparisons are normalization-sensitive: Schaposnik uses a 1/2 scalar-kinetic convention and gives E >= pi phi0^2 |N|, which maps to our pi N0^2 |n| target; many other references write 2 pi v^2 |n| with a different scalar normalization.
```