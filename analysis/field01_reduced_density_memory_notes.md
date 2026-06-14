# Field 01 Boundary Memory And Reduced Density Matrices

This note connects the Field 01 boundary-memory language with the standard idea of a reduced density matrix. It does not derive Hawking radiation and does not solve the black-hole information problem. It only gives a cautious mathematical reading of the phrase:

```text
horizon thermality may reflect reduced access to boundary phase information rather than literal destruction of the record.
```

Status labels:

- **Standard structure** — known mathematical framework.
- **Field 01 interpretation** — model-specific reading.
- **Open problem** — not solved here.

## 1. Full State And Accessible State

Start with a formal full state

```math
\rho_{\mathrm{full}}
```

on a factorized or effectively decomposed Hilbert space

```math
\mathcal{H}_{\mathrm{full}}
\simeq
\mathcal{H}_{\mathrm{external}}\otimes\mathcal{H}_{\mathrm{hidden}}.
```

The external observer has access only to

```math
\rho_{\mathrm{external}}
=
\mathrm{Tr}_{\mathrm{hidden}}\rho_{\mathrm{full}}.
```

**Standard structure:** tracing out inaccessible degrees of freedom can make a pure full state appear mixed to a restricted observer.

## 2. Field 01 Memory Reading

Field 01 introduces memory as a class of preserved phase data:

```math
\mathcal{M}_{\mathrm{bulk}}
=[\varphi,N,A_\mu]_{\sim_{\mathrm{bulk}}}.
```

At a horizon-like boundary:

```math
N\to0,
\qquad
\Pi_\partial:\mathcal{M}_{\mathrm{bulk}}\to\mathcal{M}_{\partial}.
```

The reduced density matrix can be interpreted as describing limited access to this boundary memory:

```math
\rho_{\mathrm{external}}
\sim
\mathrm{accessible\ description\ of\ }\mathcal{M}_{\partial}.
```

This does not mean that `\rho_{\mathrm{external}}` literally equals memory. It means that external observables are functions of the accessible part of the boundary record.

## 3. Accessible And Hidden Memory Sectors

Split boundary memory schematically as

```math
\mathcal{M}_{\partial}
=
(\mathcal{M}_{\mathrm{acc}},\mathcal{M}_{\mathrm{hid}},\mathcal{C}_{\mathrm{corr}}),
```

where:

- `\mathcal{M}_{\mathrm{acc}}` is externally accessible boundary data;
- `\mathcal{M}_{\mathrm{hid}}` is inaccessible or traced-over boundary data;
- `\mathcal{C}_{\mathrm{corr}}` denotes correlations between accessible and hidden sectors.

Then the reduced description is schematically

```math
\rho_{\mathrm{external}}
=
\mathrm{Tr}_{\mathcal{M}_{\mathrm{hid}}}\rho(\mathcal{M}_{\partial}).
```

This is a Field 01 notation for the standard idea of tracing inaccessible degrees of freedom.

## 4. Thermality As Reduced Access

A reduced state may be approximately thermal:

```math
\rho_{\mathrm{external}}
\approx
\frac{e^{-\beta H_{\mathrm{eff}}}}{Z}.
```

Field 01 interpretation:

```text
thermal appearance = reduced external access to the full boundary phase record.
```

This is different from saying:

```text
the underlying record is destroyed.
```

Safe statement:

```text
Field 01 interprets horizon thermality, if present, as an effective description of limited access to boundary memory. It does not by itself refute or replace Hawking's calculation.
```

## 5. What Is Preserved?

In the Field 01 memory language, the full boundary record may preserve invariants such as

```math
Q_{\mathrm{wind}},
\qquad
\Phi_F,
\qquad
\mathcal{J},
\qquad
\mathcal{B},
\qquad
\mathcal{C}_{\mathrm{corr}}.
```

External reduction may hide part of this data. Therefore an external observer may see entropy increase even if the full memory class remains well-defined.

Schematic distinction:

```math
S(\rho_{\mathrm{full}})
\quad \text{and} \quad
S(\rho_{\mathrm{external}})
```

need not be the same.

## 6. Entropy In This Language

The von Neumann entropy of the reduced state is

```math
S_{\mathrm{ext}}
=-\mathrm{Tr}(\rho_{\mathrm{external}}\log\rho_{\mathrm{external}}).
```

Field 01 reading:

```text
S_ext measures missing access to full boundary-memory correlations, not necessarily destruction of memory.
```

For a black-hole-like system, one would need to connect this to

```math
S_{\mathrm{BH}}=\frac{k_B A}{4\ell_P^2}.
```

Open problem: Field 01 has not derived the Bekenstein--Hawking coefficient or the Hawking spectrum.

## 7. Boundary Memory Map And Reduction Map

There are now two maps:

```math
\Pi_\partial:\mathcal{M}_{\mathrm{bulk}}\to\mathcal{M}_{\partial},
```

and

```math
\mathcal{R}_{\mathrm{ext}}:\rho_{\mathrm{full}}\to\rho_{\mathrm{external}}
=\mathrm{Tr}_{\mathrm{hidden}}\rho_{\mathrm{full}}.
```

Field 01 must eventually explain how these relate:

```math
\mathcal{R}_{\mathrm{ext}}\circ\rho(\mathcal{M}_{\partial})
\quad ? \quad
\rho_{\mathrm{external}}.
```

In words:

```text
How does a boundary memory class determine the reduced state seen by an external observer?
```

## 8. Important Distinction

Field 01 should distinguish three claims:

1. **Standard:** restricted access gives a reduced density matrix.
2. **Interpretive:** thermal appearance can be read as limited access to boundary memory.
3. **Unproven:** the full black-hole evaporation process preserves all information in exactly this way.

Only the first is standard. The second is the current Field 01 interpretation. The third remains open.

## 9. Toy Example: Two-Sector Entanglement

A minimal schematic pure state can be written as

```math
|\Psi\rangle
=
\sum_i c_i |i\rangle_{\mathrm{acc}}|i\rangle_{\mathrm{hid}}.
```

Then

```math
\rho_{\mathrm{full}}=|\Psi\rangle\langle\Psi|,
```

while

```math
\rho_{\mathrm{acc}}
=
\mathrm{Tr}_{\mathrm{hid}}\rho_{\mathrm{full}}
=
\sum_i |c_i|^2 |i\rangle\langle i|.
```

The accessible state is mixed even though the full state is pure.

Field 01 reading:

```text
external mixture can reflect inaccessible correlations within boundary memory.
```

## 10. What This Achieves

This note gives a cautious bridge:

```text
boundary phase memory -> restricted access -> reduced density matrix -> possible thermality.
```

It supports the model's language without claiming a completed theory.

## 11. What Remains Open

Required future work:

1. define the Hilbert space of boundary memory;
2. define observables associated with `\mathcal{M}_{\partial}`;
3. derive the reduced density matrix from those observables;
4. compare with Hawking's semiclassical calculation;
5. determine whether information is preserved unitarily, encoded holographically, or coarse-grained;
6. connect entropy to horizon area;
7. identify any testable difference from standard descriptions.

## 12. Next Step

The next step is to build a compact mathematical roadmap for the whole formalization sequence:

```text
phase -> closed node -> normal retention -> gauge-like compensation -> current -> memory class -> boundary map -> reduced state
```

This can become the skeleton of a future formalization paper.