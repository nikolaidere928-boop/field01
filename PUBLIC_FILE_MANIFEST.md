# Field 01 Public File Manifest

This manifest lists the files that are currently expected to be included in the first public repository, plus files that should remain private or ignored.

Use this file before uploading to GitHub/GitLab.

## Include in First Public Repository

### Core Public Documents

- `FIELD01_GITHUB_START_HERE.md`
- `README.md`
- `FIELD01_OVERVIEW_EN.md`
- `CONTRIBUTING.md`
- `LICENSE_NOTE.md`
- `PUBLIC_READY_STATUS.md`
- `FIELD01_REFERENCE_MAP.md`
- `RELEASE_CHECKLIST.md`
- `FIRST_PUBLIC_POSTS.md`
- `BEGINNER_PUBLICATION_GUIDE_RU.md`
- `FEEDBACK_LOG.md`
- `FOUR_WEEK_LAUNCH_PLAN.md`

### Roadmap and Outreach

- `PROJECT_ROADMAP_EN.md`
- `PROJECT_ROADMAP.md`
- `OUTREACH_PACKAGE_EN.md`
- `OUTREACH_LETTER_EN.md`
- `OUTREACH_LETTER_RU.md`
- `ABSTRACTS_EN.md`
- `FIELD01_GLOSSARY.md`

### Main Articles

- `articles/field01_formalization_program_en.tex`
- `articles/particle_as_closed_wave_en.tex`
- `articles/horizon_as_phase_recording_surface_en.tex`

Optional for public context:

- `articles/field01_formalization_program_en.pdf` — only if generated intentionally before release
- `articles/particle_as_closed_wave.tex`
- `articles/horizon_as_phase_recording_surface.tex`

### Analysis Notes

Useful, but review before wide public attention. Start with the current formalization checkpoint:

- `analysis/README.md`
- `analysis/field01_github_ready_manifest_v1.md`
- `analysis/field01_internal_consistency_pass_v1.md`
- `analysis/field01_two_layer_formalization_plan.md`
- `analysis/field01_standard_core_v1.md`
- `analysis/field01_vortex_convention_dictionary.md`
- `analysis/field01_schaposnik_vortices_convention_map.md`
- `analysis/field01_memory_map_definitions_v1.md`
- `analysis/field01_memory_map_radial_examples_v1.md`
- `analysis/field01_profile_class_invariants_note.md`
- `analysis/field01_interpretation_layer_v1.md`

Older/background analysis notes, useful after review:

- `analysis/field01_abelian_higgs_comparison.md`
- `analysis/field01_covariant_gauge_bridge.md`
- `analysis/field01_formalization_notes.md`
- `analysis/field01_formalization_roadmap.md`
- `analysis/field01_memory_equivalence_notes.md`
- `analysis/field01_noether_current_notes.md`
- `analysis/field01_reduced_density_memory_notes.md`
- `analysis/field01_screened_numerical_results.md`
- `analysis/field01_screened_phase_normal_model.md`
- `analysis/field01_toy_numerical_results.md`
- `analysis/field01_toy_phase_normal_model.md`

### Numerical Reproducibility

Current radial-vortex formalization diagnostics:

- `analysis/numerics/solve_radial_vortex_profile.py`
- `analysis/numerics/sweep_radial_vortex_coupling.py`
- `analysis/numerics/radial_vortex_results.json`
- `analysis/numerics/radial_vortex_coupling_sweep.json`
- `analysis/numerics/radial_vortex_profile_distances.json`

Earlier phase-normal toy diagnostics, optional after review:

- `analysis/numerics/solve_phase_normal_profile.py`
- `analysis/numerics/solve_screened_phase_normal_profile.py`
- `analysis/numerics/phase_normal_profile_results.json`
- `analysis/numerics/screened_phase_normal_results.json`

Generated CSV/PNG profile artifacts should remain ignored unless intentionally included as release assets.

## Keep Private / Do Not Upload

These are local or potentially private workspace materials:

- `AGENTS.md`
- `uploads/`
- `prism-uploads/`
- `.git/`

These are currently ignored by `.gitignore`.

## Ignore / Do Not Track

Temporary files should not be uploaded:

- LaTeX build artifacts: `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex`, `.synctex.gz`
- Python cache: `__pycache__/`, `.pyc`
- temporary build folders: `build/`, `latex-build/`, `.tmp/`, `.cache/`

## Current Git Status Snapshot

The current public-preparation files are not yet committed. Before publishing, review `git status --short` and confirm that only intended files are staged or uploaded.

Suggested command:

```sh
git status --short
```

Suggested ignored-file check:

```sh
git status --short --ignored
```

## Manual Review Checklist

Before uploading, open and skim these files:

- [ ] `FIELD01_GITHUB_START_HERE.md`
- [ ] `README.md`
- [ ] `FIELD01_REFERENCE_MAP.md`
- [ ] `FIELD01_OVERVIEW_EN.md`
- [ ] `PUBLIC_READY_STATUS.md`
- [ ] `LICENSE_NOTE.md`
- [ ] `articles/field01_formalization_program_en.tex`
- [ ] `analysis/field01_github_ready_manifest_v1.md`
- [ ] `analysis/field01_standard_core_v1.md`
- [ ] `analysis/field01_memory_map_definitions_v1.md`
- [ ] `analysis/numerics/solve_radial_vortex_profile.py`
- [ ] `analysis/numerics/sweep_radial_vortex_coupling.py`

Check for:

- private names or contact details you do not want public;
- absolute local paths;
- accidental claims of a completed theory;
- hostile language toward established physics;
- files copied from uploads that should remain private;
- large files that are unnecessary for first release.

## Recommended Upload Strategy

If uploading manually through GitHub web UI, upload in this order:

1. root `.md` files;
2. `articles/` folder;
3. selected `analysis/` notes;
4. selected `analysis/numerics/` scripts and outputs;
5. selected PDFs only if intentional.

If using Git locally, commit only after reviewing `git status --short`.

Do not commit or upload `uploads/`, `prism-uploads/`, or `AGENTS.md`.