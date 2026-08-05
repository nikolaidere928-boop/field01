# Field 01

**Current reviewer entrypoint:** start with [FIELD01_GITHUB_START_HERE.md](FIELD01_GITHUB_START_HERE.md) before reading the broader archive.

**Author:** Nikolai Dereviankin.

**Release checkpoint:** `v0.3-fixed-background`, dated 2026-08-05.

Field 01 is a public working archive for separating a standard vortex-math/convention layer from a speculative interpretation layer, so that the terminology can be criticized before any stronger claims are made.

The current goal is to translate a book-level conceptual model into clearer working notes: standard definitions first, Field 01 labels second, open problems last. The particle paper is currently the most developed conceptual and mathematical entry point; the other papers provide context and open directions.

## One-Sentence Summary

Field 01 studies whether selected particle-like and boundary-like ideas can be organized around phase circulation, radial scalar profiles, gauge-convention choices, equivalence classes, and boundary maps at toy-model level.

## Current Status

This repository is a working archive. It contains drafts, notes, toy-model calculations, and reference material. The public structure distinguishes between:

1. established mathematics and physics;
2. Field 01 interpretation;
3. speculative hypotheses;
4. open problems requiring criticism and formalization.

The most developed single paper is currently `Elementary Particle as a Closed Wave of Field 01`. Its central question is whether an elementary particle can be treated as a stable closed phase configuration with finite energy, a local scalar / VEV-like profile, and no point core. The most developed mathematical direction still resembles known Abelian-Higgs or vortex-like structures. In that layer, `N(r)` is treated first as a radial scalar modulus or order-parameter profile approaching a vacuum value. Field 01 labels such as `normal retention`, `memory`, and `boundary recording` are interpretation-layer vocabulary, not standard physics terminology.

This release also contains a compact fixed-background numerical checkpoint. Six gated one-coordinate profile families are closed around one retained discrete shape. The largest conservative unresolved one-coordinate headroom is `0.332421%`, below the internal `1%` direct-fold threshold. See [the checkpoint report](numerics/fixed_background_checkpoint_v0_3/CHECKPOINT_REPORT.md).

## Current Limit

Field 01 is not presented here as a completed physical theory. The current aim is narrower: define the standard baseline, identify which parts are reinterpretation, and make the open problems explicit.

The numerical checkpoint is not a full nonlinear solution, experimental result, stability proof, or validation of the Field 01 interpretation. Full static backreaction and dynamic-root analysis are outside this release.

## Main Working Papers

- [articles/particle_as_closed_wave_en.tex](articles/particle_as_closed_wave_en.tex) / [PDF](articles/particle_as_closed_wave_en.pdf) — elementary particle as a closed phase configuration.
- [articles/horizon_as_phase_recording_surface_en.tex](articles/horizon_as_phase_recording_surface_en.tex) / [PDF](articles/horizon_as_phase_recording_surface_en.pdf) — horizon-like boundary recording interpretation.
- [articles/field01_formalization_program_en.tex](articles/field01_formalization_program_en.tex) / [PDF](articles/field01_formalization_program_en.pdf) — formalization program using phase, winding, radial scalar profiles, gauge-like compensation, current-like flow, memory classes, and boundary maps.

PDF files are included for easier reading. The `.tex` sources remain the canonical editable versions.

## Supporting Material

- [FIELD01_GITHUB_START_HERE.md](FIELD01_GITHUB_START_HERE.md) — first-entry guide for reviewers, with read order and review questions.
- [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md) — short first-entry overview for new readers.
- [FIELD01_REFERENCE_MAP.md](FIELD01_REFERENCE_MAP.md) — map from Field 01 terms to standard references and vocabulary.
- [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md) — compact English roadmap.
- [ABSTRACTS_EN.md](ABSTRACTS_EN.md) — short abstracts for the current papers.
- [FIELD01_GLOSSARY.md](FIELD01_GLOSSARY.md) — Russian glossary with recommended English equivalents; a stricter English glossary is planned after the terminology stabilizes.
- [LICENSE_NOTE.md](LICENSE_NOTE.md) — temporary usage note before choosing a formal license.
- [LITERATURE_BRIDGE.md](LITERATURE_BRIDGE.md) — working map from book recommended literature to academic references.
- [numerics/fixed_background_checkpoint_v0_3/README.md](numerics/fixed_background_checkpoint_v0_3/README.md) — numerical scope, reproduction command, and file map.
- [RELEASE_NOTES_V0_3.md](RELEASE_NOTES_V0_3.md) — exact release boundary and non-claims.

## Working Scope

The project currently tries to organize the following toy-level vocabulary:

- closed phase nodes can be represented by winding;
- the Field 01 term `normal retention` can be attached, at toy level, to a standard radial scalar modulus or order-parameter profile;
- gauge-like compensation can reduce long-range phase mismatch;
- a current-like object follows from phase-shift symmetry in the toy model;
- memory can be formalized as an equivalence class of selected/recorded data;
- boundary recording can be represented by a bulk-to-boundary map;
- reduced external descriptions can be interpreted as limited access to boundary data.

## What Remains Open

Important unresolved problems include:

- defining a precise fundamental action;
- comparing the model rigorously with Abelian-Higgs, vortex, soliton, and topological-defect literature;
- clarifying any relation to the Standard Model;
- deriving or rejecting links to spin, charge, and particle spectra;
- constructing a boundary Hilbert-space description;
- comparing the boundary-recording interpretation with standard black-hole thermodynamics, Hawking radiation, and holographic language;
- identifying whether any testable or theoretically distinguishable prediction exists.
- testing genuinely new profile bases beyond the closed separable polynomial family;
- solving the full static backreaction system;
- auditing dynamic roots and stability.

## Review Questions

The most useful review is critical and specific. In particular:

- Where does this reduce to known physics?
- Which terms are misleading or nonstandard?
- Which equations are mathematically inconsistent or underdefined?
- Which claims should be weakened or removed?
- What literature must be compared first?
- What minimal toy model should be formalized before any broader claims are made?

The most useful response is precise correction: standard terminology, missing references, wrong equations, or places where Field 01 language should be weakened.

## Suggested Reading Order

For a first look:

1. [FIELD01_GITHUB_START_HERE.md](FIELD01_GITHUB_START_HERE.md)
2. [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
3. [ABSTRACTS_EN.md](ABSTRACTS_EN.md)
4. [numerics/fixed_background_checkpoint_v0_3/CHECKPOINT_REPORT.md](numerics/fixed_background_checkpoint_v0_3/CHECKPOINT_REPORT.md)
5. [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)
6. [articles/particle_as_closed_wave_en.tex](articles/particle_as_closed_wave_en.tex) / [PDF](articles/particle_as_closed_wave_en.pdf)
7. [articles/field01_formalization_program_en.tex](articles/field01_formalization_program_en.tex) / [PDF](articles/field01_formalization_program_en.pdf)
8. [articles/horizon_as_phase_recording_surface_en.tex](articles/horizon_as_phase_recording_surface_en.tex) / [PDF](articles/horizon_as_phase_recording_surface_en.pdf)

## Build Notes

The LaTeX papers can be compiled with `latexmk`, for example:

```sh
latexmk -pdf articles/particle_as_closed_wave_en.tex
latexmk -pdf articles/field01_formalization_program_en.tex
latexmk -pdf articles/horizon_as_phase_recording_surface_en.tex
```

If using a temporary output directory:

```sh
mkdir -p build
latexmk -pdf -outdir=build articles/particle_as_closed_wave_en.tex
```

## Collaboration Note

This project is especially open to readers who can help compare the current formulation with established mathematics and physics. The best contribution at this stage is not agreement, but careful criticism.