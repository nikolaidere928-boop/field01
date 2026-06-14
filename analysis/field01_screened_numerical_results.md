# Field 01 Screened Toy Numerical Results

This file records the first numerical check of the screened phase-normal toy model. The purpose is to test whether a gauge-like screening field can reduce the long-range winding cost and create a bridge toward charge-like structure.

Related files:

- `analysis/field01_screened_phase_normal_model.md` — screened model and equations.
- `analysis/numerics/solve_screened_phase_normal_profile.py` — numerical solver.
- `analysis/numerics/screened_phase_normal_results.json` — numerical summary.
- `analysis/numerics/screened_particle_boundary_screened_profile.csv` — screened particle-like profile.
- `analysis/numerics/screened_horizon_boundary_screened_profile.csv` — screened horizon-like profile.
- `analysis/numerics/screened_phase_normal_profiles.png` — plot of `N(r)` and `a(r)`.

## 1. Equation Solved

The screened toy energy is

```math
E_n[N,a]
=2\pi\int_0^R
\left[
\frac{A}{2}(N')^2
+\frac{B}{2}\frac{(n-a)^2N^2}{r^2}
+\frac{C}{2}\frac{(a')^2}{r^2}
+\frac{\lambda}{4}(N^2-N_0^2)^2
\right]r\,dr.
```

The equations solved were

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

Parameters:

```math
A=B=C=\lambda=N_0=1,
\qquad
n=1,
\qquad
r\in[10^{-3},12].
```

## 2. Screened Particle-Like Boundary

Boundary conditions:

```math
N(r_{\min})=0,
\qquad
a(r_{\min})=0,
\qquad
N(R)=1,
\qquad
a(R)=1.
```

Numerical result:

```text
success: true
energy on finite disk: 3.634049488649256
winding Q_phase: 1
screened phase mismatch at R: 0.0
N_mid: 0.9997910894715802
a_mid: 0.9885528318107607
max residual outside tiny core: 1.23e-7
```

Interpretation:

- the normal profile reaches the retained value `N_0`;
- the screening field reaches `a(R)=n`, cancelling the long-range phase mismatch;
- the energy on the same finite disk is much lower than in the unscreened particle-like case.

Comparison:

```text
unscreened particle-like energy: 9.009336660846957
screened particle-like energy:   3.634049488649256
```

## 3. Screened Horizon-Like Boundary

Boundary conditions:

```math
N(r_{\min})=0,
\qquad
a(r_{\min})=0,
\qquad
N(R_H)=0,
\qquad
a(R_H)=1.
```

Numerical result:

```text
success: true
energy on finite disk: 37.26388860127473
winding Q_phase: 1
screened phase mismatch at R_H: 0.0
N_mid: 0.9991663909786757
a_mid: 0.9885371618696168
N_right: ~0
a_right: 1.0
max residual outside tiny core: 1.23e-7
```

Interpretation:

- normal retention is forced to disappear at the outer boundary;
- the screening field still reaches `a(R_H)=n`;
- phase winding remains `Q=1`;
- this gives a stronger toy analogue of horizon recording: `N\to0` while compensated phase data remains on the boundary.

## 4. Main Mathematical Lesson

The screened model improves the previous toy model:

```math
\frac{n}{r}
\quad\longrightarrow\quad
\frac{n-a(r)}{r},
\qquad
a(R)\to n.
```

This removes the long-range phase mismatch at the boundary and lowers the particle-like energy on the finite disk.

Field 01 reading:

```text
a closed phase node may require a field response that compensates its external phase mismatch.
```

This is the first mathematical bridge toward charge-like or gauge-like structure, but not yet a derivation of electromagnetism.

## 5. Cautions

The screening field `a(r)` is not yet a physical electromagnetic potential. To become gauge theory, the model must still define:

- gauge transformations;
- a conserved current;
- coupling to matter fields;
- relation to electric charge;
- spin and polarization;
- relativistic covariance;
- comparison with QED or known vortex models.

## 6. Next Step

The next mathematical step is to write the screened toy model in a more standard covariant form:

```math
D_\mu\varphi = \partial_\mu\varphi - A_\mu,
```

and identify the symmetry:

```math
\varphi \mapsto \varphi + \chi,
\qquad
A_\mu \mapsto A_\mu + \partial_\mu\chi.
```

If this symmetry can be made precise, then `Q` may begin to split into two notions:

1. topological winding;
2. gauge/charge-like compensation.