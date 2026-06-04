import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp, trapezoid

A = 1.0
B = 1.0
lam = 1.0
N0 = 1.0
n = 1
r_min = 1.0e-3
R = 12.0
num_points = 500
out_dir = Path('analysis/numerics')


def ode(r, y):
    N = y[0]
    dN = y[1]
    # A(N'' + N'/r) - B n^2 N/r^2 - lambda N(N^2-N0^2)=0
    ddN = -dN / r + (B / A) * n**2 * N / r**2 + (lam / A) * N * (N**2 - N0**2)
    return np.vstack((dN, ddN))


def solve_case(name, boundary_right, initial_kind):
    r = np.linspace(r_min, R, num_points)
    if initial_kind == 'particle':
        guess_N = np.tanh(r)
    elif initial_kind == 'horizon':
        guess_N = np.sin(np.pi * (r - r_min) / (R - r_min))
        guess_N = np.clip(guess_N, 0, None)
    else:
        raise ValueError(initial_kind)
    guess_dN = np.gradient(guess_N, r)
    y_guess = np.vstack((guess_N, guess_dN))

    def bc(ya, yb):
        return np.array([ya[0], yb[0] - boundary_right])

    sol = solve_bvp(ode, bc, r, y_guess, max_nodes=20000, tol=1e-5, verbose=0)
    rr = np.linspace(r_min, R, 1200)
    yy = sol.sol(rr)
    N = yy[0]
    dN = yy[1]
    density = 0.5 * A * dN**2 + 0.5 * B * n**2 * N**2 / rr**2 + lam / 4.0 * (N**2 - N0**2)**2
    radial_integrand = 2 * np.pi * density * rr
    energy = float(trapezoid(radial_integrand, rr))
    winding = int(n)
    yy_derivative = sol.sol(rr, 1)
    residual = yy_derivative - ode(rr, yy)
    # Ignore a tiny core neighborhood for the max residual because the radial
    # equation contains 1/r and 1/r^2 terms and r_min is only a numerical cutoff.
    core_mask = rr > 5.0e-2
    result = {
        'case': name,
        'success': bool(sol.success),
        'message': sol.message,
        'parameters': {'A': A, 'B': B, 'lambda': lam, 'N0': N0, 'n': n, 'r_min': r_min, 'R': R},
        'boundary_conditions': {'N(r_min)': 0.0, 'N(R)': boundary_right},
        'energy_finite_disk': energy,
        'winding_Q': winding,
        'max_N': float(np.max(N)),
        'min_N': float(np.min(N)),
        'N_mid': float(N[len(N)//2]),
        'N_left': float(N[0]),
        'N_right': float(N[-1]),
        'max_abs_ode_residual': float(np.max(np.abs(residual[:, core_mask]))),
    }
    np.savetxt(out_dir / f'{name}_profile.csv', np.column_stack([rr, N, dN, density, radial_integrand]), delimiter=',', header='r,N,dN,density,2pi_r_density', comments='')
    return result, rr, N


def main():
    particle, r1, N1 = solve_case('particle_boundary_N0', 1.0, 'particle')
    horizon, r2, N2 = solve_case('horizon_boundary_zero', 0.0, 'horizon')

    with (out_dir / 'phase_normal_profile_results.json').open('w', encoding='utf-8') as f:
        json.dump({'particle_boundary_N0': particle, 'horizon_boundary_zero': horizon}, f, indent=2)

    plt.figure(figsize=(7, 4.5))
    plt.plot(r1, N1, label='particle-like: N(R)=N0')
    plt.plot(r2, N2, label='horizon-like: N(R)=0')
    plt.xlabel('r')
    plt.ylabel('N(r)')
    plt.title('Toy Field 01 phase-normal radial profiles')
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / 'phase_normal_profiles.png', dpi=180)

    print(json.dumps({'particle_boundary_N0': particle, 'horizon_boundary_zero': horizon}, indent=2))


if __name__ == '__main__':
    main()