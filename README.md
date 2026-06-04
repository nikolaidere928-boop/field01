# Field 01

Field 01 is an independent research and writing project exploring a cautious phase-based language for particles, memory, and boundary recording.

At the present stage, Field 01 is **not** presented as a completed physical theory. It does not claim to replace the Standard Model, quantum field theory, general relativity, or black-hole thermodynamics. The current goal is narrower: to translate a book-level conceptual model into clear working papers, toy mathematical structures, numerical checks, and open questions that can be criticized by readers with stronger backgrounds in physics and mathematics.

## One-Sentence Summary

Field 01 studies whether particle-like and horizon-like phenomena can be described, at toy-model level, using phase circulation, closed nodes, normal retention, memory classes, and boundary recording.

## Current Status

This repository is a working archive. It contains drafts, notes, toy-model calculations, and outreach material. The project is intentionally cautious and distinguishes between:

1. established mathematics and physics;
2. Field 01 interpretation;
3. speculative hypotheses;
4. open problems requiring criticism and formalization.

The most developed mathematical direction currently resembles known Abelian-Higgs or vortex-like structures. Field 01 should therefore not claim novelty merely from phase winding, gauge-like notation, or scalar radial profiles. The possible value, if any, lies in the proposed interpretation of normal retention, memory, and boundary recording.

## Main Working Papers

- `articles/particle_as_closed_wave_en.tex` — elementary particle as a closed phase configuration.
- `articles/horizon_as_phase_recording_surface_en.tex` — black-hole horizon as a phase recording surface.
- `articles/field01_formalization_program_en.tex` — formalization program using phase, winding, normal retention, gauge-like compensation, current-like flow, memory classes, and boundary maps.

## Supporting Material

- `FIELD01_OVERVIEW_EN.md` — short first-entry overview for new readers.
- `PROJECT_ROADMAP_EN.md` — compact English roadmap.
- `OUTREACH_PACKAGE_EN.md` — guide for sharing the project with external readers.
- `OUTREACH_LETTER_EN.md` — cautious first-contact message template.
- `ABSTRACTS_EN.md` — short abstracts for the current papers.
- `FIELD01_GLOSSARY.md` — current terminology and preferred cautious language.
- `CONTRIBUTING.md` — how to give useful criticism or help with the project.
- `FIRST_PUBLIC_POSTS.md` — cautious templates for Reddit, repository announcements, and first public messages.
- `RELEASE_CHECKLIST.md` — checklist for the first public repository release.
- `LICENSE_NOTE.md` — temporary usage note before choosing a formal license.
- `BEGINNER_PUBLICATION_GUIDE_RU.md` — practical Russian guide for publishing the project as a beginner.
- `FEEDBACK_LOG.md` — template for recording criticism, references, and revision decisions.
- `PUBLIC_READY_STATUS.md` — current readiness summary for first public release.
- `PUBLIC_FILE_MANIFEST.md` — file-by-file manifest for GitHub/GitLab upload.
- `NEXT_ACTIONS_RU.md` — immediate step-by-step actions for GitHub release and first Reddit post.
- `analysis/` — notes, comparisons, and numerical toy-model results.

## What This Project Claims

The project currently claims only that Field 01 can be organized into a coherent research program with a toy-level formal vocabulary:

- closed phase nodes can be represented by winding;
- normal retention can be modeled by a scalar profile;
- gauge-like compensation can reduce long-range phase mismatch;
- a current-like object follows from phase-shift symmetry in the toy model;
- memory can be formalized as an equivalence class of preserved data;
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

1. `FIELD01_OVERVIEW_EN.md`
2. `ABSTRACTS_EN.md`
3. `PROJECT_ROADMAP_EN.md`
4. `articles/field01_formalization_program_en.tex`

For conceptual background:

1. `articles/particle_as_closed_wave_en.tex`
2. `articles/horizon_as_phase_recording_surface_en.tex`

For outreach or collaboration:

1. `OUTREACH_PACKAGE_EN.md`
2. `OUTREACH_LETTER_EN.md`

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