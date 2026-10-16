"""Tests for the KCBS contextuality baseline.

Each test checks a mathematical property that must hold by definition.
Failures indicate either a coding error or a violated assumption — investigate
before changing expected values.
"""

import numpy as np
import pytest

from contextuality import (
    DIM, NC_BOUND,
    analytic_threshold, analytic_witness, analytic_witness_dephasing,
    analytic_witness_amplitude_damping, analytic_threshold_amplitude_damping,
    amplitude_damp, depolarize, dephase, ideal_state, kcbs_projectors, witness,
)


# --- projector geometry ---

def test_projectors_hermitian_idempotent_rank_one():
    for P in kcbs_projectors():
        assert np.allclose(P, P.conj().T), "not Hermitian"
        assert np.allclose(P @ P, P), "not idempotent"
        assert np.isclose(np.trace(P), 1.0), "trace != 1"


def test_adjacent_projectors_orthogonal():
    projs = kcbs_projectors()
    for i in range(5):
        j = (i + 1) % 5
        assert np.allclose(projs[i] @ projs[j], np.zeros((DIM, DIM)), atol=1e-10), \
            f"P_{i} and P_{j} are not orthogonal"


# --- state validity ---

def test_ideal_state_is_valid_density_matrix():
    rho = ideal_state()
    assert np.allclose(rho, rho.conj().T)
    assert np.isclose(np.trace(rho), 1.0)
    assert np.linalg.eigvalsh(rho).min() >= -1e-10


# --- quantum benchmark ---

def test_ideal_witness_equals_sqrt5():
    assert np.isclose(witness(ideal_state()), np.sqrt(5.0), atol=1e-10)


# --- depolarizing channel ---

@pytest.mark.parametrize("p", [0.0, 0.25, 0.5, 0.75, 1.0])
def test_depolarized_state_is_valid(p):
    noisy = depolarize(ideal_state(), p)
    assert np.isclose(np.trace(noisy), 1.0)
    assert np.allclose(noisy, noisy.conj().T)
    assert np.linalg.eigvalsh(noisy).min() >= -1e-10


def test_depolarize_rejects_invalid_p():
    with pytest.raises(ValueError):
        depolarize(ideal_state(), -0.1)
    with pytest.raises(ValueError):
        depolarize(ideal_state(), 1.1)


# --- numerical vs analytic agreement ---

@pytest.mark.parametrize("p", np.linspace(0.0, 1.0, 11))
def test_numerical_matches_analytic(p):
    numerical = witness(depolarize(ideal_state(), p))
    assert np.isclose(numerical, analytic_witness(p), atol=1e-10), \
        f"mismatch at p={p:.2f}: numerical={numerical}, analytic={analytic_witness(p)}"


# --- dephasing channel ---

@pytest.mark.parametrize("p", [0.0, 0.25, 0.5, 0.75, 1.0])
def test_dephased_state_is_valid(p):
    noisy = dephase(ideal_state(), p)
    assert np.isclose(np.trace(noisy), 1.0)
    assert np.allclose(noisy, noisy.conj().T)
    assert np.linalg.eigvalsh(noisy).min() >= -1e-10


def test_dephase_rejects_invalid_p():
    with pytest.raises(ValueError):
        dephase(ideal_state(), -0.1)
    with pytest.raises(ValueError):
        dephase(ideal_state(), 1.1)


def test_dephase_ideal_state_unchanged():
    """Ideal state is diagonal — dephasing must leave it identical."""
    rho = ideal_state()
    for p in [0.0, 0.5, 1.0]:
        assert np.allclose(dephase(rho, p), rho), f"state changed at p={p}"


@pytest.mark.parametrize("p", np.linspace(0.0, 1.0, 11))
def test_dephasing_witness_constant_sqrt5(p):
    """Lemma: K(p) = sqrt(5) for all p under dephasing on the ideal state."""
    numerical = witness(dephase(ideal_state(), p))
    assert np.isclose(numerical, np.sqrt(5.0), atol=1e-10)
    assert np.isclose(numerical, analytic_witness_dephasing(p), atol=1e-10)


def test_dephasing_no_threshold():
    """K(p) never crosses the noncontextual bound under dephasing on ideal state."""
    for p in np.linspace(0.0, 1.0, 100):
        assert analytic_witness_dephasing(p) > NC_BOUND


# --- amplitude damping channel ---

@pytest.mark.parametrize("p", [0.0, 0.25, 0.5, 0.75, 1.0])
def test_amplitude_damped_state_is_valid(p):
    noisy = amplitude_damp(ideal_state(), p)
    assert np.isclose(np.trace(noisy), 1.0)
    assert np.allclose(noisy, noisy.conj().T)
    assert np.linalg.eigvalsh(noisy).min() >= -1e-10


def test_amplitude_damp_rejects_invalid_p():
    with pytest.raises(ValueError):
        amplitude_damp(ideal_state(), -0.1)
    with pytest.raises(ValueError):
        amplitude_damp(ideal_state(), 1.1)


def test_amplitude_damp_p0_is_identity():
    rho = ideal_state()
    assert np.allclose(amplitude_damp(rho, 0.0), rho)


def test_amplitude_damp_p1_is_ground_state():
    """Full decay: all population ends in |0><0|."""
    rho_p1 = amplitude_damp(ideal_state(), 1.0)
    ground = np.zeros((DIM, DIM), dtype=complex)
    ground[0, 0] = 1.0
    assert np.allclose(rho_p1, ground)


def test_amplitude_damp_kraus_completeness():
    """sum_k K_k^dag K_k = I for all p."""
    for p in np.linspace(0.0, 1.0, 11):
        K0 = np.diag([1.0, np.sqrt(1-p), (1-p)]).astype(complex)
        K1 = np.zeros((DIM, DIM), dtype=complex); K1[0, 1] = np.sqrt(p)
        K2 = np.zeros((DIM, DIM), dtype=complex); K2[1, 2] = np.sqrt(2*p*(1-p))
        K3 = np.zeros((DIM, DIM), dtype=complex); K3[0, 2] = p
        total = sum(K.conj().T @ K for K in [K0, K1, K2, K3])
        assert np.allclose(total, np.eye(DIM)), f"completeness fails at p={p:.2f}"


@pytest.mark.parametrize("p", np.linspace(0.0, 1.0, 11))
def test_amplitude_damping_numerical_matches_analytic(p):
    numerical = witness(amplitude_damp(ideal_state(), p))
    assert np.isclose(numerical, analytic_witness_amplitude_damping(p), atol=1e-10)


def test_amplitude_damping_threshold_at_nc_bound():
    p_star = analytic_threshold_amplitude_damping()
    assert np.isclose(analytic_witness_amplitude_damping(p_star), NC_BOUND, atol=1e-10)


def test_amplitude_damping_threshold_separates_violation():
    p_star = analytic_threshold_amplitude_damping()
    assert analytic_witness_amplitude_damping(p_star - 0.01) > NC_BOUND
    assert analytic_witness_amplitude_damping(p_star + 0.01) < NC_BOUND


def test_amplitude_damping_threshold_less_than_depolarizing():
    """Amplitude damping destroys contextuality ~3x faster than depolarization."""
    assert analytic_threshold_amplitude_damping() < analytic_threshold()


# --- depolarizing threshold ---

def test_threshold_is_at_nc_bound():
    p_star = analytic_threshold()
    assert np.isclose(analytic_witness(p_star), NC_BOUND, atol=1e-10)


def test_threshold_separates_violation_from_no_violation():
    p_star = analytic_threshold()
    assert analytic_witness(p_star - 0.01) > NC_BOUND
    assert analytic_witness(p_star + 0.01) < NC_BOUND
