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
| 2026-06-23 | Reddit r/AskPhysics | In Abelian-Higgs strings/vortices, it is common to say the Higgs/scalar field forms a condensate with nonzero VEV away from the core, and that this condensate/VEV-profile vanishes in the soliton core; avoid confusing this background condensate with massive Higgs perturbations. | terminology, known-physics-overlap, writing-clarity | Agree; describe `N(r)` in the standard layer as scalar modulus / order-parameter magnitude / VEV-profile, and keep `normal retention` only as Field 01 interpretation. | First feedback-pass applied to standard layer, interpretation layer, overview, glossary, two-layer plan, and cheatsheet. | resolved |
| 2026-06-26 | Reddit batch from `reddit.docx` | Six collected posts suggest the best current strategy: standard Abelian-Higgs/vortex vocabulary first; explicit gauge-profile convention, boundary conditions, near-core asymptotics, and BPS normalization caveats; Field 01 terms only as interpretation. | terminology, known-physics-overlap, boundary-condition, equation, publication-strategy | Agree; this becomes the next feedback-pass checklist. | First feedback-pass applied; keep summary as checklist for future public-release pass. | resolved |

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


### Entry 003 — Reddit: Scalar Modulus / VEV Profile Terminology

**Date:** 2026-06-23

**Source:** Reddit `r/AskPhysics`, author-archived screenshot/private local note.

**Comment Summary:**

```text
For Abelian-Higgs strings/vortices, it is common to say that the scalar/Higgs field forms a condensate where the VEV is nonzero, and that this condensate vanishes in the core of the soliton. However, this can be ambiguous because the background condensate is not the same as the massive Higgs-field perturbations. A safer phrasing is to talk about the scalar VEV/order-parameter profile changing from its value at infinity to zero in the string/vortex core.
```

**Type:** `terminology`, `known-physics-overlap`, `writing-clarity`

**Initial Response:**

This is useful and consistent with the current two-layer discipline. In the standard vortex layer, `N(r)` should be described as the scalar modulus, order-parameter magnitude, or VEV/background profile. The Field 01 phrase `normal retention` should remain explicitly interpretive and must not be presented as an additional independent physical degree of freedom.

**Action Needed:**

- Update standard terminology around `N(r)` after waiting for possible additional Reddit comments.
- Prefer `scalar modulus / order-parameter magnitude / VEV-profile` in standard sections.
- Use `normal retention` only in labelled Field 01 interpretation sections.
- Add a caution that `condensate` can be ambiguous if it is confused with massive Higgs perturbations.

**Files To Review:**

- `analysis/field01_standard_core_v1.md`
- `analysis/field01_interpretation_layer_v1.md`
- `analysis/model01_cheatsheet_v1.md`
- `analysis/field01_two_layer_formalization_plan.md`
- `FIELD01_OVERVIEW_EN.md`
- `FIELD01_GLOSSARY.md`

**Status:** `resolved`

### Entry 004 — Reddit Batch: Standard Vortex Layer Checklist

**Date:** 2026-06-26

**Source:** User-collected Reddit archive, summarized in local working notes before this public feedback log entry.

**Comment Summary:**

```text
The collected posts point to one consistent revision strategy: write the standard layer in ordinary Abelian-Higgs / Nielsen-Olesen / Abrikosov-Ginzburg-Landau vortex vocabulary; define the gauge-profile convention explicitly; state boundary and near-core conditions; treat BPS normalization as convention-dependent; keep Field 01 terms such as normal retention only as labelled interpretation.
```

**Type:** `terminology`, `known-physics-overlap`, `boundary-condition`, `equation`, `publication-strategy`

**Initial Response:**

Agree. This is not endorsement of the broader Field 01 interpretation, but it is valuable technical feedback for making the project clearer, less overclaimed, and easier to compare with known vortex literature.

**Action Needed:**

- Use `analysis/reddit_feedback_summary_2026-06-26.md` as the next edit checklist.
- Update `N(r)` terminology: scalar modulus / VEV-profile / order-parameter profile first; `normal retention` second and labelled.
- Keep `A=a(r)d\theta` versus `\mathcal A=(a(r)/g)d\theta` explicit.
- Keep finite-energy boundary conditions and near-core behavior visible.
- Keep `\lambda=g^2/2` and `E_{BPS}=\pi N_0^2|n|` explicitly tied to the stated ordinary Abelian-Higgs normalization.
- Do not extend the BPS statement to Chern-Simons, dielectric, or otherwise modified gauge sectors without a new analysis.

**Files To Review:**

- `analysis/field01_standard_core_v1.md`
- `analysis/field01_interpretation_layer_v1.md`
- `analysis/model01_cheatsheet_v1.md`
- `analysis/field01_two_layer_formalization_plan.md`
- `FIELD01_GLOSSARY.md`
- `FIELD01_OVERVIEW_EN.md`

**Status:** `resolved`

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
| `N(r)` | Should not be introduced as a new independent physical degree of freedom in the standard vortex layer. | scalar modulus, order-parameter magnitude, VEV-profile, background scalar profile | open |
| condensate | Can be ambiguous: background/VEV condensate is not the same as massive Higgs perturbations. | scalar VEV-profile, background order-parameter profile | open |
| BPS normalization | `E_BPS` differs by factors of 2 across references depending on scalar kinetic normalization, vacuum parameter, and coupling placement. | State the full convention before comparing `E_BPS`; say “in this normalization.” | open |
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
| 2026-06-23 | Use standard terminology for `N(r)` before Field 01 interpretation. | Reddit feedback indicates that `N(r)` is normally discussed as scalar modulus / VEV or order-parameter profile in vortex/string language. | `analysis/field01_standard_core_v1.md`, `analysis/field01_interpretation_layer_v1.md`, `analysis/field01_two_layer_formalization_plan.md`, `analysis/model01_cheatsheet_v1.md`, `README.md`, `FIELD01_GITHUB_START_HERE.md`, `FIELD01_OVERVIEW_EN.md`, `FIELD01_GLOSSARY.md`, `FIELD01_REFERENCE_MAP.md`, `ABSTRACTS_EN.md`, `FIRST_PUBLIC_POSTS.md`, `OUTREACH_PACKAGE_EN.md`, public-release/outreach copies | v0.2-feedback |
| 2026-06-26 | Treat the Reddit batch as a feedback-pass checklist, not as validation of the theory. | The useful output is convention/terminology discipline: standard vortex layer first, interpretation second. | `analysis/reddit_feedback_summary_2026-06-26.md` plus files above | v0.2-feedback |

## Release Notes from Feedback

Use this section when preparing a new release such as `v0.2-feedback`.

### v0.2-feedback Draft Notes

Detailed draft:

```text
RELEASE_NOTES_v0.2_FEEDBACK.md
```

Main changes applied in the first Reddit feedback pass:

- Standard layer now names `N(r)` first as `scalar modulus / VEV-profile / order-parameter profile`.
- `FIELD01_REFERENCE_MAP.md` now uses scalar modulus / VEV / order-parameter wording before `normal retention`.
- `ABSTRACTS_EN.md`, `FIRST_PUBLIC_POSTS.md`, and `OUTREACH_PACKAGE_EN.md` now use standard-first scalar-profile wording.
- `normal retention` is kept only as a labelled Field 01 interpretation, not a new standard degree of freedom.
- The condensate wording now distinguishes background/VEV-profile from massive Higgs perturbations.
- The gauge-profile convention `A=a(r)d\theta` versus `\mathcal A=(a(r)/g)d\theta` is stated more explicitly.
- Boundary conditions, near-core behavior, and BPS normalization caveats are kept visible.
- The release note explicitly says this is a terminology/convention pass, not validation of the theory.

## Russian Quick Guide — How To Record Reddit Feedback

Этот раздел объясняет, как практически вести журнал замечаний после Reddit, GitHub или личных сообщений.

### 1. Не записывай всё подряд

Записывай только полезное:

- человек дал ссылку;
- указал на ошибку;
- сказал, что термин звучит плохо;
- сказал, что это похоже на известную модель;
- указал, что утверждение слишком сильное;
- задал вопрос, на который у тебя нет хорошего ответа.

Не нужно записывать:

- оскорбления;
- пустое “this is wrong” без объяснения;
- споры ради споров;
- комментарии, где человек явно не читал текст.

### 2. Минимальная запись

Если мало времени, записывай в таблицу `Feedback Table` в таком виде:

```text
Date | Source | Comment / Objection | Type | Response | Action | Status
```

Пример:

```text
2026-06-04 | Reddit r/PhysicsStudents | The phrase “normal retention” sounds nonstandard. | terminology | Agree; needs clearer definition. | Consider replacing with “scalar retention profile” in overview. | open
```

### 3. Как выбирать Type

Используй один или несколько типов:

```text
terminology
```
если проблема в слове или названии.

```text
known-physics-overlap
```
если говорят “это уже Abelian-Higgs / vortex / soliton / gauge theory”.

```text
missing-reference
```
если дали статью, книгу, автора или стандартную модель для сравнения.

```text
overclaim
```
если говорят, что ты слишком сильно заявляешь.

```text
vague-definition
```
если говорят, что понятие не определено.

```text
equation
```
если замечание касается формулы.

```text
writing-clarity
```
если текст непонятен или звучит плохо.

### 4. Как выбирать Status

Используй:

```text
open
```
замечание принято, но ещё не исправлено.

```text
in progress
```
ты уже правишь файл.

```text
resolved
```
исправлено.

```text
deferred
```
важно, но не сейчас.

```text
rejected with reason
```
ты решил не менять, но записал почему.

### 5. Что писать в Response

Response — это не ответ человеку на Reddit, а твоя внутренняя реакция.

Примеры:

```text
Agree. This term is unclear for external readers.
```

```text
Probably correct. Need to compare with Abelian-Higgs literature.
```

```text
Unclear. Need another opinion before changing the paper.
```

```text
Disagree for now, but the wording should still be softened.
```

### 6. Что писать в Action

Action — это конкретное действие.

Плохо:

```text
Think about it.
```

Хорошо:

```text
Add a paragraph to FIELD01_OVERVIEW_EN.md explaining that N is only a scalar proxy.
```

Хорошо:

```text
Add reference request to the next Reddit post about Abelian-Higgs vortices.
```

Хорошо:

```text
Replace “memory” with “preserved phase-structural data” in first-contact material.
```

### 7. Как отвечать людям

Если замечание полезное, отвечай коротко:

```text
Thank you, this is useful. I will record this as a terminology issue and revise the overview.
```

Если дали ссылку:

```text
Thank you. I will add this to my comparison list and check whether the current toy model is just a standard version of that structure.
```

Если сказали, что всё слишком vague:

```text
That is fair. Could you point to the first definition that becomes too vague to be useful?
```

### 8. Что делать после 5–10 замечаний

Когда накопится несколько полезных замечаний:

1. Открой этот файл.
2. Посмотри, какие типы повторяются чаще всего.
3. Если много `terminology` — правь `FIELD01_OVERVIEW_EN.md`.
4. Если много `known-physics-overlap` — усиливай сравнение с Abelian-Higgs/vortex literature.
5. Если много `overclaim` — ослабляй формулировки в `README.md` и overview.
6. Если много `vague-definition` — выбери один термин и формализуй его первым.

### 9. Главный принцип

Не защищай каждое предложение.

Используй критику как материал для следующей версии:

```text
v0.2-feedback
```

Цель не в том, чтобы выиграть спор на Reddit. Цель — сделать проект более ясным, осторожным и проверяемым.
### Entry 002 — Reddit: Mimic Style and Vocabulary of Relevant Papers

**Date:** 2026-06-05

**Source:** Reddit / r/PhysicsStudents

**Comment:**

```text
The idea is that you take the papers you read and that you are using as inspiration for this research, and roughly write in the same way as those papers. You will want to mimic their style and their choice of vocabulary. Don't forget to cite the relevant papers, even if you disagree with them. You can and must of course explain why your work is different/better/improving on the previous papers.
```

**Type:** `writing-clarity`, `missing-reference`, `known-physics-overlap`, `publication-strategy`

**Initial Response:**

Agree. The project should adopt the style, vocabulary, and citation habits of the closest relevant literature instead of relying on isolated original terminology. This is especially important for Abelian-Higgs, vortex, soliton, gauge-field, topological-defect, and boundary/holography comparisons.

**Action Needed:**

- Identify 5--10 closest reference papers or textbook sections.
- Extract their standard vocabulary for phase fields, winding, scalar profiles, gauge fields, vortices, and boundary states.
- Revise `FIELD01_OVERVIEW_EN.md` and `articles/field01_formalization_program_en.tex` to use more standard terms first, with Field 01 terms introduced only as interpretation.
- Add citations or at least a reference list before the next public technical post.
- Add a comparison section explaining what is standard, what is interpretation, and what remains an open hypothesis.

**Files To Review:**

- `FIELD01_OVERVIEW_EN.md`
- `articles/field01_formalization_program_en.tex`
- `README.md`
- `FIELD01_GLOSSARY.md`

**Status:** `open`