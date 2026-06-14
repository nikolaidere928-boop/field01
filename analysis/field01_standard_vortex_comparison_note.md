# Standard Vortex Comparison Note

Purpose: isolate the standard field-theory content of the current toy model and remove the interpretive language. This note should be usable as a sanity check before any public discussion.

## 1. Minimal Question

Does the following two-dimensional screened phase-winding ansatz reduce to, or most closely resemble, the Abelian-Higgs / Nielsen-Olesen vortex construction?

The toy ingredients are:

```math
\varphi = n\theta,
\qquad
N=N(r),
\qquad
A_\theta=a(r),
\qquad
D_\mu\varphi=\partial_\mu\varphi-A_\mu.
```

The winding number is:

```math
Q_{\mathrm{wind}}
=\frac{1}{2\pi}\oint_C d\varphi
=n.
```

The screened angular-gradient term is:

```math
N^2 |D\varphi|^2
\sim
\frac{(n-a(r))^2N(r)^2}{r^2}.
```

## 2. Standard Translation

The closest standard packaging is a complex scalar field in polar form:

```math
\Psi(x)=N(x)e^{i\varphi(x)}.
```

With a U(1) gauge field:

```math
D_\mu\Psi=(\partial_\mu-iA_\mu)\Psi.
```

Then:

```math
|D_\mu\Psi|^2
=(\partial_\mu N)(\partial^\mu N)
+N^2(\partial_\mu\varphi-A_\mu)(\partial^\mu\varphi-A^\mu).
```

So the pair `(N, phi)` is mathematically just the polar decomposition of a complex scalar, and `A_mu` is naturally described as a U(1) gauge field or Abelian connection.

## 3. Static 2D Energy Skeleton

A standard-like static energy density has the schematic form:

```math
\mathcal E
=\frac{1}{2}|D_i\Psi|^2
+\frac{1}{4}F_{ij}F_{ij}
+V(|\Psi|),
\qquad i,j=1,2.
```

In polar variables:

```math
\mathcal E
=\frac{1}{2}(\partial_iN)^2
+\frac{1}{2}N^2(\partial_i\varphi-A_i)^2
+\frac{1}{4}F_{ij}F_{ij}
+V(N).
```

For the radial ansatz this produces the characteristic screened angular term:

```math
\frac{1}{2}\frac{(n-a(r))^2N(r)^2}{r^2}.
```

This is the main reason the toy model should be compared first with Abelian-Higgs / Nielsen-Olesen vortices.

## 4. Boundary Conditions To State Clearly

For a vortex-like finite-energy configuration, one normally expects conditions of the following type:

```math
N(0)=0,
\qquad
N(r\to\infty)\to N_0,
```

```math
a(0)=0,
\qquad
a(r\to\infty)\to n,
```

up to conventions for how `A_theta` and `a(r)` are normalized.

The essential idea is:

```text
bare phase winding remains topological, but the covariant phase gradient is screened at large radius.
```

That is:

```math
\oint d\varphi=2\pi n,
\qquad
D_\theta\varphi=n-a(r)\to0
\quad\text{as}\quad r\to\infty.
```

## 5. Safe Terminology

Use:

- `complex scalar in polar form`;
- `phase winding`;
- `winding number`;
- `U(1) gauge field` or `Abelian gauge field`;
- `covariant derivative`;
- `gauge-covariant phase gradient`;
- `asymptotic cancellation of the angular covariant derivative`;
- `radial vortex ansatz`;
- `Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex-like structure`.

Avoid in the technical comparison:

- `memory`;
- `normal retention`;
- `particle`;
- `universe`;
- `horizon`;
- `new theory`;
- `explains`.

## 6. What Is Standard

The following should be treated as standard or standard-like, not novel:

| Toy notation | Standard reading |
|---|---|
| `phi` | phase of a complex scalar |
| `N(r)` | scalar modulus / radial amplitude |
| `Q_wind` | winding number |
| `A_mu` | U(1) gauge field / Abelian connection |
| `D_mu phi` | gauge-invariant phase gradient |
| `(n-a(r))^2 N(r)^2 / r^2` | screened vortex angular-gradient term |
| `F_{mu nu}` | Abelian field strength |

## 7. What Is Not Established

The toy model does not yet establish:

- a new particle model;
- electric charge;
- spin;
- Standard Model structure;
- a black-hole or horizon model;
- a new interpretation of quantum mechanics;
- a physically predictive theory.

At this stage the honest statement is:

```text
The minimal screened phase-winding toy model appears to be in the same mathematical class as standard Abelian-Higgs / Nielsen-Olesen vortex ansatzes, unless additional structure is defined.
```

## 8. If Keeping Field 01 Interpretation Separate

The separate Field 01 interpretation may use `N` as a proxy for local depth or normal retention, and may read winding as preserved phase-structural data. But this must be explicitly separated from the standard mathematics.

Safe wording:

```text
Mathematically, this is closest to a standard Abelian-Higgs vortex ansatz. My additional language about depth, retention, or memory is interpretive and should not be presented as part of the standard construction.
```

## 9. Minimal Public Question

A narrow public question should look like this:

```text
I have a 2D radial ansatz with phi=n theta, a scalar modulus N(r), and a U(1)-like gauge field with D_mu phi = partial_mu phi - A_mu. The energy contains a term like (n-a(r))^2 N(r)^2/r^2. Is the closest standard reference the Abelian-Higgs / Nielsen-Olesen vortex? If yes, what conventions should I use for a(r), A_theta, and the boundary conditions?
```