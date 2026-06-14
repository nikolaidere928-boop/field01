# Schaposnik Vortices Convention Map

Purpose: map the current Field 01 radial vortex notation against F.A. Schaposnik, *Vortices*, arXiv:hep-th/0611028, using the uploaded PDF `0611028v1.pdf`.

Status: PDF-based convention map. This is a standard-math comparison aid, not a proof, endorsement, or final literature review. No Field 01 interpretation is used here.

Date: 2026-06-14.

## 1. Source And Extraction Status

Reference:

```text
F.A. Schaposnik, Vortices, arXiv:hep-th/0611028v1.
```

Local source used:

```text
uploaded PDF: 0611028v1.pdf
```

Extraction notes:

- The PDF has 60 pages.
- Text was extracted with `pypdf` into `/tmp` for analysis only; no PDF copy was added to the repository.
- Equation numbers and page-level locations below come from the uploaded PDF.
- Some formula signs and small factors in equation (11) should still be visually checked before a final citation-grade manuscript, because PDF text extraction can lose small glyphs. The normalization conclusions below are based on the clearly extracted action, energy, and Bogomolny equations.

## 2. Reference Landmarks

Schaposnik's notes provide a useful standard comparison for the convention bridge:

| Topic | PDF location | Equation / statement |
|---|---:|---|
| Start point | p. 1 abstract | starts from the Nielsen-Olesen ansatz for the Abelian Higgs model |
| Abrikosov / condensed-matter link | pp. 2--3 | vortices originate in Abrikosov superconductivity and connect to Ginzburg-Landau theory |
| Critical point in Schaposnik convention | p. 3 | `e^2 = 8 lambda`, eq. (1) |
| Abelian-Higgs action | p. 3 | action with Maxwell term, scalar kinetic term, and symmetry-breaking potential, eq. (2) |
| Field strength | p. 3 | `F_mu nu = partial_mu A_nu - partial_nu A_mu`, eq. (3) |
| Complex scalar | p. 3 | `phi = phi_1 + i phi_2`, eq. (4) |
| Covariant derivative | p. 3 | `D_mu = partial_mu + i e A_mu`, eq. (5) |
| Symmetry-breaking potential | p. 3 | `V ~ lambda (|phi|^2 - phi_0^2)^2`, eq. (6), as reflected in energy eq. (13) |
| Singular fluxon | p. 4 | phase winding and quantized flux, eq. (9) |
| Gauge winding map | p. 4 | `g_N(varphi)=exp(iN varphi)`, eq. (10) |
| Regular Nielsen-Olesen ansatz | p. 4 | radial scalar profile and radial gauge profile, eq. (11) |
| Boundary conditions | p. 4 | `f(0)=a(0)=0`, `f(infty)=phi_0`, `a(infty)=1`, eq. (12) |
| Energy per unit length | p. 5 | two-dimensional vortex energy, eq. (13) |
| Topology | p. 5 | `g_N:S^1_infty -> S^1`, `Pi_1(S^1)=Z`, eqs. (14)--(15) |
| Mass scales | p. 5 | `m_V=e phi_0`, `m_phi=2 sqrt(2 lambda) phi_0`, eqs. (17)--(18) |
| Scaled energy | p. 6 | rescaled energy with coefficient `lambda/e^2`, eq. (21) |
| Real-component covariant derivative | p. 6 | `D_i^{ab}=delta^{ab} partial_i + epsilon^{ab} A_i`, eq. (22) |
| Bogomolny completion | p. 7 | square completion with term `(lambda/e^2 - 1/8)`, eq. (23) |
| BPS bound | p. 7 | `E >= phi_0^2 pi |N|`, eq. (26) |
| BPS equations | p. 7 | first-order vortex equations, eq. (27) |

## 3. Main Standard-Math Identification

Definition / standard comparison:

The current Field 01 technical ansatz:

```math
\Psi=N(r)e^{in\theta},
\qquad
A_r=0,
\qquad
A_\theta=a(r),
```

with an angular covariant derivative term:

```math
D_\theta\Psi
\propto i\,[n-a(r)]N(r)e^{in\theta},
\qquad
a(r)\to n,
\qquad
D_\theta\Psi\to0
\quad(r\to\infty),
```

is structurally the same radial vortex machinery as the Nielsen-Olesen / Abelian-Higgs ansatz in Schaposnik eqs. (9)--(13).

Interpretation warning:

This identification applies only to the standard mathematical layer: winding, scalar modulus, gauge field, covariant derivative, finite-energy boundary behavior, magnetic flux, topology, and BPS normalization. It does not validate any Field 01 interpretation of memory, normal retention, horizon behavior, or charge-like meaning.

## 4. Notation Map

| Concept | Field 01 notation | Schaposnik notation | Comment |
|---|---|---|---|
| Complex scalar | `\Psi=N(r)e^{in\theta}` | `\phi=f(r)g_N(\varphi)` with `g_N=e^{iN\varphi}` | same winding-scalar structure |
| Scalar profile | `N(r)` | `f(r)` | radial modulus |
| Vacuum modulus | `N_0` | `\phi_0` | both set asymptotic scalar magnitude |
| Winding | `n` | `N` | integer vortex number |
| Angular coordinate | `\theta` | `\varphi` | notation only |
| Gauge coupling placement | coupling in Maxwell term `1/(2g^2)B^2` | coupling in `D_\mu=\partial_\mu+i e A_\mu` | requires mapping |
| Gauge profile boundary | `a_{ours}(\infty)=n` | `a_S(\infty)=1` | roughly `a_{ours}=n a_S`, up to sign/coupling convention |
| Core boundary | `N(0)=0`, `a(0)=0` | `f(0)=0`, `a(0)=0` | matched |
| Topological class | `Q=(2\pi)^{-1}\oint d\varphi=n` | `\Pi_1(S^1)=Z` and flux number `N` | matched topological content |

## 5. Energy Normalization Map

Schaposnik's energy per unit length, eq. (13), is:

```math
E_S=\int d^2x\left[
\frac14 F_{ij}^2
+\frac12 |D_i\phi|^2
+\lambda_S(|\phi|^2-\phi_0^2)^2
\right].
```

In two spatial dimensions:

```math
\frac14F_{ij}^2=\frac12 B_S^2.
```

The current Field 01 radial-vortex normalization is:

```math
E_{ours}=\int d^2x\left[
\frac12|D_i\Psi|^2
+\frac{1}{2g^2}B_{ours}^2
+\frac{\lambda_{ours}}{4}(|\Psi|^2-N_0^2)^2
\right].
```

A consistent coefficient map is:

```math
N_0\leftrightarrow\phi_0,
\qquad
n\leftrightarrow N,
\qquad
g\leftrightarrow e,
\qquad
B_{ours}\leftrightarrow eB_S,
\qquad
\lambda_{ours}=4\lambda_S.
```

Then Schaposnik's critical condition, eq. (1),

```math
e^2=8\lambda_S,
```

maps exactly to the current convention:

```math
\lambda_{ours}=4\lambda_S=\frac{e^2}{2}=\frac{g^2}{2}.
```

Thus the current internal critical-coupling statement:

```math
\lambda_{ours,\mathrm{BPS}}=\frac{g^2}{2},
\qquad
\beta=\frac{2\lambda_{ours}}{g^2}=1,
```

is consistent with Schaposnik after translating coupling placement and potential normalization.

## 6. BPS Energy Check

Schaposnik's Bogomolny completion, eq. (23), contains the convention-sensitive term:

```math
\left(\frac{\lambda_S}{e^2}-\frac18\right)(|\phi|^2-1)^2.
```

At the critical point, this term vanishes. Schaposnik then obtains the bound, eq. (26):

```math
E_S\ge \pi\phi_0^2|N|.
```

Under the map:

```math
\phi_0\leftrightarrow N_0,
\qquad
N\leftrightarrow n,
```

this is exactly the current internal BPS target:

```math
E_{ours,\mathrm{BPS}}=\pi N_0^2|n|.
```

Conclusion:

- The `pi` BPS target is not an error in the current `1/2 |D_i\Psi|^2` normalization.
- It is directly aligned with Schaposnik eq. (26).
- The alternative public form `2 pi v^2 |n|` belongs to a different scalar-field normalization and should not be mixed without an explicit map.

## 7. Terminology Update

Prefer this public wording:

```text
The scalar profile is coupled to a U(1) gauge field through the covariant derivative. In the vortex ansatz, the angular component of the covariant derivative tends to zero at infinity because the gauge profile asymptotically cancels the phase winding.
```

Avoid as the main public phrase:

```text
angularly screened phase winding
```

Allowed internal shorthand:

```text
screened angular gradient
```

but only after defining it as:

```math
D_\theta\varphi=n-a(r),
\qquad
D_\theta\varphi\to0
\quad(r\to\infty).
```

## 8. Physics Threshold

Schaposnik's presentation supports doctor_lobo's caution: the ansatz is embedded in physics only after specifying the action, equations of motion, energy functional, and boundary conditions.

For Field 01, the safe rule is:

- before the energy functional is stated, say `toy ansatz`, `formal analogy`, or `standard vortex-like mathematical structure`;
- after the energy functional is stated, say `toy field-theory-like model` only with clear normalization and non-claim warnings;
- do not say `particle model`, `new field theory`, or `physical solution` unless dynamics, observables, and interpretation are separately established.

## 9. Two-Layer Separation

Standard technical layer:

```text
phase winding + scalar modulus + U(1) covariant derivative + vortex boundary conditions + flux/BPS convention
```

Field 01 interpretive layer:

```text
normal retention, phase-structural memory, horizon-like suppression, charge-like compensation
```

Rule:

The first layer may cite Abelian-Higgs / Nielsen-Olesen / Abrikosov / Ginzburg-Landau vortex mathematics. The second layer must remain labelled `Interpretation`, `Hypothesis`, or `Open problem` until independently formalized.

## 10. Concrete Edits Implied By This Map

1. Keep `A_theta=a(r)` as an allowed convention, but state that Schaposnik uses a profile tending to `1`, so our profile is roughly `n` times the normalized reference profile.
2. Keep `lambda_ours=g^2/2`; Schaposnik eq. (1) maps to it through `lambda_ours=4 lambda_S` and `g=e`.
3. Keep `E_BPS=pi N0^2 |n|` in the explicit `1/2 |D_i Psi|^2` normalization; Schaposnik eq. (26) is consistent with this normalization map.
4. Add `Abrikosov` and `Ginzburg-Landau` to public-safe standard names.
5. Use covariant-derivative language instead of informal `angular screening` language.

## 11. Public-Safe Summary

```text
The technical core is a toy radial vortex ansatz using standard Abelian-Higgs / Nielsen-Olesen / Abrikosov vortex machinery: a winding scalar phase, a radial scalar profile, and a U(1) covariant derivative whose angular component vanishes asymptotically. In Schaposnik's conventions the BPS point is e^2=8 lambda_S and the bound is E >= pi phi_0^2 |N|; with our coupling placement this maps to lambda_ours=g^2/2 and E_BPS=pi N0^2 |n|. Any Field 01 language about memory or normal retention is interpretive and separate.
```