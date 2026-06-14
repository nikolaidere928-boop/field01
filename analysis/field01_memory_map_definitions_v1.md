# Field 01 Memory Map Definitions v1

Purpose: define the first precise version of the Field 01 memory equivalence relations and the bulk-to-boundary memory map, while avoiding thermality, black-hole, or cosmological claims.

Status: internal definition draft. This is an interpretive formalization layer built on `field01_standard_core_v1.md`; it is not a standard physics result and not a public claim.

Date: 2026-06-14.

Depends on:

```text
analysis/field01_standard_core_v1.md
analysis/field01_interpretation_layer_v1.md
analysis/field01_memory_equivalence_notes.md
analysis/field01_memory_map_radial_examples_v1.md
```

## 1. Label Discipline

This file uses only these labels:

- **Definition:** a proposed mathematical definition.
- **Requirement:** a condition a definition must satisfy.
- **Interpretation:** Field 01 reading of the definition.
- **Hypothesis:** a nonstandard claim requiring proof or testing.
- **Open problem:** something not yet fixed.
- **Non-claim:** a statement explicitly not being made.

## 2. Domain And Configuration Space

**Definition:** let `\Omega` be a two-dimensional oriented spatial domain with boundary `\partial\Omega`. For vortex configurations with a core, use the punctured or regularized domain:

```math
\Omega^\circ=\Omega\setminus Z_N,
```

where `Z_N` is the zero set of the scalar modulus.

**Definition:** a bulk configuration is:

```math
X=(\varphi,N,A;\Omega),
```

where:

```math
\Psi=N e^{i\varphi},
\qquad
A=A_i dx^i,
\qquad
D\varphi=d\varphi-A.
```

**Definition:** the first bulk configuration space is:

```math
\mathcal{C}_{\mathrm{bulk}}
=
\{(\varphi,N,A;\Omega)\;|\;E[X]<\infty\text{ or }E_R[X]<\infty\},
```

where `E` is the standard radial vortex energy in `field01_standard_core_v1.md`, and `E_R` denotes the corresponding finite-domain energy when the outer radius is finite.

**Open problem:** decide whether `\mathcal{C}_{\mathrm{bulk}}` should include only smooth finite-energy vortex fields, weak fields, distributional cores, numerical profiles, or quantum states.

## 3. Gauge Redundancy

**Definition:** let `\mathcal{G}_{\Omega}` be the group of allowed gauge transformations:

```math
\chi:\Omega^\circ\to\mathbb{R}/2\pi\mathbb{Z}.
```

It acts by:

```math
\varphi\mapsto\varphi+\chi,
\qquad
A\mapsto A+d\chi,
\qquad
N\mapsto N.
```

**Definition:** the gauge-reduced configuration class is:

```math
[X]_G
=
\{(\varphi+\chi,N,A+d\chi;\Omega):\chi\in\mathcal{G}_{\Omega}\}.
```

**Requirement:** Field 01 memory must be defined on gauge-reduced data or on gauge-invariant quantities. It must not depend on a raw phase representative.

**Open problem:** decide whether large gauge transformations with nonzero boundary winding are included in `\mathcal{G}_{\Omega}` or treated as changing the sector. Until fixed, winding should be stated either as flux-derived or as representative-dependent after a boundary gauge choice.

## 4. Bulk Invariants: Minimal And Refined

**Definition:** define the curvature two-form:

```math
F=dA.
```

**Definition:** define the flux invariant:

```math
\Phi_F[X]=\int_{\Omega}F.
```

For the standard radial vortex sector:

```math
\Phi_F=2\pi n.
```

**Definition:** define the flux-derived vortex number:

```math
\nu[X]=\frac{1}{2\pi}\Phi_F[X].
```

In the standard finite-energy sector:

```math
\nu=n.
```

**Definition:** define the boundary covariant mismatch:

```math
\Delta_{\partial}[X]
=
\oint_{\partial\Omega}D\varphi
=
\oint_{\partial\Omega}(d\varphi-A).
```

For the standard finite-energy vortex boundary:

```math
\Delta_{\partial}\to0.
```

**Definition:** define the boundary data class:

```math
\mathcal{B}_{\partial}[X]
=
[N|_{\partial\Omega},e^{i\varphi}|_{\partial\Omega},A|_{\partial\Omega}]_{\mathcal{G}_{\partial}}.
```

**Definition:** the minimal v1 bulk invariant map is the topological/boundary map:

```math
\boxed{
\mathcal{I}^{(1,min)}_{\mathrm{bulk}}([X]_G)
=
\mathcal{I}^{(1,top)}_{\mathrm{bulk}}([X]_G)
=
\left(
\nu[X],
\Delta_{\partial}[X],
\mathcal{B}_{\partial}[X]
\right).
}
```

**Interpretation:** this minimal map records the vortex sector, boundary covariant mismatch, and boundary scalar/phase/connection class. It does not record the full radial profile or exact finite-domain energy.

**Definition:** define an energy class with tolerance `\Delta E`:

```math
E_{\mathrm{class}}[X]
=
[E[X]]_{\Delta E}.
```

For finite numerical domains, replace `E[X]` by `E_R[X]`.

**Definition:** define a parameter label for a fixed model convention:

```math
P_{\mathrm{model}}[X]
=
(\lambda,g,N_0),
```

when the comparison varies the coupling or vacuum scale.

**Definition:** the refined v1 bulk invariant map is:

```math
\boxed{
\mathcal{I}^{(1,ref)}_{\mathrm{bulk}}([X]_G)
=
\left(
\nu[X],
\Delta_{\partial}[X],
\mathcal{B}_{\partial}[X],
E_{\mathrm{class}}[X],
P_{\mathrm{model}}[X]
\right).
}
```

**Requirement:** `E_{\mathrm{class}}` and `P_{\mathrm{model}}` are refined invariants, not required minimal invariants. Use them only when the question is about energetic, dynamical, or coupling-dependent distinctions.

**Conclusion:** examples in `field01_memory_map_radial_examples_v1.md` motivate this split: changing `\lambda` changes energy while preserving the same minimal vortex/boundary class, whereas changing `N|_{\partial\Omega}` changes the boundary class itself.

**Open problem:** decide whether current integrals, correlation data, or local profile classes should be part of the minimal invariant set or only refined invariant sets.

## 5. Bulk Memory Equivalence Relation

**Definition:** two bulk configurations are minimally memory-equivalent at v1 if their minimal invariant maps agree:

```math
\boxed{
X_1\sim_{\mathrm{bulk}}^{(1,min)}X_2
\quad\Longleftrightarrow\quad
\mathcal{I}^{(1,min)}_{\mathrm{bulk}}([X_1]_G)
=
\mathcal{I}^{(1,min)}_{\mathrm{bulk}}([X_2]_G).
}
```

**Definition:** two bulk configurations are refined-memory-equivalent at v1 if their refined invariant maps agree:

```math
\boxed{
X_1\sim_{\mathrm{bulk}}^{(1,ref)}X_2
\quad\Longleftrightarrow\quad
\mathcal{I}^{(1,ref)}_{\mathrm{bulk}}([X_1]_G)
=
\mathcal{I}^{(1,ref)}_{\mathrm{bulk}}([X_2]_G).
}
```

**Definition:** the minimal v1 bulk memory class is:

```math
\boxed{
\mathcal{M}^{(1,min)}_{\mathrm{bulk}}(X)
=
[X]_{\sim_{\mathrm{bulk}}^{(1,min)}}.
}
```

**Definition:** the refined v1 bulk memory class is:

```math
\boxed{
\mathcal{M}^{(1,ref)}_{\mathrm{bulk}}(X)
=
[X]_{\sim_{\mathrm{bulk}}^{(1,ref)}}.
}
```

**Requirement:** the shorthand `\mathcal{M}^{(1)}` or `\sim^{(1)}` should be read as the minimal level only when no refined invariant is under discussion. Public or technical writing should state the level explicitly.

**Interpretation:** this is the first precise version of `memory as selected phase-normal-gauge equivalence-class data`, with a controlled distinction between minimal topological/boundary memory and refined energetic/model memory.

**Non-claim:** this does not prove that physical memory is preserved. It only defines what the current toy formalization will call the same memory class.

## 6. Boundary Configuration Space

**Definition:** boundary data are restrictions of bulk data:

```math
Y_{\partial}
=
(N_{\partial},e^{i\varphi_{\partial}},A_{\partial};\partial\Omega),
```

with:

```math
N_{\partial}=N|_{\partial\Omega},
\qquad
\varphi_{\partial}=\varphi|_{\partial\Omega},
\qquad
A_{\partial}=A|_{\partial\Omega}.
```

**Definition:** the boundary gauge group `\mathcal{G}_{\partial}` acts by restriction of `\mathcal{G}_{\Omega}`:

```math
\varphi_{\partial}\mapsto\varphi_{\partial}+\chi_{\partial},
\qquad
A_{\partial}\mapsto A_{\partial}+d_{\partial}\chi_{\partial},
\qquad
N_{\partial}\mapsto N_{\partial}.
```

**Definition:** the boundary configuration class is:

```math
[Y_{\partial}]_{G_{\partial}}.
```

## 7. Minimal Boundary Invariants

**Definition:** define the boundary vortex-sector label `\nu_{\partial}` as the boundary record of the bulk flux-derived sector:

```math
\nu_{\partial}
=
\nu
=
\frac{1}{2\pi}\int_{\Omega}F
```

when a filling bulk configuration is specified. If only boundary data are given, `\nu_{\partial}` must be supplied as a lifted sector label or boundary degree, not inferred from `H_A` alone.

**Definition:** define boundary holonomy data:

```math
H_A[Y_{\partial}]
=
\exp\left(i\oint_{\partial\Omega}A_{\partial}\right).
```

**Definition:** define boundary covariant mismatch holonomy:

```math
H_D[Y_{\partial}]
=
\exp\left(i\oint_{\partial\Omega}(d\varphi_{\partial}-A_{\partial})\right).
```

**Definition:** define boundary scalar class:

```math
[N_{\partial}]_{\mathrm{class}},
```

which may be a fixed value, a tolerance class, or a limiting label such as `N_{\partial}=N_0` or `N_{\partial}\to0`.

**Definition:** the minimal v1 boundary invariant map is:

```math
\boxed{
\mathcal{I}^{(1)}_{\partial}([Y_{\partial}]_{G_{\partial}})
=
\left(
\nu_{\partial},
H_A[Y_{\partial}],
H_D[Y_{\partial}],
[N_{\partial}]_{\mathrm{class}}
\right).
}
```

**Reason:** for integer vortex sectors, `H_A=\exp(i2\pi n)=1`, so holonomy alone does not distinguish `n`. The lifted sector label `\nu_{\partial}` is required whenever the integer vortex number is part of memory.

**Open problem:** if the boundary has multiple components, replace each entry by a tuple over boundary components.

## 8. Boundary Memory Equivalence Relation

**Definition:** two boundary configurations are boundary-memory-equivalent at v1 if:

```math
\boxed{
Y_1\sim_{\partial}^{(1)}Y_2
\quad\Longleftrightarrow\quad
\mathcal{I}^{(1)}_{\partial}([Y_1]_{G_{\partial}})
=
\mathcal{I}^{(1)}_{\partial}([Y_2]_{G_{\partial}}).
}
```

**Definition:** the v1 boundary memory class is:

```math
\boxed{
\mathcal{M}^{(1)}_{\partial}(Y)
=
[Y]_{\sim_{\partial}^{(1)}}.
}
```

**Interpretation:** boundary memory is the retained boundary class of scalar, phase, and connection data after quotienting out representation choices.

## 9. Bulk-To-Boundary Restriction Map

**Definition:** define the restriction map:

```math
r_{\partial}:\mathcal{C}_{\mathrm{bulk}}\to\mathcal{C}_{\partial},
\qquad
r_{\partial}(X)=Y_{\partial}.
```

**Definition:** define the v1 memory projection:

```math
\boxed{
\Pi^{(1,min)}_{\partial}:
\mathcal{M}^{(1,min)}_{\mathrm{bulk}}\to
\mathcal{M}^{(1)}_{\partial}
}
```

by:

```math
\boxed{
\Pi^{(1,min)}_{\partial}
\left(\mathcal{M}^{(1,min)}_{\mathrm{bulk}}(X)\right)
=
\mathcal{M}^{(1)}_{\partial}(r_{\partial}X).
}
```

**Requirement:** this map is well-defined only if:

```math
X_1\sim_{\mathrm{bulk}}^{(1,min)}X_2
\quad\Longrightarrow\quad
r_{\partial}X_1\sim_{\partial}^{(1)}r_{\partial}X_2.
```

**Requirement:** the minimal projection does not make `E_{\mathrm{class}}` or `P_{\mathrm{model}}` boundary-recoverable unless additional boundary refined invariants are defined.

**Open problem:** prove this implication for the chosen invariant maps, or adjust `\mathcal{I}^{(1,min)}_{\mathrm{bulk}}` and `\mathcal{I}^{(1)}_{\partial}` until it holds.

## 10. Boundary-Recoverability Statement

**Definition:** a bulk invariant `K` is boundary-recoverable through `\Pi_{\partial}^{(1,min)}` if there exists a boundary function `k_{\partial}` such that:

```math
K(X)
=
k_{\partial}\left(\Pi_{\partial}^{(1,min)}(\mathcal{M}^{(1,min)}_{\mathrm{bulk}}(X))\right).
```

**Hypothesis:** in the standard finite-energy vortex sector, the vortex number is boundary-recoverable in this sense:

```math
\nu[X]
=
\frac{1}{2\pi}\Phi_F[X]
\quad\leadsto\quad
H_A[Y_{\partial}]
=
\exp(i2\pi\nu),
\qquad
\nu_{\partial}=\nu.
```

**Non-claim:** this does not imply preservation of all physical information. It only states preservation of selected invariants under the defined map.

## 11. What Is Quotiented Out

**Definition:** `\sim_{\mathrm{bulk}}^{(1,min)}` and `\sim_{\partial}^{(1)}` quotient out:

- gauge representation;
- raw phase choice;
- coordinate description of the same boundary class;
- small profile changes that leave the chosen minimal invariant classes unchanged;
- exact energy differences, coupling differences, and model-parameter differences.

**Definition:** `\sim_{\mathrm{bulk}}^{(1,ref)}` keeps the minimal quotienting above but can distinguish energy classes and model-parameter labels through `E_{\mathrm{class}}` and `P_{\mathrm{model}}`.

**Interpretation:** this formalizes the phrase `memory is not the object's shape` as a quotient operation.

**Open problem:** decide which profile changes are physically meaningful and which are only representation or tolerance changes.

## 12. Additional Refined Invariants For Later Versions

**Open problem:** later versions may add refined invariants beyond `E_{\mathrm{class}}` and `P_{\mathrm{model}}`, such as:

```math
\mathcal{J}=\int_{\Sigma}J^{\mu}d\Sigma_{\mu},
```

correlation data:

```math
\mathcal{C}_{\mathrm{corr}},
```

or profile classes:

```math
[N(r)]_{\mathrm{profile}}.
```

**Requirement:** each added invariant must be:

1. gauge-invariant or gauge-quotiented;
2. defined on the chosen configuration space;
3. measurable or at least computable in the toy model;
4. compatible with the boundary projection if it is claimed to be boundary-recoverable.

## 13. Minimal Worked Vortex Sector

**Definition:** for the standard radial finite-energy sector:

```math
N(\infty)=N_0,
\qquad
a(\infty)=n,
\qquad
D_{\theta}\varphi\to0,
```

one has:

```math
\nu=n,
\qquad
\Delta_{\partial}=0,
\qquad
H_A=\exp(i2\pi n)=1,
\qquad
H_D=1.
```

**Interpretation:** the integer sector is retained, while the local representative `(\varphi,A)` is quotiented by gauge redundancy.

**Definition / v1 fix:** because `H_A=1` for integer `n`, the boundary invariant includes the lifted integer sector label:

```math
\nu_{\partial}=\nu\in\mathbb{Z}.
```

This is part of both bulk and boundary memory whenever integer vortex number must be distinguished.

## 14. Non-Claims

This file does not claim:

- that the v1 invariant set is final;
- that the map is unique;
- that all physical information is preserved;
- that reduced density matrices follow from this map;
- that thermality follows from this map;
- that any gravitational system is modeled here.

## 15. Public-Safe Summary

```text
Memory Map v1 defines memory as an equivalence class of phase-normal-gauge configurations after quotienting gauge redundancy and recording a selected invariant set. The minimal bulk invariants are vortex sector, boundary covariant mismatch, and boundary data class. Energy class and model parameters belong to refined memory, not minimal memory. The boundary memory class is defined by boundary scalar/phase/connection data modulo boundary gauge transformations. The bulk-to-boundary map is only valid if minimally bulk-equivalent configurations restrict to boundary-equivalent configurations. This is a definition framework, not a proof of physical memory preservation.
```

## 16. Follow-Up Status

The updated definitions are tested against radial examples in:

```text
analysis/field01_memory_map_radial_examples_v1.md
```

The profile-class question is separated into:

```text
analysis/field01_profile_class_invariants_note.md
```

Current v1 convention:

```text
minimal memory = topological/boundary class
refined memory = minimal memory + energy/coupling/model class
profile-refined memory = refined memory + radial profile class, only after a tolerance is fixed
```