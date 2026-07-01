# Field 01 GitHub Start Here

Status: public working archive entrypoint.

Date: 2026-07-01.

## 1. Short Framing

Field 01 is a public working archive for separating a standard vortex-math/convention layer from a speculative interpretation layer, so that the terminology can be criticized before any stronger claims are made.

The repository contains:

- conceptual writing drafts;
- standard Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex comparison notes;
- exploratory Field 01 interpretation notes;
- toy numerical diagnostics;
- reference and roadmap documents.

The safest current reading is:

```text
standard radial vortex mathematics
-> scalar modulus / order-parameter profile and gauge-convention layer
-> convention map and numerical diagnostics
-> labelled equivalence-class / memory-map definitions
-> clearly separated Field 01 interpretation and open problems
```

## 2. What This Is

This is an attempt to organize a speculative conceptual project into a form that can be checked against standard definitions.

The strongest current technical substrate is standard radial vortex mathematics related to Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau conventions. In that standard layer, `N(r)` should be read first as a radial scalar modulus or order-parameter profile approaching a vacuum value.

The Field 01 terms `memory`, `normal retention`, `boundary recording`, `horizon-like`, and `charge-like` are interpretive labels unless explicitly defined in a formal note. In particular, `normal retention` is a Field 01 reading of the scalar profile, not a new standard degree of freedom.

## 3. Current Limit

Field 01 is not presented here as a completed physical theory. The current aim is narrower: define the standard baseline, identify which parts are reinterpretation, and make the open problems explicit.

## 4. Recommended First Reading Path

For the current formalization checkpoint, start with:

1. [analysis/field01_standard_core_v1.md](analysis/field01_standard_core_v1.md)
2. [analysis/field01_vortex_convention_dictionary.md](analysis/field01_vortex_convention_dictionary.md)
3. [analysis/field01_schaposnik_vortices_convention_map.md](analysis/field01_schaposnik_vortices_convention_map.md)
4. [analysis/field01_bps_coupling_convention_note.md](analysis/field01_bps_coupling_convention_note.md)
5. [analysis/field01_memory_map_definitions_v1.md](analysis/field01_memory_map_definitions_v1.md)
6. [analysis/field01_memory_map_radial_examples_v1.md](analysis/field01_memory_map_radial_examples_v1.md)
7. [analysis/field01_profile_class_invariants_note.md](analysis/field01_profile_class_invariants_note.md)
8. [analysis/field01_interpretation_layer_v1.md](analysis/field01_interpretation_layer_v1.md)
9. [analysis/field01_two_layer_formalization_plan.md](analysis/field01_two_layer_formalization_plan.md)

For a broader but less formal overview, read:

1. [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
2. [FIELD01_REFERENCE_MAP.md](FIELD01_REFERENCE_MAP.md)
3. [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)

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

## 6. Questions For Reviewers

Useful review checks at this stage:

- Are the Abelian-Higgs / Nielsen-Olesen / Abrikosov convention mappings stated correctly?
- Are the BPS normalization statements clear and convention-safe?
- Are the memory-map equivalence relations mathematically well-defined enough to criticize?
- Is the standard-first wording around `N(r)` as a radial scalar modulus / order-parameter profile clear enough?
- Which Field 01 terms are misleading or too strong?

## 7. Current Status

Current status: public working archive checkpoint.

The next useful step is technical review of the standard-vortex convention map, the `N(r)` terminology, the memory-equivalence definitions, and the separation between standard mathematics and Field 01 interpretation.