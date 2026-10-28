# Reproduce the finite scientific checks

The analytical claims are proved in the [scientific account](../science/model.md). The checks here reconstruct finite Hamiltonians and operations independently of the shortened formulas, then compare the resulting energies, states and spectra. They address support, channel, normalization and boundary-condition errors.

## Run the checks

The recorded run used Python 3.12.14 and NumPy 2.3.5. Install the pinned numerical dependency and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner prints a JSON object with an overall `ok` field and returns a nonzero exit code if either check fails. It does not write files unless an output path is supplied:

```bash
python3 verification/run_all.py --output verification/actual/research_checks.json
```

[The recorded output](expected/research_checks.json) is a reference run. Reproduction is judged by the scripts' numerical tolerances and analytical comparisons, not by byte-for-byte equality of floating-point output or version strings. The ignored `actual/` directory is available for local runs.

## What is checked

### Energy-information theorem and exact examples

```bash
python3 verification/check_energy_information.py
```

The script has three parts.

**Support and channel identity.** A five-qubit Hamiltonian contains the three-site XX ground state together with two frozen spectator qubits. Alice and Bob each control a four-dimensional local space with a rank-two ground-state marginal. The script constructs complete local instruments, including a deliberately rare outcome, and checks conditional energy changes directly from the global state.

The feedback cases include small-angle unitaries, weak amplitude damping, excitation into an unoccupied local level, maps acting nontrivially only outside the occupied support, and seeded random isometries of different Kraus ranks. These cases check the load-bearing small-disturbance regime as well as genuinely nonunitary maps. The script compares the direct energy change with the support-compressed observable, checks the branch reference cost and response norm estimate, and verifies the averaged Pinsker inequality. The written proof combines these ingredients into the final energy bound.

**Three-qubit sharpness.** Direct diagonalization checks the ground state, gap, local spectrum and centered energy norm. Explicit instruments and feedback matrices check the energy and entropy formulas for multiple measurement strengths and two energy scales.

**Four-qubit sharpness.** The first-order source, exact resolvent and state derivative are checked algebraically as finite matrices. Direct diagonalization and feedback check the small-link energy coefficient and upper/lower correlation estimates. The asymptotic claim is established by analytic perturbation theory in [Sharpness](../science/sharpness.md), not by fitting these points.

The default seed is `20261028`. The optional parameters are `--seed`, `--trials` for the number of random-isometry cases, and `--output PATH`. The default run checks 19 channels and 95 conditioned branches. Its largest direct/compressed energy-identity discrepancy was below $9\times10^{-16}$; it included nonzero disturbance $q^2$ near $4.6\times10^{-13}$ and an outcome probability near $7.5\times10^{-11}$.

### Critical Ising stiffness

```bash
python3 verification/check_critical_ising.py
```

Dense Hamiltonians for rings of sizes $N=4,5,6,8$ are diagonalized. Including odd $N$ checks the fermion-parity boundary convention. The calculation checks the ground and first-excited parities, ground energy, global gap, one-site marginal, neighboring correlator, full complex local covariance and energy forms, generalized eigenvalues, centered local norm, and uniform stiffness matrix inequality.

The largest formula discrepancy in the recorded run was below $7\times10^{-15}$. The positive stiffness for every $N\ge4$ and the thermodynamic limit follow from the determinant argument and exact expressions in [Local excitation stiffness](../science/local_stiffness.md). The finite sample does not establish those limits.

## Reproduce the figure

The optional plot dependency is separate from the NumPy-only verification suite:

```bash
python3 -m pip install -r verification/plot_requirements.txt
python3 verification/plot_critical_stiffness.py
```

This writes [critical_stiffness.svg](../figures/critical_stiffness.svg). The generator imports the stiffness spectrum from the verified critical-chain implementation and evaluates the exact finite-ring gap. It uses no fit or extrapolated simulation data.

A raster preview can be generated for inspection:

```bash
python3 verification/plot_critical_stiffness.py --preview verification/actual/critical_stiffness.png
```

The committed figure was visually inspected through such a preview. A plot of the exact local coefficient does not establish an optimal QET spatial-decay exponent.

## Evidence boundaries

The checks diagnose finite implementation and algebra errors. The universal CPTP theorem, the support-conditioning argument, the sharp powers, and the uniform critical-family result depend on the written proofs. Agreement at small sizes is not external peer review or a substitute for those proofs.

The repository does not infer a complete controller-work balance, a finite-delay transport theorem, a continuum statement, or an optimal distance exponent from the numerical checks.
