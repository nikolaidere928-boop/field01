# Field 01 GitHub Start Here

Status: public working archive entrypoint.

Date: 2026-08-05.

## 1. Short Framing

Field 01 is a public working archive for separating a standard vortex-math/convention layer from a speculative interpretation layer, so that the terminology can be criticized before any stronger claims are made.

The repository contains:

- conceptual writing drafts;
- standard Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex comparison notes;
- exploratory Field 01 interpretation notes;
- toy numerical diagnostics;
- a compact reproducible fixed-background checkpoint;
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

The most developed current paper is the particle paper: `Elementary Particle as a Closed Wave of Field 01`. Its core test question is whether an elementary particle can be described as a stable closed phase configuration with finite energy, a local scalar / VEV-like profile, and no point core. The strongest current technical substrate remains standard radial vortex mathematics related to Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau conventions. In that standard layer, `N(r)` should be read first as a radial scalar modulus or order-parameter profile approaching a vacuum value.

The Field 01 terms `memory`, `normal retention`, `boundary recording`, `horizon-like`, and `charge-like` are interpretive labels unless explicitly defined in a formal note. In particular, `normal retention` is a Field 01 reading of the scalar profile, not a new standard degree of freedom.

## 3. Current Limit

Field 01 is not presented here as a completed physical theory. The current aim is narrower: define the standard baseline, identify which parts are reinterpretation, and make the open problems explicit.

## 4. Recommended First Reading Path

For this reader-only package, start with:

1. [FIELD01_OVERVIEW_EN.md](FIELD01_OVERVIEW_EN.md)
2. [ABSTRACTS_EN.md](ABSTRACTS_EN.md)
3. [numerics/fixed_background_checkpoint_v0_3/CHECKPOINT_REPORT.md](numerics/fixed_background_checkpoint_v0_3/CHECKPOINT_REPORT.md)
4. [PROJECT_ROADMAP_EN.md](PROJECT_ROADMAP_EN.md)
5. [articles/particle_as_closed_wave_en.tex](articles/particle_as_closed_wave_en.tex) / [PDF](articles/particle_as_closed_wave_en.pdf)
6. [articles/field01_formalization_program_en.tex](articles/field01_formalization_program_en.tex) / [PDF](articles/field01_formalization_program_en.pdf)
7. [articles/horizon_as_phase_recording_surface_en.tex](articles/horizon_as_phase_recording_surface_en.tex) / [PDF](articles/horizon_as_phase_recording_surface_en.pdf)

For terminology and literature context after that, read:

1. [FIELD01_REFERENCE_MAP.md](FIELD01_REFERENCE_MAP.md)
2. [LITERATURE_BRIDGE.md](LITERATURE_BRIDGE.md)

## 5. Current Numerical Diagnostics

This release includes one deliberately narrow numerical package:

```text
numerics/fixed_background_checkpoint_v0_3/
```

It contains six closure summaries, one unified summary, and a standalone standard-library audit script. It does not contain the complete exploratory workspace or claim full primary-solver reproducibility.

The checkpoint should not be read as physical evidence or as a claim of a new force, interaction, particle spectrum, nonlinear solution, or accepted numerical result.

## 6. Questions For Reviewers

Useful review checks at this stage:

- Is the particle paper clear enough as the current central entry point?
- Can a finite-energy closed phase node be defined without a point core?
- Is the standard-first wording around `N(r)` as a radial scalar modulus / order-parameter profile clear enough?
- Are the Abelian-Higgs / Nielsen-Olesen / Abrikosov convention mappings stated correctly?
- Are the memory-map equivalence relations mathematically well-defined enough to criticize?
- Which Field 01 terms are misleading or too strong?

## 7. Current Status

Current status: `v0.3-fixed-background` public working archive checkpoint.

The most useful next step is independent review of the checkpoint logic and claim boundaries, followed by technical review of the particle paper, standard-vortex convention map, `N(r)` terminology, memory-equivalence definitions, and separation between standard mathematics and Field 01 interpretation.