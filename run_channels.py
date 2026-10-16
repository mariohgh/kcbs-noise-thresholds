"""Plot KCBS witness K(p) under three noise channels on the ideal qutrit state.

Channels compared:
  - Depolarizing:      K(p) = (1-p)*sqrt(5) + p*(5/3)          threshold p* ~ 0.4146
  - Dephasing:         K(p) = sqrt(5)  (constant, no threshold)
  - Amplitude damping: K(p) = A*p*(2-p) + sqrt(5)*(1-p)^2      threshold p* ~ 0.1493
"""

import numpy as np
import matplotlib.pyplot as plt

from contextuality import (
    NC_BOUND,
    analytic_threshold, analytic_witness,
    analytic_witness_dephasing,
    analytic_witness_amplitude_damping, analytic_threshold_amplitude_damping,
)

p_vals = np.linspace(0.0, 1.0, 500)

K_dep = np.array([analytic_witness(p) for p in p_vals])
K_dph = np.array([analytic_witness_dephasing(p) for p in p_vals])
K_ad  = np.array([analytic_witness_amplitude_damping(p) for p in p_vals])

p_star_dep = analytic_threshold()
p_star_ad  = analytic_threshold_amplitude_damping()

print(f"Depolarizing threshold p*  : {p_star_dep:.6f}")
print(f"Dephasing threshold        : none (K = sqrt(5) for all p)")
print(f"Amplitude damping threshold: {p_star_ad:.6f}")
print(f"Ratio (dep / AD)           : {p_star_dep / p_star_ad:.4f}x")

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(p_vals, K_dep, color="#1f77b4", lw=2,       label=f"Depolarizing  (p* ≈ {p_star_dep:.4f})")
ax.plot(p_vals, K_dph, color="#2ca02c", lw=2,       label="Dephasing  (no threshold — fully robust)")
ax.plot(p_vals, K_ad,  color="#d62728", lw=2,       label=f"Amplitude damping  (p* ≈ {p_star_ad:.4f})")

ax.axhline(NC_BOUND,    color="black", lw=1.2, ls=":",  label="Noncontextual bound  K = 2")
ax.axvline(p_star_dep,  color="#1f77b4", lw=1,  ls="--", alpha=0.7)
ax.axvline(p_star_ad,   color="#d62728", lw=1,  ls="--", alpha=0.7)

ax.fill_between(p_vals, NC_BOUND, K_dep,
                where=(K_dep > NC_BOUND), alpha=0.08, color="#1f77b4")
ax.fill_between(p_vals, NC_BOUND, K_dph,
                where=(K_dph > NC_BOUND), alpha=0.08, color="#2ca02c")
ax.fill_between(p_vals, NC_BOUND, K_ad,
                where=(K_ad  > NC_BOUND), alpha=0.08, color="#d62728")

ax.set_xlim(0, 1)
ax.set_ylim(1.3, 2.4)
ax.set_xlabel("Noise parameter p", fontsize=12)
ax.set_ylabel("KCBS witness K(p)", fontsize=12)
ax.set_title(
    "KCBS contextuality under three noise channels — spin-1 qutrit\n"
    "Shaded region: quantum violation (K > 2)",
    fontsize=11,
)
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig("kcbs_three_channels.png", dpi=200)
print("Plot saved: kcbs_three_channels.png")
