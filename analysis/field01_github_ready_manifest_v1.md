# Field 01 GitHub-Ready Manifest v1

Purpose: define the safe reading order, file roles, publication boundaries, and feedback request shape for a future GitHub package.

Status: internal release-planning manifest. This is not a GitHub release, not a Reddit post, not a paper draft, and not a public claim of new physics.

Date: 2026-06-14.

Depends on:

```text
analysis/field01_internal_consistency_pass_v1.md
analysis/field01_two_layer_formalization_plan.md
analysis/field01_standard_core_v1.md
analysis/field01_memory_map_definitions_v1.md
analysis/field01_profile_class_invariants_note.md
```

## 1. Release Principle

**Decision:** GitHub should present this package as a cautious formalization workspace, not as a completed theory.

The safe public framing is:

```text
This repository contains a standard radial vortex mathematical core and a clearly labelled exploratory equivalence-class interpretation layer. The standard vortex content is separated from Field 01 interpretation. The current goal is convention checking, internal consistency checking, and feedback on formal definitions.
```

**Non-claim:** the GitHub package must not present Field 01 as a verified physical model.

## 2. Recommended Reading Order

### 2.1 Minimal External Reading Path

For a technically trained external reader, use this order:

1. `analysis/field01_two_layer_formalization_plan.md`
2. `analysis/field01_standard_core_v1.md`
3. `analysis/field01_vortex_convention_dictionary.md`
4. `analysis/field01_schaposnik_vortices_convention_map.md`
5. `analysis/field01_memory_map_definitions_v1.md`
6. `analysis/field01_memory_map_radial_examples_v1.md`
7. `analysis/field01_profile_class_invariants_note.md`
8. `analysis/field01_internal_consistency_pass_v1.md`

### 2.2 Numerics Reading Path

For checking the numerical diagnostics:

1. `analysis/numerics/radial_vortex_results.json`
2. `analysis/numerics/radial_vortex_coupling_sweep.json`
3. `analysis/numerics/radial_vortex_profile_distances.json`
4. `analysis/numerics/solve_radial_vortex_profile.py`
5. `analysis/numerics/sweep_radial_vortex_coupling.py`

Generated CSV and PNG files are local artifacts under the current ignore rules. The compact tracked records are JSON summaries and scripts.

## 3. File Role Classification

| file | role | public readiness | caution |
|---|---|---|---|
| `field01_two_layer_formalization_plan.md` | layer separation plan | near-public after review | do not oversell interpretation |
| `field01_standard_core_v1.md` | standard vortex math core | near-public after review | standard substrate only |
| `field01_vortex_convention_dictionary.md` | notation/convention map | near-public after review | convention-sensitive factors |
| `field01_schaposnik_vortices_convention_map.md` | Schaposnik comparison | internal-to-near-public | PDF extraction should be visually checked before citation-grade use |
| `field01_interpretation_layer_v1.md` | labelled interpretation layer | internal | hypothesis/interpretation only |
| `field01_memory_map_definitions_v1.md` | formal memory-map definitions | internal-to-near-public | definition framework, not physics proof |
| `field01_memory_map_radial_examples_v1.md` | examples against existing JSON | internal-to-near-public | consistency check only |
| `field01_profile_class_invariants_note.md` | profile-refined diagnostic layer | internal-to-near-public | profile distances are not physical memory |
| `field01_internal_consistency_pass_v1.md` | claim-discipline audit | internal | gate before public release |
| `analysis/numerics/*.json` | compact numerical records | shareable with caveats | generated from toy scripts |
| `analysis/numerics/*.py` | reproducibility helpers | shareable with caveats | local script style, not packaged software |

## 4. Standard Math Versus Interpretation

### 4.1 Standard Math Layer

The standard layer may use:

- complex scalar;
- scalar modulus / radial profile;
- winding number;
- `U(1)` gauge field;
- covariant derivative;
- Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau vortex terminology;
- flux and BPS convention statements after normalization is stated.

This layer is not novel by itself.

### 4.2 Field 01 Interpretation Layer

The interpretation layer may use only labelled language:

- **Definition:** chosen equivalence relation, invariant map, or projection;
- **Interpretation:** Field 01 reading of the formal object;
- **Hypothesis:** claim requiring proof or tests;
- **Open problem:** missing definition, proof, or validation step;
- **Non-claim:** explicit boundary of what is not asserted.

Field 01 terms such as `memory`, `normal retention`, `horizon-like`, and `charge-like` must remain labelled and separate from standard vortex facts.

## 5. Current Claims Allowed

Allowed statements:

- The standard-core ansatz uses standard radial vortex mathematics.
- The current convention maps Schaposnik's critical coupling to `lambda = g^2/2` under the stated normalization map.
- The current BPS energy target `E = pi` for `N0=1`, `n=1` is normalization-consistent in the explicit `1/2 |D_i Psi|^2` convention.
- The memory-map notes define equivalence classes and selected invariant maps.
- The radial examples test those definitions against existing toy numerical outputs.
- Profile distances are refined diagnostics, not minimal memory.

## 6. Claims Not Allowed

Do not claim:

- a new field theory;
- a new particle model;
- a black-hole model;
- a solution to the black-hole information problem;
- a derivation of Hawking radiation;
- a derivation of Bekenstein-Hawking entropy;
- physical memory preservation;
- that profile similarity is physical memory;
- that the memory-map invariant set is final;
- that the toy numerics validate Field 01 as physics.

## 7. Reproducibility Notes

Current tracked reproducibility files:

```text
analysis/numerics/solve_radial_vortex_profile.py
analysis/numerics/sweep_radial_vortex_coupling.py
analysis/numerics/radial_vortex_results.json
analysis/numerics/radial_vortex_coupling_sweep.json
analysis/numerics/radial_vortex_profile_distances.json
```

Current local generated artifacts include CSV profiles and PNG plots, but these are ignored by repository rules. If GitHub needs them, decide explicitly whether to:

1. keep only JSON summaries and scripts;
2. add selected CSV files with `git add -f`;
3. add a generated-artifacts archive outside the main repo;
4. regenerate plots only in release assets.

**Recommended v1 choice:** track scripts and compact JSON summaries; leave large generated CSV/PNG files ignored until a release asset policy is chosen.

## 8. GitHub Feedback Request Shape

Safe request:

```text
I am preparing a cautious formalization package. The standard radial vortex layer is separated from an exploratory equivalence-class interpretation layer. I would appreciate feedback on notation conventions, the Abelian-Higgs/Nielsen-Olesen mapping, and whether the invariant-map bookkeeping is internally consistent.
```

Avoid:

```text
This proves a new physical memory mechanism.
```

Avoid:

```text
This solves black-hole information preservation.
```

## 9. Reddit Gate

Reddit should wait until after the GitHub package is readable and self-contained.

When used, Reddit should ask a narrow technical question, for example:

```text
Does this convention map and equivalence-class bookkeeping for a radial Abelian-Higgs/Nielsen-Olesen toy model look internally consistent?
```

Do not ask Reddit to judge Field 01 as a physical theory at this stage.

## 10. Pre-Push Checklist

Before GitHub push or release:

1. run README reference check;
2. run JSON validity check;
3. run Python syntax check for numerics scripts;
4. check `git status --short` and leave only intentional files;
5. decide what to do with untracked `AGENTS.md`;
6. decide whether generated CSV/PNG files remain ignored;
7. prepare a short top-level public-safe pointer from `README.md` or a release note;
8. do one final scan for strong claims.

## 11. Current Status

**Conclusion:** the package is not yet a public release, but it is close to a GitHub-preparation checkpoint.

The next internal step should be a top-level public-safe pointer or release note that tells a GitHub visitor where to start, without forcing them into the entire internal `analysis/` tree.