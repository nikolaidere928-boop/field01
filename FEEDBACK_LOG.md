# Field 01 Feedback Log

This file is used to collect criticism, references, objections, and revision decisions after public sharing.

The goal is not to defend every claim. The goal is to turn feedback into clearer definitions, weaker claims, better references, and more honest formalization.

## How to Use This File

For every useful comment, add one entry under the relevant section.

Recommended workflow:

1. Copy the comment or summarize it fairly.
2. Classify the problem type.
3. Decide whether action is needed.
4. Record what file or section should be changed.
5. Mark the status as `open`, `in progress`, `resolved`, or `rejected with reason`.

Do not delete uncomfortable criticism. If the criticism is valid, use it. If it is not valid, explain why briefly and respectfully.

## Problem Types

Use one or more of these labels:

- `terminology`
- `equation`
- `known-physics-overlap`
- `missing-reference`
- `overclaim`
- `vague-definition`
- `numerical-method`
- `boundary-condition`
- `horizon-interpretation`
- `memory-formalization`
- `writing-clarity`
- `repository-structure`
- `publication-strategy`

## Status Labels

Use these status labels:

- `open` — needs review;
- `in progress` — being addressed;
- `resolved` — change made or answer documented;
- `rejected with reason` — no change, reason recorded;
- `deferred` — important but not for the current release.

## Feedback Table

| Date | Source | Comment / Objection | Type | Response | Action | Status |
|---|---|---|---|---|---|---|
| 2026-06-04 | Example | This looks close to Abelian-Higgs vortices. | known-physics-overlap, missing-reference | Agree; the project must state overlap more explicitly. | Add comparison references and weaken novelty language. | open |

## Detailed Entries

### Entry 001 — Example: Abelian-Higgs Overlap

**Date:** 2026-06-04

**Source:** Example / placeholder

**Comment:**

```text
This looks close to the Abelian-Higgs model or Nielsen-Olesen vortex structure.
```

**Type:** `known-physics-overlap`, `missing-reference`

**Initial Response:**

This is likely correct for the current screened toy model. Field 01 should not claim novelty for winding, scalar polar variables, gauge-like compensation, or vortex-like radial profiles.

**Action Needed:**

- Add or improve references to Abelian-Higgs and vortex literature.
- Make the formalization paper clearer that the mathematical skeleton is close to known structures.
- State that the possible contribution is interpretational, not the invention of these equations.

**Files To Review:**

- `articles/field01_formalization_program_en.tex`
- `FIELD01_OVERVIEW_EN.md`
- `README.md`

**Status:** `open`

## References Suggested by Others

Add references here when someone suggests literature.

| Date | Suggested Reference | Suggested By | Why It Matters | Added To Text? |
|---|---|---|---|---|
| 2026-06-04 | Example reference on vortices | Example | Needed for Abelian-Higgs comparison | no |

## Terms to Reconsider

Use this section for words that may be misleading or nonstandard.

| Term | Concern | Possible Replacement | Status |
|---|---|---|---|
| normal retention | Nonstandard; may sound metaphysical without definition. | scalar retention profile, radial scalar profile, local depth proxy | open |
| gauge-like compensation | May be too informal or imprecise. | connection field, compensating connection, screened phase derivative | open |
| memory | Could be confused with psychological memory or information storage claims. | preserved phase-structural data, equivalence class of field data | open |

## Claims to Weaken

Use this section when a statement sounds too strong.

| File | Claim | Why Too Strong | Safer Version | Status |
|---|---|---|---|---|
| `FIELD01_OVERVIEW_EN.md` | Example: Field 01 describes particles. | Sounds like a completed theory. | Field 01 explores whether particle-like configurations can be represented in a toy phase language. | open |

## Questions to Ask Next

Use this section to turn confusion into better public questions.

- What is the closest standard reference for the screened radial energy used in the toy model?
- Is “memory as equivalence class” better described through moduli spaces, gauge equivalence, homotopy classes, or conserved charges?
- Which boundary conditions make the finite-disk numerical profiles mathematically meaningful?
- Which claims in the horizon interpretation are most likely to conflict with standard QFT in curved spacetime?

## Revision Decisions

Record decisions made after feedback.

| Date | Decision | Reason | Files Changed | Release |
|---|---|---|---|---|
| 2026-06-04 | Example: avoid novelty claims for vortex-like equations. | Feedback indicates strong overlap with known Abelian-Higgs structures. | pending | v0.2-feedback |

## Release Notes from Feedback

Use this section when preparing a new release such as `v0.2-feedback`.

### v0.2-feedback Draft Notes

- Clarified overlap with Abelian-Higgs/vortex-like structures.
- Weakened language around novelty.
- Added references suggested by readers.
- Improved definition of memory as an equivalence class.
- Clarified that numerical profiles are toy checks, not evidence for a physical theory.