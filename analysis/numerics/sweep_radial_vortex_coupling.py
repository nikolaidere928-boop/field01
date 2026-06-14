import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp, trapezoid

# Standard radial U(1) scalar-gauge vortex-like ansatz.
# Convention:
#   D_i Psi = (partial_i - i A_i) Psi
#   E = int [ 1/2 |D_i Psi|^2 + 1/(2 g^2) B^2
#             + lambda/4 (|Psi|^2 - N0^2)^2 ] d^2x

GAUGE_COUPLING = 1.0
VACUUM_MODULUS = 1.0
WINDING = 1
R_MIN = 1.0e-3
R_MAX = 20.0
NUM_POINTS = 900
OUT_DIR = Path('analysis/numerics')
LAMBDA_VALUES = [0.25, 0.5, 1.0, 2.0]


def make_ode(lambda_value):
    def ode(radial_points, state):
        modulus = state[0]
        modulus_derivative = state[1]
        gauge_profile = state[2]
        gauge_derivative = state[3]
        second_modulus = (
            -modulus_derivative / radial_points
            + ((WINDING - gauge_profile) ** 2 / radial_points**2) * modulus
            + lambda_value * modulus * (modulus**2 - VACUUM_MODULUS**2)
        )
        second_gauge = (
            gauge_derivative / radial_points
            + GAUGE_COUPLING**2 * (gauge_profile - WINDING) * modulus**2
        )
        return np.vstack((modulus_derivative, second_modulus, gauge_derivative, second_gauge))

    return ode


def radial_integrand_without_2pi(radial_points, modulus, modulus_derivative, gauge_profile, gauge_derivative, lambda_value):
    return (
        0.5 * radial_points * modulus_derivative**2
        + 0.5 * (WINDING - gauge_profile) ** 2 * modulus**2 / radial_points
        + 0.5 * gauge_derivative**2 / (GAUGE_COUPLING**2 * radial_points)
        + lambda_value * radial_points * (modulus**2 - VACUUM_MODULUS**2) ** 2 / 4.0
    )


def radial_energy_density(radial_points, modulus, modulus_derivative, gauge_profile, gauge_derivative, lambda_value):
    return (
        0.5 * modulus_derivative**2
        + 0.5 * (WINDING - gauge_profile) ** 2 * modulus**2 / radial_points**2
        + 0.5 * gauge_derivative**2 / (GAUGE_COUPLING**2 * radial_points**2)
        + lambda_value * (modulus**2 - VACUUM_MODULUS**2) ** 2 / 4.0
    )


def lambda_label(lambda_value):
    return str(lambda_value).replace('.', 'p')


def load_profile_csv(profile_csv):
    return np.genfromtxt(OUT_DIR / profile_csv, delimiter=',', names=True)


def profile_distance(profile_a, profile_b):
    common_rho = np.linspace(0.0, 1.0, 1800)
    modulus_a = np.interp(common_rho, profile_a['rho'], profile_a['N'])
    modulus_b = np.interp(common_rho, profile_b['rho'], profile_b['N'])
    gauge_a = np.interp(common_rho, profile_a['rho'], profile_a['a'])
    gauge_b = np.interp(common_rho, profile_b['rho'], profile_b['a'])
    modulus_difference = modulus_a - modulus_b
    gauge_difference = gauge_a - gauge_b
    max_abs_modulus = float(np.max(np.abs(modulus_difference)))
    max_abs_gauge = float(np.max(np.abs(gauge_difference)))
    l2_rho = float(np.sqrt(trapezoid(modulus_difference**2 + gauge_difference**2, common_rho)))
    return max(max_abs_modulus, max_abs_gauge), max_abs_modulus, max_abs_gauge, l2_rho


def write_profile_distances(results):
    rows = []
    records = []
    profiles = {item['lambda']: load_profile_csv(item['profile_csv']) for item in results}
    for left_index, left in enumerate(results):
        for right in results[left_index + 1:]:
            d_max, d_n, d_a, d_l2 = profile_distance(profiles[left['lambda']], profiles[right['lambda']])
            rows.append([left['lambda'], right['lambda'], d_max, d_n, d_a, d_l2])
            records.append(
                {
                    'lambda_left': float(left['lambda']),
                    'lambda_right': float(right['lambda']),
                    'd_profile_max': d_max,
                    'max_abs_N': d_n,
                    'max_abs_a': d_a,
                    'd_profile_l2_rho': d_l2,
                }
            )
    rows = np.array(rows)
    csv_path = OUT_DIR / 'radial_vortex_profile_distances.csv'
    np.savetxt(
        csv_path,
        rows,
        delimiter=',',
        header='lambda_left,lambda_right,d_profile_max,max_abs_N,max_abs_a,d_profile_l2_rho',
        comments='',
    )
    json_path = OUT_DIR / 'radial_vortex_profile_distances.json'
    with json_path.open('w', encoding='utf-8') as output_file:
        json.dump(
            {
                'source': csv_path.name,
                'profile_columns': [
                    'r',
                    'rho',
                    'N',
                    'a',
                    'n_minus_a',
                    'B',
                    'dN',
                    'da_dr',
                    'energy_density',
                    '2pi_radial_integrand',
                ],
                'distance_definition': {
                    'd_profile_max': 'max over rho of max(abs(Delta N), abs(Delta a))',
                    'd_profile_l2_rho': 'sqrt integral_0^1 [(Delta N)^2 + (Delta a)^2] d rho',
                },
                'results': records,
            },
            output_file,
            indent=2,
        )
        output_file.write('\n')
    return csv_path.name, json_path.name


def solve_for_lambda(lambda_value, previous_solution=None):
    radial_mesh = np.linspace(R_MIN, R_MAX, NUM_POINTS)
    if previous_solution is None:
        guess_modulus = VACUUM_MODULUS * np.tanh(radial_mesh)
        guess_gauge = WINDING * (1.0 - np.exp(-radial_mesh**2 / 4.0))
        state_guess = np.vstack(
            (
                guess_modulus,
                np.gradient(guess_modulus, radial_mesh),
                guess_gauge,
                np.gradient(guess_gauge, radial_mesh),
            )
        )
    else:
        state_guess = previous_solution.sol(radial_mesh)

    ode = make_ode(lambda_value)

    def boundary_conditions(left_state, right_state):
        return np.array(
            [
                left_state[0],
                left_state[2],
                right_state[0] - VACUUM_MODULUS,
                right_state[2] - WINDING,
            ]
        )

    solution = solve_bvp(
        ode,
        boundary_conditions,
        radial_mesh,
        state_guess,
        max_nodes=40000,
        tol=1.0e-5,
        verbose=0,
    )

    sample_points = np.linspace(R_MIN, R_MAX, 1800)
    sampled_state = solution.sol(sample_points)
    modulus = sampled_state[0]
    modulus_derivative = sampled_state[1]
    gauge_profile = sampled_state[2]
    gauge_derivative = sampled_state[3]
    integrand = radial_integrand_without_2pi(
        sample_points,
        modulus,
        modulus_derivative,
        gauge_profile,
        gauge_derivative,
        lambda_value,
    )
    density = radial_energy_density(
        sample_points,
        modulus,
        modulus_derivative,
        gauge_profile,
        gauge_derivative,
        lambda_value,
    )
    rho = (sample_points - R_MIN) / (R_MAX - R_MIN)
    magnetic_field = gauge_derivative / sample_points
    energy = float(2.0 * np.pi * trapezoid(integrand, sample_points))
    flux = float(2.0 * np.pi * (gauge_profile[-1] - gauge_profile[0]))
    beta = float(2.0 * lambda_value / GAUGE_COUPLING**2)
    bps_energy_target = float(np.pi * VACUUM_MODULUS**2 * abs(WINDING))

    bps_modulus_residual = modulus_derivative - (WINDING - gauge_profile) * modulus / sample_points
    bps_gauge_residual = gauge_derivative / sample_points - 0.5 * GAUGE_COUPLING**2 * (
        VACUUM_MODULUS**2 - modulus**2
    )
    ode_residual = solution.sol(sample_points, 1) - ode(sample_points, sampled_state)
    core_mask = sample_points > 5.0e-2

    result = {
        'lambda': float(lambda_value),
        'beta_2lambda_over_g2': beta,
        'success': bool(solution.success),
        'message': solution.message,
        'energy_finite_disk': energy,
        'energy_minus_pi': float(energy - bps_energy_target),
        'energy_over_pi': float(energy / bps_energy_target),
        'bps_energy_target_pi_N0sq_absn': bps_energy_target,
        'flux_finite_disk': flux,
        'flux_over_2pi': float(flux / (2.0 * np.pi)),
        'screened_phase_mismatch_right': float(WINDING - gauge_profile[-1]),
        'max_abs_ode_residual_excluding_core': float(np.max(np.abs(ode_residual[:, core_mask]))),
        'max_abs_bps_modulus_residual_excluding_core': float(np.max(np.abs(bps_modulus_residual[core_mask]))),
        'max_abs_bps_gauge_residual_excluding_core': float(np.max(np.abs(bps_gauge_residual[core_mask]))),
        'N_mid': float(modulus[len(modulus) // 2]),
        'a_mid': float(gauge_profile[len(gauge_profile) // 2]),
        'profile_csv': f'radial_vortex_profile_lambda_{lambda_label(lambda_value)}.csv',
    }
    np.savetxt(
        OUT_DIR / result['profile_csv'],
        np.column_stack(
            [
                sample_points,
                rho,
                modulus,
                gauge_profile,
                WINDING - gauge_profile,
                magnetic_field,
                modulus_derivative,
                gauge_derivative,
                density,
                2.0 * np.pi * integrand,
            ]
        ),
        delimiter=',',
        header='r,rho,N,a,n_minus_a,B,dN,da_dr,energy_density,2pi_radial_integrand',
        comments='',
    )
    return result, solution


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    previous_solution = None
    for lambda_value in LAMBDA_VALUES:
        result, previous_solution = solve_for_lambda(lambda_value, previous_solution)
        results.append(result)

    profile_distances_csv, profile_distances_json = write_profile_distances(results)

    output = {
        'parameters': {
            'g': GAUGE_COUPLING,
            'N0': VACUUM_MODULUS,
            'n': WINDING,
            'r_min': R_MIN,
            'R': R_MAX,
            'lambda_values': LAMBDA_VALUES,
        },
        'profile_distances_csv': profile_distances_csv,
        'profile_distances_json': profile_distances_json,
        'results': results,
    }

    with (OUT_DIR / 'radial_vortex_coupling_sweep.json').open('w', encoding='utf-8') as output_file:
        json.dump(output, output_file, indent=2)

    rows = np.array(
        [
            [
                item['lambda'],
                item['beta_2lambda_over_g2'],
                item['energy_finite_disk'],
                item['energy_over_pi'],
                item['energy_minus_pi'],
                item['flux_over_2pi'],
                item['max_abs_bps_modulus_residual_excluding_core'],
                item['max_abs_bps_gauge_residual_excluding_core'],
            ]
            for item in results
        ]
    )
    np.savetxt(
        OUT_DIR / 'radial_vortex_coupling_sweep.csv',
        rows,
        delimiter=',',
        header='lambda,beta,energy,energy_over_pi,energy_minus_pi,flux_over_2pi,max_abs_bps_N_residual,max_abs_bps_a_residual',
        comments='',
    )

    beta_values = rows[:, 1]
    energy_values = rows[:, 2]
    plt.figure(figsize=(6.8, 4.2))
    plt.plot(beta_values, energy_values, marker='o', label='finite-disk energy')
    plt.axhline(np.pi, linestyle='--', color='black', linewidth=1, label='BPS target pi')
    plt.axvline(1.0, linestyle=':', color='gray', linewidth=1, label='beta=1')
    plt.xlabel('beta = 2 lambda / g^2')
    plt.ylabel('Energy')
    plt.title('Radial vortex coupling sweep')
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'radial_vortex_coupling_sweep.png', dpi=180)

    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()