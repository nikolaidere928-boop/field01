# Field 01 Upload Manifest — v0.2-feedback

Canonical upload source for the next online repository sync:

```text
GITHUB_UPLOAD_READY/
```

Status: dry-run upload manifest. This does not publish anything.

## Upload Rule

Upload or sync the contents of `GITHUB_UPLOAD_READY/` only. Do not upload the whole workspace.

Keep out of the upload:

- `AGENTS.md`;
- `uploads/`;
- `prism-uploads/`;
- local LaTeX build files and logs;
- Python `__pycache__/` directories;
- legacy local toy-profile diagnostics not present in `GITHUB_UPLOAD_READY/`;
- generated CSV/PNG artifacts unless intentionally selected later.

## Current File Count

`44` files are currently present in `GITHUB_UPLOAD_READY/`.

## Safety Check Summary

- Forbidden/private path hits: `0`.
- Legacy upload filename hits: `0`.
- Main entrypoint: `FIELD01_GITHUB_START_HERE.md`.
- Main technical paper: `articles/field01_formalization_program_en.tex`.
- Current numerical scripts: `analysis/numerics/solve_radial_vortex_profile.py`, `analysis/numerics/sweep_radial_vortex_coupling.py`.

## File List

```text
ABSTRACTS_EN.md
CONTRIBUTING.md
FIELD01_GITHUB_START_HERE.md
FIELD01_GLOSSARY.md
FIELD01_OVERVIEW_EN.md
FIELD01_REFERENCE_MAP.md
LICENSE_NOTE.md
LITERATURE_BRIDGE.md
PROJECT_ROADMAP_EN.md
README.md
UPLOAD_MANIFEST_v0.2_FEEDBACK.md
analysis/README.md
analysis/field01_abelian_higgs_comparison.md
analysis/field01_bps_coupling_convention_note.md
analysis/field01_covariant_gauge_bridge.md
analysis/field01_formalization_notes.md
analysis/field01_formalization_roadmap.md
analysis/field01_interpretation_layer_v1.md
analysis/field01_math_core_v0.md
analysis/field01_memory_equivalence_notes.md
analysis/field01_memory_map_definitions_v1.md
analysis/field01_memory_map_radial_examples_v1.md
analysis/field01_noether_current_notes.md
analysis/field01_profile_class_invariants_note.md
analysis/field01_radial_vortex_bps_sweep_results.md
analysis/field01_radial_vortex_functional_derivation.md
analysis/field01_radial_vortex_numerical_results.md
analysis/field01_reduced_density_memory_notes.md
analysis/field01_schaposnik_vortices_convention_map.md
analysis/field01_standard_core_v1.md
analysis/field01_standard_vortex_comparison_note.md
analysis/field01_two_layer_formalization_plan.md
analysis/field01_vortex_convention_dictionary.md
analysis/field01_vortex_convention_external_feedback.md
analysis/numerics/radial_vortex_coupling_sweep.json
analysis/numerics/radial_vortex_profile_distances.json
analysis/numerics/radial_vortex_results.json
analysis/numerics/solve_radial_vortex_profile.py
analysis/numerics/sweep_radial_vortex_coupling.py
articles/field01_formalization_program_en.tex
articles/horizon_as_phase_recording_surface.tex
articles/horizon_as_phase_recording_surface_en.tex
articles/particle_as_closed_wave.tex
articles/particle_as_closed_wave_en.tex
```

## Publish Decision

The package is prepared for manual review. Publish/update only after opening the online repository and confirming that its file list should be replaced by this manifest.