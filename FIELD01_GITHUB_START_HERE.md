# Field 01 GitHub Start Here

Status: public working archive entrypoint.  
Date: 2026-08-07.  
Checkpoint: `v0.4-fixed-background-handoff`.

## 1. Short Framing

Field 01 is an independent research and writing project. The repository separates:

1. established mathematics and physics;
2. Field 01 interpretation;
3. new hypotheses;
4. open mathematical and physical problems.

The safest reading path is:

```text
standard phase / gauge / vortex language
-> radial scalar profile and convention layer
-> fixed-background numerical benchmark
-> Field 01 interpretation labels
-> explicit open proof obligations
```

## 2. Recommended Reading Path

1. [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
2. [ABSTRACTS_EN.md](ABSTRACTS_EN.md)
3. [numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md](numerics/fixed_background_checkpoint_v0_4/CHECKPOINT_REPORT.md)
4. [numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md](numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md)
5. [articles/fixed_background_optimization_v0_4_en.pdf](articles/fixed_background_optimization_v0_4_en.pdf)
6. [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)
7. [articles/particle_as_closed_wave_en.pdf](articles/particle_as_closed_wave_en.pdf)
8. [articles/field01_formalization_program_en.pdf](articles/field01_formalization_program_en.pdf)
9. [articles/horizon_as_phase_recording_surface_en.pdf](articles/horizon_as_phase_recording_surface_en.pdf)

For terminology and literature context:

1. [FIELD01_REFERENCE_MAP.md](FIELD01_REFERENCE_MAP.md)
2. [FIELD01_GLOSSARY.md](FIELD01_GLOSSARY.md)
3. [LITERATURE_BRIDGE.md](LITERATURE_BRIDGE.md)

## 3. Bilingual Numerical Report

The retained checkpoint is documented in a standalone report with complete Russian and English editions:

- [English LaTeX](articles/fixed_background_optimization_v0_4_en.tex) / [English PDF](articles/fixed_background_optimization_v0_4_en.pdf)
- [Russian LaTeX](articles/fixed_background_optimization_v0_4.tex) / [Russian PDF](articles/fixed_background_optimization_v0_4.pdf)
- [Retained-localizer figure](figures/fixed_background_v0_4_retained_localizers.png)
- [Sampled profile data](analysis/numerics/fixed_background_v0_4_retained_localizers.csv)
- [Figure generator](analysis/numerics/plot_fixed_background_v0_4_retained_localizers.py)

The report explains the profile families, optimization gates, direct-fold validation, nine-coordinate closure, public audit, literature context, and explicit non-claims.

## 4. Numerical Handoff

The current compact checkpoint is located at:

```text
numerics/fixed_background_checkpoint_v0_4/
```

It records a confirmed retained fold diagnostic:

```text
xi_br,max = 2.0934591793773114e-3
```

Nine selected profile coordinates are closed under structural, fixed-background, predictor-gain, matching-radius, and direct-fold authorization rules. The largest unresolved connected-coordinate predictor gain is `0.917518%`, below the internal `1%` direct-fold threshold.

This is a closure statement for the audited fixed-background ansatz, not a proof of global functional optimality.

## 5. What The Checkpoint Reproduces

The public audit verifies:

- one consistent confirmed fold value;
- nine coordinate-closure flags;
- direct-fold validation and matching-radius flags;
- the maximum unresolved predictor gain;
- absence of full-static or dynamic-root authorization.

The release does not include the complete exploratory workspace or rerun every primary boundary-value solve.

## 6. Questions For Reviewers

- Is the numerical claim boundary stated clearly enough?
- Are the profile coordinates and retained shape documented unambiguously?
- Are the standard vortex and scalar-profile comparisons appropriate?
- Which Field 01 terms remain misleading or underdefined?
- What independent physical sector should be tested before full backreaction?
- Which assumptions would prevent the retained fixed-background shape from extending to a consistent action?

## 7. Current Limit

Field 01 is not presented as a completed physical theory. Full static backreaction, dynamic roots, physical particle spectra, and experimental interpretation remain open.