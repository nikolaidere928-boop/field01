# Field 01 Outreach Package

This note is a compact guide for sending the current Field 01 materials to external readers. It is intended as a cover document, not as a new article.

## Project Status

Field 01 is an independent research program, not a completed physical theory. It does not present itself as a replacement for the Standard Model, quantum field theory, or general relativity.

The current aim is more limited: to formulate a cautious phase-based and topological language for discussing elementary particles, mass, memory, and black-hole horizons, and to identify what must be formalized mathematically.

## Core Materials

Available package materials:

1. `OUTREACH_LETTER_EN.md` --- email text for first contact.
2. `ABSTRACTS_EN.md` --- abstracts and short summaries.
3. `articles/particle_as_closed_wave_en.tex` --- English working paper on elementary particles as closed waves.
4. `articles/horizon_as_phase_recording_surface_en.tex` --- English working paper on horizons as phase recording surfaces.
5. `articles/field01_formalization_program_en.tex` --- technical formalization supplement; send only on request or to mathematically oriented readers.
5. `FIELD01_GLOSSARY.md` --- current terminology and cautious translations.
6. `PROJECT_ROADMAP_EN.md` --- English development plan and open formalization tasks.
7. `PROJECT_ROADMAP.md` --- original Russian roadmap.

For a first email, send only the letter plus one conceptual paper:

```text
OUTREACH_LETTER_EN.md
articles/particle_as_closed_wave_en.tex
```

If the reader is more interested in black holes, send:

```text
OUTREACH_LETTER_EN.md
articles/horizon_as_phase_recording_surface_en.tex
```

## Suggested Attachment Order

Best order for an external reader:

1. short email text;
2. one-sentence project description;
3. one conceptual working paper;
4. optional second conceptual paper if relevant;
5. formalization supplement only if they ask for mathematics;
6. glossary only if they ask for terminology;
7. roadmap only if they ask about the research program.

Do not overload the first contact with the whole book or the full technical supplement.

## One-Sentence Description

Field 01 explores whether particles and black-hole horizons can be described as phase-structural regimes of a field: open transport, closed waves, normal retention, memory, and boundary recording.

## Short Project Description

Field 01 is a speculative but cautious research program that interprets elementary particles as stable closed phase configurations and black-hole horizons as boundary recording surfaces for phase information. The project distinguishes established physics from interpretation and open hypotheses, and its next task is mathematical formalization rather than making strong claims of replacement.

## What Feedback To Request

Ask external readers for:

- conceptual weak points;
- unclear or nonstandard terminology;
- conflicts with established theory;
- missing references;
- mathematical obstacles;
- possible links to known structures such as solitons, topological defects, QFT in curved spacetime, holography, and black-hole information;
- advice on what must be formalized first.

Avoid asking for endorsement or confirmation that the model is correct.

## Safe Framing

Use phrases such as:

```text
interpretational framework
```

```text
working hypothesis
```

```text
phase-topological language
```

```text
requires further mathematical formalization
```

```text
I am seeking critical feedback rather than endorsement.
```

Avoid phrases such as:

```text
new theory of everything
```

```text
proof that existing physics is wrong
```

```text
Hawking was wrong
```

```text
the Standard Model is replaced
```

## Current Next Research Tasks

The next internal tasks are:

1. build a minimal mathematical formalization of phase, circulation, normal degree of freedom, and memory;
2. define a candidate energy functional or action;
3. formalize the bulk-to-boundary map `M_bulk -> M_boundary`;
4. compare the horizon interpretation with Hawking radiation and reduced density matrices;
5. clarify links and differences with solitons, topological charges, gauge theory, and holography.

## Build Notes

The English papers can be compiled with:

```text
latexmk -pdf articles/particle_as_closed_wave_en.tex
latexmk -pdf articles/horizon_as_phase_recording_surface_en.tex
```

For clean temporary builds, use an external output directory, for example:

```text
mkdir -p /tmp/prism-latex-build
latexmk -pdf -outdir=/tmp/prism-latex-build articles/particle_as_closed_wave_en.tex
latexmk -pdf -outdir=/tmp/prism-latex-build articles/horizon_as_phase_recording_surface_en.tex
```