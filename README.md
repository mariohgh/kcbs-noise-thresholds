# Quantum Contextuality Lab

Reproducible study of quantum contextuality under noise.
Current status: **baseline reproduction only — no novelty claimed.**

## Mathematical model

**System**: Qutrit (C^3), five rank-one projectors P_0,...,P_4.

**KCBS witness**: K = Σ_i Tr(ρ P_i)

**Noncontextual bound**: K ≤ 2  (under KCBS assumptions)

**Quantum maximum**: K = √5 ≈ 2.2361  (ideal state, no noise)

**Noise model** (state depolarization):
  ρ(p) = (1−p)ρ + p·I/3,   p ∈ [0,1]

**Analytic witness**: K(p) = (1−p)√5 + p·(5/3)

**Noise threshold**: p* = (√5 − 2) / (√5 − 5/3) ≈ 0.4146

This models noise acting on the quantum state, not on the measurements.
These are different physical situations with potentially different consequences
for contextuality — the distinction must be explicit in any paper.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```bash
python -m pytest -v                # run all tests
python run_baseline.py             # reproduce baseline + save plot
```

## Files

| File | Purpose |
|---|---|
| `contextuality.py` | Core math: projectors, channel, witness |
| `test_contextuality.py` | Automated tests for all mathematical properties |
| `run_baseline.py` | Reproduce baseline plot and print key values |
| `literature.md` | Annotated bibliography and novelty ledger |
| `requirements.txt` | Pinned dependencies |

## References

1. Klyachko et al., *PRL* **101**, 020403 (2008). https://doi.org/10.1103/PhysRevLett.101.020403
2. Budroni et al., *Rev. Mod. Phys.* **94**, 045007 (2022). https://doi.org/10.1103/RevModPhys.94.045007
