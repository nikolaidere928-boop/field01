# NUM67: Exact Midpoint Decomposition of a Local RHS Difference

**Date:** 10 September 2026  
**Type:** exact rational-arithmetic audit of saved states

NUM67 compares the `baseline17` (`NUM53`, `full`) and `split9` (`NUM62`,
`split9`) saved states at the midpoint of their common first mesh cell. It
reconstructs the midpoint with the stored Hermite--Simpson rule and evaluates
the difference in the third component of the forced right-hand side.

At the common midpoint radius `r`, the state-dependent part of that component
is

```text
F_3(r,q,w,v) = -4v/r + 3w^2 + r^2 w^3 + q^2 + r^2 w q^2.
```

The common forcing correction cancels in the difference. Let index 0 denote
`baseline17`, index 1 denote `split9`, and write `delta x = x_1 - x_0`,
`mean(w) = (w_1+w_0)/2`, and `mean(q^2) = (q_1^2+q_0^2)/2`. The symmetric
variable decomposition is

```text
Cq = [1 + r^2 mean(w)] (q_1+q_0) delta(q)
Cw = [3(w_1+w_0) + r^2(w_1^2+w_1w_0+w_0^2) + r^2 mean(q^2)] delta(w)
Cv = -4 delta(v)/r
delta F_3 = Cq + Cw + Cv
```

The exact-rational replay gives these decimal displays; exact fractions are
stored in the JSON result:

```text
delta F_3(midpoint) = 0.0004678056046977509598349958415123727298038
delta Q_mid         = 0.00007428118714700580221344388786438748690375
```

```text
Cq =  0.001041042437093473536931548499355568733048
Cw =  0.0006398724792316857548840248190032009364338
Cv = -0.001213109311627408331980577476846396939678
```

The three terms sum exactly to the same right-hand-side difference. This is
an algebraic accounting identity for these two saved states, not a unique
causal attribution, independent perturbation of the fields, stability result,
new solver run, or physical validation.

## Reproduction

From this directory, using only the Python standard library:

```sh
python verify_num67.py --inputs inputs --check NUM67_MIDPOINT_DECOMPOSITION_01.json
```

The verifier checks the raw input hashes, saved-state and mesh hashes,
midpoint reconstruction, local balance identities, both decompositions, and
the coefficient-source provenance. The source snapshots and coefficient
script are included so the check does not depend on the larger working
archive. The archived script lacks its final line feed; the verifier checks
both its raw hash and the hash after appending that single line feed against
the source hash recorded in NUM66. It parses the coefficient tuple without
executing the script.

Workspace path prefixes in the source-hash maps are normalized in this
reproduction package. Recorded content hashes and numerical inputs are
preserved; the normalization changes no state, mesh, coefficient, or result.

## Provenance and limitations

The saved JSON preserves the provenance note recorded when NUM67 was first
written. A subsequent archive check supplies the source script and confirms
its coefficient tuple and hash convention. The replay confirms the saved
NUM66 numbers and local NUM67 algebra, but does not audit the full ancestor
calculation chain, establish causal attribution, or validate a physical
model. No new solves, meshes, or extrema searches are performed.

The machine-readable exact result is
`NUM67_MIDPOINT_DECOMPOSITION_01.json`.