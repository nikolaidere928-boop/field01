# Vortex Convention External Feedback

Purpose: record external feedback on the public Abelian-Higgs / Nielsen-Olesen vortex convention-check question.

Status: external diagnostic feedback. This is not a proof and not a final reference; it is a useful check against likely standard usage.

Date: 2026-06-10.

## 1. Context

A public convention-check question asked whether the current two-dimensional screened phase-winding ansatz is best compared with Abelian-Higgs / Nielsen-Olesen vortex notation.

The question emphasized that the Field 01 interpretation is speculative and that the goal is only to identify standard mathematics, terminology, and normalization.

## 2. Feedback Summary

The external reply confirmed the following points:

1. The convention `A_theta = a(r)` is acceptable, though less common than profile conventions such as:

```math
a(r)=n\alpha(r),
\qquad
\alpha(0)=0,
\qquad
\alpha(\infty)=1,
```

or:

```math
a(r)=n[1-P(r)],
\qquad
P(0)=1,
\qquad
P(\infty)=0.
```

2. The stated critical-coupling relation was confirmed in this convention:

```math
\lambda=\frac{g^2}{2},
\qquad
\beta=\frac{2\lambda}{g^2}=1.
```

3. No obvious missing factors of `r`, `2`, or `g` were identified in the radial energy terms:

```math
E=2\pi\int dr\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right].
```

4. The main caution was the BPS energy normalization. The reply expected the standard vortex mass/bound to be:

```math
E_{\mathrm{BPS}}=2\pi N_0^2 |n|,
```

whereas the current notes state:

```math
E_{\mathrm{BPS}}=\pi N_0^2 |n|.
```

## 3. Assessment

The `pi` versus `2 pi` issue is likely a normalization difference rather than an immediate error in the radial functional.

The current normalization uses:

```math
E=\int d^2x\left[
\frac{1}{2}|D_i\Psi|^2
+\frac{1}{2g^2}B^2
+\frac{\lambda}{4}(|\Psi|^2-N_0^2)^2
\right].
```

With this explicit `1/2` multiplying the complex scalar kinetic term, the Bogomolny completion in `field01_bps_coupling_convention_note.md` gives:

```math
E_{\mathrm{BPS}}=\frac{N_0^2}{2}\int B\,d^2x
=\pi N_0^2 |n|,
```

because:

```math
\int B\,d^2x=2\pi n.
```

Many standard Abelian-Higgs references instead use a complex scalar kinetic term without this extra `1/2`, or define the vacuum scale differently. In those conventions the same bound is commonly written as:

```math
E_{\mathrm{BPS}}=2\pi v^2 |n|.
```

Therefore, the safest public statement is not simply `E = pi`, but:

```text
With my explicit 1/2 |D_i Psi|^2 normalization, the Bogomolny completion gives E_BPS = pi N0^2 |n|. In the more common complex-scalar normalization this is often written as 2 pi v^2 |n|, so I need to state the normalization before comparing numerical BPS energies.
```

## 4. Practical Consequences

- Keep `A_theta=a(r)` as an allowed but less common convention.
- Keep `lambda=g^2/2` and `beta=1` as the current critical-coupling convention.
- Do not state `E=pi` publicly without the phrase `with my explicit 1/2 scalar-kinetic normalization`.
- If comparing against standard references, map both the scalar kinetic normalization and the vacuum parameter before comparing BPS energy values.
- Treat this as a useful warning to make the convention dictionary more explicit, not as a failure of the toy model.

## 5. Suggested Follow-Up Reply

```text
Thank you, this is exactly the kind of convention issue I was trying to catch.

I used an explicit 1/2 in front of |D_i Psi|^2, so my current Bogomolny completion gives E_BPS = (N0^2/2) Phi_B = pi N0^2 n when Phi_B = 2 pi n. I understand that many Abelian-Higgs references use the complex scalar kinetic term without that extra 1/2, in which case the bound is written as 2 pi v^2 n.

So the safest wording is probably: the ansatz and radial energy are standard up to normalization, but the BPS energy must be compared only after mapping the scalar kinetic normalization and vacuum parameter.

Does that sound like the right way to phrase it?
```