# Analysis Notes

This directory contains internal analysis and mathematical formalization notes for Field 01. These files are working documents, not book inserts and not final papers.

Current files:

- `field01_formalization_notes.md` — first mathematical skeleton of the model: phase, circulation, normal degree of freedom, mass, memory, horizon limit, and open problems.
- `field01_toy_phase_normal_model.md` — first toy mathematical model: phase winding, normal-retention profile, energy functional, radial equation, and horizon boundary limit.
- `field01_toy_numerical_results.md` — first numerical solution of the phase-normal radial profile and horizon-like boundary test.
- `field01_screened_phase_normal_model.md` — gauge-like screened extension of the toy model, introduced to remove long-range phase divergence and bridge toward charge-like structure.
- `field01_screened_numerical_results.md` — numerical solution of the screened toy model, showing reduced particle-like energy and horizon-like normal suppression with phase compensation.
- `field01_covariant_gauge_bridge.md` — covariant notation for the screened toy model, gauge-like transformation, and first separation between winding and charge-like compensation.
- `field01_noether_current_notes.md` — first conserved current-like object from phase-shift symmetry, `J^mu ~ N^2 D^mu phi`, and its cautious charge-like interpretation.
- `field01_abelian_higgs_comparison.md` — comparison between the Field 01 toy formalization and Abelian Higgs/vortex-like mathematics, separating standard structure from Field 01 interpretation.
- `field01_standard_vortex_comparison_note.md` — one-page technical note isolating the standard Abelian-Higgs / Nielsen-Olesen vortex-like content from Field 01 interpretation.
- `field01_math_core_v0.md` — stripped technical core of the toy model: phase winding, scalar modulus, U(1)-like covariant derivative, radial vortex ansatz, and explicit non-claims.
- `field01_standard_core_v1.md` — clean standard-math core: radial Abelian-Higgs/Nielsen-Olesen/Abrikosov vortex ansatz, energy, equations, flux, BPS normalization, and Schaposnik convention map, without interpretation.
- `field01_radial_vortex_functional_derivation.md` — derives the explicit polar-coordinate radial energy functional, metric factors, boundary conditions, flux, and Euler-Lagrange equations for the screened vortex ansatz.
- `field01_radial_vortex_numerical_results.md` — numerical solution of the explicit radial vortex functional and comparison with the older screened toy solver.
- `field01_bps_coupling_convention_note.md` — identifies the BPS/critical coupling in the current radial vortex normalization, including the `lambda = g^2/2` convention and BPS energy target.
- `field01_radial_vortex_bps_sweep_results.md` — coupling sweep confirming numerically that `lambda = g^2/2` gives energy close to `pi` for `n=1`, `N0=1`.
- `field01_vortex_convention_dictionary.md` — maps current radial vortex notation to common Abelian-Higgs/Nielsen-Olesen symbols, including gauge-profile conventions, coupling placement, flux, and BPS normalization warnings.
- `field01_vortex_convention_external_feedback.md` — records external feedback confirming the vortex notation while flagging the convention-sensitive `pi` versus `2 pi` BPS energy normalization.
- `field01_doctor_lobo_feedback.md` — records external guidance on Nielsen-Olesen/Abrikosov framing, covariant-derivative terminology, and the need for an explicit energy functional before physics claims.
- `field01_schaposnik_vortices_convention_map.md` — PDF-based convention map against F.A. Schaposnik, *Vortices*, including equation-number checks for the ansatz, critical coupling, and BPS energy normalization.
- `field01_memory_equivalence_notes.md` — formalizes memory as an equivalence class of phase-normal-gauge data and defines the first bulk-to-boundary memory map.
- `field01_reduced_density_memory_notes.md` — connects boundary memory to reduced density matrices and thermality as limited access, without claiming a black-hole information solution.
- `field01_interpretation_layer_v1.md` — labelled Field 01 interpretation layer: normal retention, memory classes, boundary map, reduced access, proof obligations, and explicit non-claims.
- `field01_memory_map_definitions_v1.md` — first precise definitions of bulk/boundary memory equivalence, minimal invariant maps, and the bulk-to-boundary projection.
- `field01_memory_map_radial_examples_v1.md` — applies the memory-map definitions to existing radial vortex JSON outputs, separating minimal topological memory from refined energy/coupling classes.
- `field01_profile_class_invariants_note.md` — defines radial profile classes as an optional profile-refined diagnostic, not part of minimal topological/boundary memory.
- `field01_two_layer_formalization_plan.md` — separates the standard vortex mathematics checked against convention feedback from Field 01 interpretation, listing proof obligations and public-safe wording rules.
- `field01_formalization_roadmap.md` — compact roadmap for a future formalization paper, organizing the chain from phase to reduced state.

Working rule:

- use the book and existing articles as the semantic source;
- do not rewrite the book here;
- mark each formal statement as definition, interpretation, hypothesis, or open problem;
- keep formulas cautious until a precise action or state space is defined.