# Field 01 Overview

This is a short entry document for readers encountering Field 01 for the first time.

Field 01 separates a standard mathematical comparison layer from a speculative interpretation layer. The purpose of this overview is to state the central idea clearly: what is standard background, what is Field 01 interpretation, and what remains open.

## 1. Basic Idea

Field 01 is an independent research and writing project built around a phase-based interpretation of physical structure.

At the conceptual level, the project uses two primitive modes:

- `0` — fixation, retention, boundary, recording, local depth;
- `1` — direction, motion, circulation, transport, unfolding.

The phrase “Field 01” refers to the proposed unity of these two modes. At the current stage, this is not yet a rigorously defined fundamental physical field. It is an interpretive language that is being compared with mathematical objects such as phase variables, winding numbers, scalar profiles, connection-like fields, currents, equivalence classes, and boundary maps.

The current formalization chain is:

```text
phase
-> closed node
-> radial scalar modulus / order-parameter profile
-> Field 01 interpretation as normal retention
-> gauge-like compensation
-> current-like flow
-> memory class
-> boundary map
-> reduced state
```

## 2. What Is Being Formalized

The central question is whether the conceptual language of Field 01 can be expressed in a controlled mathematical form.

The current toy-level variables are:

- `phi` — a phase variable;
- `N` — in the standard vortex layer, a radial scalar modulus / order-parameter profile; in Field 01 language, an interpretive proxy for normal retention or local depth;
- `A_mu` — a connection-like compensating field;
- `M` — memory, treated as preserved phase-structural data;
- `Q_wind` — a winding number or topological record of closed circulation.

The first mathematical representation of a closed phase node is standard winding:

```text
Q_wind = (1 / 2 pi) integral_C d phi = n,  n in Z.
```

This is not claimed as new mathematics. It is used as a first bridge between the Field 01 vocabulary and known phase/topological models.

## 3. Particles as Closed Phase Configurations

The first conceptual paper interprets an elementary particle as a stable closed phase configuration rather than a point-like object.

In this language:

- a photon is treated as open phase transport;
- a massive particle is treated as closed phase circulation;
- mass is associated, at toy-model level, with the energy cost of retaining a closed phase-scalar structure with a normal-retention interpretation;
- memory is associated with preserved phase structure.

The cautious form of the hypothesis is:

```text
massive particle ~ retained closed phase-scalar configuration with a normal-retention interpretation
```

This is not yet a derivation of physical mass. It is a proposed interpretational route that must be compared with quantum field theory, solitons, topological defects, the Higgs mechanism, spin, charge, and the Standard Model particle spectrum.

## 4. Normal Retention

Field 01 uses the phrase “normal retention” for the local-depth reading assigned to the radial scalar profile layer of a closed configuration.

In the standard Abelian-Higgs / vortex comparison layer, the relevant object is simply the radial scalar modulus or order-parameter magnitude:

```text
N = N(r).
```

The phrase “normal retention” is a Field 01 interpretation of this scalar profile, not a new independent degree of freedom in the standard vortex layer. A closed winding without compensation has long-range energy cost. Introducing `N(r)` gives a way to discuss localization and retention, but by itself it is not enough to define a complete physical particle.

The current interpretation is:

```text
normal retention = local scalar depth needed to maintain a closed phase node
```

This phrase is model-specific and should be treated carefully. It is not standard Abelian-Higgs terminology and is not yet a standard physical observable.

## 5. Gauge-Like Compensation

The formalization introduces a connection-like field `A_mu` and a covariant-looking phase derivative:

```text
D_mu phi = partial_mu phi - A_mu.
```

For radial winding, this corresponds schematically to replacing:

```text
n / r  ->  (n - a(r)) / r.
```

This reduces the long-range mismatch of a bare winding in the toy model. The structure is close to known Abelian-Higgs or vortex models, especially when one writes a complex field in polar form:

```text
Psi = N exp(i phi).
```

This similarity is important. Field 01 should not claim that phase winding, gauge-like compensation, scalar radial profiles or order-parameter profiles are new. The responsible next step is comparison with existing vortex, soliton, topological-defect, and Abelian-Higgs literature.

## 6. Memory as Preserved Structure

Field 01 uses “memory” not as psychological memory, but as preserved phase-structural data.

The current formalization treats memory as an equivalence class:

```text
M_bulk = [phi, N, A_mu]_{~ bulk}.
```

The equivalence relation is intended to identify configurations that preserve selected invariants while quotienting out gauge choice, coordinate representation, and small smooth deformations that do not change the record.

Candidate invariants include:

- winding number;
- flux or connection data;
- current-like flux;
- energy class;
- boundary-accessible phase data.

This is an early mathematical proposal, not a completed construction. It needs criticism from people familiar with geometry, topology, gauge theory, and mathematical physics.

## 7. Horizons as Boundary Recording

The second conceptual paper interprets a black-hole horizon as a boundary recording surface.

The cautious version of the idea is:

```text
bulk phase memory -> boundary phase record
```

The formalization writes this as a bulk-to-boundary map:

```text
Pi_boundary: M_bulk -> M_boundary.
```

In this interpretation, a horizon is not treated as a place where the project has already solved black-hole information. Instead, the horizon is used as a possible limiting regime where local normal depth is suppressed and accessible external description is reduced to boundary data.

This is an interpretational proposal that must be compared with quantum field theory in curved spacetime, black-hole thermodynamics, holography, and the information problem before any stronger statement is possible.

## 8. Relation to Known Physics

The project currently overlaps with several established areas:

- phase fields;
- winding numbers;
- topological defects;
- Abelian-Higgs and vortex-like models;
- gauge theory notation;
- Noether-current-like expressions;
- reduced density matrices;
- black-hole thermodynamic language;
- boundary or holographic descriptions.

This overlap is not a weakness if handled honestly. It is the starting point for making Field 01 testable as an interpretation or rejecting parts that are redundant, misleading, or incorrect.

The immediate scientific task is not to defend novelty, but to answer:

```text
What exactly is standard, what exactly is reinterpretation, and what exactly remains an open hypothesis?
```

## 9. Formalization Scope

At the current stage, the project tries to organize the following toy-level vocabulary:

- closed phase nodes can be represented by winding;
- the Field 01 phrase “normal retention” can be represented, at toy level, by a standard radial scalar modulus or order-parameter profile;
- gauge-like compensation can reduce long-range phase mismatch;
- retained covariant phase flow has a current-like expression in the toy model;
- memory can be represented as an equivalence class of preserved data;
- boundary recording can be represented by a bulk-to-boundary map;
- a reduced external state can be interpreted as limited access to a fuller boundary record.

These are formalization targets, not completed results.

## 10. Current Limit

Field 01 is not presented here as a completed physical theory. The current aim is narrower: define the standard baseline, identify which parts are reinterpretation, and make the open problems explicit.


## 11. Suggested First Reading Path

For a first technical look:

1. `README.md`
2. `PROJECT_ROADMAP_EN.md`
3. `articles/field01_formalization_program_en.tex`

For conceptual background:

1. `articles/particle_as_closed_wave_en.tex`
2. `articles/horizon_as_phase_recording_surface_en.tex`

## 12. Short Description

Field 01 is an independent formalization project exploring whether selected particle-like and boundary-like ideas can be organized through phase circulation, radial scalar profiles, gauge-like compensation, and equivalence classes of preserved data. It is a speculative framework under development and should be compared carefully with established physics.