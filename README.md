# Field 01

**Reviewer entrypoint:** [FIELD01_GITHUB_START_HERE.md](FIELD01_GITHUB_START_HERE.md)

**Author:** Nikolai Dereviankin  
**Release checkpoint:** `v0.4-fixed-background-handoff`  
**Release date:** 2026-08-06  
**Numerical report update:** 2026-08-07

Field 01 is a public working archive that separates a standard mathematical and physical baseline from a speculative interpretation layer. The project is organized so that terminology, equations, numerical assumptions, and open proof obligations can be criticized independently.

## One-Sentence Summary

Field 01 studies whether selected particle-like and boundary-like ideas can be organized around phase circulation, radial scalar profiles, gauge-convention choices, equivalence classes, and boundary maps at toy-model level.

## Current Status

The particle paper remains the central conceptual entry point. The strongest standard mathematical comparison layer remains related to Abelian-Higgs, Nielsen-Olesen, Abrikosov, Ginzburg-Landau, vortex, soliton, and topological-defect language.

Release `v0.4` freezes one restricted fixed-background optimization contour as a numerical benchmark. It records:

- one confirmed direct-fold benchmark;
- nine audited profile coordinates;
- a retained two-component shape;
- a compact standard-library consistency audit;
- explicit limits on what is and is not authorized next.

The retained checkpoint is:

```text
difference profile:
    core power q = 16
    shoulder coefficient d = 4
    node parameter zeta = 1.810582828929
    linear width c1 = 1.20
    quadratic width c2 = 0
    cubic-exponential tilt lambda = -0.35

aligned profile:
    shell power p = 1
    linear width c1 = -3.260
    quadratic width c2 = 3.041
    aligned cubic-exponential tilt rho = 0

confirmed fold diagnostic:
    xi_br,max = 2.0934591793773114e-3
```

The confirmed fold improves the previous `v0.3` benchmark by `1.218886%`. The largest unresolved connected-coordinate predictor gain is `0.917518%`, below the internal `1%` authorization threshold for another direct fold.

See:

- [numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md](numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md)
- [numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md](numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md)
- [RELEASE_NOTES_V0_4.md](RELEASE_NOTES_V0_4.md)

## Bilingual Fixed-Background Numerical Report

The new bilingual numerical report documents the retained two-component profile, the restricted optimization space, structural and physical acceptance gates, the cubic predictor, direct-fold and matching-radius validation, closure of nine coordinates, and the explicit boundary of the result.

- **English:** [LaTeX source](articles/fixed_background_optimization_v0_4_en.tex) / [PDF](articles/fixed_background_optimization_v0_4_en.pdf)
- **Russian:** [LaTeX source](articles/fixed_background_optimization_v0_4.tex) / [PDF](articles/fixed_background_optimization_v0_4.pdf)
- [Retained-localizer figure](figures/fixed_background_v0_4_retained_localizers.png)
- [Sampled profile data](analysis/numerics/fixed_background_v0_4_retained_localizers.csv)
- [Reproducible figure generator](analysis/numerics/plot_fixed_background_v0_4_retained_localizers.py)

The report includes standard numerical and localized-field references. It does not claim global optimality, a fundamental Field 01 action, full static backreaction, dynamical stability, particle spectra, or experimental evidence.

## Scientific Boundary

The numerical handoff closes the audited coordinates of the selected fixed-background ansatz under the stated gates. It does **not** prove global optimality over all functions, all actions, or all possible field content.

This release does not establish:

- a completed physical theory;
- experimental evidence;
- a fundamental action;
- a full nonlinear static solution;
- dynamic stability or a dynamic-root spectrum;
- physical particle masses, charges, or generations;
- a solution to a black-hole information problem.

Full static backreaction and dynamic-root analysis remain outside the release boundary.

## Main Working Papers

- [articles/fixed_background_optimization_v0_4_en.tex](articles/fixed_background_optimization_v0_4_en.tex) / [PDF](articles/fixed_background_optimization_v0_4_en.pdf) — reproducible numerical report for the retained fixed-background checkpoint; [Russian source](articles/fixed_background_optimization_v0_4.tex) / [Russian PDF](articles/fixed_background_optimization_v0_4.pdf).
- [articles/particle_as_closed_wave_en.tex](articles/particle_as_closed_wave_en.tex) / [PDF](articles/particle_as_closed_wave_en.pdf) — elementary particle as a closed phase configuration.
- [articles/field01_formalization_program_en.tex](articles/field01_formalization_program_en.tex) / [PDF](articles/field01_formalization_program_en.pdf) — formalization program.
- [articles/horizon_as_phase_recording_surface_en.tex](articles/horizon_as_phase_recording_surface_en.tex) / [PDF](articles/horizon_as_phase_recording_surface_en.pdf) — horizon-like boundary-recording interpretation.

Russian source versions are retained where available. The `.tex` files are canonical editable sources; PDFs are reader copies.

## Supporting Documents

- [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
- [ABSTRACTS_EN.md](ABSTRACTS_EN.md)
- [FIELD01_REFERENCE_MAP.md](FIELD01_REFERENCE_MAP.md)
- [FIELD01_GLOSSARY.md](FIELD01_GLOSSARY.md)
- [LITERATURE_BRIDGE.md](LITERATURE_BRIDGE.md)
- [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)
- [LICENSE_NOTE.md](LICENSE_NOTE.md)
- [RELEASE_MANIFEST_V0_4.md](RELEASE_MANIFEST_V0_4.md)

## Reproduce the Public Checkpoint Audit

From the repository root:

```sh
python numerics/fixed_background_checkpoint_v0_4/audit_checkpoint.py
```

The script uses only the Python standard library. It audits the compact derived records; it does not rerun the complete internal boundary-value solver campaign.

## Recommended Reading Order

1. [FIELD01_GITHUB_START_HERE.md](FIELD01_GITHUB_START_HERE.md)
2. [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
3. [numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md](numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md)
4. [numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md](numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md)
5. [articles/fixed_background_optimization_v0_4_en.pdf](articles/fixed_background_optimization_v0_4_en.pdf)
6. [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)
7. [articles/particle_as_closed_wave_en.pdf](articles/particle_as_closed_wave_en.pdf)
8. [articles/field01_formalization_program_en.pdf](articles/field01_formalization_program_en.pdf)
9. [articles/horizon_as_phase_recording_surface_en.pdf](articles/horizon_as_phase_recording_surface_en.pdf)

## Build Notes

The papers can be compiled with `latexmk`, for example:

```sh
latexmk -pdf articles/fixed_background_optimization_v0_4_en.tex
latexmk -pdf articles/fixed_background_optimization_v0_4.tex
latexmk -pdf articles/particle_as_closed_wave_en.tex
latexmk -pdf articles/field01_formalization_program_en.tex
latexmk -pdf articles/horizon_as_phase_recording_surface_en.tex
```

## Collaboration Note

The most useful contribution at this stage is precise criticism: standard terminology, missing references, incorrect equations, hidden assumptions, numerical reproducibility issues, or claims that should be weakened.