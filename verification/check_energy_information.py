#!/usr/bin/env python3
"""Reproduce the channel identity and the two exact sharpness examples.

Run from any directory with Python 3 and NumPy. Success prints one JSON object.
Assertions fail with a nonzero exit code. Files are written only when --output
is explicitly supplied. Numerical checks supplement the analytic proofs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
N = np.diag([0, 1]).astype(complex)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual, expected, *, atol=3e-12, rtol=3e-11, label="check") -> float:
    actual, expected = np.asarray(actual), np.asarray(expected)
    error = float(np.max(np.abs(actual - expected)))
    scale = float(np.max(np.abs(expected))) if expected.size else 0.0
    require(error <= atol + rtol * scale,
            f"{label}: error {error:.6g}, allowed {atol + rtol * scale:.6g}")
    return error


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def embed(local: np.ndarray, sites: tuple[int, ...], n: int) -> np.ndarray:
    """Embed an operator whose tensor factors occur in the supplied site order."""
    require(len(set(sites)) == len(sites), "duplicate sites")
    require(local.shape == (2 ** len(sites),) * 2, "operator dimension")
    rest = tuple(j for j in range(n) if j not in sites)
    order = sites + rest
    inverse = np.argsort(order).tolist()
    matrix = np.kron(local, np.eye(2 ** len(rest)))
    axes = inverse + [j + n for j in inverse]
    return matrix.reshape((2,) * (2 * n)).transpose(axes).reshape((2**n,) * 2)


def one(local: np.ndarray, site: int, n: int) -> np.ndarray:
    return embed(local, (site,), n)


def partial_trace(rho: np.ndarray, keep: tuple[int, ...], n: int) -> np.ndarray:
    rest = tuple(j for j in range(n) if j not in keep)
    order = keep + rest
    axes = list(order) + [j + n for j in order]
    a = rho.reshape((2,) * (2 * n)).transpose(axes)
    dk, dr = 2 ** len(keep), 2 ** len(rest)
    return np.trace(a.reshape(dk, dr, dk, dr), axis1=1, axis2=3)


def expect(psi: np.ndarray, operator: np.ndarray) -> complex:
    return np.vdot(psi, operator @ psi)


def pure(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def trace_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh(hermitian(rho))
    require(values.min() > -2e-11, "state has negative spectrum")
    values = values[values > 1e-15]
    return float(-np.dot(values, np.log(values)))


def binary_entropy(x: float) -> float:
    return float(-sum(v * np.log(v) for v in (x, 1 - x) if v > 0))


def sqrt_psd(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(hermitian(matrix))
    require(values.min() >= -2e-12, "effect is not positive")
    return (vectors * np.sqrt(np.maximum(values, 0))) @ vectors.conj().T


def support(rho: np.ndarray) -> tuple[np.ndarray, float, int]:
    values, vectors = np.linalg.eigh(hermitian(rho))
    occupied = values > 1e-11
    projector = vectors[:, occupied] @ vectors[:, occupied].conj().T
    return projector, float(values[occupied].min()), int(occupied.sum())


def centered_norm(operator: np.ndarray) -> float:
    values = np.linalg.eigvalsh(hermitian(operator))
    return float((values[-1] - values[0]) / 2)


def unitary_from_generator(generator: np.ndarray, angle: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(hermitian(generator))
    return (vectors * np.exp(1j * angle * values)) @ vectors.conj().T


def random_channel(rng: np.random.Generator, d: int, rank: int) -> list[np.ndarray]:
    gaussian = rng.normal(size=(rank * d, d)) + 1j * rng.normal(size=(rank * d, d))
    isometry, _ = np.linalg.qr(gaussian, mode="reduced")
    return [isometry[j * d:(j + 1) * d] for j in range(rank)]


def random_povm(rng: np.random.Generator, d: int, count: int) -> list[np.ndarray]:
    positive = []
    for _ in range(count):
        g = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        positive.append(g.conj().T @ g)
    values, vectors = np.linalg.eigh(sum(positive))
    inv_sqrt = (vectors / np.sqrt(values)) @ vectors.conj().T
    effects = [hermitian(inv_sqrt @ a @ inv_sqrt) for a in positive]
    # Preserve completeness while deliberately producing a very rare outcome.
    old = effects[0].copy()
    effects[0] = 1e-9 * old
    effects[1] += (1 - 1e-9) * old
    close(sum(effects), np.eye(d), label="POVM completeness")
    return effects


def instrument_states(psi, effects, alice, n):
    states = []
    for effect in effects:
        measurement = embed(sqrt_psd(effect), alice, n)
        post_vector = measurement @ psi
        probability = float(np.vdot(post_vector, post_vector).real)
        if probability > 0:
            states.append((probability, pure(post_vector) / probability))
        else:
            states.append((0.0, None))
    close(sum(p for p, _ in states), 1, label="instrument probabilities")
    return states


def local_stiffness(H, psi, bob, n):
    """Use all matrix units, including maps out of the occupied support."""
    d = 2 ** len(bob)
    vectors = []
    for row in range(d):
        for column in range(d):
            matrix_unit = np.zeros((d, d), dtype=complex)
            matrix_unit[row, column] = 1
            vectors.append(embed(matrix_unit, bob, n) @ psi)
    vectors = np.column_stack(vectors)
    means = psi.conj() @ vectors
    covariance = hermitian(vectors.conj().T @ vectors - np.outer(means.conj(), means))
    cost = hermitian(vectors.conj().T @ H @ vectors)
    values, basis = np.linalg.eigh(covariance)
    occupied = values > 1e-11
    close(cost @ basis[:, ~occupied], 0, label="null-variance energy directions")
    whitening = basis[:, occupied] / np.sqrt(values[occupied])
    stiffness_matrix = hermitian(whitening.conj().T @ cost @ whitening)
    stiffness = float(np.linalg.eigvalsh(stiffness_matrix)[0])
    return stiffness, int(occupied.sum())


def check_channels(seed: int, trials: int) -> dict:
    rng = np.random.default_rng(seed)
    n, alice, bob, neighborhood = 5, (0, 1), (3, 4), (2, 3, 4)
    mu, penalty = 1 / np.sqrt(2), 1.9
    xs = [one(X, j, n) for j in range(n)]
    ys = [one(Y, j, n) for j in range(n)]
    ns = [one(N, j, n) for j in range(n)]
    Hphysical = mu * (ns[0] + ns[2] + ns[3]) + penalty * (ns[1] + ns[4])
    Hphysical -= (xs[0] @ xs[2] + ys[0] @ ys[2]
                  + xs[2] @ xs[3] + ys[2] @ ys[3]) / 2
    H = Hphysical + mu * np.eye(2**n)
    psi = np.zeros(2**n, dtype=complex)
    psi[16], psi[4], psi[2] = 0.5, 1 / np.sqrt(2), 0.5
    close(H @ psi, 0, label="rank-deficient example ground state")
    rho = pure(psi)
    omega_a = partial_trace(rho, alice, n)
    omega_b = partial_trace(rho, bob, n)
    omega_c = partial_trace(rho, neighborhood, n)
    pa, lambda_a, rank_a = support(omega_a)
    pb, lambda_b, rank_b = support(omega_b)
    require(rank_a == rank_b == 2, "test must have rank-deficient local marginals")
    close([lambda_a, lambda_b], [0.25, 0.25], label="support eigenvalues")
    pc = np.kron(I2, pb)
    hb = mu * one(N, 1, 3) + penalty * one(N, 2, 3)
    hb -= (one(X, 0, 3) @ one(X, 1, 3)
           + one(Y, 0, 3) @ one(Y, 1, 3)) / 2
    h = centered_norm(hb)
    stiffness, variance_rank = local_stiffness(H, psi, bob, n)
    energies, eigenvectors = np.linalg.eigh(H)
    excitation_energies = np.maximum(energies - energies[0], 0)
    gap = float(excitation_energies[1])
    require(stiffness >= gap - 2e-11, "gap does not certify computed stiffness")
    require(variance_rank == 7, "maps outside the rank-two support were omitted")

    g = hermitian(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
    g /= np.linalg.norm(g, 2)
    channels = []
    for angle in (0.2, 1e-4, 1e-6):
        channels.append((f"unitary_angle_{angle:g}", [unitary_from_generator(g, angle)]))
    for gamma in (1e-4, 1e-8):
        k0 = np.diag([1, np.sqrt(1 - gamma)])
        k1 = np.array([[0, np.sqrt(gamma)], [0, 0]])
        channels.append((f"amplitude_damping_{gamma:g}", [np.kron(k0, I2), np.kron(k1, I2)]))
    gamma = 1e-6
    k0 = np.diag([np.sqrt(1 - gamma), 1])
    k1 = np.array([[0, 0], [np.sqrt(gamma), 0]])
    channels.append(("weak_excitation_into_unoccupied_level", [np.kron(I2, k0), np.kron(I2, k1)]))
    u = random_channel(rng, 4, 1)[0]
    channels.append(("identity_on_support_only", [pb, u @ (np.eye(4) - pb)]))
    for j in range(trials):
        rank = (1, 2, 4, 6)[j % 4]
        channels.append((f"random_isometry_{j}_rank_{rank}", random_channel(rng, 4, rank)))

    max_identity_error = 0.0
    max_support_error = 0.0
    max_norm_ratio = 0.0
    minimum_probability = 1.0
    positive_gain_branches = 0
    nonzero_q2 = []
    rows = []
    for label, kraus in channels:
        close(sum(k.conj().T @ k for k in kraus), np.eye(4), label=f"{label} TP")
        means = [np.trace(omega_b @ k) for k in kraus]
        ws = [(k - a * np.eye(4)) @ pb for k, a in zip(kraus, means)]
        q2 = float(sum(np.trace(omega_b @ w.conj().T @ w).real for w in ws))
        close(q2, 1 - sum(abs(a)**2 for a in means), label=f"{label} q identity")
        if q2 > 1e-25:
            nonzero_q2.append(q2)
        w_stack = np.vstack(ws)
        require(np.linalg.norm(w_stack, 2) <= np.sqrt(max(q2, 0) / lambda_b) + 2e-12,
                f"{label}: support norm estimate")
        global_kraus = [embed(k, bob, n) for k in kraus]
        # Spectral evaluation avoids cancellation against the zero ground energy.
        cost = 0.0
        for k in global_kraus:
            amplitudes = eigenvectors.conj().T @ (k @ psi)
            cost += float(np.dot(excitation_energies, abs(amplitudes)**2))
        require(cost + 3e-12 >= stiffness * q2, f"{label}: local stiffness")
        local_kraus = [np.kron(I2, k) for k in kraus]
        local_ws = [np.kron(I2, w) for w in ws]
        representative = np.zeros((8, 8), dtype=complex)
        for k, w in zip(local_kraus, local_ws):
            representative += pc @ k.conj().T @ (hb @ w - w @ hb) @ pc
        close(np.trace(omega_c @ representative), cost, label=f"{label} unconditioned identity")
        norm_limit = 2 * h * np.sqrt(max(q2, 0) / lambda_b)
        representative_norm = float(np.linalg.norm(representative, 2))
        require(representative_norm <= norm_limit + 4e-12, f"{label}: response norm")
        norm_ratio = representative_norm / norm_limit if norm_limit > 1e-13 else 0.0
        max_norm_ratio = max(max_norm_ratio, norm_ratio)

        effects = random_povm(rng, 4, 5)
        states = instrument_states(psi, effects, alice, n)
        average_c = np.zeros((8, 8), dtype=complex)
        conditional_quadratic = 0.0
        average_entropy = 0.0
        max_case_error = 0.0
        for effect, (probability, conditional) in zip(effects, states):
            require(conditional is not None, "random POVM unexpectedly has null probability")
            minimum_probability = min(minimum_probability, probability)
            sigma = partial_trace(conditional, neighborhood, n)
            support_error = float(np.linalg.norm(sigma - pc @ sigma @ pc))
            max_support_error = max(max_support_error, support_error)
            close(sigma, pc @ sigma @ pc, label=f"{label}: conditional support")
            compressed_effect = pa @ effect @ pa
            require(probability + 2e-12 >= lambda_a * np.linalg.norm(compressed_effect, 2),
                    f"{label}: rare-branch effect estimate")
            output = sum(k @ conditional @ k.conj().T for k in global_kraus)
            direct_change = float(np.trace(H @ (output - conditional)).real)
            compressed_change = np.trace(sigma @ representative)
            error = close(compressed_change, direct_change,
                          label=f"{label}: conditioned total-energy identity")
            max_case_error = max(max_case_error, error)
            delta = sigma - omega_c
            close(cost + np.trace(delta @ representative), direct_change,
                  label=f"{label}: cost-response decomposition")
            positive_gain_branches += int(direct_change < -1e-10)
            average_c += probability * sigma
            conditional_quadratic += probability * trace_norm(delta)**2
            average_entropy += probability * entropy(sigma)
        close(average_c, omega_c, label=f"{label}: unconditioned neighborhood")
        mutual_information = entropy(omega_c) - average_entropy
        require(conditional_quadratic <= 2 * mutual_information + 3e-11,
                f"{label}: averaged Pinsker conversion")
        max_identity_error = max(max_identity_error, max_case_error)
        rows.append(dict(channel=label, q_squared=q2, ground_cost=cost,
                         response_norm_ratio=norm_ratio,
                         max_conditional_identity_error=max_case_error))

    require(minimum_probability < 1e-9, "rare-outcome test did not run")
    require(positive_gain_branches > 0, "stress set did not include an extracting branch")
    return dict(local_dimensions=dict(A=4, B=4, C=8),
                support_ranks=dict(A=rank_a, B=rank_b),
                support_eigenvalues=dict(A=lambda_a, B=lambda_b),
                all_operator_variance_rank=variance_rank, stiffness=stiffness,
                global_gap=gap, centered_energy_norm=h,
                channels_checked=len(channels), conditional_branches=5 * len(channels),
                minimum_outcome_probability=minimum_probability,
                minimum_nonzero_q_squared=min(nonzero_q2),
                positive_gain_branches=positive_gain_branches,
                maximum_conditional_identity_error=max_identity_error,
                maximum_support_error=max_support_error,
                maximum_response_norm_ratio=max_norm_ratio, channels=rows)


def check_three_qubit() -> dict:
    n = 3
    xs, ys, ns = ([one(a, j, n) for j in range(n)] for a in (X, Y, N))
    psi = np.zeros(8, dtype=complex)
    psi[4], psi[2], psi[1] = 0.5, 1 / np.sqrt(2), 0.5
    rho = pure(psi)
    omega_c = partial_trace(rho, (1, 2), n)
    rows = []
    max_energy_error = 0.0
    max_entropy_error = 0.0
    for coupling in (1.0, 2.3):
        mu = coupling / np.sqrt(2)
        H = mu * sum(ns) - coupling * (xs[0] @ xs[1] + ys[0] @ ys[1]
                                       + xs[1] @ xs[2] + ys[1] @ ys[2]) / 2
        hb = mu * ns[2] - coupling * (xs[1] @ xs[2] + ys[1] @ ys[2]) / 2
        expected_spectrum = sorted([0, 3 * mu, mu - np.sqrt(2) * coupling, mu,
                                    mu + np.sqrt(2) * coupling,
                                    2 * mu - np.sqrt(2) * coupling, 2 * mu,
                                    2 * mu + np.sqrt(2) * coupling])
        close(np.linalg.eigvalsh(H), expected_spectrum, label="three-qubit spectrum")
        close(H @ psi, -mu * psi, label="three-qubit ground state")
        close(centered_norm(hb), 3 * coupling / (2 * np.sqrt(2)), label="three-qubit local norm")
        for strength in (0.0, 1e-3, 0.02, 0.3, 0.8, 1.0):
            effects = [(I2 + sign * strength * X) / 2 for sign in (-1, 1)]
            states = instrument_states(psi, effects, (0,), n)
            cost = 3 * coupling / (2 * np.sqrt(2))
            signal = coupling * strength / (2 * np.sqrt(2))
            angle = -0.5 * np.arctan2(signal, cost)
            gain, entropy_average = 0.0, 0.0
            for sign, (probability, conditional) in zip((-1, 1), states):
                close(probability, 0.5, label="three-qubit outcome probability")
                sigma = partial_trace(conditional, (1, 2), n)
                radius = np.sqrt(0.25 + 0.75 * strength**2)
                expected_values = [0, 0, (1 - radius) / 2, (1 + radius) / 2]
                close(np.linalg.eigvalsh(sigma), expected_values,
                      label="three-qubit conditional spectrum")
                close(np.trace(conditional @ (ys[2] @ hb @ ys[2] - hb)), cost,
                      label="three-qubit rotation cost")
                close(1j * np.trace(conditional @ (hb @ ys[2] - ys[2] @ hb)), sign * signal,
                      label="three-qubit conditional force")
                u = np.cos(angle) * np.eye(8) + 1j * sign * np.sin(angle) * ys[2]
                gain += probability * np.trace(H @ (conditional - u @ conditional @ u.conj().T)).real
                entropy_average += probability * entropy(sigma)
            formula_gain = coupling * strength**2 / (4 * np.sqrt(2) * (np.sqrt(9 + strength**2) + 3))
            formula_information = binary_entropy(0.75) - binary_entropy(
                (1 + np.sqrt(0.25 + 0.75 * strength**2)) / 2)
            information = entropy(omega_c) - entropy_average
            max_energy_error = max(max_energy_error, close(gain, formula_gain, label="three-qubit exact gain"))
            max_entropy_error = max(max_entropy_error, close(information, formula_information,
                                                            label="three-qubit exact information"))
            if strength == 1e-3:
                ratio = formula_gain / formula_information
                expected_ratio = coupling / (9 * np.sqrt(2) * np.log(3))
                close(ratio, expected_ratio, atol=1e-8, rtol=2e-6, label="linear-information exponent")
            rows.append(dict(J=coupling, measurement_strength=strength,
                             extracted_energy=float(gain), mutual_information=float(information)))
    return dict(maximum_energy_formula_error=max_energy_error,
                maximum_information_formula_error=max_entropy_error,
                asymptotic_energy_over_information_at_J1=float(1 / (9 * np.sqrt(2) * np.log(3))),
                cases=rows)


def check_four_qubit() -> dict:
    n = 4
    xs, ys, zs = ([one(a, j, n) for j in range(n)] for a in (X, Y, Z))
    root5 = np.sqrt(5)
    k, normalization = root5 + 2, 10 + 4 * root5
    dimer = np.array([k, 0, 0, 1], dtype=complex) / np.sqrt(normalization)
    psi0 = np.kron(dimer, dimer)
    H0 = -sum(zs) - xs[0] @ xs[1] - xs[2] @ xs[3]
    hb = -zs[3] - xs[2] @ xs[3]
    source_operator = xs[1] @ xs[2]
    derivative = np.zeros(16, dtype=complex)
    odd_indices = [5, 6, 9, 10]
    derivative[odd_indices] = [1 / 8, (4 + 3 * root5) / 40, (-4 + 3 * root5) / 40, 1 / 8]
    close(H0 @ psi0, -2 * root5 * psi0, label="four-qubit dimer ground state")
    resolvent = (9 * np.eye(4) / (16 * root5)
                 + (np.kron(X, I2) + np.kron(I2, X)) / 16
                 + np.kron(X, X) / (16 * root5))
    odd_cost = 2 * root5 * np.eye(4) - np.kron(X, I2) - np.kron(I2, X)
    close(odd_cost @ resolvent, np.eye(4), label="exact odd-sector resolvent")
    close(resolvent @ np.array([k, k**2, 1, k]) / normalization,
          derivative[odd_indices], label="exact first-order ground vector")
    perturbation_residual = close((H0 + 2 * root5 * np.eye(16)) @ derivative,
                                  source_operator @ psi0, label="first-order eigenvector equation")
    close(np.vdot(psi0, derivative), 0, label="derivative normalization gauge")
    cost_operator = ys[3] @ hb @ ys[3] - hb
    signal_operator = 1j * xs[0] @ (hb @ ys[3] - ys[3] @ hb)
    curvature = float(expect(psi0, cost_operator).real)
    signal_derivative = float(2 * np.vdot(derivative, signal_operator @ psi0).real)
    correlation_derivative = float(2 * np.vdot(derivative, xs[0] @ xs[3] @ psi0).real)
    mixed_derivative = float(2 * np.vdot(derivative, xs[0] @ xs[2] @ zs[3] @ psi0).real)
    close(curvature, 6 / root5, label="four-qubit curvature")
    close(signal_derivative, 1 / (5 * root5), label="four-qubit force derivative")
    close(correlation_derivative, 3 / (5 * root5), label="four-qubit correlation derivative")
    close(mixed_derivative, 7 / (10 * root5), label="four-qubit mixed derivative")
    coefficient = signal_derivative**2 / (4 * curvature)
    close(coefficient, 1 / (600 * root5), label="four-qubit extraction coefficient")
    rows = []
    max_direct_error = 0.0
    for link in (0.1, 0.03, 0.01, 0.003):
        H = H0 - link * source_operator
        values, vectors = np.linalg.eigh(H)
        psi = vectors[:, 0]
        rho = pure(psi)
        cost = float(expect(psi, cost_operator).real)
        signal = float(expect(psi, signal_operator).real)
        angle = -0.5 * np.arctan2(signal, cost)
        states = instrument_states(psi, [(I2 - X) / 2, (I2 + X) / 2], (0,), n)
        gain = 0.0
        for sign, (probability, conditional) in zip((-1, 1), states):
            close(probability, 0.5, label="four-qubit outcome probability")
            close(np.trace(conditional @ cost_operator), cost, label="four-qubit conditional curvature")
            u = np.cos(angle) * np.eye(16) + 1j * sign * np.sin(angle) * ys[3]
            gain += probability * np.trace(H @ (conditional - u @ conditional @ u.conj().T)).real
        stable_gain = signal**2 / (2 * (np.hypot(cost, signal) + cost))
        max_direct_error = max(max_direct_error, close(gain, stable_gain, label="four-qubit direct feedback"))
        ac = partial_trace(rho, (0, 2, 3), n)
        a = partial_trace(rho, (0,), n)
        c = partial_trace(rho, (2, 3), n)
        correlation_upper = trace_norm(ac - np.kron(a, c))
        correlation_lower = abs(expect(psi, xs[0] @ xs[3]) - expect(psi, xs[0]) * expect(psi, xs[3]))
        require(correlation_lower <= correlation_upper + 2e-12, "correlation trace-norm comparison")
        bob_lambda = float(np.linalg.eigvalsh(partial_trace(rho, (3,), n))[0])
        require(bob_lambda > 0.04, "weak-link local conditioning deteriorates")
        require(values[1] - values[0] >= root5 - 1 - 2 * link - 2e-12, "weak-link gap estimate")
        rows.append(dict(link=link, gap=float(values[1] - values[0]), lambda_b=bob_lambda,
                         energy_over_link_squared=float(stable_gain / link**2),
                         correlation_lower_over_link=float(correlation_lower / link),
                         correlation_upper_over_link=float(correlation_upper / link)))
    close(rows[-1]["energy_over_link_squared"], coefficient,
          atol=1e-10, rtol=3e-5, label="weak-link extraction asymptotic")
    close(rows[-1]["correlation_lower_over_link"], 3 / (5 * root5),
          atol=1e-10, rtol=3e-5, label="weak-link correlation asymptotic")
    return dict(first_order_equation_residual=perturbation_residual,
                maximum_direct_energy_error=max_direct_error, curvature_at_zero=curvature,
                force_derivative=signal_derivative, xx_correlation_derivative=correlation_derivative,
                extraction_coefficient=coefficient, cases=rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261028)
    parser.add_argument("--trials", type=int, default=12,
                        help="number of random isometry channels, in addition to fixed stress cases")
    parser.add_argument("--output", type=Path, help="optional path for the same JSON printed to stdout")
    args = parser.parse_args()
    require(args.trials >= 1, "--trials must be positive")
    result = dict(ok=True, status="passed", seed=args.seed, numpy_version=np.__version__,
                  channel_support_identity=check_channels(args.seed, args.trials),
                  three_qubit_information=check_three_qubit(),
                  four_qubit_correlations=check_four_qubit())
    encoded = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
