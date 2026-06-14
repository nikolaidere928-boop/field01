# Field 01 Covariant Gauge Bridge

This note rewrites the screened phase-normal toy model in a covariant-looking notation. It is a bridge document: it does not claim that Field 01 has derived electromagnetism or the Standard Model gauge sector. Its purpose is to identify the first precise mathematical symmetry suggested by the screened toy model.

Status labels:

- **Toy definition** — a formal structure used for testing.
- **Result** — a verified mathematical property of the toy structure.
- **Interpretation** — possible Field 01 reading.
- **Open problem** — required before physical claims can be made.

## 1. From Screening Function To Connection

The screened radial model replaced the bare phase gradient by

```math
\frac{n}{r}\quad\longrightarrow\quad\frac{n-a(r)}{r}.
```

This suggests introducing a connection-like field `A_\mu` and a covariant phase derivative

```math
D_\mu\varphi = \partial_\mu\varphi - A_\mu.
```

In polar coordinates, the previous radial ansatz corresponds schematically to

```math
\varphi=n\theta,
\qquad
A_\theta=a(r),
\qquad
D_\theta\varphi=n-a(r).
```

Field 01 interpretation:

```text
A_mu is a compensating field response that cancels long-range phase mismatch.
```

At this stage `A_\mu` is not yet the electromagnetic four-potential. It is only a gauge-like compensating variable.

## 2. Gauge-Like Transformation

Define the transformation

```math
\varphi \mapsto \varphi' = \varphi + \chi,
```

```math
A_\mu \mapsto A'_\mu = A_\mu + \partial_\mu\chi.
```

Then

```math
D'_\mu\varphi'
= \partial_\mu(\varphi+\chi) - (A_\mu+\partial_\mu\chi)
= \partial_\mu\varphi - A_\mu
= D_\mu\varphi.
```

**Result:** `D_\mu\varphi` is invariant under this gauge-like transformation.

This is the first clean gauge-like symmetry in the toy model.

## 3. Minimal Covariant Toy Energy / Action

A minimal covariant-looking density can be written as

```math
\mathcal{L}_{\mathrm{toy}}
= \frac{A_N}{2}(\partial_\mu N)(\partial^\mu N)
+ \frac{B}{2}N^2(D_\mu\varphi)(D^\mu\varphi)
- V(N)
- \frac{C}{4}F_{\mu\nu}F^{\mu\nu},
```

where

```math
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
```

The signs depend on metric convention. For static energy one would use positive spatial gradient terms. The important structural point is the replacement

```math
\partial_\mu\varphi
\quad\longrightarrow\quad
D_\mu\varphi=\partial_\mu\varphi-A_\mu.
```

## 4. Gauge Invariance Of The Building Blocks

Under

```math
\varphi \mapsto \varphi+\chi,
\qquad
A_\mu\mapsto A_\mu+\partial_\mu\chi,
```

the following objects are invariant:

```math
D_\mu\varphi,
```

```math
(D_\mu\varphi)(D^\mu\varphi),
```

```math
F_{\mu\nu},
```

```math
F_{\mu\nu}F^{\mu\nu},
```

provided `N` is gauge-neutral:

```math
N\mapsto N.
```

Therefore the toy density built from these terms is gauge-like invariant.

## 5. Relation To The Radial Screened Model

For the static two-dimensional ansatz

```math
\varphi=n\theta,
\qquad
A_\theta=a(r),
\qquad
N=N(r),
```

the covariant phase term gives

```math
N^2|D\varphi|^2
\sim
N^2\frac{(n-a(r))^2}{r^2}.
```

The field-strength term gives a radial cost for the screening field. In a full polar-coordinate derivation this term must be handled carefully with metric factors. The previous toy model used the simplified radial cost

```math
\frac{(a')^2}{r^2}.
```

Open problem: derive the exact radial functional from a fully specified covariant action and metric convention, instead of choosing the radial cost by hand.

## 6. Charge-Like Interpretation

In ordinary gauge theory, charge is tied to a local symmetry and a conserved current. In the toy Field 01 bridge, we have only the first ingredient: a gauge-like redundancy.

A possible current-like object from variation with respect to `A_\mu` is

```math
J^\mu_{\mathrm{toy}}
\propto
N^2D^\mu\varphi.
```

Field 01 interpretation:

```text
charge-like behavior may correspond to persistent phase mismatch requiring compensating field response.
```

But this is not yet electric charge. To become a physical charge, the model must show:

1. a well-defined conserved current;
2. a coupling law;
3. quantization or classification of charge;
4. relation to known gauge groups;
5. relation to observed electromagnetic interaction.

## 7. Winding Versus Charge

The previous toy models used the winding number

```math
Q_{\mathrm{wind}}=\frac{1}{2\pi}\oint d\varphi=n.
```

With a connection, there are now two distinct quantities:

```math
Q_{\mathrm{wind}}=\frac{1}{2\pi}\oint d\varphi,
```

and

```math
Q_{\mathrm{cov}}=\frac{1}{2\pi}\oint D\varphi
=\frac{1}{2\pi}\oint(d\varphi-A).
```

For a fully screened configuration at large radius,

```math
A_\theta\to n,
```

so

```math
Q_{\mathrm{cov}}\to0
```

while

```math
Q_{\mathrm{wind}}=n.
```

Interpretation:

- winding records the topological phase structure;
- the compensating field cancels external mismatch;
- charge-like behavior, if it emerges, may live in the relation between winding and compensation rather than in winding alone.

## 8. Horizon Boundary Reading

For a horizon-like boundary, the toy conditions may be

```math
N(R_H)\to0,
\qquad
A_\theta(R_H)\to n.
```

Then

```math
D_\theta\varphi(R_H)\to0,
```

but

```math
\oint d\varphi=2\pi n.
```

Field 01 reading:

```text
normal retention disappears, external phase mismatch is screened, but the winding record can remain in boundary data.
```

This is a more refined mathematical version of the earlier horizon statement.

## 9. What Is Actually Achieved

This bridge achieves the following:

1. turns the screening function into a connection-like object;
2. defines a gauge-like transformation;
3. verifies that `D_\mu\varphi` is invariant;
4. separates topological winding from covariant mismatch;
5. suggests how charge-like behavior might enter later.

It does not yet derive:

- electromagnetism;
- QED;
- electric charge;
- spin-1 photons;
- Standard Model gauge groups;
- coupling constants;
- experimental predictions.

## 10. Next Mathematical Step

The next step should be to derive the Noether current of the covariant toy model and check whether

```math
\partial_\mu J^\mu=0
```

holds under the equations of motion.

If a conserved current can be defined, the model will have a clearer mathematical bridge from phase compensation toward charge-like structure.

## 11. Symbolic Sanity Check

The gauge-like invariance was checked symbolically with `sympy` in two coordinates `(x,y)`.

For

```math
D_x\varphi=\partial_x\varphi-A_x,
\qquad
D_y\varphi=\partial_y\varphi-A_y,
```

and transformation

```math
\varphi' = \varphi+\chi,
\qquad
A'_x=A_x+\partial_x\chi,
\qquad
A'_y=A_y+\partial_y\chi,
```

the check gives

```text
D_x invariant: True
D_y invariant: True
```

For

```math
F_{xy}=\partial_xA_y-\partial_yA_x,
```

the transformed field strength satisfies

```text
F_xy invariant: True
```

So the basic covariant building blocks used in this bridge are mathematically gauge-like invariant.