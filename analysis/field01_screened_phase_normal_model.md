# Field 01 Screened Phase-Normal Toy Model

This note extends the first phase-normal toy model by adding a gauge-like screening field. The purpose is not to claim that Field 01 has derived electromagnetism. The purpose is narrower: to remove the long-range logarithmic divergence of a bare phase winding and to create a first mathematical bridge toward charge/gauge-like structure.

Status labels:

- **Toy definition** — mathematical test object only.
- **Model interpretation** — possible Field 01 meaning.
- **Result** — consequence inside the toy model.
- **Open problem** — not solved here.

## 1. Why Screening Is Needed

The unscreened phase-normal model uses

```math
\varphi_n=n\theta,
\qquad
N=N(r).
```

The phase-gradient term behaves as

```math
|\nabla\varphi_n|^2 = \frac{n^2}{r^2},
```

so the energy contains

```math
\int \frac{n^2}{r^2}r\,dr \sim \log R.
```

This means a bare winding is not finite-energy on an infinite plane.

Field 01 interpretation:

```text
closed phase circulation requires a compensating/screening structure if it is to become a localized finite-energy node.
```

This is the first mathematical reason to introduce a gauge-like connection.

## 2. Gauge-Like Phase Compensation

Introduce a circular screening function `a(r)` by replacing the bare angular phase gradient with

```math
\frac{n}{r}
\quad \longrightarrow \quad
\frac{n-a(r)}{r}.
```

Equivalently, define a covariant phase derivative

```math
D_\theta\varphi = \partial_\theta\varphi - a(r),
```

so that for `\varphi=n\theta`,

```math
D_\theta\varphi_n = n-a(r).
```

Boundary behavior for screening:

```math
a(0)=0,
\qquad
a(r)\to n \quad \text{as } r\to\infty.
```

Then the angular phase energy changes from

```math
\frac{n^2N^2}{r^2}
```

to

```math
\frac{(n-a)^2N^2}{r^2}.
```

If `a(r)\to n`, the long-range phase-gradient cost is screened.

## 3. Screened Energy Functional

A minimal screened radial functional is

```math
E_n[N,a]
=2\pi\int_0^R
\left[
\frac{A}{2}(N')^2
+\frac{B}{2}\frac{(n-a)^2N^2}{r^2}
+\frac{C}{2}\frac{(a')^2}{r^2}
+V(N)
\right]r\,dr.
```

Use the same retention potential as before:

```math
V(N)=\frac{\lambda}{4}(N^2-N_0^2)^2.
```

Interpretation of terms:

- `A(N')^2/2` — cost of changing normal retention;
- `B(n-a)^2N^2/(2r^2)` — screened phase-retention cost;
- `C(a')^2/(2r^2)` — cost of changing the screening field;
- `V(N)` — allowed retention regimes.

This resembles a vortex-like gauge-field structure, but here it is only a toy Field 01 screening mechanism.

## 4. Euler-Lagrange Equations

For

```math
L(r,N,N',a,a')
= r\left[
\frac{A}{2}(N')^2
+\frac{B}{2}\frac{(n-a)^2N^2}{r^2}
+\frac{C}{2}\frac{(a')^2}{r^2}
+\frac{\lambda}{4}(N^2-N_0^2)^2
\right],
```

the radial equations are

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{(n-a)^2}{r^2}N
- \lambda N(N^2-N_0^2)=0,
```

and

```math
a''-\frac{1}{r}a'
+\frac{B}{C}(n-a)N^2=0.
```

These are the first screened toy equations.

## 5. Finite-Energy Boundary Conditions

A particle-like finite-energy profile should satisfy approximately

```math
N(0)=0,
\qquad
a(0)=0,
```

and

```math
N(\infty)=N_0,
\qquad
a(\infty)=n.
```

Then far from the core,

```math
\frac{(n-a)^2N^2}{r^2}\to0,
```

so the logarithmic divergence of the bare winding is removed.

## 6. Field 01 Interpretation

The screening function `a(r)` can be read cautiously as the first mathematical proxy for phase compensation:

```math
a(r) \sim \text{field response that cancels long-range phase mismatch}.
```

This may become a bridge toward charge only if a later version shows that:

1. `a` transforms as a connection;
2. the energy is invariant under a phase symmetry;
3. a conserved current exists;
4. the construction relates to known gauge theory.

Until then, `a(r)` is only a screening variable.

## 7. Horizon-Like Boundary Variant

For a horizon-like boundary, one may impose

```math
N(R_H)=0
```

while the boundary phase/screening data may still carry winding information:

```math
Q_\partial
=\frac{1}{2\pi}\oint d\varphi = n.
```

A useful question is whether the screened model permits a configuration where

```math
N(R_H)=0,
\qquad
a(R_H)\approx n,
```

so that normal retention disappears at the boundary while the screened phase record remains encoded in boundary data.

## 8. What This Adds To The Previous Toy Model

The previous model showed:

```math
\text{closed phase} + N(r) \Rightarrow \text{regular finite-domain node}.
```

The screened model adds:

```math
\text{closed phase} + N(r) + a(r)
\Rightarrow
\text{candidate finite-energy localized node on a large/infinite domain}.
```

Mathematically, this is the first step toward turning the winding number into something closer to a charge-like or gauge-related structure.

## 9. What Must Be Checked Numerically

Next numerical test:

1. set `A=B=C=\lambda=N_0=1` and `n=1`;
2. solve the coupled BVP for `N(r)` and `a(r)`;
3. impose particle-like boundary conditions `N(0)=0`, `a(0)=0`, `N(R)=1`, `a(R)=1`;
4. compute energy and compare with the unscreened case;
5. test horizon-like boundary `N(R_H)=0`, `a(R_H)=1`;
6. check whether winding remains `Q=1` while normal retention disappears at the boundary.

## 10. Symbolic Sanity Check

The Euler-Lagrange equations above were checked symbolically with `sympy`.

For

```math
L(r,N,N',a,a')
= r\left[
\frac{A}{2}(N')^2
+\frac{B}{2}\frac{(n-a)^2N^2}{r^2}
+\frac{C}{2}\frac{(a')^2}{r^2}
+\frac{\lambda}{4}(N^2-N_0^2)^2
\right],
```

the symbolic variation gives exactly

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{(n-a)^2}{r^2}N
- \lambda N(N^2-N_0^2)=0,
```

and

```math
a''-\frac{1}{r}a'
+\frac{B}{C}(n-a)N^2=0.
```

So the screened equations are internally consistent at the variational level.