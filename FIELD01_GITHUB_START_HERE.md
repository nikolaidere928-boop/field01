# Field 01 GitHub Start Here

Status: public-safe entrypoint draft for future GitHub readers. This file is a guide, not a release announcement and not a claim that the project is complete.

Date: 2026-06-14.

## 1. Short Framing

Field 01 is currently a cautious formalization workspace.

The repository contains:

- conceptual writing drafts;
- standard vortex-math comparison notes;
- exploratory Field 01 interpretation notes;
- toy numerical diagnostics;
- reference and roadmap documents intended to make the project easier to criticize.

The safest current reading is:

```text
standard radial vortex mathematics
-> scalar modulus / VEV-profile and gauge-convention layer
-> convention map and numerical diagnostics
-> labelled equivalence-class / memory-map definitions
-> clearly separated Field 01 interpretation and open problems
```

## 2. What This Is

This is an attempt to organize a speculative conceptual project into a form that can be criticized.

The strongest current technical substrate is standard radial vortex mathematics related to Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau conventions. In that standard layer, `N(r)` should be read first as a scalar modulus, VEV-profile, or order-parameter profile.

The Field 01 terms `memory`, `normal retention`, `boundary recording`, `horizon-like`, and `charge-like` are interpretive labels unless explicitly defined in a formal note. In particular, `normal retention` is not a new standard degree of freedom; it is a Field 01 reading of the scalar profile unless additional structure is defined.

## 3. What This Is Not

This repository does not currently claim:

- a new verified physical theory;
- a replacement for the Standard Model;
- a replacement for general relativity;
- a new particle model;
- a black-hole model;
- a solution to the black-hole information problem;
- a derivation of Hawking radiation;
- a derivation of Bekenstein-Hawking entropy;
- physical memory preservation;
- experimental predictions.

If any file appears to suggest one of these claims, treat it as a draft wording problem unless the claim is explicitly labelled, defined, and supported.

## 4. Recommended First Reading Path

For the current formalization checkpoint, start with:

1. `analysis/field01_standard_core_v1.md`
2. `analysis/field01_vortex_convention_dictionary.md`
3. `analysis/field01_schaposnik_vortices_convention_map.md`
4. `analysis/field01_bps_coupling_convention_note.md`
5. `analysis/field01_memory_map_definitions_v1.md`
6. `analysis/field01_memory_map_radial_examples_v1.md`
7. `analysis/field01_profile_class_invariants_note.md`
8. `analysis/field01_interpretation_layer_v1.md`
9. `analysis/field01_two_layer_formalization_plan.md`

For a broader but less formal overview, read:

1. `FIELD01_OVERVIEW_EN.md`
2. `FIELD01_REFERENCE_MAP.md`
3. `PROJECT_ROADMAP_EN.md`

## 5. Current Numerical Diagnostics

The compact tracked numerical records are:

```text
analysis/numerics/radial_vortex_results.json
analysis/numerics/radial_vortex_coupling_sweep.json
analysis/numerics/radial_vortex_profile_distances.json
```

The tracked helper scripts are:

```text
analysis/numerics/solve_radial_vortex_profile.py
analysis/numerics/sweep_radial_vortex_coupling.py
```

Generated CSV/PNG artifacts are local/generated files under the current ignore policy unless intentionally added later.

## 6. Feedback Requested

Useful feedback at this stage:

- Are the Abelian-Higgs / Nielsen-Olesen / Abrikosov convention mappings stated correctly?
- Are the BPS normalization statements clear and convention-safe?
- Are the memory-map equivalence relations mathematically well-defined enough to criticize?
- Is the standard-first wording around `N(r)` as scalar modulus / VEV or order-parameter profile clear enough?
- Which Field 01 terms are misleading or too strong?

Less useful at this stage:

- judging Field 01 as a completed physical theory;
- debating black-hole information claims that are explicitly not being made;
- treating interpretive labels as established physics.

## 7. Repository Hygiene

The public repository should contain only project-facing files: overview documents, working papers, analysis notes, numerical summaries, and contribution guidance.

Do not upload personal workflow material or local helper artifacts:

```text
local agent-instruction files
local upload folders
local Prism/GitHub helper folders
local upload-helper folders
local transfer archives
LaTeX temporary files
Python cache files
local publication checklists or personal step-by-step notes
```

## 8. Current Status

Current status: public working archive checkpoint.

The next useful step is technical criticism of the standard-vortex convention map, the `N(r)` terminology, the memory-equivalence definitions, and the separation between standard mathematics and Field 01 interpretation.