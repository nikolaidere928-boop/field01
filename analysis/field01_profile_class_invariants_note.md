# Field 01 Profile Class Invariants Note

Purpose: decide how radial profile data should enter the Field 01 memory-map framework, after the v1 split between minimal topological/boundary memory and refined energy/coupling memory.

Status: working definition note. This is not a new simulation, not a physical memory-preservation claim, and not a standalone result.

Date: 2026-06-14.

Depends on:

```text
analysis/field01_standard_core_v1.md
analysis/field01_memory_map_definitions_v1.md
analysis/field01_memory_map_radial_examples_v1.md
analysis/numerics/radial_vortex_results.json
analysis/numerics/radial_vortex_coupling_sweep.json
analysis/numerics/radial_vortex_profile_distances.json
```

## 1. Label Discipline

This file uses:

- **Definition:** a proposed computation or classification rule.
- **Requirement:** a condition a profile invariant must satisfy.
- **Observation:** a fact about existing numerical data or existing definitions.
- **Conclusion:** a limited working decision for v1/v1.1 terminology.
- **Open problem:** something not yet decided or not computable from current data.
- **Non-claim:** a statement explicitly not being made.

## 2. Starting Point From Memory Map v1

**Observation:** `field01_memory_map_definitions_v1.md` defines the minimal bulk invariant map as:

```math
\mathcal{I}^{(1,min)}_{\mathrm{bulk}}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial}).
```

It explicitly excludes exact finite-domain energy and the full radial profile from minimal memory.

**Observation:** the refined v1 map includes:

```math
E_{\mathrm{class}},
\qquad
P_{\mathrm{model}}=(\lambda,g,N_0),
```

but does not yet include a profile class.

**Conclusion:** radial profile information should not be added to minimal memory. It may be added only as a refined invariant after defining a profile map, a norm, and tolerances.

## 3. What Counts As A Radial Profile

For the current standard radial vortex ansatz:

```math
\Psi(r,\theta)=N(r)e^{in\theta},
\qquad
A_r=0,
\qquad
A_\theta=a(r),
```

the profile-level data may include:

```math
N(r),
\qquad
a(r),
\qquad
D_\theta\varphi(r)=n-a(r),
\qquad
B(r)=\frac{a'(r)}{r}.
```

**Definition:** on a finite numerical interval `r in [r_min,R]`, define the normalized radial coordinate:

```math
\rho=\frac{r-r_{\min}}{R-r_{\min}}
\in[0,1].
```

**Definition:** the finite-domain radial profile map is:

```math
\mathcal{P}_R[X]
=
\left(
N_R(\rho),
a_R(\rho),
n-a_R(\rho),
B_R(\rho)
\right),
```

where `N_R`, `a_R`, and `B_R` mean the profiles resampled onto a common `rho` grid.

**Requirement:** `\mathcal{P}_R` must be compared only after fixing:

1. the model convention and parameters;
2. the finite-domain interval or normalization rule;
3. the interpolation/resampling rule;
4. the norm and numerical tolerances;
5. whether boundary values are included or compared separately through `\mathcal{B}_{\partial}`.

## 4. Profile Distance And Class

**Definition:** a simple v1.1 profile distance can be:

```math
d_{\mathcal{P}}(X_1,X_2)
=
\max_{\rho\in[0,1]}
\left(
|N_1(\rho)-N_2(\rho)|,
|a_1(\rho)-a_2(\rho)|
\right).
```

**Definition:** an energy-weighted or radial `L^2` alternative is:

```math
d_{\mathcal{P},2}^2(X_1,X_2)
=
\int_0^1 d\rho\,w(\rho)
\left[
|N_1-N_2|^2+|a_1-a_2|^2
\right],
```

with the weight `w` fixed before comparison.

**Definition:** for a tolerance `\epsilon_{\mathcal{P}}`, define the profile class:

```math
[\mathcal{P}_R(X)]_{\epsilon_{\mathcal{P}}}
=
\{X'\,|\,d_{\mathcal{P}}(X,X')\le\epsilon_{\mathcal{P}}\}.
```

**Requirement:** this class is a numerical/refined class unless a continuum norm and convergence statement are supplied.

## 5. Placement In The Memory Hierarchy

**Definition:** the minimal memory remains:

```math
\mathcal{M}^{(1,min)}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial}).
```

**Definition:** the existing refined memory is:

```math
\mathcal{M}^{(1,ref)}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial},E_{\mathrm{class}},P_{\mathrm{model}}).
```

**Definition:** a future profile-refined memory level may be:

```math
\mathcal{M}^{(1,prof)}
=
(\nu,\Delta_{\partial},\mathcal{B}_{\partial},E_{\mathrm{class}},P_{\mathrm{model}},[\mathcal{P}_R]_{\epsilon_{\mathcal{P}}}).
```

**Conclusion:** `\mathcal{M}^{(1,prof)}` should be treated as a refined diagnostic layer, not as the default meaning of Field 01 memory.

## 6. Decision Table

| comparison | minimal memory | refined energy/coupling memory | profile class role |
|---|---|---|---|
| same `nu`, same `Delta_partial`, same boundary class, same parameters, profiles differ only below tolerance | same | same | same profile class |
| same minimal class, different `lambda` or `g` | same | different if `P_model` is included | profile comparison is optional and secondary |
| same `nu` and `a(R)`, but different `N(R)` boundary class | different | different | not a profile-only distinction |
| same minimal/refined labels, profile distance above tolerance | same minimal | possibly same refined | different profile-refined class or solver/multiple-branch warning |
| different winding or flux-derived sector | different | different | profile comparison is not the primary classifier |

**Conclusion:** profile classes should answer the question `same shape within tolerance?`, not the question `same topological/boundary memory?`.

## 7. Existing Data Status

**Observation:** existing JSON files contain summary profile probes such as `N_mid`, `a_mid`, `N_right`, `a_right`, energies, fluxes, and residuals.

**Observation:** the current local radial vortex run exports non-empty full profile CSV files for:

```text
analysis/numerics/standard_vortex_boundary_radial_vortex_profile.csv
analysis/numerics/forced_outer_zero_boundary_radial_vortex_profile.csv
analysis/numerics/radial_vortex_profile_lambda_0p25.csv
analysis/numerics/radial_vortex_profile_lambda_0p5.csv
analysis/numerics/radial_vortex_profile_lambda_1p0.csv
analysis/numerics/radial_vortex_profile_lambda_2p0.csv
```

with columns:

```text
r,rho,N,a,n_minus_a,B,dN,da_dr,energy_density,2pi_radial_integrand
```

**Observation:** the pairwise coupling-sweep profile distances are summarized in:

```text
analysis/numerics/radial_vortex_profile_distances.json
```

The CSV profile arrays remain local/generated artifacts under the current repository ignore rules; the JSON distance summary is the compact tracked record.

## 8. First Coupling-Sweep Profile Distances

**Observation:** using:

```math
d_{\mathcal{P}}=\max_{\rho}\max(|\Delta N|,|\Delta a|),
```

and:

```math
d_{\mathcal{P},2}=\sqrt{\int_0^1[(\Delta N)^2+(\Delta a)^2]d\rho},
```

the existing sweep gives:

| lambda pair | `d_profile_max` | `max_abs_N` | `max_abs_a` | `d_profile_l2_rho` |
|---:|---:|---:|---:|---:|
| 0.25 / 0.50 | 0.109044 | 0.109044 | 0.054732 | 0.039976 |
| 0.25 / 1.00 | 0.220476 | 0.220476 | 0.103829 | 0.075315 |
| 0.25 / 2.00 | 0.330519 | 0.330519 | 0.145089 | 0.105658 |
| 0.50 / 1.00 | 0.114584 | 0.114584 | 0.049850 | 0.036003 |
| 0.50 / 2.00 | 0.230982 | 0.230982 | 0.092490 | 0.067531 |
| 1.00 / 2.00 | 0.120069 | 0.120069 | 0.043367 | 0.032165 |

**Conclusion:** profile distance varies with coupling even when the minimal vortex/boundary memory class is unchanged. This supports keeping profile shape in `\mathcal{M}^{(1,prof)}`, not in `\mathcal{M}^{(1,min)}`.

## 9. Recommended v1.1 Convention

**Conclusion:** use this convention until a physical profile tolerance is justified:

```text
minimal memory = topological/boundary class
refined memory = minimal memory + energy/coupling/model class
profile-refined memory = refined memory + radial profile class, only after full profile arrays and tolerances are fixed
```

**Requirement:** do not infer a physical memory claim from profile similarity. At most, profile similarity is a refined equivalence-class diagnostic inside the toy formalization.

**Requirement:** when comparing profiles, first state whether boundary values are part of `\mathcal{B}_{\partial}` or part of the profile norm. Double-counting the same boundary difference should be avoided.

**Open problem:** choose a numerical or physical tolerance `\epsilon_{\mathcal{P}}`. Until that tolerance is fixed, profile distances are diagnostics, not equivalence-class decisions.

## 10. Non-Claims

This note does not claim:

- that radial profile shape is physical memory;
- that profile similarity proves information preservation;
- that the profile class is gauge-independent before the gauge convention is fixed;
- that the current profile distances define a final tolerance;
- that the CSV profile arrays are required minimal-memory data;
- that `\mathcal{M}^{(1,prof)}` should replace minimal memory.

## 11. Public-Safe Summary

```text
Profile classes are a possible refined diagnostic, not part of minimal Field 01 memory. The minimal memory map records vortex sector, boundary covariant mismatch, and boundary data class. Energy and model parameters already define a refined level. The current profile-distance table is a first diagnostic, but a profile-refined equivalence class still requires an explicit tolerance. This is a bookkeeping definition, not a physical memory-preservation claim.
```