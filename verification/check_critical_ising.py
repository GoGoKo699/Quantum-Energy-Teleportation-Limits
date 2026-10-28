#!/usr/bin/env python3
"""Check the exact finite-ring local-stiffness formulas using only NumPy.

Run from any directory with Python 3 and NumPy installed. The script performs
no file writes, prints one JSON object to stdout, and returns nonzero if a
validation fails. All systems and parameters are fixed; no randomness is used.
"""

from __future__ import annotations

import json
import platform
import sys

import numpy as np


TOLERANCE = 2.0e-10
SIZES = (4, 5, 6, 8)


def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def close(actual: np.ndarray | float, expected: np.ndarray | float,
          description: str, tolerance: float = TOLERANCE) -> float:
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    require(error <= tolerance, f"{description}: error {error:.6g} > {tolerance}")
    return error


def pauli_action(vector: np.ndarray, site: int, axis: str) -> np.ndarray:
    """Apply a Pauli matrix with site 0 the least significant basis bit."""
    labels = np.arange(vector.size, dtype=np.int64)
    z_sign = 1 - 2 * ((labels >> site) & 1)
    if axis == "z":
        return z_sign * vector
    flipped = labels ^ (1 << site)
    result = np.empty(vector.shape, dtype=np.complex128)
    if axis == "x":
        result[flipped] = vector
    elif axis == "y":
        result[flipped] = 1j * z_sign * vector
    else:
        raise ValueError(f"Unknown Pauli axis: {axis}")
    return result


def ising_hamiltonian(size: int) -> np.ndarray:
    """Periodic critical Ising Hamiltonian, with J = h = 1."""
    dimension = 1 << size
    labels = np.arange(dimension, dtype=np.int64)
    hamiltonian = np.zeros((dimension, dimension), dtype=np.float64)
    diagonal = np.zeros(dimension, dtype=np.float64)
    for site in range(size):
        diagonal -= 1 - 2 * ((labels >> site) & 1)
        flipped = labels ^ (1 << site) ^ (1 << ((site + 1) % size))
        hamiltonian[flipped, labels] -= 1.0
    hamiltonian[labels, labels] += diagonal
    return hamiltonian


def generalized_spectrum(cost: np.ndarray, covariance: np.ndarray) -> np.ndarray:
    """Quotient only the covariance kernel, retaining zero cost eigenvalues."""
    values, vectors = np.linalg.eigh(covariance)
    require(float(values[0]) >= -TOLERANCE, "Covariance is not positive")
    active = values > TOLERANCE
    if np.any(~active):
        close(cost @ vectors[:, ~active], 0.0, "Cost on covariance kernel")
    require(bool(np.any(active)), "No nonzero-variance local operator")
    whitening = vectors[:, active] / np.sqrt(values[active])[None, :]
    whitened_cost = whitening.conj().T @ cost @ whitening
    close(whitened_cost, whitened_cost.conj().T, "Whitened cost Hermiticity")
    return np.linalg.eigvalsh(whitened_cost)


def expected_forms(magnetization: float) -> tuple[np.ndarray, np.ndarray]:
    m = magnetization
    covariance = np.array([
        [1.0, 1j * m, 0.0],
        [-1j * m, 1.0, 0.0],
        [0.0, 0.0, 1.0 - m * m],
    ], dtype=np.complex128)
    cost = np.array([
        [2.0 * m, 2j, 0.0],
        [-2j, 6.0 * m, 0.0],
        [0.0, 0.0, 4.0 * m],
    ], dtype=np.complex128)
    return covariance, cost


def expected_stiffness_spectrum(magnetization: float) -> np.ndarray:
    m = magnetization
    discriminant = np.sqrt(1.0 - 3.0 * m * m + 3.0 * m**4)
    denominator = 1.0 - m * m
    return np.sort(np.array([
        2.0 * (m - discriminant) / denominator,
        2.0 * (m + discriminant) / denominator,
        4.0 * m / denominator,
    ], dtype=np.float64))


def check_ring(size: int, limiting_stiffness: float) -> dict:
    hamiltonian = ising_hamiltonian(size)
    energies, vectors = np.linalg.eigh(hamiltonian)
    ground = vectors[:, 0].astype(np.complex128)
    energy = float(energies[0])
    gap = float(energies[1] - energies[0])
    shifted = hamiltonian - energy * np.eye(1 << size)

    x = np.pi / (2.0 * size)
    m = float(1.0 / (size * np.sin(x)))
    expected_energy = float(-2.0 / np.sin(x))
    expected_gap = float(2.0 * np.tan(x / 2.0))
    energy_error = close(energy, expected_energy, f"N={size} ground energy")
    gap_error = close(gap, expected_gap, f"N={size} global gap")
    require(gap > TOLERANCE, f"N={size} ground state is not unique")

    labels = np.arange(1 << size, dtype=np.int64)
    parity_sign = np.ones(1 << size, dtype=np.int64)
    for site in range(size):
        parity_sign *= 1 - 2 * ((labels >> site) & 1)
    parity = np.vdot(ground, parity_sign * ground)
    close(parity, 1.0, f"N={size} even ground-state parity")
    first_excited = vectors[:, 1].astype(np.complex128)
    first_excited_parity = np.vdot(first_excited, parity_sign * first_excited)
    close(first_excited_parity, -1.0, f"N={size} odd first-excited parity")
    close(float(energies[1]), -2.0 / np.tan(x),
          f"N={size} lowest odd-sector energy")

    local_vectors = np.column_stack([
        pauli_action(ground, 0, axis) for axis in ("x", "y", "z")
    ])
    means = ground.conj() @ local_vectors
    close(means, np.array([0.0, 0.0, m]), f"N={size} Pauli means")
    xx_ground = pauli_action(pauli_action(ground, 1, "x"), 0, "x")
    bond = np.vdot(ground, xx_ground)
    close(bond, m, f"N={size} neighboring XX mean")

    covariance = local_vectors.conj().T @ local_vectors - np.outer(
        means.conj(), means
    )
    cost = local_vectors.conj().T @ shifted @ local_vectors
    expected_covariance, expected_cost = expected_forms(m)
    covariance_error = close(
        covariance, expected_covariance, f"N={size} covariance form"
    )
    cost_error = close(cost, expected_cost, f"N={size} excitation form")
    spectrum = generalized_spectrum(cost, covariance)
    expected_spectrum = expected_stiffness_spectrum(m)
    spectrum_error = close(
        spectrum, expected_spectrum, f"N={size} generalized eigenvalues"
    )

    # Environment labels index rows and the least significant Bob bit columns.
    reshaped_ground = ground.reshape((-1, 2))
    bob_state = reshaped_ground.T @ reshaped_ground.conj()
    bob_spectrum = np.linalg.eigvalsh(bob_state)
    expected_bob_spectrum = np.array([(1.0 - m) / 2.0, (1.0 + m) / 2.0])
    close(bob_spectrum, expected_bob_spectrum, f"N={size} Bob spectrum")

    uniform_slack = cost - limiting_stiffness * covariance
    uniform_slack_min = float(np.linalg.eigvalsh(uniform_slack)[0])
    require(uniform_slack_min >= -TOLERANCE,
            f"N={size} uniform stiffness inequality")
    require(float(spectrum[0]) >= limiting_stiffness - TOLERANCE,
            f"N={size} stiffness below thermodynamic lower bound")

    return {
        "N": size,
        "ground_energy_over_J": energy,
        "gap_over_J": gap,
        "gap_formula_over_J": expected_gap,
        "ground_parity": float(parity.real),
        "first_excited_parity": float(first_excited_parity.real),
        "magnetization_formula": m,
        "lambda_B": float(bob_spectrum[0]),
        "kappa_over_J": float(spectrum[0]),
        "kappa_formula_over_J": float(expected_spectrum[0]),
        "unitary_only_kappa_over_J": 2.0 * m,
        "generalized_spectrum_over_J": spectrum.tolist(),
        "minimum_uniform_slack_eigenvalue_over_J": uniform_slack_min,
        "maximum_absolute_errors": {
            "ground_energy": energy_error,
            "global_gap": gap_error,
            "covariance_form": covariance_error,
            "excitation_form": cost_error,
            "generalized_spectrum": spectrum_error,
        },
    }


def check_local_norm() -> float:
    labels = np.arange(8, dtype=np.int64)
    local_energy = np.zeros((8, 8), dtype=np.float64)
    local_energy[labels, labels] = -(1 - 2 * ((labels >> 1) & 1))
    for left, right in ((0, 1), (1, 2)):
        local_energy[labels ^ (1 << left) ^ (1 << right), labels] -= 1.0
    norm = float(np.max(np.abs(np.linalg.eigvalsh(local_energy))))
    close(norm, np.sqrt(5.0), "Three-site local energy norm")
    return norm


def run_checks() -> dict:
    limiting_m = 2.0 / np.pi
    limiting_spectrum = expected_stiffness_spectrum(limiting_m)
    limiting_stiffness = float(limiting_spectrum[0])
    limiting_lambda = (1.0 - limiting_m) / 2.0
    m4 = 1.0 / (4.0 * np.sin(np.pi / 8.0))
    uniform_lambda = (1.0 - m4) / 2.0
    require(limiting_stiffness > 0.0, "Limiting stiffness is not positive")
    require(uniform_lambda > 0.0, "Uniform local conditioning is not positive")
    rings = [check_ring(size, limiting_stiffness) for size in SIZES]
    local_norm = check_local_norm()
    return {
        "ok": True,
        "check": "critical_ising_local_stiffness",
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "absolute_tolerance": TOLERANCE,
        "coupling_J": 1.0,
        "rings": rings,
        "thermodynamic_constants": {
            "magnetization": limiting_m,
            "kappa_over_J": limiting_stiffness,
            "generalized_spectrum_over_J": limiting_spectrum.tolist(),
            "lambda_B": limiting_lambda,
            "h_B_over_J": local_norm,
            "energy_information_coefficient_over_J": (
                2.0 * local_norm**2 / (limiting_stiffness * limiting_lambda)
            ),
        },
        "uniform_constants_for_all_N_at_least_4": {
            "kappa_lower_bound_over_J": limiting_stiffness,
            "lambda_B_lower_bound": uniform_lambda,
            "h_B_over_J": local_norm,
        },
        "scope": (
            "Finite checks validate normalization and parity conventions. "
            "The all-N stiffness bound is proved analytically in "
            "science/local_stiffness.md. No critical spatial exponent is tested."
        ),
    }


def main() -> int:
    try:
        report = run_checks()
        exit_code = 0
    except Exception as error:
        report = {
            "ok": False,
            "check": "critical_ising_local_stiffness",
            "error_type": type(error).__name__,
            "error": str(error),
        }
        exit_code = 1
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
