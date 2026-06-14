import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp, trapezoid

# Convention:
#   D_i Psi = (partial_i - i A_i) Psi
#   energy density = 1/2 |D_i Psi|^2 + 1/(4 g^2) F_ij F^ij + V(N)
#   Psi = N exp(i phi), phi = n theta, A_r = 0, A_theta = a(r)
#
# Radial energy:
#   E = 2 pi int dr [ r N'^2/2 + (n-a)^2 N^2/(2r)
#                    + a'^2/(2 g^2 r) + lambda r (N^2-N0^2)^2/4 ]

lam = 1.0
g = 1.0
N0 = 1.0
n = 1
r_min = 1.0e-3
R = 12.0
num_points = 700
out_dir = Path('analysis/numerics')


def ode(r, y):
    N = y[0]
    dN = y[1]
    a = y[2]
    da = y[3]
    ddN = -dN / r + ((n - a) ** 2 / r**2) * N + lam * N * (N**2 - N0**2)
    dda = da / r + g**2 * (a - n) * N**2
    return np.vstack((dN, ddN, da, dda))


def radial_energy_density(r, N, dN, a, da):
    return (
        0.5 * dN**2
        + 0.5 * (n - a) ** 2 * N**2 / r**2
        + 0.5 * da**2 / (g**2 * r**2)
        + lam / 4.0 * (N**2 - N0**2) ** 2
    )


def radial_integrand_without_2pi(r, N, dN, a, da):
    return (
        0.5 * r * dN**2
        + 0.5 * (n - a) ** 2 * N**2 / r
        + 0.5 * da**2 / (g**2 * r)
        + lam * r * (N**2 - N0**2) ** 2 / 4.0
    )


def solve_case(name, N_right, a_right, initial_kind):
    r = np.linspace(r_min, R, num_points)

    if initial_kind == 'vortex':
        guess_N = N0 * np.tanh(r)
        guess_a = n * (1.0 - np.exp(-r**2 / 4.0))
    elif initial_kind == 'outer_zero':
        guess_N = N0 * np.sin(np.pi * (r - r_min) / (R - r_min))
        guess_N = np.clip(guess_N, 0, None)
        guess_a = n * (1.0 - np.exp(-r**2 / 4.0))
    else:
        raise ValueError(initial_kind)

    y_guess = np.vstack((guess_N, np.gradient(guess_N, r), guess_a, np.gradient(guess_a, r)))

    def bc(ya, yb):
        return np.array([ya[0], ya[2], yb[0] - N_right, yb[2] - a_right])

    sol = solve_bvp(ode, bc, r, y_guess, max_nodes=30000, tol=1.0e-5, verbose=0)
    rr = np.linspace(r_min, R, 1400)
    yy = sol.sol(rr)
    N = yy[0]
    dN = yy[1]
    a = yy[2]
    da = yy[3]

    density = radial_energy_density(rr, N, dN, a, da)
    integrand = radial_integrand_without_2pi(rr, N, dN, a, da)
    rho = (rr - r_min) / (R - r_min)
    magnetic_field = da / rr
    energy = float(2.0 * np.pi * trapezoid(integrand, rr))
    flux = float(2.0 * np.pi * (a[-1] - a[0]))
    covariant_mismatch_right = float(n - a[-1])

    yy_derivative = sol.sol(rr, 1)
    residual = yy_derivative - ode(rr, yy)
    core_mask = rr > 5.0e-2

    result = {
        'case': name,
        'success': bool(sol.success),
        'message': sol.message,
        'parameters': {'lambda': lam, 'g': g, 'N0': N0, 'n': n, 'r_min': r_min, 'R': R},
        'boundary_conditions': {'N(r_min)': 0.0, 'a(r_min)': 0.0, 'N(R)': N_right, 'a(R)': a_right},
        'energy_finite_disk': energy,
        'winding_Q_phase': int(n),
        'flux_finite_disk': flux,
        'flux_over_2pi': float(flux / (2.0 * np.pi)),
        'screened_phase_mismatch_right': covariant_mismatch_right,
        'max_N': float(np.max(N)),
        'min_N': float(np.min(N)),
        'N_mid': float(N[len(N) // 2]),
        'N_left': float(N[0]),
        'N_right': float(N[-1]),
        'a_left': float(a[0]),
        'a_mid': float(a[len(a) // 2]),
        'a_right': float(a[-1]),
        'max_abs_ode_residual_excluding_core': float(np.max(np.abs(residual[:, core_mask]))),
    }

    np.savetxt(
        out_dir / f'{name}_radial_vortex_profile.csv',
        np.column_stack([rr, rho, N, a, n - a, magnetic_field, dN, da, density, 2.0 * np.pi * integrand]),
        delimiter=',',
        header='r,rho,N,a,n_minus_a,B,dN,da_dr,energy_density,2pi_radial_integrand',
        comments='',
    )
    return result, rr, N, a


def main():
    standard, r1, N1, a1 = solve_case('standard_vortex_boundary', N0, n, 'vortex')
    forced_outer_zero, r2, N2, a2 = solve_case('forced_outer_zero_boundary', 0.0, n, 'outer_zero')
    results = {
        'standard_vortex_boundary': standard,
        'forced_outer_zero_boundary': forced_outer_zero,
    }

    with (out_dir / 'radial_vortex_results.json').open('w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    axes[0].plot(r1, N1, label='standard N(R)=N0')
    axes[0].plot(r2, N2, label='forced N(R)=0')
    axes[0].set_xlabel('r')
    axes[0].set_ylabel('N(r)')
    axes[0].set_title('Scalar modulus')
    axes[0].legend()

    axes[1].plot(r1, a1, label='standard a(R)=n')
    axes[1].plot(r2, a2, label='forced a(R)=n')
    axes[1].axhline(n, linestyle='--', linewidth=1, color='black', label='n')
    axes[1].set_xlabel('r')
    axes[1].set_ylabel('a(r)')
    axes[1].set_title('Angular gauge profile')
    axes[1].legend()

    fig.suptitle('Radial U(1) scalar-gauge vortex-like profiles')
    fig.tight_layout()
    fig.savefig(out_dir / 'radial_vortex_profiles.png', dpi=180)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()