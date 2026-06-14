# Field 01 Memory Map Radial Examples v1

Purpose: test `field01_memory_map_definitions_v1.md` on existing radial vortex numerical outputs, without introducing new physics claims.

Status: working consistency check. This note uses already-generated numerical data in `analysis/numerics/`; it is not a new simulation and not a public result.

Date: 2026-06-14.

Depends on:

```text
analysis/field01_standard_core_v1.md
analysis/field01_memory_map_definitions_v1.md
analysis/numerics/radial_vortex_results.json
analysis/numerics/radial_vortex_coupling_sweep.json
```

## 1. Label Discipline

This file uses:

- **Definition:** a computation or classification rule used in the examples.
- **Observation:** a numerical fact read from existing output files.
- **Interpretation:** Field 01 reading of the example.
- **Conclusion:** a limited working conclusion for the memory-map definitions.
- **Open problem:** something not yet decided.
- **Non-claim:** a statement explicitly not being made.

## 2. Radial Memory Quantities

For a finite numerical domain `r in [r_min,R]`, use:

```math
\nu_R
=\frac{1}{2\pi}\Phi_F
= a(R)-a(r_{\min}).
```

For the current numerical boundary conditions, `a(r_min)=0`, so:

```math
\nu_R=a(R).
```

Define the finite-radius boundary covariant mismatch:

```math
\Delta_R
=\oint_{r=R}(d\varphi-A)
=2\pi[n-a(R)].
```

Define the boundary scalar class by the outer scalar value:

```math
[N_{\partial}]_{\mathrm{class}}
\sim N(R),
```

with tolerance to be fixed later.

Define an optional energy class:

```math
E_{\mathrm{class}}
=[E_R]_{\Delta E}.
```

## 3. Source Data

Existing numerical source files:

```text
analysis/numerics/radial_vortex_results.json
analysis/numerics/radial_vortex_coupling_sweep.json
```

The first file compares:

- `standard_vortex_boundary`: `N(R)=N0`, `a(R)=n`;
- `forced_outer_zero_boundary`: `N(R)=0`, `a(R)=n`.

The second file sweeps:

```math
\lambda\in\{0.25,0.50,1.00,2.00\},
```

with:

```math
g=1,
\qquad
N_0=1,
\qquad
n=1,
\qquad
R=20.
```

## 4. Example A: Same Vortex Sector, Different Scalar Boundary Class

**Observation:** existing finite-disk radial outputs give:

| case | lambda | `N(R)` | `a(R)` | `nu=flux/2pi` | `Delta_R=2pi(n-aR)` | energy | memory note |
|---|---:|---:|---:|---:|---:|---:|---|
| `standard_vortex_boundary` | 1.00 | 1 | 1 | 1 | 0.000e+00 | 3.63404949 | same topological sector; scalar boundary `N0` |
| `forced_outer_zero_boundary` | 1.00 | 0 | 1 | 1 | 0.000e+00 | 37.2638886 | same topological sector; different scalar boundary class |

**Definition:** the topological reduced invariant map is:

```math
\mathcal{I}^{(1,top)}_{\mathrm{bulk}}
=(\nu,\Delta_{\partial},\mathcal{B}_{\partial}).
```

If `\mathcal{B}_{\partial}` includes `[N_{\partial}]_{\mathrm{class}}`, then these two examples are not boundary-memory-equivalent:

```math
[N_{\partial}]_{\mathrm{standard}}=[N_0]
\neq
[0]=[N_{\partial}]_{\mathrm{forced}}.
```

**Conclusion:** vortex sector alone is too coarse if Field 01 wants boundary scalar state to matter. The boundary scalar class should remain part of `\mathcal{I}^{(1)}_{\partial}` whenever the normal-retention interpretation is being studied.

**Non-claim:** the forced `N(R)=0` case is only a boundary-condition test. It is not a claim about any physical boundary.

## 5. Example B: Same Minimal Topological Memory, Different Coupling/Energy

**Observation:** the coupling sweep gives:

| lambda | beta | `nu` | `Delta_R` | energy | energy/pi | BPS `N` residual | BPS `a` residual | memory note |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.25 | 0.50 | 1 | 0.000e+00 | 2.72660526 | 0.867905411 | 3.113e-02 | 9.372e-02 | same minimal topological memory; different energy/refined class |
| 0.50 | 1.00 | 1 | 0.000e+00 | 3.1415668 | 0.99999177 | 3.770e-04 | 2.653e-06 | BPS value |
| 1.00 | 2.00 | 1 | 0.000e+00 | 3.63402694 | 1.1567467 | 5.433e-02 | 1.166e-01 | same minimal topological memory; different energy/refined class |
| 2.00 | 4.00 | 1 | 0.000e+00 | 4.21152278 | 1.34056934 | 1.424e-01 | 2.597e-01 | same minimal topological memory; different energy/refined class |

**Observation:** all sweep cases have:

```math
\nu=1,
\qquad
\Delta_R=0.
```

The outer boundary conditions are the same standard vortex boundary type, but the finite-disk energies differ.

**Conclusion:** the minimal topological memory class should not automatically include exact energy. Otherwise the same vortex sector at different couplings would be classified as different memory even when the selected topological/boundary labels are unchanged.

**Recommended v1 convention:** use two memory levels:

```math
\mathcal{M}^{(1,top)}=(\nu,\Delta_{\partial},\mathcal{B}_{\partial}),
```

and:

```math
\mathcal{M}^{(1,ref)}=(\nu,\Delta_{\partial},\mathcal{B}_{\partial},E_{\mathrm{class}},\lambda,g,N_0).
```

**Interpretation:** `\mathcal{M}^{(1,top)}` records the selected vortex-sector and boundary labels, while `\mathcal{M}^{(1,ref)}` also records dynamical/refined sector information.

## 6. BPS Check As A Normalization Example

**Observation:** at:

```math
\lambda=0.50,
\qquad
g=1,
\qquad
\beta=1,
```

the numerical energy is:

```math
E_R=3.1415668,
```

and:

```math
\frac{E_R}{\pi}=0.99999177.
```

The BPS residuals are small compared with the non-BPS cases:

```math
\max |R_N|\approx3.77\times10^{-4},
\qquad
\max |R_a|\approx2.65\times10^{-6}.
```

**Conclusion:** the radial examples remain consistent with the standard-core normalization:

```math
\lambda_{\mathrm{BPS}}=\frac{g^2}{2},
\qquad
E_{\mathrm{BPS}}=\pi N_0^2|n|.
```

This supports using the existing numerical files for memory-map examples without changing the standard vortex convention.

## 7. Bulk-To-Boundary Well-Definedness In These Examples

**Definition:** the v1 projection is well-defined only if:

```math
X_1\sim_{\mathrm{bulk}}^{(1)}X_2
\Longrightarrow
r_{\partial}X_1\sim_{\partial}^{(1)}r_{\partial}X_2.
```

**Observation:** for the coupling sweep, the same `n`, same `a(R)=n`, and same `N(R)=N0` make the boundary class stable across `\lambda` if energy is omitted from minimal memory.

**Observation:** for the forced outer-zero case, the same `n` and `a(R)=n` do not imply the same boundary scalar class, because `N(R)` changes from `N0` to `0`.

**Conclusion:** the current boundary invariant map is doing useful work: it distinguishes changes in the scalar boundary class while allowing topologically equivalent coupling-sweep configurations to remain equivalent at the minimal topological level.

## 8. Decision On `E_class`

**Conclusion:** for v1, use:

```math
E_{\mathrm{class}}
```

as a refined invariant, not a required minimal invariant.

Minimal memory:

```math
\mathcal{I}^{(1,min)}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial}).
```

Refined memory:

```math
\mathcal{I}^{(1,ref)}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial},E_{\mathrm{class}},\lambda,g,N_0).
```

**Open problem:** decide whether two configurations with the same `\nu` and boundary class but different radial profiles should be considered the same memory, the same topological memory, or different refined memories.

## 9. Public-Safe Summary

```text
The radial examples indicate that the memory-map definitions distinguish at least two levels. The minimal topological level records the vortex sector and boundary covariant mismatch. The boundary scalar class distinguishes a standard outer boundary from a forced outer-zero boundary. Energy should be treated as a refined invariant, because configurations with the same vortex sector and boundary type can have different energies when the coupling changes. This is a consistency check of definitions, not a physical memory-preservation claim.
```

## 10. Non-Claims

This note does not claim:

- that the v1 memory map is final;
- that physical information is preserved;
- that energy is or is not memory in a physical sense;
- that the forced outer-zero case represents a physical boundary;
- that these examples go beyond standard radial vortex numerics.

## 11. Follow-Up Status

The two-level distinction has been incorporated into:

```text
analysis/field01_memory_map_definitions_v1.md
```

Profile-class invariants are separated in:

```text
analysis/field01_profile_class_invariants_note.md
```

Use the profile note for profile-refined diagnostics; do not fold profile shape into minimal memory.