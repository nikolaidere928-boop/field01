# Field 01 Project Roadmap

This document summarizes the current development plan for Field 01 in English. It is intended for external readers who need a compact orientation before reading the working papers.

## 1. Project Status

Field 01 is an independent research program and public working archive. The current aim is to define a standard mathematical baseline, separate it from Field 01 interpretation, and list the open problems clearly. The particle paper is currently the most developed paper and should be read as the central working node of the archive.

The current working formulation is:

```text
Field 01 proposes an interpretational and phase-topological language in which selected particle-like and boundary-like ideas are described using phase circulation, radial scalar profiles, equivalence classes, and boundary maps.
```

The project distinguishes four levels:

1. established physics;
2. Field 01 interpretation;
3. new hypotheses;
4. open mathematical and physical problems.

## 2. Main Goal

The immediate goal is to translate the book-level intuitive model into short, cautious working papers and then into a minimal mathematical formalization.

Development path:

```text
book-level idea
-> working drafts
-> standard-first terminology map
-> English working papers
-> mathematical formalization
-> comparison with established physics
```

## 3. Current Working Papers

### Paper 1: Elementary Particle as a Closed Wave

Current English source:

```text
articles/particle_as_closed_wave_en.tex
```

Main thesis:

```text
An elementary particle can be interpreted as a stable closed phase configuration of Field 01, rather than as a point-like object.
```

Key ideas:

- photon as open phase transport;
- massive particle as closed phase circulation;
- radial scalar modulus / order-parameter profile language interpreted through the Field 01 local-depth / normal-retention label;
- mass as energy cost of maintaining a closed configuration;
- memory as retained phase structure;
- horizon as a limiting case where the local scalar / VEV-like profile is suppressed.

Open tasks:

- define the phase variable precisely;
- define whether the scalar / VEV-like profile is only a scalar modulus proxy or requires additional geometric structure;
- construct an energy functional or action;
- compare with QFT particles, solitons, topological defects, spin, and the Higgs mechanism.

### Paper 2: Horizon as a Phase Recording Surface

Current English source:

```text
articles/horizon_as_phase_recording_surface_en.tex
```

Main thesis:

```text
A black-hole horizon can be interpreted as a boundary recording surface where volumetric phase structure is represented as surface information.
```

Key ideas:

- suppression of the radial scalar / VEV-like profile;
- transition from volumetric memory to boundary record;
- relation to the Bekenstein--Hawking area law;
- thermality as a reduced-access description;
- caution regarding Hawking radiation and standard semiclassical results.

Open tasks:

- define the map from bulk memory to boundary memory;
- relate horizon area to distinguishable phase records;
- compare with QFT in curved spacetime;
- clarify relation to holography and the black-hole information problem.

## 4. Fixed-Background Numerical Checkpoint

Release `v0.3-fixed-background` adds a compact audit of six one-coordinate profile families. All six families retain one discrete shape and one fold measure. The largest conservative unresolved one-coordinate headroom is `0.332421%`, below the internal `1%` direct-fold threshold.

This closes the tested separable polynomial profile family as a fixed-background benchmark. It does not establish global functional optimality, full static backreaction, dynamic stability, or a physical prediction.

The public audit package is located at:

```text
numerics/fixed_background_checkpoint_v0_3/
```

## 5. Mathematical Vocabulary To Develop

Already used as working notation:

```text
F_01        field 01
0           fixation, holding, recording
1           direction, motion, circulation
phi         phase
C           phase circulation contour
N           radial scalar modulus / order-parameter profile; Field 01 normal-retention interpretation
M           memory / phase record
```

Core formalization targets:

1. state space of the field;
2. dynamical variables;
3. action or energy functional;
4. topological charge or winding number;
5. stability condition for closed nodes;
6. bulk-to-boundary map;
7. relation to known quantum numbers;
8. possible observable or theoretical differences.

## 6. Current Limit

The repository should be read as a working archive, not as a finished theory. Its useful content is the separation between standard mathematical structures, Field 01 interpretation, and open proof obligations.

## 7. Next Research Steps

1. Preserve the v0.3 retained shape as a frozen fixed-background benchmark.
2. Test a genuinely new profile basis rather than reopen closed coordinates.
3. Build a minimal mathematical model for phase circulation and closed waves.
4. Define the scalar / VEV-like profile and its suppression near a boundary.
5. Propose a candidate energy functional for stable closed configurations.
6. Formalize memory as phase relation or equivalence class.
7. Define a candidate bulk-to-boundary map.
8. Compare with solitons, topological charges, gauge theory, QFT in curved spacetime, and holography.
9. Identify whether any testable or theoretically distinguishable consequences exist.
10. Treat full static backreaction and dynamic-root analysis as separate gated stages.

## 8. Recommended Use

Use this roadmap as broad project context after reading `FIELD01_GITHUB_START_HERE.md` and `README.md`.