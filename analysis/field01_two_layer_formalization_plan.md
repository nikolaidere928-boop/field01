# Field 01 Two-Layer Formalization Plan

Purpose: separate the standard vortex mathematics checked against external feedback and Schaposnik's notes from the Field 01 interpretive layer that still requires independent definitions, hypotheses, and tests.

Status: internal planning note. Not a book insert, not a paper draft, and not a public claim of novelty.

Date: 2026-06-14.

## 1. Guiding Rule

Every statement must belong to exactly one of these classes:

- **Definition:** a chosen mathematical object, convention, boundary condition, or map.
- **Standard result:** a known Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau vortex fact, with convention mapping.
- **Interpretation:** Field 01 language attached to the standard construction.
- **Hypothesis:** a new claim that would require proof, simulation, or comparison with known physics.
- **Open problem:** a missing definition, derivation, or validation step.

No interpretive phrase should be allowed to look like a standard physics result.

## 2. Layer A: Standard Technical Core

### 2.1 Standard Vocabulary

Use these terms as the public-safe technical vocabulary:

- complex scalar;
- scalar modulus / radial profile;
- compact phase;
- winding number;
- `U(1)` gauge field;
- covariant derivative;
- angular covariant derivative;
- finite-energy vortex boundary conditions;
- magnetic flux;
- Abelian-Higgs vortex;
- Nielsen-Olesen vortex;
- Abrikosov / Ginzburg-Landau vortex;
- BPS / Bogomolny critical coupling, only after conventions are stated.

Avoid using these terms as primary technical vocabulary:

- angular screening;
- memory;
- normal retention;
- closed wave as particle;
- horizon;
- charge-like meaning;
- new physical model.

Internal shorthand such as `screened angular gradient` is allowed only after defining it through the covariant derivative.

### 2.2 Core Ansatz

Definition:

```math
\Psi(r,\theta)=N(r)e^{in\theta},
\qquad
A_r=0,
\qquad
A_\theta=a(r).
```

Definition:

```math
D_i=\partial_i-iA_i.
```

For the angular part, in the current convention:

```math
D_\theta\Psi
\propto i[n-a(r)]N(r)e^{in\theta}.
```

Finite-energy vortex behavior:

```math
N(0)=0,
\qquad
a(0)=0,
\qquad
N(\infty)=N_0,
\qquad
a(\infty)=n.
```

Therefore:

```math
D_\theta\Psi\to0
\quad(r\to\infty),
```

which should be described as asymptotic cancellation of the angular covariant derivative.

### 2.3 Energy Functional

Definition / current convention:

```math
E=\int d^2x\left[
\frac12|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right].
```

Radial form:

```math
E=2\pi\int_0^R dr\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right].
```

Definition:

```math
B=\frac{a'}{r},
\qquad
\Phi_B=2\pi n.
```

Physics-threshold rule:

Before this or another action/energy is stated, the construction is only a radial ansatz. After it is stated, it may be called a toy field-theory-like model, but not a new physical theory.

### 2.4 Checked Standard Mapping

Standard result / convention map:

Schaposnik uses a scalar kinetic term with explicit `1/2`, a covariant derivative with coupling inside `D_mu`, and potential coefficient `lambda_S`:

```math
E_S=\int d^2x\left[
\frac14F_{ij}^2
+\frac12|D_i\phi|^2
+\lambda_S(|\phi|^2-\phi_0^2)^2
\right].
```

The useful map is:

```math
N_0\leftrightarrow\phi_0,
\qquad
n\leftrightarrow N,
\qquad
g\leftrightarrow e,
\qquad
\lambda_{ours}=4\lambda_S.
```

Schaposnik's critical point:

```math
e^2=8\lambda_S
```

maps to:

```math
\lambda_{ours}=\frac{g^2}{2},
\qquad
\beta=\frac{2\lambda_{ours}}{g^2}=1.
```

Schaposnik's BPS bound:

```math
E_S\ge\pi\phi_0^2|N|
```

maps to:

```math
E_{ours,\mathrm{BPS}}=\pi N_0^2|n|.
```

Therefore, `E=pi` for `N0=1`, `n=1` is convention-consistent in the present explicit `1/2 |D_i Psi|^2` normalization. It must not be compared directly with `2 pi v^2 n` conventions without a scalar-normalization map.

## 3. Layer B: Field 01 Interpretive Layer

The following terms are not standard vortex results. They may be used only with labels.

| Field 01 term | Allowed label | Technical object it may refer to | Required caution |
|---|---|---|---|
| normal retention | Interpretation / Hypothesis | scalar modulus `N(r)` | not a standard scalar-field meaning |
| phase-structural memory | Interpretation / Hypothesis | winding, boundary data, gauge-equivalence class | requires precise state space |
| memory preservation | Hypothesis | conserved winding or boundary equivalence class | not proven by vortex math alone |
| horizon-like suppression | Interpretation / Open problem | boundary condition or limit where `N` is suppressed | not a black-hole claim |
| charge-like compensation | Interpretation / Open problem | gauge profile / Noether current / flux | not electric charge unless defined |
| particle-like object | Avoid / Hypothesis | finite-energy vortex solution | requires dynamics and observables |
| reduced memory state | Definition / Hypothesis | reduced density matrix or boundary map | requires Hilbert/state-space definition |

Rule:

Layer B may use Layer A as a mathematical substrate, but Layer A does not imply Layer B.

## 4. Dependency Chain

Safe chain:

```text
phase winding
-> scalar modulus
-> U(1) covariant derivative
-> radial vortex ansatz
-> finite-energy boundary conditions
-> flux / BPS convention
-> equivalence-class language
-> possible memory interpretation
```

Forbidden shortcut:

```text
vortex ansatz
-> memory is physically real
```

The interpretation begins only after an explicit definition of a memory state, equivalence relation, and map between bulk data and boundary data.

## 5. Proof Obligations Before Public Claims

### 5.1 Mathematical Obligations

Open problems:

1. Define the exact action or energy functional for every variant before discussing physics.
2. Specify field dimensions, coupling dimensions, and normalization conventions.
3. Specify the configuration space and admissible boundary conditions.
4. Define the gauge-equivalence relation precisely.
5. Derive Euler-Lagrange equations from the chosen energy/action.
6. Check existence, numerical stability, or at least consistency of the proposed solutions.
7. Identify which statements remain after subtracting standard vortex content.

### 5.2 Interpretive Obligations

Open problems:

1. Define `memory` as a mathematical object, not a metaphor.
2. Define the bulk-to-boundary memory map.
3. Explain whether memory is topological, metric, gauge-invariant, or state-dependent.
4. Clarify whether `normal retention` is a scalar amplitude, an order parameter, or only a Field 01 label.
5. Specify what would count as failure of the interpretation.
6. Avoid any black-hole, particle, or cosmological claim until the toy model is embedded in a relevant physical setting.

## 6. Public-Safe Abstract

```text
This project currently isolates a standard mathematical core: a two-dimensional radial vortex ansatz with phase winding, a scalar modulus, and a U(1) covariant derivative whose angular component vanishes asymptotically. The closest standard comparisons are Abelian-Higgs / Nielsen-Olesen vortices and Abrikosov / Ginzburg-Landau vortices. In the present normalization, Schaposnik's convention maps to lambda=g^2/2 and E_BPS=pi N0^2 |n|. Any Field 01 language about memory, normal retention, or horizon-like behavior is interpretive and must be defined separately. No new physical model is claimed at this stage.
```

## 7. Immediate Editing Plan

1. Keep `field01_math_core_v0.md` as the stripped standard-math core.
2. Use `field01_schaposnik_vortices_convention_map.md` as the citation/convention checkpoint.
3. Use this file as the separation checklist before editing `field01_formalization_roadmap.md`.
4. Update public-facing summaries only after every sentence is tagged as standard math, interpretation, hypothesis, or open problem.
5. Do not push a public GitHub update until the standard layer and interpretation layer are visibly separated in the repository.

## 8. Next Internal Deliverable

Recommended next file:

```text
analysis/field01_standard_core_v1.md
```

Purpose:

- contain only Layer A;
- remove all Field 01 interpretation;
- state the ansatz, energy, boundary conditions, flux, BPS normalization, and convention map;
- provide a clean base that can later be cited by interpretive notes.