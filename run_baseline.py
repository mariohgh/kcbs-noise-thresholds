"""Reproduce the KCBS noise baseline and save a plot.

This is a reproduction of a known result, not a new contribution.
"""

import numpy as np
import matplotlib.pyplot as plt

from contextuality import (
    NC_BOUND, analytic_threshold, analytic_witness,
    depolarize, ideal_state, witness,
)


def main():
    rho = ideal_state()
    p_vals = np.linspace(0.0, 1.0, 201)

    numerical  = np.array([witness(depolarize(rho, p)) for p in p_vals])
    analytical = np.array([analytic_witness(p) for p in p_vals])
    p_star     = analytic_threshold()

    print(f"Ideal quantum value  : {witness(rho):.10f}  (expected sqrt(5) = {np.sqrt(5):.10f})")
    print(f"Noncontextual bound  : {NC_BOUND:.10f}")
    print(f"Noise threshold p*   : {p_star:.10f}")
    print(f"Max numerical error  : {np.max(np.abs(numerical - analytical)):.3e}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(p_vals, numerical,  label="Numerical")
    ax.plot(p_vals, analytical, "--", label="Analytic")
    ax.axhline(NC_BOUND, color="black", linestyle=":", label="Noncontextual bound (K=2)")
    ax.axvline(p_star,   color="red",   linestyle=":", label=f"Threshold p* ≈ {p_star:.4f}")
    ax.set_xlabel("Depolarizing probability p")
    ax.set_ylabel("KCBS witness K")
    ax.set_title("KCBS contextuality under state depolarization\n(baseline reproduction — not a new result)")
    ax.legend()
    fig.tight_layout()
    fig.savefig("kcbs_noise_baseline.png", dpi=200)
    print("Plot saved: kcbs_noise_baseline.png")


if __name__ == "__main__":
    main()
