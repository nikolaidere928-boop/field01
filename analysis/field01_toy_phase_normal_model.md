# Field 01 Toy Phase-Normal Model

This file is a first mathematical laboratory for Field 01. It is not a claim that the model is physically complete. Its purpose is narrower: to test whether the words "open phase transport", "closed phase node", "normal retention", "mass as retention energy", and "horizon limit" can be represented by a minimal mathematical structure.

Status labels:

- **Toy definition** — chosen only for mathematical testing.
- **Model interpretation** — connection to Field 01 language.
- **Result** — consequence inside this toy model.
- **Open problem** — not solved here.

## 1. Minimal Choice

We start with the simplest possible setting:

```math
X = \mathbb{R}^2,
\qquad
\varphi : X\setminus\{0\} \to S^1,
\qquad
N : X \to \mathbb{R}_{\ge 0}.
```

Here:

- `\varphi` is the phase field;
- `N` is a scalar first approximation to the normal degree of freedom `\mathcal{N}`;
- `X=\mathbb{R}^2` is not physical spacetime, only a test domain;
- the origin is removed for the phase map because a nonzero winding cannot be globally smooth at the center.

Field 01 interpretation:

```math
\varphi \sim \text{mode-1 circulation},
\qquad
N \sim \text{mode-0 retention / local depth}.
```

## 2. Closed Phase Ansatz

Use polar coordinates `(r,\theta)` and define the winding ansatz

```math
\varphi_n(r,\theta) = n\theta,
\qquad n\in\mathbb{Z}.
```

Then

```math
\oint_{\mathcal{C}_R} d\varphi_n = 2\pi n,
```

where `\mathcal{C}_R` is a circle of radius `R` around the origin.

**Result:** the closed-wave condition from the formalization notes appears naturally as a winding number.

Field 01 reading:

```math
n=0 \quad \text{no closed node},
\qquad
n\ne0 \quad \text{closed phase circulation}.
```

## 3. Why A Normal Field Is Needed

If the phase energy is only

```math
E_\varphi = \int |\nabla\varphi|^2\,d^2x,
```

then for `\varphi_n=n\theta`,

```math
|\nabla\varphi_n|^2 = \frac{n^2}{r^2}.
```

The energy on an annulus `a\le r\le R` is

```math
E_\varphi(a,R)
= 2\pi n^2 \log\frac{R}{a}.
```

This diverges as `a\to0` and as `R\to\infty`.

**Interpretation:** a pure phase winding is not enough to produce a finite localized particle-like structure. The model needs an additional retention/profile field that regularizes the core and localizes the configuration.

This is the first mathematical meaning of the Field 01 statement:

```math
\text{massive particle} = \text{closed phase circulation} + \text{normal retention}.
```

## 4. Normal-Retention Profile

Introduce a radial normal-retention profile

```math
N(r)\ge0.
```

For a closed node, choose boundary behavior

```math
N(0)=0,
\qquad
N(r)\to N_0>0 \quad \text{for intermediate/localized region},
\qquad
N(r)\to0 \quad \text{at a horizon-like boundary or open limit}.
```

This boundary behavior is deliberately flexible. It allows two different uses:

1. **particle core regularization:** `N(0)=0` avoids a singular center;
2. **horizon limit:** `N\to0` represents loss of volumetric normal retention at a boundary.

Open problem: a realistic model must decide whether the particle vacuum has `N\to N_0` or `N\to0` far away. The toy model only tests the mechanism.

## 5. Candidate Energy Functional

A minimal radial energy can be written as

```math
E[N,\varphi]
= 2\pi\int_0^R
\left[
\frac{A}{2}(N')^2
+ \frac{B}{2}N^2(\varphi')_\theta^2
+ V(N)
\right] r\,dr.
```

For the winding ansatz `\varphi=n\theta`, the angular phase-gradient term becomes

```math
(\varphi')_\theta^2 = \frac{n^2}{r^2},
```

so

```math
E_n[N]
= 2\pi\int_0^R
\left[
\frac{A}{2}(N')^2
+ \frac{B}{2}\frac{n^2N^2}{r^2}
+ V(N)
\right]r\,dr.
```

Field 01 interpretation:

- `A(N')^2/2` — cost of changing normal retention;
- `B n^2N^2/(2r^2)` — cost of holding closed circulation with normal depth;
- `V(N)` — preference for allowed retention regimes.

## 6. Euler-Lagrange Equation For The Radial Profile

For the radial functional

```math
E_n[N] = 2\pi\int_0^R L(r,N,N')\,dr,
```

with

```math
L(r,N,N') = r\left[\frac{A}{2}(N')^2 + \frac{B}{2}\frac{n^2N^2}{r^2}+V(N)\right],
```

the Euler-Lagrange equation is

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{n^2}{r^2}N
- \frac{dV}{dN}=0.
```

This is the first concrete toy equation for a Field 01 closed node.

## 7. Example Potential

A simple double-well-like retention potential is

```math
V(N)=\frac{\lambda}{4}(N^2-N_0^2)^2.
```

Then

```math
\frac{dV}{dN}=\lambda N(N^2-N_0^2),
```

and the radial equation becomes

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{n^2}{r^2}N
- \lambda N(N^2-N_0^2)=0.
```

Near the core, the winding term forces `N(0)=0` for regularity when `n\ne0`. Away from the core, the potential may drive `N\to N_0` if the configuration is not projected to a horizon boundary.

This resembles the logic of vortex profiles in known field theories, but Field 01 is not identified with those theories at this stage.

## 8. Open Mode In The Toy Model

The open photon-like mode is represented not by a vortex, but by phase transport with no retained normal profile:

```math
N=0,
\qquad
Q=0 \text{ for local closed-node winding}.
```

The toy model does not yet describe photon polarization, gauge invariance, or spin. It only captures the Field 01 distinction:

```math
\text{open transport} \ne \text{closed retained node}.
```

## 9. Mass Proxy

Inside the toy model, a mass proxy for the closed node is the finite part of the closed-node energy:

```math
m_n c^2 \sim E_n[N_n] - E_{\mathrm{background}}.
```

where `N_n` is a stable or extremal radial profile.

This matches the Field 01 phrase:

```math
\text{mass} \sim \text{energy of retaining a closed phase-normal configuration}.
```

Open problem: this is only a proxy. It is not yet a relativistic mass spectrum and is not connected to the Higgs mechanism.

## 10. Horizon Limit In The Toy Model

Let `R_H` be a boundary interpreted as a horizon-like surface. The Field 01 horizon limit is represented as

```math
N(R_H) \to 0.
```

The phase-memory map is then represented schematically by preserving boundary phase data:

```math
\Pi_{\partial}:
(\varphi_n,N)_\mathrm{bulk}
\mapsto
[\varphi_n|_{r=R_H}]_\mathrm{boundary}.
```

If the winding is still detectable at the boundary,

```math
Q_\partial
= \frac{1}{2\pi}\oint_{r=R_H} d\varphi_n
= n.
```

**Toy result:** the normal profile can vanish at a boundary while the winding/phase record remains encoded on the boundary circle.

This is the first clean mathematical analogue of the book statement:

```math
\text{normal disappears, but phase structure is recorded on the horizon}.
```

## 11. What This Toy Model Achieves

It gives a minimal formal version of five Field 01 ideas:

1. **Closed wave:** winding condition `\oint d\varphi=2\pi n`.
2. **Normal retention:** scalar profile `N(r)` supports/localizes the closed node.
3. **No point object:** the core is a field profile, not a material point.
4. **Mass proxy:** energy of the retained closed configuration.
5. **Horizon record:** `N\to0` at a boundary while phase/winding data remains accessible as boundary information.

## 12. What It Does Not Achieve

This toy model does not yet derive:

- Standard Model particles;
- spin;
- charge;
- gauge fields;
- photon polarization;
- gravity;
- Hawking radiation;
- the Bekenstein--Hawking coefficient;
- a real black-hole horizon;
- a relativistic quantum theory.

Therefore it should be used only as a mathematical test bed.

## 13. Next Computational Check

A useful next check is numerical:

1. choose constants `A=B=\lambda=N_0=1`;
2. solve the radial equation for `n=1` with boundary conditions `N(0)=0`, `N(R)=N_0`;
3. compute the finite energy on a finite disk;
4. then impose `N(R_H)=0` to mimic a horizon boundary;
5. compare whether the winding `Q=n` remains while normal retention disappears at the boundary.

The symbolic check below should verify the Euler-Lagrange equation and the winding integral.

## 14. Symbolic Sanity Check

The following identities were checked symbolically with `sympy`.

### Winding

For `\varphi_n=n\theta`,

```math
\int_0^{2\pi} n\,d\theta = 2\pi n.
```

This confirms

```math
\oint_{\mathcal{C}} d\varphi_n = 2\pi n.
```

### Pure Phase Energy

For the pure phase term on an annulus `a\le r\le R`,

```math
\int_0^{2\pi}\int_a^R \frac{n^2}{r^2}r\,dr\,d\theta
= 2\pi n^2\log\frac{R}{a}.
```

This confirms the logarithmic divergence of a bare winding profile.

### Radial Euler-Lagrange Equation

For

```math
L(r,N,N')
= r\left[\frac{A}{2}(N')^2
+ \frac{B}{2}\frac{n^2N^2}{r^2}
+ \frac{\lambda}{4}(N^2-N_0^2)^2\right],
```

the Euler-Lagrange equation is

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{n^2}{r^2}N
- \lambda N(N^2-N_0^2)=0.
```

The symbolic check matched this expression exactly.