# Field 01 Reference Map

This file maps the current Field 01 vocabulary to standard physics and mathematics vocabulary. It is intended as a working guide for revising the public papers after early external feedback.

The rule is:

```text
standard term -> standard reference -> Field 01 interpretation -> open hypothesis
```

Field 01 should not introduce its own terminology before naming the nearest standard structure.

## 1. Core Writing Rule

For every important concept, write in this order:

1. name the standard mathematical/physical object;
2. cite or list the closest standard reference;
3. explain how Field 01 reinterprets the object;
4. explicitly state what remains speculative.

Example:

```text
In standard Abelian-Higgs/Nielsen-Olesen vortex models, a complex scalar field has a phase winding and a radial scalar profile, with a gauge field screening the long-range phase gradient. Field 01 uses this same toy-level structure as a controlled language for closed phase nodes, normal retention, and phase memory. The mathematical ingredients are standard; the interpretation is Field 01-specific and remains hypothetical.
```

## 2. Reference Map Table

| Field 01 term | Standard vocabulary first | Closest references | What is standard | Field 01 interpretation | Writing instruction |
|---|---|---|---|---|---|
| `phase`, `rhythm` | phase field; angular variable; phase of a complex scalar/order parameter | Feynman Lectures; Landau-Lifshitz Quantum Mechanics; Nielsen-Olesen vortex; Manton-Sutcliffe Topological Solitons | Phase variables and phase gradients are standard. | Phase is read as rhythm or mode-1 circulation. | Use `phase variable` first; introduce `rhythm` as interpretation only. |
| `closed phase node` | vortex; topological defect; closed phase winding; topological charge | Nielsen and Olesen, 1973; Manton and Sutcliffe, 2004; Vilenkin and Shellard, 1994 | Integer winding and topological charge are standard. | A closed node is read as a retained phase-memory configuration. | Say “represented by winding” rather than “is proven to be a particle.” |
| `normal retention` | scalar amplitude; radial scalar profile; order-parameter modulus; Higgs/amplitude profile | Nielsen-Olesen vortex; Abelian-Higgs model; Ginzburg-Landau/Abrikosov vortex literature | Scalar radial profiles in vortices are standard. | `N(r)` is interpreted as local depth or retained normal component. | Use `scalar profile N(r)` first; define `normal retention` as model language. |
| `gauge-like compensation` | U(1) gauge field; connection; covariant derivative; screening of phase gradient | Nielsen-Olesen, 1973; Ginzburg-Landau superconductivity; Abelian-Higgs model | Gauge fields and covariant derivatives are standard. | The compensating field is read as field response to retained phase mismatch. | Prefer `connection-like field` or `compensating gauge field`; avoid implying electromagnetism is derived. |
| `current-like flow` | Noether current; gauge current; conserved phase current | Noether theorem; field theory textbooks; Abelian-Higgs current | Conservation from phase symmetry is standard. | Retained covariant phase flow is interpreted as memory-carrying circulation. | Say `current-like object inside the toy model`; do not call it electric current. |
| `memory` | preserved field data; equivalence class; gauge-equivalence class; invariant data | Gauge theory; topology; moduli spaces; quantum information references | Quotienting by gauge/coordinate choices is standard. | Memory is read as preserved phase-normal-gauge structure. | Define invariants first; avoid psychological meaning of memory. |
| `bulk memory` | bulk field configuration modulo equivalence | Gauge theory; topological defects; holography literature | Bulk fields and equivalence classes are standard tools. | Field 01 treats local structure as memory class. | Use schematic notation only until Hilbert/state space is defined. |
| `boundary recording` | boundary data; holographic boundary; surface degrees of freedom | Bekenstein; Hawking; 't Hooft; Susskind; Maldacena | Boundary/horizon information language is standard. | Boundary record is interpreted as preserved phase memory at a limiting surface. | Do not claim solution to black-hole information problem. |
| `reduced external state` | reduced density matrix; partial trace; inaccessible degrees of freedom | Nielsen-Chuang; Preskill; Almheiri et al.; Page | Reduced states and thermality from tracing are standard. | External thermality is interpreted as limited access to boundary record. | Say `may be interpreted`; do not say Hawking radiation is false. |
| `horizon as phase recording surface` | black-hole horizon; entropy area law; holographic screen; boundary degrees of freedom | Bekenstein 1973; Hawking 1975; 't Hooft 1993; Susskind 1995; Maldacena 1997 | Horizon thermodynamics and holography are established frameworks. | Horizon is read as a limiting phase-recording boundary. | Present as interpretation requiring comparison, not derivation. |

## 3. Exact References Already Present in Source Materials

These references were extracted from the book/preprint source materials and can be used immediately as anchors.

### General Physics and Quantum Information

- R. Feynman, R. Leighton, M. Sands, *The Feynman Lectures on Physics*, Vol. I--III.
- L. Landau, E. Lifshitz, *Course of Theoretical Physics*, Vol. 3: *Quantum Mechanics*.
- M. Nielsen, I. Chuang, *Quantum Computation and Quantum Information*.
- J. Preskill, *Quantum Information and Quantum Computing* lecture notes.
- R. Penrose, *The Road to Reality*.

### QFT in Curved Spacetime and Horizons

- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space*, Cambridge University Press, 1982.
- R. M. Wald, *Quantum Field Theory in Curved Spacetime*, University of Chicago Press, 1994.
- S. W. Hawking, “Particle Creation by Black Holes,” *Communications in Mathematical Physics* 43, 199 (1975).
- W. G. Unruh, “Notes on Black-Hole Evaporation,” *Physical Review D* 14, 870 (1976).
- J. D. Bekenstein, “Black holes and entropy,” *Physical Review D* 7, 2333 (1973).
- D. N. Page, “Information in black hole radiation,” *Physical Review Letters* 71, 3743 (1993).
- A. Almheiri et al., “The entropy of Hawking radiation,” *Reviews of Modern Physics* 93, 035002 (2021).
- A. Almheiri, D. Marolf, J. Polchinski, J. Sully, “Black holes: complementarity or firewalls?,” *JHEP* 2013, 062 (2013).

### Holography and Entanglement Geometry

- G. 't Hooft, “Dimensional Reduction in Quantum Gravity,” arXiv:gr-qc/9310026 (1993).
- L. Susskind, “The World as a Hologram,” *Journal of Mathematical Physics* 36, 6377 (1995).
- J. Maldacena, “The Large N Limit of Superconformal Field Theories and Supergravity,” *International Journal of Theoretical Physics* 38, 1113 (1999).
- J. Maldacena and L. Susskind, “Cool horizons for entangled black holes,” *Fortschritte der Physik* 61, 781 (2013).
- M. Van Raamsdonk, “Building up spacetime with quantum entanglement,” *General Relativity and Gravitation* 42, 2323 (2010).
- B. Swingle, “Entanglement renormalization and holography,” *Physical Review D* 86, 065007 (2012).

### Cosmology / Black-Hole Astrophysics Already Present

- M. Begelman, M. Volonteri, M. Rees, “Massive black hole seeds from direct collapse,” *Monthly Notices of the Royal Astronomical Society* 370, 289 (2006).
- R. Larson et al., “A JWST search for early black holes at z > 5,” *Astrophysical Journal* 953, L29 (2023).
- ALICE Collaboration, “Elliptic flow of charged particles in Pb-Pb collisions,” *Physical Review Letters* 105, 252302 (2010).

## 4. Missing References To Add Before a Technical Post

These are the most important missing references for the formalization paper because the toy model currently resembles vortex/Abelian-Higgs mathematics.

| Priority | Reference | Why It Matters |
|---|---|---|
| 1 | H. B. Nielsen and P. Olesen, “Vortex-line models for dual strings,” *Nuclear Physics B* 61, 45--61 (1973). | Closest classic source for scalar field + phase winding + gauge field vortex structure. |
| 2 | A. A. Abrikosov, “On the magnetic properties of superconductors of the second group,” *Soviet Physics JETP* 5, 1174--1182 (1957). | Classic source for vortex lattice / type-II superconductivity analogy. |
| 3 | N. Manton and P. Sutcliffe, *Topological Solitons*, Cambridge University Press, 2004. | Standard vocabulary for solitons, vortices, topology, charges, moduli. |
| 4 | A. Vilenkin and E. P. S. Shellard, *Cosmic Strings and Other Topological Defects*, Cambridge University Press, 1994. | Standard reference for topological defects and cosmological context. |
| 5 | Standard Abelian-Higgs model review or textbook section. | Needed to align notation for `Psi = N exp(i phi)`, covariant derivative, and current. |
| 6 | Standard Ginzburg-Landau superconductivity reference. | Needed for screening, scalar order parameter, and vortex analogy. |

## 5. How To Rewrite the Formalization Paper

The current paper should be revised with a “standard-first” style.

### Current Style

```text
Field 01 interprets a massive local node as more than a phase winding. It also requires normal retention, represented by N(r).
```

### Better Academic Style

```text
In vortex and Abelian-Higgs-type models, a complex scalar field can be written in polar form, with a phase variable and a radial amplitude/profile. A configuration with nonzero winding requires a scalar profile that regularizes the core and, in the gauged case, a connection field that screens the long-range phase gradient. Field 01 uses this standard mathematical structure as a toy representation of a closed phase node. The model-specific interpretation is to call the scalar profile a proxy for normal retention or local depth.
```

## 6. What Is Same / Different

### Same as Standard Models

- phase variable;
- winding number;
- scalar radial profile;
- gauge/connection field;
- covariant derivative;
- field strength;
- current-like expression from phase symmetry;
- finite-energy or screened vortex logic;
- reduced density matrix language;
- boundary/holographic vocabulary.

### Field 01-Specific Interpretation

- phase as rhythm;
- `N` as normal retention / local depth;
- winding as phase memory;
- gauge-like compensation as field response;
- memory as preserved phase-normal-gauge data;
- horizon as boundary phase recording;
- thermality as reduced access to boundary record.

### Still Open / Not Claimed

- final fundamental action;
- derivation of Standard Model particles;
- spin and charge derivation;
- physical mass spectrum;
- black-hole entropy derivation;
- Hawking radiation derivation or replacement;
- testable prediction.

## 7. Revision Status After v0.2

Completed in `articles/field01_formalization_program_en.tex` v0.2:

1. Added a `Standard-First Vocabulary Rule` section.
2. Added immediate reference anchors for Abelian-Higgs/vortex, soliton, topological-defect, and horizon-information comparisons.
3. Rewrote the normal-retention section to introduce the standard scalar profile first.
4. Rewrote the gauge-like section as connection-like compensation before the Field 01 interpretation.
5. Added explicit caution that the Abelian-Higgs/vortex structure is not a new invention.

Still open before a technical post:

1. Replace inline reference anchors with a formal bibliography or BibTeX file.
2. Ask a domain expert or a focused physics forum for the best textbook review on Abelian-Higgs vortices before posting the technical paper.
3. Add exact page/section pointers for the standard references after checking the sources directly.

## 8. Short Answer to Early External Feedback

A good response to this advice is:

```text
Thank you, this is exactly the direction I need. I have now started building a reference map that links my terms to standard vocabulary: phase winding, scalar amplitude/profile, Abelian-Higgs/Nielsen-Olesen vortices, topological defects, Noether currents, reduced density matrices, and holographic boundary language. The next revision will introduce standard terms and citations first, and only then explain the Field 01 interpretation.
```