# Field 01 Math Core v0

Purpose: define the smallest technical core that can be compared with standard field theory. This file deliberately avoids interpretive language such as memory, universe, particle, horizon, consciousness, or new theory.

Status: toy model / comparison draft. Not a physical theory and not a claim of novelty.

## 1. Minimal State Variables

Work on a two-dimensional spatial domain or spatial slice with polar coordinates `(r, theta)`.

Use the following fields:

```math
N(r)\ge 0,
\qquad
\varphi(r,\theta)=n\theta,
\qquad
A_i(r),
\qquad i=1,2.
```

Where:

- `N(r)` is a scalar modulus / radial amplitude;
- `phi` is a compact phase;
- `n` is an integer winding number;
- `A_i` is a U(1)-like Abelian gauge field;
- `D_i phi = partial_i phi - A_i` is the gauge-covariant phase gradient; `screened phase gradient` is only a local shorthand after this definition.

Package `N` and `phi` as a complex scalar:

```math
\Psi=N e^{i\varphi}.
```

## 2. Winding Number

The topological winding of the phase around a closed contour `C` is:

```math
Q_{\mathrm{wind}}
=\frac{1}{2\pi}\oint_C d\varphi
=n,
\qquad n\in\mathbb Z.
```

For the ansatz `phi = n theta`, this gives integer winding around the origin.

## 3. Gauge-Covariant Phase Gradient

Define:

```math
D_i\varphi=\partial_i\varphi-A_i.
```

Under the U(1)-like transformation:

```math
\varphi\mapsto\varphi+\chi,
\qquad
A_i\mapsto A_i+\partial_i\chi,
```

one has:

```math
D_i\varphi\mapsto D_i\varphi.
```

Thus `D_i phi` is the gauge-invariant / gauge-covariant phase-gradient object used in the energy.

The field strength is:

```math
F_{ij}=\partial_iA_j-\partial_jA_i.
```

## 4. Static Energy Skeleton

A minimal standard-like static energy density is:

```math
\mathcal E
=\frac{1}{2}(\partial_iN)^2
+\frac{1}{2}N^2(D_i\varphi)^2
+\frac{1}{4g^2}F_{ij}F_{ij}
+V(N).
```

A typical symmetry-breaking potential may be written as:

```math
V(N)=\frac{\lambda}{4}(N^2-N_0^2)^2.
```

This is structurally the polar-variable form of a U(1) Abelian-Higgs-like scalar-gauge model.

## 5. Radial Vortex Ansatz

For a rotational ansatz, choose conventions such that:

```math
\varphi=n\theta,
\qquad
A=a(r)\,d\theta,
\qquad
A_r=0,
\qquad
N=N(r).
```

Then the angular part of the covariant phase-gradient term has the schematic form:

```math
N^2(D\varphi)^2
\supset
\frac{(n-a(r))^2N(r)^2}{r^2}.
```

The exact radial functional depends on the convention used for the coordinate one-form profile `a(r)`, metric factors in polar coordinates, and normalization of the gauge coupling. These conventions must be stated explicitly before comparing equations term-by-term. In the current convention, `a(r)` is dimensionless and can be written equivalently as `A=a(r)\,d\theta` or `\mathcal A=(a(r)/g)\,d\theta` when the coupling is placed in the covariant derivative.

## 6. Boundary Conditions

For a finite-energy vortex-like configuration one normally expects conditions of the form:

```math
N(0)=0,
\qquad
N(r\to\infty)=N_0,
```

```math
a(0)=0,
\qquad
a(r\to\infty)=n,
```

again up to normalization conventions.

The qualitative content is:

```text
The bare phase has nonzero winding, but the covariant phase gradient is screened at large radius.
```

That is:

```math
\oint d\varphi=2\pi n,
\qquad
D_\theta\varphi=n-a(r)\to0
\quad\text{as}\quad r\to\infty.
```

## 7. What This Core Can Claim

Safe claims:

1. The ansatz contains a compact phase with integer winding.
2. The scalar profile `N(r)` acts like the modulus of a complex scalar.
3. The gauge field screens the angular phase gradient.
4. The energy skeleton is standard-like and close to Abelian-Higgs / Nielsen-Olesen vortex mathematics.
5. The construction should be checked against standard vortex conventions before any interpretation is added.

## 8. What This Core Cannot Claim

This core does not establish:

- a particle spectrum;
- electric charge;
- spin;
- Standard Model gauge structure;
- gravity;
- black-hole physics;
- quantum measurement theory;
- a new interpretation of quantum mechanics;
- any experimental prediction.

## 9. Terminology Rules

Use in technical sections:

- `complex scalar`;
- `scalar modulus`;
- `phase`;
- `winding number`;
- `U(1) gauge field`;
- `covariant derivative`;
- `gauge-covariant phase gradient`;
- `asymptotic cancellation of the angular covariant derivative`;
- `field strength`;
- `radial vortex ansatz`;
- `Abelian-Higgs-like`;
- `Nielsen-Olesen-like`.

Avoid in technical sections:

- `memory`;
- `normal retention`;
- `closed wave as particle`;
- `horizon`;
- `universe`;
- `consciousness`;
- `explains`;
- `proof`;
- `new theory`.

If interpretive terms are used elsewhere, label them explicitly as interpretation and not as part of this mathematical core.

## 10. Immediate Open Problems

Before this can be presented as more than a toy comparison, define:

1. the exact action or static energy functional;
2. units and dimensions of all fields and couplings;
3. the precise polar-coordinate convention for `A_theta` and `a(r)`;
4. the boundary conditions at `r=0` and `r=infinity`, including near-core regularity `N(r)~r^|n|` and `a(r)~O(r^2)`;
5. whether the domain is infinite, finite, or bounded;
6. how the toy equations relate to standard Abelian-Higgs vortex equations;
7. whether anything remains after subtracting the standard Abelian-Higgs content.

## 11. One-Sentence Summary

```text
The current mathematical core is a 2D U(1) scalar-gauge vortex-like toy ansatz with phase winding, radial scalar modulus, and an angular covariant derivative that vanishes asymptotically; its first comparison targets are Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex conventions.
```