# Information, local energy cost, and the physical limit

The [main theorem](energy_information.md) relates two changes caused by feedback. A channel that acts nontrivially on the ground state has an unconditional energetic cost. Conditioning that channel on Alice's record can offset the cost, but the useful local response becomes small with the disturbance. Keeping both terms is what produces the quadratic law.

## Why the useful response is second order

For one feedback branch, let $q^2$ measure the loss of entanglement fidelity when the same channel is applied to the unmeasured ground state. Local stiffness implies a reference energy cost of at least $\kappa_B q^2$. The support-aware proof bounds the change in the response caused by a conditional neighborhood state by

```math
\frac{2h_B}{\sqrt{\lambda_B}}\,
q\left\lVert \rho_{C|m}-\omega_C\right\rVert_1 .

```

Thus a branch cannot gain more than a linear signal in $q$ minus a quadratic cost in $q$. Completing the square gives a gain quadratic in the conditional state displacement. This argument applies to the entire channel, without selecting a weak measurement or a small rotation in advance.

The measurement strength and feedback strength play different roles. Alice determines the ensemble of conditional states. Bob selects a channel for each ensemble member. A strong channel cannot avoid its reference energetic cost merely because its label came from a rare outcome. Averaging the branch inequality includes every outcome, including those on which the best action is to do nothing.

The information bound follows because squared trace distance is bounded by relative entropy. Averaging the latter over a classical record gives exactly $I(M:C)$. The [three-qubit family](sharpness.md) shows that linear dependence on this information is attained as the information tends to zero. No stronger universal power follows under the same controlled local parameters.

## Local stiffness and the bulk gap answer different questions

A nondegenerate global gap bounds the energy of every state orthogonal to the ground state. Local stiffness asks a narrower question: how much energy must an operator supported on Bob's finite region create, relative to its variance in the ground state?

The global gap therefore supplies a lower bound on local stiffness. The converse need not hold. A delocalized low-energy excitation may have little relevance to the cost of a disturbance confined to one receiver site.

The [critical Ising calculation](local_stiffness.md) makes this distinction explicit. The finite-ring bulk gap vanishes as the ring grows. The smallest generalized eigenvalue of the full one-site energy and variance forms instead approaches a positive constant. Both the local marginal eigenvalue and the norm of the energy terms Bob can change stay controlled. Consequently, the information coefficient stays finite in this gapless limit.

This is a statement about a particular certified receiver and family. It does not imply positive local stiffness for every critical ground state. The generalized-eigenvalue test retains non-Hermitian local operators and every nonzero-variance zero-energy direction. Removing such a direction would incorrectly certify a positive stiffness.

## What the correlation bound adds

The first theorem controls the conditional displacement of Bob's interaction neighborhood. A spatial correlation bound instead constrains products of local observables before Alice has measured. Relating these quantities requires care with the normalization of rare branches.

Compression of Alice's effects to the support of her ground-state marginal supplies that control. The resulting [correlation theorem](correlation_bounds.md) has no outcome-count or minimum-probability factor, but it depends on Alice's smallest positive marginal eigenvalue and support rank. Under uniform local constants, a connected-correlation envelope $f(d)$ gives an energy envelope proportional to $f(d)^2$.

For an exponential envelope, the exponent in that supplied bound doubles. The correlation length in a general clustering theorem can be conservative, and the bound does not identify the optimal energy decay rate. The four-qubit weak-link family establishes sharpness in correlation strength while keeping the endpoint marginals well conditioned. It varies a coupling at fixed geometry, so it does not establish sharp distance scaling.

## The energy ledger

The local operator $H_B$ includes all Hamiltonian terms that Bob can change, including couplings to neighboring sites. A decrease of Bob's bare onsite Hamiltonian alone need not be a decrease of total system energy.

Alice's unconditioned operation leaves the state of $C$ unchanged because $A$ and $C$ are disjoint. Bob's record-independent local channel therefore cannot lower the initial ground-state energy. The record is useful because it selects different channels on the different conditional states.

Alice's measurement can inject positive total energy. Bob's subsequent reduction of that energy is the quantity bounded here. In the usual ideal unitary-feedback description, a cyclic external controller can receive this reduction as work. An arbitrary channel can also transfer energy to a discarded environment. The CPTP theorem is an upper bound on system-energy reduction and therefore also constrains narrower implementations; it does not grant free ancillas, free resets or a complete work-accounting identity.

There is no free Hamiltonian evolution between the two interventions in the model. Allowing a finite delay can let energy injected near Alice propagate toward Bob. That physical contribution would need to be separated from the information-assisted gain before applying a zero-offset ground-state statement.

## Relation to established results

[Hotta's minimal-model analysis](../references/RELATED_WORK.md#hotta2010) already relates extracted energy linearly to measurement information. Explicit QET protocols also exhibit the familiar square of a correlation divided by a local energetic cost. Those facts are the starting context for this work.

The general proof here shows that the response structure constrains every instrument and every local feedback channel in the stated model. It incorporates the reference-cost bookkeeping of [Hotta's many-body bound](../references/RELATED_WORK.md#hotta2013) and the gap/Schmidt-spectrum ideas behind [CP-local passivity](../references/RELATED_WORK.md#alhambra2019). The all-operator stiffness certificate supplies a finite coefficient in the critical example. The precise comparison with earlier information and spatial bounds is recorded in [Related work](../references/RELATED_WORK.md).

The universal theorem, the exact power-sharp examples, and the critical certificate support different parts of the conclusion. The theorem supplies the converse. The small systems establish that the powers cannot generally be increased. The critical chain demonstrates that a bulk gap is not the controlling physical requirement. The numerical checks test finite identities and normalizations; they do not replace these arguments.
