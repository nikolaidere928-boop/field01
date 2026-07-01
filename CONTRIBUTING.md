# Contributing to Field 01

Thank you for considering a contribution to Field 01.

Field 01 is an independent formalization project, not a completed physical theory. Contributions are most useful when they help clarify, criticize, compare, reproduce, or weaken claims where needed.

The project does not ask readers to endorse it. The best contribution at this stage is careful criticism.

## Project Status

Field 01 currently explores a toy-level formal vocabulary involving:

- phase variables;
- winding and closed phase nodes;
- scalar normal-retention profiles;
- gauge-like compensation;
- current-like expressions;
- memory as an equivalence class;
- boundary recording and reduced external descriptions.

Much of the current mathematical structure is close to known Abelian-Higgs, vortex, soliton, topological-defect, gauge-theory, and boundary-description frameworks. Pointing out these overlaps is not hostile; it is exactly what the project needs.

## Best Ways to Help

### 1. Technical Criticism

Please point out:

- incorrect equations;
- missing assumptions;
- nonstandard notation;
- unjustified physical claims;
- conflicts with established theory;
- places where a statement should be weakened.

A strong contribution can be as simple as:

```text
This equation is standard Abelian-Higgs notation; cite X and avoid claiming novelty here.
```

or:

```text
This term is misleading because it usually means Y in mathematical physics.
```

### 2. Literature Orientation

The project needs references before it needs agreement.

Helpful suggestions include references on:

- Abelian-Higgs vortices;
- Nielsen-Olesen vortices;
- solitons and topological defects;
- gauge theory in polar variables;
- Noether currents;
- reduced density matrices;
- QFT in curved spacetime;
- black-hole thermodynamics;
- holography and boundary Hilbert spaces;
- mathematical treatments of equivalence classes and moduli spaces.

When suggesting a reference, please add one sentence explaining why it matters.

### 3. Mathematical Formalization

Useful mathematical help includes:

- proposing a cleaner state space;
- defining the equivalence relation for memory more rigorously;
- checking the bulk-to-boundary map language;
- comparing the toy energy functional with standard vortex models;
- clarifying boundary conditions;
- identifying whether the model has finite-energy solutions under stated assumptions.

### 4. Numerical Reproduction

The repository contains toy numerical calculations under `analysis/numerics/`.

Helpful contributions include:

- reproducing the current profiles;
- checking sensitivity to parameters;
- identifying numerical artifacts;
- improving documentation of the scripts;
- comparing unscreened and screened energies;
- suggesting better boundary conditions.

### 5. Scientific Writing

The project also needs help with language.

Useful edits include:

- making claims more cautious;
- replacing nonstandard phrases with standard terminology;
- separating interpretation from established physics;
- improving English style;
- making abstracts shorter and clearer;
- removing overstatement.

## What Not to Contribute Yet

At this stage, please do not contribute:

- claims that Field 01 is a proven new theory;
- claims that established physics is simply wrong;
- unsupported experimental predictions;
- large speculative expansions without formal definitions;
- arXiv strategy as a substitute for technical improvement;
- promotional language.

The project should become more modest, clearer, and more testable before becoming more public.

## Preferred Issue Types

If using GitHub or GitLab, useful issue titles include:

```text
Terminology: "normal retention" may be misleading
```

```text
Reference needed: Abelian-Higgs comparison
```

```text
Equation check: screened radial energy
```

```text
Claim too strong: horizon interpretation section
```

```text
Numerics: reproduce screened profile
```

```text
Writing: make abstract more cautious
```

## Suggested First Tasks

Good first contributions:

1. Read `FIELD01_OVERVIEW_EN.md` and identify the weakest paragraph.
2. Read `articles/field01_formalization_program_en.tex` and mark where it duplicates standard vortex theory.
3. Check whether the phrase “gauge-like compensation” is acceptable or should be replaced.
4. Suggest three references that must be cited before public release.
5. Reproduce one numerical result from `analysis/numerics/`.
6. Rewrite one paragraph to distinguish established physics from Field 01 interpretation.

## How to Phrase Review Notes

The most useful review notes are specific and actionable.

Less useful:

```text
This is wrong.
```

More useful:

```text
This looks wrong because equation X assumes Y, but section Z treats Y as optional. I suggest either adding assumption Y explicitly or weakening the claim.
```

Less useful:

```text
This is already known.
```

More useful:

```text
This part is essentially the Abelian-Higgs model in polar variables. Compare with reference X; the Field 01 text should say that the mathematics is standard and that only the interpretation is new.
```

## Current Reading Order

For a first contribution, please read:

1. `FIELD01_OVERVIEW_EN.md`
2. `README.md`
3. `articles/field01_formalization_program_en.tex`
4. `FIELD01_GLOSSARY.md` if terminology is unclear

For conceptual background, read:

1. `articles/particle_as_closed_wave_en.tex`
2. `articles/horizon_as_phase_recording_surface_en.tex`

## Tone and Scope

Critical comments are welcome. Dismissive or promotional comments are not useful.

The goal is to determine whether Field 01 can become a careful formalization program, and if not, where exactly it fails.

## Author Note

The author is independent and outside an academic institution. For that reason, the project prioritizes:

- cautious claims;
- public versioning;
- reproducible toy calculations;
- explicit comparison with known physics;
- willingness to correct or remove weak claims;
- criticism before endorsement.