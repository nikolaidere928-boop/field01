import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp, trapezoid

A = 1.0
B = 1.0
C = 1.0
lam = 1.0
N0 = 1.0
n = 1
r_min = 1.0e-3
R = 12.0
num_points = 700
out_dir = Path('analysis/numerics')


def ode(r, y):
    N = y[0]
    dN = y[1]
    alpha = y[2]
    dalpha = y[3]
    ddN = -dN / r + (B / A) * (n - alpha) ** 2 * N / r**2 + (lam / A) * N * (N**2 - N0**2)
    ddalpha = dalpha / r - (B / C) * (n - alpha) * N**2
    return np.vstack((dN, ddN, dalpha, ddalpha))


def solve_case(name, N_right, alpha_right, initial_kind):
    r = np.linspace(r_min, R, num_points)
    if initial_kind == 'particle':
        guess_N = np.tanh(r)
        guess_alpha = n * (1.0 - np.exp(-r**2 / 4.0))
    elif initial_kind == 'horizon':
        guess_N = np.sin(np.pi * (r - r_min) / (R - r_min))
        guess_N = np.clip(guess_N, 0, None)
        guess_alpha = n * (1.0 - np.exp(-r**2 / 4.0))
    else:
        raise ValueError(initial_kind)

    y_guess = np.vstack((guess_N, np.gradient(guess_N, r), guess_alpha, np.gradient(guess_alpha, r)))

    def bc(ya, yb):
        return np.array([ya[0], ya[2], yb[0] - N_right, yb[2] - alpha_right])

    sol = solve_bvp(ode, bc, r, y_guess, max_nodes=30000, tol=1e-5, verbose=0)
    rr = np.linspace(r_min, R, 1400)
    yy = sol.sol(rr)
    N = yy[0]
    dN = yy[1]
    alpha = yy[2]
    dalpha = yy[3]
    density = (
        0.5 * A * dN**2
        + 0.5 * B * (n - alpha) ** 2 * N**2 / rr**2
        + 0.5 * C * dalpha**2 / rr**2
        + lam / 4.0 * (N**2 - N0**2) ** 2
    )
    radial_integrand = 2 * np.pi * density * rr
    energy = float(trapezoid(radial_integrand, rr))
    yy_derivative = sol.sol(rr, 1)
    residual = yy_derivative - ode(rr, yy)
    core_mask = rr > 5.0e-2
    result = {
        'case': name,
        'success': bool(sol.success),
        'message': sol.message,
        'parameters': {'A': A, 'B': B, 'C': C, 'lambda': lam, 'N0': N0, 'n': n, 'r_min': r_min, 'R': R},
        'boundary_conditions': {'N(r_min)': 0.0, 'a(r_min)': 0.0, 'N(R)': N_right, 'a(R)': alpha_right},
        'energy_finite_disk': energy,
        'winding_Q_phase': int(n),
        'screened_phase_mismatch_right': float(n - alpha[-1]),
        'max_N': float(np.max(N)),
        'min_N': float(np.min(N)),
        'N_mid': float(N[len(N)//2]),
        'N_left': float(N[0]),
        'N_right': float(N[-1]),
        'a_left': float(alpha[0]),
        'a_mid': float(alpha[len(alpha)//2]),
        'a_right': float(alpha[-1]),
        'max_abs_ode_residual': float(np.max(np.abs(residual[:, core_mask]))),
    }
    np.savetxt(
        out_dir / f'{name}_screened_profile.csv',
        np.column_stack([rr, N, dN, alpha, dalpha, density, radial_integrand]),
        delimiter=',',
        header='r,N,dN,a,da,density,2pi_r_density',
        comments='',
    )
    return result, rr, N, alpha


def main():
    particle, r1, N1, a1 = solve_case('screened_particle_boundary', 1.0, 1.0, 'particle')
    horizon, r2, N2, a2 = solve_case('screened_horizon_boundary', 0.0, 1.0, 'horizon')
    results = {'screened_particle_boundary': particle, 'screened_horizon_boundary': horizon}
    with (out_dir / 'screened_phase_normal_results.json').open('w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    axes[0].plot(r1, N1, label='particle N')
    axes[0].plot(r2, N2, label='horizon N')
    axes[0].set_xlabel('r')
    axes[0].set_ylabel('N(r)')
    axes[0].legend()
    axes[0].set_title('Normal retention')
    axes[1].plot(r1, a1, label='particle a')
    axes[1].plot(r2, a2, label='horizon a')
    axes[1].axhline(n, linestyle='--', linewidth=1, color='black', label='n')
    axes[1].set_xlabel('r')
    axes[1].set_ylabel('a(r)')
    axes[1].legend()
    axes[1].set_title('Screening field')
    fig.suptitle('Screened Field 01 phase-normal toy profiles')
    fig.tight_layout()
    fig.savefig(out_dir / 'screened_phase_normal_profiles.png', dpi=180)
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()