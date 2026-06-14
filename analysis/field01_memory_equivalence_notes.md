# Field 01 Memory As Equivalence Class

This note formalizes the Field 01 idea of memory as preserved phase-structural data. It does not claim that the full physical information problem is solved. It defines a first mathematical language for `memory` compatible with the toy models developed so far.

Status labels:

- **Definition** — a working mathematical definition.
- **Interpretation** — Field 01 reading.
- **Open problem** — not yet solved.

## 1. Why Memory Needs A Formal Definition

The book uses memory in a physical/informational sense:

```text
memory is not stored in the object's shape; it is carried by phase relation, rhythm, circulation history, and recording.
```

The toy models now contain several mathematical structures:

```math
\varphi,
\qquad
N,
\qquad
A_\mu,
\qquad
D_\mu\varphi,
\qquad
Q_{\mathrm{wind}},
\qquad
J^\mu,
\qquad
E.
```

So we need to define what combination of these counts as `memory`.

## 2. Bulk Configuration Data

Define a local/bulk field configuration as

```math
\mathcal{X}_{\mathrm{bulk}}
=
(\varphi,N,A_\mu;\Omega),
```

where:

- `\varphi` is phase;
- `N` is normal retention/local depth;
- `A_\mu` is compensating connection-like field;
- `\Omega` is the domain or region where the configuration is defined.

A more detailed data package may include derived quantities:

```math
\mathcal{D}_{\mathrm{bulk}}
=
(\varphi,N,A_\mu,D_\mu\varphi,F_{\mu\nu},J^\mu,E,Q_{\mathrm{wind}};\Omega).
```

This is not yet memory. It is the full local description available in the toy model.

## 3. Memory As Equivalence Class

Define memory as an equivalence class:

```math
\boxed{
\mathcal{M}_{\mathrm{bulk}}
=
[\varphi,N,A_\mu]_{\sim_{\mathrm{bulk}}}
}
```

The equivalence relation `\sim_{\mathrm{bulk}}` identifies configurations that differ in local representation but preserve selected invariants.

A first invariant set is

```math
\mathcal{I}_{\mathrm{bulk}}
=
\left(
Q_{\mathrm{wind}},
\Phi_F,
\mathcal{J},
E_{\mathrm{class}},
\mathcal{B}
\right),
```

where:

```math
Q_{\mathrm{wind}}=\frac{1}{2\pi}\oint d\varphi,
```

```math
\Phi_F=\oint A
\quad \text{or more generally} \quad
\int F,
```

```math
\mathcal{J}=\int_\Sigma J^\mu d\Sigma_\mu,
```

```math
E_{\mathrm{class}}=\text{energy class or finite-energy sector},
```

and `\mathcal{B}` denotes boundary-accessible phase data.

Working definition:

```math
\mathcal{X}_1\sim_{\mathrm{bulk}}\mathcal{X}_2
\quad\Longleftrightarrow\quad
\mathcal{I}_{\mathrm{bulk}}(\mathcal{X}_1)=\mathcal{I}_{\mathrm{bulk}}(\mathcal{X}_2).
```

This is a first formal version of memory as preserved phase-normal-gauge information.

## 4. Gauge Redundancy Must Be Quotiented Out

Because the screened toy model has gauge-like redundancy,

```math
\varphi\mapsto\varphi+\chi,
\qquad
A_\mu\mapsto A_\mu+\partial_\mu\chi,
```

memory must not depend on gauge representation.

Therefore the memory class should be gauge-invariant:

```math
[\varphi,N,A_\mu]_{\sim}
=
[\varphi+\chi,N,A_\mu+\partial_\mu\chi]_{\sim}.
```

This means memory cannot be simply the raw phase `\varphi`. It must be built from gauge-invariant or topological data such as:

- winding;
- covariant phase mismatch;
- field strength;
- current flux;
- boundary phase class;
- energy sector.

## 5. What Memory Preserves And What It Forgets

Memory preserves:

```text
phase topology, boundary-accessible phase class, conserved/current-like data, energy sector, and possibly correlations.
```

Memory forgets or quotients out:

```text
coordinate representation, gauge choice, small smooth deformations that do not change invariants, and object-like shape.
```

This matches the book-level statement:

```text
memory is not the shape of the object; memory is the retained phase relation.
```

## 6. Boundary Memory

At a horizon-like boundary, the normal retention goes to zero:

```math
N\to0.
```

The local bulk node no longer exists as a normal-retained object. But boundary data may remain.

Define boundary memory as

```math
\boxed{
\mathcal{M}_{\partial}
=
[\varphi_{\partial},A_{\partial},F_{\partial},Q_{\partial}]_{\sim_{\partial}}
}
```

where

```math
\varphi_{\partial}=\varphi|_{\partial\Omega},
\qquad
A_{\partial}=A|_{\partial\Omega},
```

and

```math
Q_{\partial}=\frac{1}{2\pi}\oint_{\partial\Omega}d\varphi.
```

In a screened boundary case,

```math
D_\theta\varphi|_{\partial\Omega}\to0,
\qquad
Q_{\partial}=n.
```

Interpretation:

```text
external mismatch may be screened while topological phase record remains.
```

## 7. Bulk-To-Boundary Map

Define a first boundary projection:

```math
\boxed{
\Pi_{\partial}:\mathcal{M}_{\mathrm{bulk}}\to\mathcal{M}_{\partial}
}
```

with schematic action

```math
\Pi_{\partial}
\left([
\varphi,N,A_\mu
]_{\sim_{\mathrm{bulk}}}\right)
=
[
\varphi|_{\partial\Omega},
A|_{\partial\Omega},
Q_{\mathrm{wind}},
\mathcal{B}
]_{\sim_{\partial}}.
```

The horizon limit is then expressed as

```math
N\to0,
\qquad
\Pi_{\partial}(\mathcal{M}_{\mathrm{bulk}})=\mathcal{M}_{\partial}.
```

This is the formal version of the phrase:

```text
local memory becomes boundary record.
```

## 8. Relation To Current

The current-like object is

```math
J^\mu=BN^2D^\mu\varphi.
```

If

```math
N\to0,
```

then local current tends to vanish, provided `D^\mu\varphi` remains finite:

```math
J^\mu\to0.
```

But memory can still preserve winding:

```math
Q_{\mathrm{wind}}=n.
```

Therefore Field 01 should distinguish:

```text
local dynamical current
```

from

```text
boundary phase memory.
```

This distinction is important for horizons.

## 9. Relation To Energy

Energy may be part of memory only as a class, not necessarily as an exact local density.

Possible definition:

```math
E_{\mathrm{class}}(\mathcal{X})
=
\left[ E[\mathcal{X}] \right]_{\Delta E},
```

where `\Delta E` is a tolerance or equivalence scale.

Open problem: in a real physical theory, energy should be defined by the stress-energy tensor or Hamiltonian, not by a toy functional alone.

## 10. What This Achieves

This note gives the first formal version of memory:

```math
\mathcal{M}=[\varphi,N,A_\mu]_{\sim}.
```

It also defines the first formal horizon recording map:

```math
\Pi_{\partial}:\mathcal{M}_{\mathrm{bulk}}\to\mathcal{M}_{\partial}.
```

Conceptually, this supports the Field 01 chain:

```text
closed phase node
→ normal-retained local memory
→ normal suppression
→ boundary phase record.
```

## 11. What Remains Open

The equivalence relation is not yet unique. We must decide:

1. which invariants are physically necessary;
2. whether correlations must be included;
3. whether memory is classical, quantum, or operator-valued;
4. how this relates to density matrices;
5. how `\Pi_\partial` relates to holographic maps;
6. whether the map is unitary, coarse-graining, projection, or encoding;
7. how black-hole thermality appears from reduced access.

## 12. Next Step

The next mathematical step is to connect boundary memory to reduced density matrices:

```math
\rho_{\mathrm{external}}
=\mathrm{Tr}_{\mathrm{hidden}}\rho_{\mathrm{full}}.
```

Field 01 question:

```text
Can horizon thermality be represented as reduced access to M_boundary rather than destruction of M_bulk?
```