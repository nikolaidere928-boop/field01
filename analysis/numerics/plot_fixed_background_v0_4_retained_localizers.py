from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


DATA_PATH = Path("analysis/numerics/fixed_background_v0_4_retained_localizers.csv")
FIGURE_PATH = Path("figures/fixed_background_v0_4_retained_localizers.png")


def retained_localizers(host: np.ndarray) -> dict[str, np.ndarray]:
    vacuum = 1.0 - host**2

    q = 16
    d = 4.0
    s = 1
    zeta = 1.8105828289285173
    difference_c1 = 1.20
    difference_c2 = 0.0
    difference_lambda = -0.35

    raw_difference = (
        host**2
        * vacuum**s
        * (1.0 - zeta * host**2)
        * (1.0 + difference_c1 * vacuum + difference_c2 * vacuum**2)
        * np.exp(difference_lambda * vacuum**3)
    )
    difference_normalization = 1.0 / np.max(np.abs(raw_difference))
    difference_basis = difference_normalization * raw_difference
    difference_core = vacuum**q
    difference_shoulder = d * difference_basis
    difference_total = difference_core + difference_shoulder

    p = 1
    aligned_c1 = -3.260
    aligned_c2 = 3.041
    aligned_rho = 0.0

    raw_aligned = (
        host**2
        * vacuum**p
        * (1.0 + aligned_c1 * vacuum + aligned_c2 * vacuum**2)
        * np.exp(aligned_rho * vacuum**3)
    )
    aligned_normalization = 1.0 / np.max(raw_aligned)
    aligned = aligned_normalization * raw_aligned

    return {
        "host": host,
        "vacuum": vacuum,
        "difference_core": difference_core,
        "difference_shoulder": difference_shoulder,
        "difference_total": difference_total,
        "aligned": aligned,
    }


def save_data(profiles: dict[str, np.ndarray]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    columns = np.column_stack(tuple(profiles.values()))
    header = ",".join(profiles.keys())
    np.savetxt(DATA_PATH, columns, delimiter=",", header=header, comments="", fmt="%.12e")


def save_figure(profiles: dict[str, np.ndarray]) -> None:
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)

    host = profiles["host"]
    node = 1.0 / np.sqrt(1.8105828289285173)

    figure, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), constrained_layout=True)

    difference_axis = axes[0]
    difference_axis.plot(
        host,
        profiles["difference_core"],
        color="#6b7280",
        linestyle="--",
        linewidth=1.8,
        label=r"core $V^{q}$",
    )
    difference_axis.plot(
        host,
        profiles["difference_shoulder"],
        color="#2563eb",
        linestyle="-.",
        linewidth=1.8,
        label=r"shoulder $dB_{\Delta}$",
    )
    difference_axis.plot(
        host,
        profiles["difference_total"],
        color="#991b1b",
        linewidth=2.3,
        label=r"total $L_{\Delta}$",
    )
    difference_axis.axhline(0.0, color="#111827", linewidth=0.8)
    difference_axis.axvline(
        node,
        color="#7c3aed",
        linestyle=":",
        linewidth=1.6,
        label=r"node $H=1/\sqrt{\zeta}$",
    )
    difference_axis.set_title("(a) Difference channel")
    difference_axis.set_xlabel(r"Normalized host $H$")
    difference_axis.set_ylabel("Localizer amplitude")
    difference_axis.legend(frameon=False, fontsize=8.5, loc="best")
    difference_axis.grid(alpha=0.22, linewidth=0.7)

    aligned_axis = axes[1]
    aligned_axis.plot(
        host,
        profiles["aligned"],
        color="#047857",
        linewidth=2.3,
        label=r"retained $L_{\mathrm{A}}$",
    )
    aligned_axis.axhline(0.0, color="#111827", linewidth=0.8)
    aligned_axis.set_title("(b) Aligned channel")
    aligned_axis.set_xlabel(r"Normalized host $H$")
    aligned_axis.set_ylabel("Localizer amplitude")
    aligned_axis.legend(frameon=False, fontsize=8.5, loc="best")
    aligned_axis.grid(alpha=0.22, linewidth=0.7)

    for axis in axes:
        axis.set_xlim(0.0, 1.0)
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)

    figure.savefig(FIGURE_PATH, dpi=300, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    profiles = retained_localizers(np.linspace(0.0, 1.0, 1001))
    save_data(profiles)
    save_figure(profiles)
    print(f"Wrote {DATA_PATH}")
    print(f"Wrote {FIGURE_PATH}")


if __name__ == "__main__":
    main()