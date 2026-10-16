"""KCBS contextuality baseline for a qutrit.

Scenario: five rank-one projectors on C^3, adjacent pairs orthogonal.
Witness:  K = sum_i Tr(rho P_i)
Noncontextual bound: K <= 2  (KCBS assumptions)
Quantum maximum: K = sqrt(5) ~ 2.2361  (ideal state, no noise)

References
----------
Klyachko et al., PRL 101, 020403 (2008). DOI: 10.1103/PhysRevLett.101.020403
Budroni et al., Rev. Mod. Phys. 94, 045007 (2022). DOI: 10.1103/RevModPhys.94.045007
"""

import numpy as np

DIM = 3
N_PROJ = 5
NC_BOUND = 2.0


def kcbs_projectors() -> list[np.ndarray]:
    """Five symmetric rank-one KCBS projectors on C^3.

    Vectors lie on a cone: polar angle theta satisfies cos^2(theta) = 1/sqrt(5).
    Azimuthal angles are evenly spaced at 4*pi*i/5.
    Adjacent vectors are orthogonal by construction.
    """
    cos_t = 5.0 ** (-0.25)
    sin_t = np.sqrt(1.0 - cos_t ** 2)

    projectors = []
    for i in range(N_PROJ):
        phi = 4.0 * np.pi * i / N_PROJ
        v = np.array([sin_t * np.cos(phi), sin_t * np.sin(phi), cos_t])
        v /= np.linalg.norm(v)
        projectors.append(np.outer(v, v))
    return projectors


def ideal_state() -> np.ndarray:
    """Optimal pure qutrit state |2><2| (north pole of the cone)."""
    v = np.array([0.0, 0.0, 1.0])
    return np.outer(v, v)


def depolarize(rho: np.ndarray, p: float) -> np.ndarray:
    """State depolarization: rho -> (1-p)*rho + p*I/3.

    p=0: identity channel.  p=1: maximally mixed state.
    Note: this models noise on the state, not on the measurements.
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (DIM, DIM):
        raise ValueError(f"rho must be {DIM}x{DIM}")
    return (1.0 - p) * rho + p * np.eye(DIM, dtype=complex) / DIM


def witness(rho: np.ndarray) -> float:
    """K = sum_i Tr(rho P_i)."""
    val = sum(np.trace(rho @ P).real for P in kcbs_projectors())
    return float(val)


def analytic_witness(p: float) -> float:
    """Closed-form K(p) for the ideal state under depolarization.

    Derived by linearity of the trace:
        K(p) = (1-p)*sqrt(5) + p*(5/3)
    The p*(5/3) term comes from Tr(I/3 * P_i) = 1/3 for each rank-1 projector,
    summed over five projectors.
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    return (1.0 - p) * np.sqrt(5.0) + p * (5.0 / 3.0)


def dephase(rho: np.ndarray, p: float) -> np.ndarray:
    """Qutrit dephasing channel: kills off-diagonal elements by factor (1-p).

    rho(p)_ij = rho_ij        if i == j
    rho(p)_ij = (1-p)*rho_ij  if i != j

    p=0: identity channel.  p=1: fully dephased (diagonal state).
    Note: this models noise on the state, not on the measurements.
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (DIM, DIM):
        raise ValueError(f"rho must be {DIM}x{DIM}")
    mask = np.ones((DIM, DIM), dtype=complex) * (1.0 - p)
    np.fill_diagonal(mask, 1.0)
    return rho * mask


def analytic_witness_dephasing(p: float) -> float:
    """Closed-form K(p) for the ideal state under dephasing.

    Lemma: K(p) = sqrt(5) for all p in [0, 1].

    Proof: The ideal state rho = |2><2| is diagonal in the standard basis
    (all off-diagonal elements are zero). Dephasing only scales off-diagonal
    elements by (1-p), so rho(p) = rho for all p. Therefore
    K(p) = witness(rho(p)) = witness(rho) = sqrt(5) for all p.
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    return float(np.sqrt(5.0))


def amplitude_damp(rho: np.ndarray, p: float) -> np.ndarray:
    """Qutrit full-cascade amplitude damping channel.

    Models energy decay |2> -> |1> -> |0> with equal decay probability p
    per level. Four Kraus operators derived from the binomial cascade:

        K0 = diag(1, sqrt(1-p), (1-p))          no decay
        K1 = sqrt(p)   |0><1|                    |1> -> |0> jump
        K2 = sqrt(2p(1-p)) |1><2|               |2> -> |1> jump
        K3 = p |0><2|                            |2> -> |1> -> |0> two-step

    Completeness: sum_k K_k^dag K_k = I (verified analytically via
    binomial identity (1-p)^2 + 2p(1-p) + p^2 = 1).

    p=0: identity channel.  p=1: full decay to ground state |0>.
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (DIM, DIM):
        raise ValueError(f"rho must be {DIM}x{DIM}")
    K0 = np.diag([1.0, np.sqrt(1 - p), (1 - p)]).astype(complex)
    K1 = np.zeros((DIM, DIM), dtype=complex); K1[0, 1] = np.sqrt(p)
    K2 = np.zeros((DIM, DIM), dtype=complex); K2[1, 2] = np.sqrt(2 * p * (1 - p))
    K3 = np.zeros((DIM, DIM), dtype=complex); K3[0, 2] = p
    return sum(K @ rho @ K.conj().T for K in [K0, K1, K2, K3])


def analytic_witness_amplitude_damping(p: float) -> float:
    """Closed-form K(p) for the ideal state under full-cascade amplitude damping.

    Derived by substituting rho(p) = p^2|0><0| + 2p(1-p)|1><1| + (1-p)^2|2><2|
    into K = sum_i Tr(rho(p) P_i) and using:
        sum_i |v_i[0]|^2 = sum_i |v_i[1]|^2 = sin^2(theta) * 5/2 = 5/2 - sqrt(5)/2
        sum_i |v_i[2]|^2 = 5 * cos^2(theta) = sqrt(5)

    Result:
        K(p) = A * p*(2-p) + sqrt(5) * (1-p)^2
        where A = 5/2 - sqrt(5)/2
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p must be in [0, 1], got {p}")
    A = 2.5 - np.sqrt(5.0) / 2.0
    return A * p * (2.0 - p) + np.sqrt(5.0) * (1.0 - p) ** 2


def analytic_threshold_amplitude_damping() -> float:
    """Solve analytic_witness_amplitude_damping(p) = NC_BOUND = 2 for p.

    Quadratic (B-A)*p^2 - 2*(B-A)*p + (B-2) = 0
    where A = 5/2 - sqrt(5)/2, B = sqrt(5), C = B - A = 3*sqrt(5)/2 - 5/2.

    Closed form: p* = 1 - sqrt((sqrt(5)-1) / (3*sqrt(5)-5)) ~ 0.1493
    """
    return 1.0 - np.sqrt((np.sqrt(5.0) - 1.0) / (3.0 * np.sqrt(5.0) - 5.0))


def analytic_threshold() -> float:
    """Solve analytic_witness(p) = NC_BOUND = 2 for p.

    p* = (sqrt(5) - 2) / (sqrt(5) - 5/3)
    """
    return (np.sqrt(5.0) - 2.0) / (np.sqrt(5.0) - 5.0 / 3.0)
