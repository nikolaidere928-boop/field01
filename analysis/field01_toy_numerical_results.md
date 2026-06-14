# Field 01 Toy Numerical Results

This file records the first numerical check of the phase-normal toy model. It is not a physical prediction. It only tests whether the toy radial equation admits regular-looking profiles with winding and normal retention.

Related files:

- `analysis/field01_toy_phase_normal_model.md` — model definition and radial equation.
- `analysis/numerics/solve_phase_normal_profile.py` — numerical solver.
- `analysis/numerics/phase_normal_profile_results.json` — numerical summary.
- CSV profile tables and PNG plots can be regenerated locally from the solver if needed; they are not part of the compact public package.

## 1. Equation Solved

For the toy energy functional

```math
E_n[N]
= 2\pi\int_0^R
\left[
\frac{A}{2}(N')^2
+ \frac{B}{2}\frac{n^2N^2}{r^2}
+ \frac{\lambda}{4}(N^2-N_0^2)^2
\right]r\,dr,
```

the radial Euler-Lagrange equation is

```math
A\left(N''+\frac{1}{r}N'\right)
- B\frac{n^2}{r^2}N
- \lambda N(N^2-N_0^2)=0.
```

The numerical test used

```math
A=B=\lambda=N_0=1,
\qquad
n=1,
\qquad
r\in[10^{-3},12].
```

## 2. Particle-Like Boundary Condition

Boundary condition:

```math
N(r_{\min})=0,
\qquad
N(R)=N_0=1.
```

Numerical result:

```text
success: true
energy on finite disk: 9.009336660846957
winding Q: 1
N_left: ~0
N_mid: 0.9847639451614029
N_right: 1.0
max residual outside tiny core: 1.72e-7
```

Interpretation:

- the normal profile rises from zero near the core to the retained value `N_0`;
- the winding remains `Q=1`;
- the configuration is a clean toy analogue of a closed phase-normal node.

## 3. Horizon-Like Boundary Condition

Boundary condition:

```math
N(r_{\min})=0,
\qquad
N(R_H)=0.
```

Numerical result:

```text
success: true
energy on finite disk: 42.20836854396651
winding Q: 1
N_left: ~0
N_mid: 0.9840932299502564
N_right: ~0
max residual outside tiny core: 2.42e-7
```

Interpretation:

- the profile rises in the interior but is forced back to zero at the outer boundary;
- this is a toy analogue of normal suppression at a horizon-like boundary;
- the winding remains `Q=1`, so the phase record can still be represented at the boundary even when `N(R_H)=0`.

## 4. Main Mathematical Lesson

The numerical test supports the internal consistency of the toy picture:

```math
\text{closed phase circulation} + \text{normal profile}
\quad \Rightarrow \quad
\text{regular field-like node on a finite domain}.
```

For the horizon-like boundary:

```math
N(R_H)\to0,
\qquad
Q_{\partial}=1.
```

This gives a concrete mathematical analogue of the Field 01 statement:

```text
the normal disappears at the boundary, but the phase/winding record can remain.
```

## 5. Important Cautions

This result does not prove Field 01 as physics. It only shows that the proposed language has a nontrivial toy realization.

Still missing:

- a relativistic action;
- a true finite-energy infinite-domain solution;
- gauge structure;
- spin;
- particle spectrum;
- relation to the Higgs mechanism;
- relation to real black-hole geometry;
- derivation of Hawking thermality;
- observational predictions.

## 6. Next Mathematical Step

The next useful step is to improve the toy model so the energy is finite on an infinite domain. A natural direction is to add a gauge-like connection or screening field, analogous in spirit to how vortex models avoid long-range logarithmic divergence.

Possible next target:

```math
D\varphi = d\varphi - A_\theta d\theta,
```

and replace

```math
|\nabla\varphi|^2
```

by

```math
|D\varphi|^2.
```

This may become the first bridge toward charge/gauge-like structure in Field 01.