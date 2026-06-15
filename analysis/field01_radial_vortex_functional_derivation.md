# Radial Vortex Functional Derivation

Purpose: replace the schematic screened term with an explicit two-dimensional radial energy functional, including polar-coordinate metric factors and convention choices.

Status: standard-math derivation / toy comparison. No Field 01 interpretation is used here.

## 1. Geometry And Coordinates

Work on the Euclidean plane with polar coordinates:

```math
ds^2=dr^2+r^2d\theta^2.
```

The metric components are:

```math
g_{rr}=1,
\qquad
g_{\theta\theta}=r^2,
\qquad
g^{rr}=1,
\qquad
g^{\theta\theta}=\frac{1}{r^2}.
```

The area element is:

```math
d^2x=\sqrt{g}\,dr\,d\theta=r\,dr\,d\theta.
```

## 2. Convention A: Gauge Coupling In Maxwell Term

Use the charge-absorbed convention:

```math
D_i\Psi=(\partial_i-iA_i)\Psi,
\qquad
\Psi=N e^{i\varphi}.
```

Here `A_i` is a coordinate one-form component. The equivalent convention with a physical gauge potential is

```math
D_i\Psi=(\partial_i-ig\mathcal A_i)\Psi,
\qquad
A_i=g\mathcal A_i.
```

The static energy density is:

```math
\mathcal E
=\frac{1}{2}g^{ij}(D_i\Psi)^*(D_j\Psi)
+\frac{1}{4g^2}F_{ij}F^{ij}
+V(N),
```

with:

```math
F_{ij}=\partial_iA_j-\partial_jA_i,
\qquad
V(N)=\frac{\lambda}{4}(N^2-N_0^2)^2.
```

In polar variables:

```math
\mathcal E
=\frac{1}{2}g^{ij}\partial_iN\partial_jN
+\frac{1}{2}N^2g^{ij}(\partial_i\varphi-A_i)(\partial_j\varphi-A_j)
+\frac{1}{4g^2}F_{ij}F^{ij}
+V(N).
```

## 3. Radial Ansatz

Choose:

```math
\varphi=n\theta,
\qquad
N=N(r),
\qquad
A=a(r)\,d\theta,
\qquad
A_r=0,
\qquad
A_\theta=a(r).
```

Equivalently, `\mathcal A=(a(r)/g)d\theta` when the coupling is placed in the covariant derivative. In either notation `a(r)` is dimensionless.

Then:

```math
D_r\varphi=0,
\qquad
D_\theta\varphi=n-a(r).
```

The scalar-gradient term becomes:

```math
\frac{1}{2}(N')^2
+\frac{1}{2}\frac{(n-a(r))^2N(r)^2}{r^2}.
```

The only nonzero field-strength component is:

```math
F_{r\theta}=a'(r).
```

Since:

```math
F_{ij}F^{ij}=2F_{r\theta}F^{r\theta}
=2\frac{(a')^2}{r^2},
```

the gauge-field energy term is:

```math
\frac{1}{4g^2}F_{ij}F^{ij}
=\frac{1}{2g^2}\frac{(a')^2}{r^2}.
```

Equivalently, the charge-absorbed magnetic field perpendicular to the plane is:

```math
B=F_{\hat r\hat\theta}=\frac{F_{r\theta}}{r}=\frac{a'}{r},
```

and the gauge term is:

```math
\frac{1}{2g^2}B^2.
```

If one instead uses `\mathcal A=(a/g)d\theta`, the physical magnetic field is `B_{\mathrm{phys}}=a'/(g r)` and the same gauge contribution is `\frac12 B_{\mathrm{phys}}^2`.

## 4. Radial Energy Functional

The total energy is:

```math
E
=2\pi\int_0^\infty r\,dr
\left[
\frac{1}{2}(N')^2
+\frac{1}{2}\frac{(n-a)^2N^2}{r^2}
+\frac{1}{2g^2}\frac{(a')^2}{r^2}
+\frac{\lambda}{4}(N^2-N_0^2)^2
\right].
```

Equivalently, as a one-dimensional radial functional:

```math
E
=2\pi\int_0^\infty dr\,
\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right].
```

This is the precise version of the previously schematic term:

```math
\frac{(n-a(r))^2N(r)^2}{r^2}.
```

## 5. Euler-Lagrange Equations

For the radial Lagrangian density inside the `dr` integral:

```math
L_r
=\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2,
```

the Euler-Lagrange equation for `N` is:

```math
N''+\frac{1}{r}N'
-\frac{(n-a)^2}{r^2}N
-\lambda N(N^2-N_0^2)=0.
```

The Euler-Lagrange equation for `a` is:

```math
a''-\frac{1}{r}a'
+g^2(n-a)N^2=0.
```

Equivalently:

```math
a''-\frac{1}{r}a'
=g^2(a-n)N^2.
```

## 6. Boundary Conditions In This Convention

For a regular finite-energy vortex-like configuration:

```math
N(0)=0,
\qquad
a(0)=0,
```

and:

```math
N(r\to\infty)\to N_0,
\qquad
a(r\to\infty)\to n.
```

The large-radius condition ensures:

```math
D_\theta\varphi=n-a(r)\to0.
```

Near the origin, regularity usually implies:

```math
N(r)\sim c\,r^{|n|},
\qquad
a(r)\sim O(r^2),
\qquad r\to0.
```

## 7. Flux In This Convention

The magnetic flux is:

```math
\Phi_B
=\int B\,d^2x
=\int_0^{2\pi}\int_0^\infty \frac{a'}{r}\,r\,dr\,d\theta
=2\pi[a(\infty)-a(0)].
```

With the above boundary conditions:

```math
\Phi_B=2\pi n.
```

If a different convention includes electric charge `e` inside the covariant derivative, this becomes `2 pi n / e`.

## 8. Convention B: Gauge Coupling In The Covariant Derivative

A common alternative is:

```math
D_i\Psi=(\partial_i-ieA_i)\Psi,
```

with gauge energy:

```math
\frac{1}{4}F_{ij}F^{ij}.
```

Then the angular term is:

```math
\frac{1}{2}\frac{(n-eA_\theta)^2N^2}{r^2}.
```

The screening condition is:

```math
eA_\theta(r\to\infty)\to n.
```

If one defines the dimensionless coordinate one-form profile:

```math
a(r)=eA_\theta(r),
```

then the radial formula returns to Convention A, with coupling moved into the gauge-field kinetic term. If `A_\theta` is instead an orthonormal physical angular component, the coordinate one-form component includes the polar-coordinate factor `r`.

## 9. Relation To The Existing Toy Model

The previous screened toy model used the replacement:

```math
\frac{n}{r}\to\frac{n-a(r)}{r}.
```

This derivation shows that this replacement is exactly what follows from the angular part of the polar-coordinate covariant derivative for the ansatz:

```math
\varphi=n\theta,
\qquad
A=a(r)\,d\theta.
```

The gauge-field radial cost should not be written generically as just `(a')^2`; the polar-coordinate expression gives:

```math
\frac{(a')^2}{2g^2r^2}
```

inside the two-dimensional energy density, or:

```math
\frac{(a')^2}{2g^2r}
```

inside the one-dimensional radial integrand.

## 10. Immediate Use

The next numerical or analytic comparison should use the radial energy:

```math
E
=2\pi\int_0^R dr\,
\left[
\frac{r}{2}(N')^2
+\frac{(n-a)^2N^2}{2r}
+\frac{(a')^2}{2g^2r}
+\frac{\lambda r}{4}(N^2-N_0^2)^2
\right],
```

with explicitly stated boundary conditions at `r=0` and `r=R` or `r=infinity`.