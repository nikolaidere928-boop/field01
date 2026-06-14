# Field 01 Noether / Current-Like Notes

This note derives the first current-like object in the covariant toy version of Field 01. It is not yet electric current and not yet a Standard Model charge. It is a mathematical consequence of the phase-shift symmetry of the toy model.

Status labels:

- **Toy result** — follows inside the toy model.
- **Interpretation** — possible Field 01 meaning.
- **Open problem** — required before physical claims.

## 1. Starting Toy Lagrangian

Use the covariant-looking toy density

```math
\mathcal{L}_{\mathrm{toy}}
= \frac{A_N}{2}(\partial_\mu N)(\partial^\mu N)
+ \frac{B}{2}N^2(D_\mu\varphi)(D^\mu\varphi)
- V(N)
- \frac{C}{4}F_{\mu\nu}F^{\mu\nu},
```

with

```math
D_\mu\varphi = \partial_\mu\varphi - A_\mu,
```

and

```math
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
```

The only dependence on `\varphi` is through `\partial_\mu\varphi` inside `D_\mu\varphi`.

## 2. Phase-Shift Symmetry

The toy Lagrangian is invariant under a global phase shift

```math
\varphi \mapsto \varphi + \epsilon,
\qquad
\epsilon=\mathrm{const}.
```

This gives a Noether-like current

```math
J^\mu
= \frac{\partial\mathcal{L}_{\mathrm{toy}}}{\partial(\partial_\mu\varphi)}.
```

Since

```math
\frac{\partial D_\alpha\varphi}{\partial(\partial_\mu\varphi)}=\delta^\mu_{\alpha},
```

we get

```math
\boxed{
J^\mu = B N^2 D^\mu\varphi
}
```

up to sign conventions depending on the metric and Lagrangian sign.

## 3. Conservation From The Phase Equation

The Euler-Lagrange equation for `\varphi` is

```math
\partial_\mu\left(
\frac{\partial\mathcal{L}_{\mathrm{toy}}}{\partial(\partial_\mu\varphi)}
\right)
-\frac{\partial\mathcal{L}_{\mathrm{toy}}}{\partial\varphi}=0.
```

Because `\mathcal{L}_{\mathrm{toy}}` has no explicit `\varphi` dependence,

```math
\frac{\partial\mathcal{L}_{\mathrm{toy}}}{\partial\varphi}=0.
```

Therefore

```math
\boxed{
\partial_\mu J^\mu=0
}
```

with

```math
J^\mu=B N^2D^\mu\varphi.
```

**Toy result:** the covariant phase-normal model has a conserved current associated with global phase-shift symmetry.

## 4. Gauge Field Equation And Source

Variation with respect to `A_\mu` gives a field equation of the schematic form

```math
C\partial_\nu F^{\nu\mu} + B N^2D^\mu\varphi = 0,
```

or, depending on sign convention,

```math
C\partial_\nu F^{\nu\mu} = -J^\mu.
```

Thus the same object

```math
J^\mu = B N^2D^\mu\varphi
```

acts as the source for the compensating field `A_\mu`.

**Interpretation:** in the toy model, current is not added by hand. It appears as the covariant phase mismatch weighted by normal retention.

## 5. Field 01 Reading

The current-like object can be read as

```math
J^\mu \sim \text{retained phase flow that still requires compensation}.
```

Because it contains `N^2`, the current is strongest where normal retention exists:

```math
N\neq0 \quad \Rightarrow \quad J^\mu \text{ may exist}.
```

If the normal disappears,

```math
N\to0,
```

then locally

```math
J^\mu\to0
```

unless boundary/topological data remains separately encoded.

This fits the Field 01 distinction:

- local particle regime: retained normal + phase circulation;
- horizon boundary regime: normal suppressed, phase record may remain as boundary data.

## 6. Winding, Covariant Mismatch, And Current

The toy model now has three related but distinct structures:

```math
Q_{\mathrm{wind}}=\frac{1}{2\pi}\oint d\varphi,
```

```math
Q_{\mathrm{cov}}=\frac{1}{2\pi}\oint(d\varphi-A),
```

```math
J^\mu=BN^2D^\mu\varphi.
```

Interpretation:

- `Q_wind` records closed phase topology;
- `Q_cov` measures unscreened phase mismatch;
- `J^\mu` measures local retained covariant phase flow.

This is a better mathematical separation than saying simply "charge = winding".

## 7. Why This Is Not Yet Electric Charge

The current-like object is conserved inside the toy model, but it is not yet physical electric current.

Missing pieces:

1. correct relativistic signs and units;
2. coupling constants and dimensional analysis;
3. relation to U(1) electromagnetism;
4. relation to photon degrees of freedom;
5. quantization of charge;
6. comparison with known matter fields;
7. experimental interpretation.

Therefore the safe statement is:

```text
The toy model has a conserved phase-compensation current. This may be a bridge toward charge-like structure, but it is not yet electric charge.
```

## 8. Horizon Limit

At a horizon-like boundary, the toy model uses

```math
N(R_H)\to0.
```

Then the local current density tends to vanish:

```math
J^\mu(R_H)\to0
```

if `D^\mu\varphi` remains finite.

But the winding record may still remain:

```math
Q_{\mathrm{wind}}=n.
```

Interpretation:

```text
local retained current can disappear while topological/boundary phase record remains.
```

This strengthens the distinction between local dynamics and boundary memory.

## 9. Next Mathematical Step

The next useful step is dimensional analysis and comparison with known Abelian Higgs / vortex structures. The question is:

```text
Is this toy model merely an Abelian-Higgs-like analogy, or can Field 01 add a distinct interpretation through normal retention and memory?
```

That comparison must be explicit before any stronger claim is made.

## 10. Symbolic Sanity Check

The current formula was checked symbolically with `sympy` using the Euclidean-sign phase term

```math
\mathcal{L}_{\mathrm{phase}}
=\frac{B}{2}N^2\left[(\partial_x\varphi-A_x)^2+(\partial_y\varphi-A_y)^2\right].
```

The symbolic derivatives give

```math
\frac{\partial\mathcal{L}_{\mathrm{phase}}}{\partial(\partial_x\varphi)}
=BN^2(\partial_x\varphi-A_x),
```

```math
\frac{\partial\mathcal{L}_{\mathrm{phase}}}{\partial(\partial_y\varphi)}
=BN^2(\partial_y\varphi-A_y).
```

So

```math
J_i=BN^2D_i\varphi.
```

The variation with respect to the compensating field gives the opposite sign:

```math
\frac{\partial\mathcal{L}_{\mathrm{phase}}}{\partial A_i}=-J_i.
```

Thus the same current appears as the source term for the compensating field equation, with sign depending on the convention used for the full action.