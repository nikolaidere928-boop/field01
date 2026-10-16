# Field 01

**Nikolai Dereviankin** · Research notes and working papers

Field 01 explores a phase-based interpretation of localized field configurations, memory, and boundary recording. The papers distinguish standard mathematical constructions from proposed interpretations and open physical questions.

## Reading Guide

- [Overview](FIELD01_OVERVIEW_EN.md) — the idea, terminology, and scope.
- [Working papers and abstracts](ABSTRACTS_EN.md) — a short guide to the articles.
- [For reviewers](FIELD01_GITHUB_START_HERE.md) — results, limitations, and questions for criticism.

## Working Papers

| Paper | English edition | Source | Reader copy |
|---|---|---|---|
| Elementary Particle as a Closed Wave | v0.4.3 · 16 October 2026 | [LaTeX](articles/particle_as_closed_wave_en.tex) | [PDF](articles/particle_as_closed_wave_en.pdf) |
| A Formalization Program for Field 01 | v0.5.2 · 16 October 2026 | [LaTeX](articles/field01_formalization_program_en.tex) | [PDF](articles/field01_formalization_program_en.pdf) |
| Reading a Past Label versus Updating a Surface Record | v0.2 · 16 October 2026 | [LaTeX](articles/reading_past_label_vs_updating_surface_record_en.tex) | [PDF](articles/reading_past_label_vs_updating_surface_record_en.pdf) |
| Horizon as a Phase Recording Surface | v0.2 · editorial revision, 16 October 2026 | [LaTeX](articles/horizon_as_phase_recording_surface_en.tex) | [PDF](articles/horizon_as_phase_recording_surface_en.pdf) |
| Fixed-Background Profile Optimization | v0.4 · 7 August 2026 | [LaTeX](articles/fixed_background_optimization_v0_4_en.tex) | [PDF](articles/fixed_background_optimization_v0_4_en.pdf) |

The current English particle and formalization papers distinguish the scalar/gauge vortex benchmark from a physical photon. They make no new numerical claim. The horizon paper presents a separate hypothesis, not a consequence established by the other papers.

The October methodological paper studies reading and updating in a specified linear bulk--boundary model. Its operational results do not test the cosmological proposal or establish a general physical memory mechanism.

## Numerical Benchmark

The August fixed-background checkpoint retains the diagnostic

```text
xi_br,max = 2.0934591793773114e-3
```

It concerns a selected two-component profile family with nine audited coordinates. The result is limited to that family and its stated acceptance criteria; it is not a global optimum or a particle prediction.

- [Numerical report](articles/fixed_background_optimization_v0_4_en.pdf)
- [Checkpoint and data](numerics/fixed_background_checkpoint_v0_4/README.md)
- [Calculation history](numerics/fixed_background_checkpoint_v0_4/NUMERICAL_EVOLUTION.md)
- [Figure data](analysis/numerics/fixed_background_v0_4_retained_localizers.csv)

The supplied consistency check validates the published summaries, not the complete underlying solver chain:

```sh
python numerics/fixed_background_checkpoint_v0_4/audit_checkpoint.py
```

### Separate exact audit: NUM67

NUM67 is a later exact-arithmetic comparison of two saved states at the
midpoint of their common first mesh cell. It decomposes one local forced-RHS
difference and reproduces the corresponding NUM66 balance contribution; it
does not add a solver run or establish causal attribution. The complete
inputs, verifier, exact result, and limitations are in the
[NUM67 reproduction package](numerics/num67_midpoint_decomposition/README.md).

## Scope

The current work does not establish a fundamental Field 01 action, a stable three-dimensional elementary particle, a physical mass or charge spectrum, a photon-to-particle transition, or a horizon radiation law. The new boundary-oscillator paper uses “record” operationally and does not test Field 01's cosmological claims. Memory and boundary recording remain interpretation-level proposals unless a specific mathematical definition is stated.

For further context, see the [research questions](PROJECT_ROADMAP_EN.md), [glossary](FIELD01_GLOSSARY.md), and [reference map](FIELD01_REFERENCE_MAP.md).

## Building the Revised Papers

From the repository root, with a LaTeX installation including `latexmk`:

```sh
cd articles
latexmk -pdf -interaction=nonstopmode -halt-on-error particle_as_closed_wave_en.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error field01_formalization_program_en.tex
```

For a byte-stable v0.2 release with the same LaTeX toolchain, run
`sh build_methodological_paper.sh` from `github_public`. It pins
`SOURCE_DATE_EPOCH` to 16 October 2026 UTC, cleans and builds the PDF, then
regenerates and checks the checksum manifest. Use this script instead of an
unpinned standalone build when preserving the release checksum.

## Current Edition

The [16 October editorial note](EDITION_2026_10_16.md) documents version 0.2 of the methodological paper. The [16 October checksums](SHA256SUMS_2026_10_16.txt) verify its source, references, reader PDF, and index files. The [September editorial note](EDITION_2026_09_10.md) distinguishes the revised papers from the unchanged August numerical release.

Precise criticism of equations, assumptions, terminology, references, and reproducibility is welcome.