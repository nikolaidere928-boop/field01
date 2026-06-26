# Field 01

**Current reviewer entrypoint:** start with `FIELD01_GITHUB_START_HERE.md` before reading the broader archive. It gives the safest current framing, read order, non-claims, and feedback targets for this work-in-progress.

Field 01 is an independent research and writing project exploring a cautious phase-based language for particles, memory, and boundary recording.

At the present stage, Field 01 is **not** presented as a completed physical theory. It does not claim to replace the Standard Model, quantum field theory, general relativity, or black-hole thermodynamics. The current goal is narrower: to translate a book-level conceptual model into clear working papers, toy mathematical structures, numerical checks, and open questions that can be criticized by readers with stronger backgrounds in physics and mathematics.

## One-Sentence Summary

Field 01 studies whether particle-like and horizon-like phenomena can be described, at toy-model level, using phase circulation, closed nodes, a standard scalar-modulus / VEV-profile layer, labelled normal-retention interpretation, memory classes, and boundary recording.

## Current Status

This repository is a working archive. It contains drafts, notes, toy-model calculations, and reference material. The project is intentionally cautious and distinguishes between:

1. established mathematics and physics;
2. Field 01 interpretation;
3. speculative hypotheses;
4. open problems requiring criticism and formalization.

The most developed mathematical direction currently resembles known Abelian-Higgs or vortex-like structures. Field 01 should therefore not claim novelty merely from phase winding, gauge-like notation, scalar radial profiles, VEV-profile layers, or order-parameter profiles. The possible value, if any, lies only in separately defined interpretations such as normal retention, memory, and boundary recording.

## Main Working Papers

- `articles/particle_as_closed_wave_en.tex` — elementary particle as a closed phase configuration.
- `articles/horizon_as_phase_recording_surface_en.tex` — black-hole horizon as a phase recording surface.
- `articles/field01_formalization_program_en.tex` — formalization program using phase, winding, scalar modulus / VEV-profile vocabulary, labelled normal-retention interpretation, gauge-like compensation, current-like flow, memory classes, and boundary maps.

## Supporting Material

- `FIELD01_GITHUB_START_HERE.md` — safest current first-entry guide for reviewers, with read order, non-claims, and feedback targets.
- `FIELD01_OVERVIEW_EN.md` — short first-entry overview for new readers.
- `FIELD01_REFERENCE_MAP.md` — map from Field 01 terms to standard references and vocabulary.
- `PROJECT_ROADMAP_EN.md` — compact English roadmap.
- `ABSTRACTS_EN.md` — short abstracts for the current papers.
- `FIELD01_GLOSSARY.md` — Russian glossary with recommended English equivalents; a stricter English glossary is planned after the terminology stabilizes.
- `CONTRIBUTING.md` — how to give useful criticism or help with the project.
- `LICENSE_NOTE.md` — temporary usage note before choosing a formal license.
- `LITERATURE_BRIDGE.md` — working map from book recommended literature to academic references.
- `analysis/` — notes, comparisons, and numerical toy-model results.

## What This Project Claims

The project currently claims only that Field 01 can be organized into a coherent research program with a toy-level formal vocabulary:

- closed phase nodes can be represented by winding;
- the Field 01 term `normal retention` can be attached, at toy level, to a standard scalar modulus / VEV or order-parameter profile;
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
- comparing the horizon interpretation with standard black-hole thermodynamics and Hawking radiation;
- identifying whether any testable or theoretically distinguishable prediction exists.

## Feedback Requested

The most useful feedback is critical and specific. In particular:

- Where does this reduce to known physics?
- Which terms are misleading or nonstandard?
- Which equations are mathematically inconsistent or underdefined?
- Which claims should be weakened or removed?
- What literature must be compared first?
- What minimal toy model should be formalized before any broader claims are made?

I am seeking criticism, orientation, and help with formalization — not endorsement.

## Suggested Reading Order

For a first look:

1. `FIELD01_GITHUB_START_HERE.md`
2. `FIELD01_OVERVIEW_EN.md`
3. `ABSTRACTS_EN.md`
4. `PROJECT_ROADMAP_EN.md`
5. `articles/field01_formalization_program_en.tex`

For conceptual background:

1. `articles/particle_as_closed_wave_en.tex`
2. `articles/horizon_as_phase_recording_surface_en.tex`

## Build Notes

The LaTeX papers can be compiled with `latexmk`, for example:

```sh
latexmk -pdf articles/field01_formalization_program_en.tex
```

If using a temporary output directory:

```sh
mkdir -p build
latexmk -pdf -outdir=build articles/field01_formalization_program_en.tex
```

## Collaboration Note

This project is especially open to readers who can help compare the current formulation with established mathematics and physics. The best contribution at this stage is not agreement, but careful criticism.