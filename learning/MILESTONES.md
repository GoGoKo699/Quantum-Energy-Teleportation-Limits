# The 30-milestone understanding map

A distant measurement can help a receiver lower the energy of an interacting quantum system. The central question is how the receiver's gain is limited by the information in the measurement record and by the ground state's correlations. Understanding the answer requires connecting the local energy cost of feedback to a statement that covers every allowed measurement and feedback channel.

This map has **10 background/preliminaries milestones** and **20 narrative/innovation milestones**. The background phase assembles states, support, channels, measurements, energy locality, and information into the complete QET setting. The narrative phase develops the response estimate into the universal bounds, then connects the critical-system certificate and two sharpness examples to their physical meaning. M10 and M30 integrate their respective phases.

The allocation follows this project's structure: its foundations are concentrated in finite-dimensional quantum information, while its main argument has several distinct consequences and supporting examples. The canonical science pages contain the full proofs and calculations. The milestones identify the connections needed to understand those results as one scientific account.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), identified as [Watrous2018](../references/RELATED_WORK.md#watrous2018). The [anchor and bridge](ANCHOR_AND_BRIDGE.md#reading-route) selects the relevant sections, translates notation, and supplies the steps specific to this project. Primary research citations remain in the canonical scientific account and its related-work references.

## Overview

| ID | Phase | Milestone |
|---|---|---|
| [M01](#m01) | Background | States and energy expectations |
| [M02](#m02) | Background | Marginals and occupied support |
| [M03](#m03) | Background | Channels and their dilations |
| [M04](#m04) | Background | Measurement records and conditional ensembles |
| [M05](#m05) | Background | The neighborhood of an energy change |
| [M06](#m06) | Background | Ground-state passivity and excitation cost |
| [M07](#m07) | Background | Observable bounds and trace distance |
| [M08](#m08) | Background | Information carried by a classical record |
| [M09](#m09) | Background | Connected correlations and clustering |
| [M10](#m10) | Background | The complete one-round QET setting |
| [M11](#m11) | Narrative | Conditional support after remote measurement |
| [M12](#m12) | Narrative | A channel's reference disturbance and cost |
| [M13](#m13) | Narrative | From a state-weighted norm to a uniform response scale |
| [M14](#m14) | Narrative | A local representative of conditioned energy change |
| [M15](#m15) | Narrative | Optimizing the response against its cost |
| [M16](#m16) | Narrative | The universal information ceiling |
| [M17](#m17) | Narrative | Rare outcomes without a probability floor |
| [M18](#m18) | Narrative | The quadratic connected-correlation bound |
| [M19](#m19) | Narrative | Squaring a spatial correlation envelope |
| [M20](#m20) | Narrative | Local stiffness as an operator variational problem |
| [M21](#m21) | Narrative | The finite critical Ising ring |
| [M22](#m22) | Narrative | Positive local stiffness with a closing bulk gap |
| [M23](#m23) | Narrative | The exact rotation mechanism |
| [M24](#m24) | Narrative | Sharp dependence on record information |
| [M25](#m25) | Narrative | A weak link creates linear state correlations |
| [M26](#m26) | Narrative | Sharp quadratic dependence on state correlations |
| [M27](#m27) | Narrative | What the two sharpness examples establish |
| [M28](#m28) | Narrative | The physical energy ledger and protocol boundaries |
| [M29](#m29) | Narrative | Established ingredients and the added response estimate |
| [M30](#m30) | Narrative | The complete energy–information argument |

## Phase I: background/preliminaries

This phase proceeds from individual quantum states and operations to the complete spatial measurement-and-feedback model. Its endpoint is a precise understanding of the task, the energy observable, and the hypotheses needed by the universal bound.

<a id="m01"></a>

### M01. States and energy expectations

- **Central question:** What mathematical objects describe a quantum state and its energy?
- **Understanding target:** Interpret a density operator, an observable, and the expectation $\mathrm{Tr}(\rho H)$. Explain why shifting the ground energy to zero preserves every energy difference and makes the reference Hamiltonian positive.
- **Dependencies and story role:** No earlier milestone is required. This supplies the state and energy language used throughout both phases.
- **Conceptual connection:** The ground state is both a quantum-information resource and the reference that prevents an unconditioned local operation from extracting energy.
- **Source pointers:** Watrous §2.1.2, through [States and records](ANCHOR_AND_BRIDGE.md#states-and-records); [Model: System, state, and local energy](../science/model.md#system-state-and-local-energy).

<a id="m02"></a>

### M02. Marginals and occupied support

- **Central question:** What information about a global state is available in a local region, and which local directions are occupied?
- **Understanding target:** Relate partial traces, reduced states, support projectors, and the Schmidt decomposition of a pure state. Distinguish the smallest positive marginal eigenvalue from a full-rank assumption, and recognize that a subsequent local operation can leave the occupied support.
- **Dependencies and story role:** Depends on [M01](#m01). It moves from a state of the whole system to the local data used by Alice and Bob and to the conditioning parameters in the theorem.
- **Conceptual connection:** Support positivity later controls conditional states, while the marginal spectrum converts a state-weighted disturbance into an operator-norm bound.
- **Source pointers:** Watrous §§2.1.2–2.1.3, through [States and records](ANCHOR_AND_BRIDGE.md#states-and-records); [Model: Support parameters and scope](../science/model.md#support-parameters-and-scope).

<a id="m03"></a>

### M03. Channels and their dilations

- **Central question:** How can a single mathematical class include unitary feedback, noise, and interaction with a local apparatus?
- **Understanding target:** Explain complete positivity and trace preservation, the Kraus representation, and the equivalent isometric dilation. Understand why Kraus operators can be non-Hermitian and why trace preservation makes the Kraus column an isometry.
- **Dependencies and story role:** Depends on [M01](#m01) and [M02](#m02). It identifies the full receiver operation class before any particular feedback protocol is selected.
- **Conceptual connection:** The dilation packages an arbitrary channel into one operator, allowing the response estimate to avoid a factor depending on Kraus rank.
- **Source pointers:** Watrous §2.2.2 and Corollary 2.27, through [Channels and disturbance](ANCHOR_AND_BRIDGE.md#channels-and-disturbance); [Model: Feedback and the extraction observable](../science/model.md#feedback-and-the-extraction-observable).

<a id="m04"></a>

### M04. Measurement records and conditional ensembles

- **Central question:** How does Alice's measurement produce both a classical outcome and a conditional state near Bob?
- **Understanding target:** Distinguish a measurement instrument from its effects and from its recorded outcomes. Explain the conditional identity $p_m\mathrm{Tr}(\sigma_mY)=\langle E_mY\rangle$ for a remote observable and the unchanged average $\sum_m p_m\sigma_m=\omega_C$.
- **Dependencies and story role:** Depends on [M02](#m02) and [M03](#m03). It connects local operations to the ensemble on which feedback acts.
- **Conceptual connection:** Alice can change the decomposition of Bob's average state into conditional states without changing that average. The record makes the decomposition operationally useful.
- **Source pointers:** Watrous §§2.3.1–2.3.2, through [States and records](ANCHOR_AND_BRIDGE.md#states-and-records); [Model: Measurement and conditional states](../science/model.md#measurement-and-conditional-states).

<a id="m05"></a>

### M05. The neighborhood of an energy change

- **Central question:** Which part of an interacting Hamiltonian can Bob change by acting only on his region?
- **Understanding target:** Explain the decomposition $H=H_B+H_{\mathrm{out}}$, why $H_B$ includes interactions touching $B$, and why its support is a larger region $C$. Interpret the centered energy scale $h_B$ and the condition $A\cap C=\varnothing$.
- **Dependencies and story role:** Depends on [M01](#m01) and [M03](#m03). It connects a local channel to the correct total-energy observable and establishes the spatial geometry.
- **Conceptual connection:** Information about the interaction neighborhood, rather than only Bob's bare onsite state, is what controls the energy Bob can change.
- **Source pointers:** [Model: System, state, and local energy](../science/model.md#system-state-and-local-energy) and [Feedback and the extraction observable](../science/model.md#feedback-and-the-extraction-observable); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m06"></a>

### M06. Ground-state passivity and excitation cost

- **Central question:** What quantitative energetic resistance must feedback overcome?
- **Understanding target:** Distinguish the nonnegative energy cost of acting on a ground state from the stronger assumption $\langle O^\dagger H O\rangle\geq\kappa_B\mathrm{Var}_{\omega}(O)$ for every local operator $O$. Explain why the operator class includes non-Hermitian operators and why a gap $\Delta$ supplies $\kappa_B=\Delta$ when the ground state is unique.
- **Dependencies and story role:** Depends on [M02](#m02), [M03](#m03), and [M05](#m05). It supplies the quantitative physical hypothesis needed for the later channel argument.
- **Conceptual connection:** Local stiffness measures the cost of a local departure from the ground state. A global gap is one sufficient certificate of that cost.
- **Source pointers:** [Model: Local stiffness over all operators](../science/model.md#local-stiffness-over-all-operators); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps). The computational certificate is developed later in M20.

<a id="m07"></a>

### M07. Observable bounds and trace distance

- **Central question:** How can a change in a quantum state bound the change in an energy expectation?
- **Understanding target:** Distinguish the operator norm from the trace norm, use their dual pairing to interpret an observable-response bound, and keep the full norm $\Vert\rho-\sigma\Vert_1$ distinct from the convention that defines trace distance with a factor of one half.
- **Dependencies and story role:** Depends on [M01](#m01) and [M02](#m02). It supplies the quantitative bridge between a conditional state displacement and an energy response.
- **Conceptual connection:** A state difference matters energetically through the norm of the observable that probes it. The project will make that observable norm shrink with the feedback disturbance.
- **Source pointers:** Watrous §3.1.1, through [Notation](ANCHOR_AND_BRIDGE.md#notation); [Energy and information: Optimize cost against response](../science/energy_information.md#4-optimize-cost-against-response).

<a id="m08"></a>

### M08. Information carried by a classical record

- **Central question:** How much does Alice's outcome tell Bob about his energy neighborhood?
- **Understanding target:** Explain the classical–quantum state of the record and neighborhood, its mutual information $I(M:C)=\sum_m p_mD(\sigma_m\Vert\omega_C)$, and the roles of Pinsker's inequality and data processing. Track the conversion from the anchor's base-two logarithms to the project's natural logarithms.
- **Dependencies and story role:** Depends on [M02](#m02), [M04](#m04), and [M07](#m07). It connects branchwise distinguishability to a single information quantity for the complete ensemble.
- **Conceptual connection:** The information actually delivered by the measurement can be smaller than the initial state correlation $I(A:C)_\omega$; data processing relates the two without identifying them.
- **Source pointers:** Watrous §§5.2.1 and 5.2.3, including Theorems 5.35 and 5.38, through [Information and energy](ANCHOR_AND_BRIDGE.md#information-and-energy); [Model: Measurement and conditional states](../science/model.md#measurement-and-conditional-states).

<a id="m09"></a>

### M09. Connected correlations and clustering

- **Central question:** How do correlations in the unmeasured ground state constrain remote steering?
- **Understanding target:** Interpret connected correlations as departures from factorized expectations and distinguish a bound for all bounded observables on $A$ and $C$ from one for a selected spin component. Explain what a clustering envelope supplies and which interaction, gap, geometry, and support assumptions enter it.
- **Dependencies and story role:** Depends on [M02](#m02), [M05](#m05), and [M07](#m07). It extends the local state language to relations between separated regions.
- **Conceptual connection:** A correlation envelope constrains the raw numerator of a conditional response. Normalizing a rare outcome requires an additional support argument later in the narrative.
- **Source pointers:** [Correlation bounds: State, geometry, and the correlation hypothesis](../science/correlation_bounds.md#1-state-geometry-and-the-correlation-hypothesis) and [Exponential clustering in a gapped spin system](../science/correlation_bounds.md#4-exponential-clustering-in-a-gapped-spin-system); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m10"></a>

### M10. The complete one-round QET setting

- **Central question:** How do the states, operations, information, and energy accounting fit into one physical task?
- **Understanding target:** Describe the complete sequence from a pure ground state through Alice's instrument and communicated record to Bob's conditional channel. State the locality and stiffness assumptions, identify $E_{\mathrm{ext}}$, and explain why every outcome remains in its average and why no intervening free evolution is included.
- **Dependencies and story role:** Integrates [M03](#m03) through [M09](#m09), together with the state and support foundations they use. This is the background phase's synthesis.
- **Conceptual connection:** The complete model separates three roles: ground-state correlations generate conditional information, the record selects feedback, and local stiffness limits the energetic benefit of that feedback.
- **Source pointers:** [Model and energy accounting](../science/model.md), especially [Support parameters and scope](../science/model.md#support-parameters-and-scope); [Reading route](ANCHOR_AND_BRIDGE.md#reading-route) and [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

## Phase II: narrative/innovation

This phase builds the local response estimate into the universal energy ceiling. It then connects that ceiling to spatial envelopes, a critical-system stiffness certificate, and examples that establish the information and correlation powers. The final milestones integrate the results with their energy accounting and precise scope.

<a id="m11"></a>

### M11. Conditional support after remote measurement

- **Central question:** Why can Alice's conditioning not populate a local direction absent from the average ground-state marginal?
- **Understanding target:** Explain how positivity and the ensemble-average identity force each positive-probability conditional state to lie on the occupied pre-feedback support. Keep this statement separate from a restriction on where Bob's channel may send the state.
- **Dependencies and story role:** Depends on [M02](#m02), [M04](#m04), and [M10](#m10). It establishes the first local ingredient of the universal proof, including rank-deficient marginals.
- **Conceptual connection:** An exact support statement replaces a full-rank assumption and makes the later norm conversion valid for every measurement branch.
- **Source pointers:** [Energy and information: Conditional support](../science/energy_information.md#1-conditional-support); Watrous §2.1.2 through [States and records](ANCHOR_AND_BRIDGE.md#states-and-records).

<a id="m12"></a>

### M12. A channel's reference disturbance and cost

- **Central question:** How costly would the selected feedback channel be if Bob applied it without Alice's record?
- **Understanding target:** Interpret $q^2=1-\sum_j\lvert\langle K_j\rangle\rvert^2$ as the channel's reference disturbance and explain the bound $Q\geq\kappa_Bq^2$. Understand why summing the all-operator stiffness inequality covers arbitrary Kraus operators without a Kraus-rank factor.
- **Dependencies and story role:** Depends on [M03](#m03), [M06](#m06), and [M10](#m10). It identifies the energetic cost that the proof must retain while estimating the useful response.
- **Conceptual connection:** The unconditional channel supplies a common physical reference even though each measurement outcome can select a different channel.
- **Source pointers:** [Energy and information: A channel's ground-state cost](../science/energy_information.md#2-a-channels-ground-state-cost); Watrous §2.2.2 and Corollary 2.27 through [Channels and disturbance](ANCHOR_AND_BRIDGE.md#channels-and-disturbance).

<a id="m13"></a>

### M13. From a state-weighted norm to a uniform response scale

- **Central question:** How does the disturbance measured in the ground state control an operator acting on every conditional branch?
- **Understanding target:** Explain the centered dilation map $W$, the identity $\mathrm{Tr}(\omega_BW^\dagger W)=q^2$, and the consequence $\Vert W\Vert\leq q/\sqrt{\lambda_B}$. Identify the input-support compression and retain possible outputs outside that support.
- **Dependencies and story role:** Depends on [M02](#m02), [M07](#m07), [M11](#m11), and [M12](#m12). It converts a reference-state quantity into the uniform operator scale needed by the branchwise proof.
- **Conceptual connection:** The smallest occupied marginal eigenvalue is the price of replacing a state-weighted norm by an operator norm. This explains a physical conditioning parameter in the final coefficient.
- **Source pointers:** [Energy and information: A channel's ground-state cost](../science/energy_information.md#2-a-channels-ground-state-cost), particularly its centered map and norm estimate; [Channels and disturbance](ANCHOR_AND_BRIDGE.md#channels-and-disturbance).

<a id="m14"></a>

### M14. A local representative of conditioned energy change

- **Central question:** How can the global energy change be represented by a local operator whose norm shrinks with the disturbance?
- **Understanding target:** Explain why the response operator $L$ is supported on $C$, why its relevant conditional expectations equal the physical channel-induced energy changes, and why $\Vert L\Vert\leq2h_Bq/\sqrt{\lambda_B}$. Distinguish the expectation identity from an unrestricted operator identity.
- **Dependencies and story role:** Depends on [M05](#m05), [M11](#m11), and [M13](#m13). This supplies the added response estimate on which the universal converse rests.
- **Conceptual connection:** Hamiltonian locality removes terms outside Bob's influence, while ground-state stationarity removes the scalar reference action. Together they make the useful response proportional to the disturbance.
- **Source pointers:** [Energy and information: A local representative of every conditioned energy change](../science/energy_information.md#3-a-local-representative-of-every-conditioned-energy-change); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m15"></a>

### M15. Optimizing the response against its cost

- **Central question:** Why does a small conditional state displacement permit only a quadratic energy gain?
- **Understanding target:** Interpret the branch bound as a linear response in $q$ minus the cost $\kappa_Bq^2$, and explain why maximizing that expression gives $g_m\leq h_B^2\Vert\sigma_m-\omega_C\Vert_1^2/(\kappa_B\lambda_B)$. Understand that this optimization does not assume weak measurement or small-angle feedback in advance.
- **Dependencies and story role:** Depends on [M07](#m07), [M12](#m12), and [M14](#m14). It joins the local proof components into the conditional quadratic law.
- **Conceptual connection:** Keeping the reference cost changes the power of the response bound. Dropping it would retain only a linear distinguishability estimate.
- **Source pointers:** [Energy and information: Optimize cost against response](../science/energy_information.md#4-optimize-cost-against-response); [Interpretation: Why the useful response is second order](../science/interpretation.md#why-the-useful-response-is-second-order).

<a id="m16"></a>

### M16. The universal information ceiling

- **Central question:** How does the branchwise quadratic law become an information bound for every allowed protocol?
- **Understanding target:** Connect averaging, Pinsker's inequality in nats, and data processing to $E_{\mathrm{ext}}\leq2h_B^2I(M:C)/(\kappa_B\lambda_B)\leq2h_B^2I(A:C)_\omega/(\kappa_B\lambda_B)$. State the theorem's operation classes and identify which constants are independent of outcome count and Kraus rank.
- **Dependencies and story role:** Depends on [M08](#m08) and [M15](#m15). It turns the local response mechanism into the first global conclusion about the entire measurement-and-feedback protocol.
- **Conceptual connection:** Information is the ensemble quantity that bounds the sum of squared conditional displacements, while the energetic coefficient comes from the receiver's local physics.
- **Source pointers:** [Theorem 1: Conditional distinguishability and information](../science/energy_information.md#theorem-1-conditional-distinguishability-and-information) and its [final proof step](../science/energy_information.md#4-optimize-cost-against-response); Watrous Theorems 5.35 and 5.38 through [Information and energy](ANCHOR_AND_BRIDGE.md#information-and-energy).

<a id="m17"></a>

### M17. Rare outcomes without a probability floor

- **Central question:** Why does dividing by a small outcome probability not destroy the correlation bound?
- **Understanding target:** Explain Alice's compressed effect $\widetilde E_m=P_AE_mP_A$ and the inequality $p_m\geq\lambda_A\Vert\widetilde E_m\Vert$. Identify how positivity ties a rare branch's probability to the size of its effect on occupied input directions.
- **Dependencies and story role:** Depends on [M04](#m04), [M09](#m09), and [M11](#m11). It supplies the additional normalization argument needed to pass from measured information to premeasurement state correlations.
- **Conceptual connection:** Rare outcomes can strongly condition a state, but their effects and probabilities are linked. This link permits a bound on the complete averaged protocol without discarding any branch.
- **Source pointers:** [Correlation bounds: Conditional states depend only on Alice's effects](../science/correlation_bounds.md#2-conditional-states-depend-only-on-alices-effects); [States and records](ANCHOR_AND_BRIDGE.md#states-and-records).

<a id="m18"></a>

### M18. The quadratic connected-correlation bound

- **Central question:** How does a bounded-observable correlation envelope control the total energy gain?
- **Understanding target:** Connect the conditional-state estimate to the summed-effect bound involving $r_A/\lambda_A$, and interpret $E_{\mathrm{ext}}\leq h_B^2r_Af(A,C)^2/(\kappa_B\lambda_A\lambda_B)$. Explain why this averaged coefficient improves on separately squaring the branchwise bound $f(A,C)/\lambda_A$.
- **Dependencies and story role:** Depends on [M09](#m09), [M15](#m15), and [M17](#m17). It extends the converse from a chosen measurement record to the original ground-state correlations.
- **Conceptual connection:** The completeness of the measurement effects turns a potentially outcome-dependent sum into Alice's occupied support rank.
- **Source pointers:** [Correlation bounds: The quadratic correlation bound](../science/correlation_bounds.md#3-the-quadratic-correlation-bound); [Interpretation: What the correlation bound adds](../science/interpretation.md#what-the-correlation-bound-adds).

<a id="m19"></a>

### M19. Squaring a spatial correlation envelope

- **Central question:** What spatial consequence follows when connected correlations decay with separation?
- **Understanding target:** Explain how a supplied envelope $f(d)$ becomes an energy envelope proportional to $f(d)^2$, with all local coefficients controlled uniformly. Distinguish distance to $C$ from distance to $B$, and distinguish the exponent of a valid bound from an exact optimal decay rate.
- **Dependencies and story role:** Depends on [M05](#m05), [M09](#m09), and [M18](#m18). It connects the correlation theorem to many-body spatial structure.
- **Conceptual connection:** Exponential clustering supplies an input from ground-state physics; the energy theorem transforms that input. Uniform support and stiffness bounds are additional requirements for a family of systems.
- **Source pointers:** [Correlation bounds: Exponential clustering in a gapped spin system](../science/correlation_bounds.md#4-exponential-clustering-in-a-gapped-spin-system) and [Scope at criticality](../science/correlation_bounds.md#5-scope-at-criticality); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m20"></a>

### M20. Local stiffness as an operator variational problem

- **Central question:** How can the local energetic hypothesis be certified from a finite set of local expectation values?
- **Understanding target:** Interpret the forms $G_B$ and $K_B$, the quotient by zero-variance directions, and the least generalized eigenvalue on that quotient. Retain nonzero-variance zero-energy directions and operators mapping occupied inputs outside their support; explain why complex coefficients are required for arbitrary channels.
- **Dependencies and story role:** Depends on [M02](#m02), [M06](#m06), and [M12](#m12). It turns the assumed physical cost into a concrete local certificate.
- **Conceptual connection:** The identity $K_{ij}=\langle F_i^\dagger[H_B,F_j]\rangle$ lets a quantity defined through the total Hamiltonian be computed from the interaction neighborhood.
- **Source pointers:** [Local stiffness: Definition on all local operators](../science/local_stiffness.md#1-definition-on-all-local-operators), [The quotient and its kernel](../science/local_stiffness.md#the-quotient-and-its-kernel), and [Generalized eigenvalue computation](../science/local_stiffness.md#generalized-eigenvalue-computation); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m21"></a>

### M21. The finite critical Ising ring

- **Central question:** What exact finite-system facts are needed to study the information coefficient at criticality?
- **Understanding target:** Explain the periodic Ising Hamiltonian, the unique even-parity ground state, the parity-dependent fermion boundary condition, and the exact finite-ring formulas for the gap and local means. Identify why both odd and even rings require the parity condition to be retained.
- **Dependencies and story role:** Depends on [M01](#m01), [M05](#m05), and [M06](#m06). It supplies a concrete critical family for the local stiffness certificate.
- **Conceptual connection:** A sequence of well-defined finite ground states allows the bulk gap to close while the receiver's local data remain explicitly calculable.
- **Source pointers:** [Local stiffness: Unique ground state and parity](../science/local_stiffness.md#unique-ground-state-and-parity) and [Critical energy, gap, and local means](../science/local_stiffness.md#critical-energy-gap-and-local-means); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m22"></a>

### M22. Positive local stiffness with a closing bulk gap

- **Central question:** Can a receiver retain a finite energetic resistance when the many-body excitation gap tends to zero?
- **Understanding target:** Connect the Ising local matrices to $\kappa_N\geq\kappa_*>0$, with $\kappa_*/J\simeq0.37125191$, and track the uniform marginal eigenvalue and centered local norm. Explain why the information coefficient remains finite and why this alone supplies no exact critical spatial decay exponent.
- **Dependencies and story role:** Depends on [M16](#m16), [M19](#m19), [M20](#m20), and [M21](#m21). It establishes that the universal ceiling is controlled by local stiffness rather than necessarily by a global gap.
- **Conceptual connection:** Delocalized low-energy excitations and energy created by an operation confined to one site answer different physical questions.
- **Source pointers:** [Local stiffness: Exact all-operator stiffness](../science/local_stiffness.md#exact-all-operator-stiffness), [Local norm and support conditioning](../science/local_stiffness.md#local-norm-and-support-conditioning), and [Thermodynamic scope](../science/local_stiffness.md#4-thermodynamic-scope-and-verification); [Interpretation: Local stiffness and the bulk gap](../science/interpretation.md#local-stiffness-and-the-bulk-gap-answer-different-questions).

<a id="m23"></a>

### M23. The exact rotation mechanism

- **Central question:** How does a concrete feedback rotation realize the competition between a useful signal and an energetic cost?
- **Understanding target:** Interpret the conditional cost $C$ and signal $D$ in the one-parameter rotation formula and explain why the achieved energy is $(\sqrt{C^2+D^2}-C)/2$. Distinguish optimization within this rotation family from optimization over every local channel.
- **Dependencies and story role:** Depends on [M05](#m05), [M06](#m06), and [M15](#m15). It supplies the common constructive mechanism used by both sharpness examples.
- **Conceptual connection:** An achieved unitary gain is enough to provide a lower bound on optimal channel extraction. A globally optimal feedback formula is unnecessary for matching an exponent.
- **Source pointers:** [Sharpness: A common rotation formula](../science/sharpness.md#a-common-rotation-formula); [Worked example](ANCHOR_AND_BRIDGE.md#worked-example).

<a id="m24"></a>

### M24. Sharp dependence on record information

- **Central question:** Can extracted energy remain proportional to the available record information as that information tends to zero?
- **Understanding target:** Explain the three-qubit fixed-ground-state construction, the weakening binary measurement, and the matching quadratic dependence of energy and record information on measurement strength. Interpret the strictly positive limiting ratio $E_{\mathrm{ext}}/I(M:C)$ while keeping the Hamiltonian, gap, and support spectra fixed.
- **Dependencies and story role:** Depends on [M04](#m04), [M08](#m08), [M16](#m16), and [M23](#m23). It shows that the exponent one in the record-information ceiling cannot generally be increased.
- **Conceptual connection:** Weakening a measurement reduces the information delivered by the record while leaving the ground-state mutual information unchanged. These are different limiting procedures.
- **Source pointers:** [Sharpness: Linear dependence on record information](../science/sharpness.md#1-linear-dependence-on-record-information), especially [Record information](../science/sharpness.md#record-information); [Worked example](ANCHOR_AND_BRIDGE.md#worked-example), using the entropy foundations of Watrous §5.2.1.

<a id="m25"></a>

### M25. A weak link creates linear state correlations

- **Central question:** How can ground-state correlations become small while the local energetic and support parameters stay controlled?
- **Understanding target:** Explain the two-dimer product ground state, its weak joining interaction, and the analytic first-order ground-state response. Understand why the connected correlations are proportional to the weak coupling while the endpoint marginal spectra and gap remain uniformly positive near zero coupling.
- **Dependencies and story role:** Depends on [M02](#m02), [M06](#m06), [M09](#m09), and [M18](#m18). It supplies a varying-state family suitable for examining the correlation exponent.
- **Conceptual connection:** Changing the state itself addresses a question that the fixed-state weak-measurement example cannot address.
- **Source pointers:** [Sharpness: Weakly joining two dimers](../science/sharpness.md#weakly-joining-two-dimers), [Exact first-order ground-state derivative](../science/sharpness.md#exact-first-order-ground-state-derivative), and [Connected correlations are linear in the weak link](../science/sharpness.md#connected-correlations-are-linear-in-the-weak-link); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m26"></a>

### M26. Sharp quadratic dependence on state correlations

- **Central question:** Does an explicit protocol achieve the square of the small state correlations in the weak-link family?
- **Understanding target:** Connect the nonzero first-order feedback signal, positive reference rotation cost, and achieved energy $E_{\mathrm{ext}}(t)=t^2/(600\sqrt5)+o(t^2)$ to the linear correlation scale. Combine this lower bound with the universal converse to identify the sharp quadratic power under controlled local parameters.
- **Dependencies and story role:** Depends on [M15](#m15), [M18](#m18), [M23](#m23), and [M25](#m25). It completes the constructive counterpart of the correlation theorem.
- **Conceptual connection:** The same cost-versus-response structure appears in an explicit protocol and in the universal upper bound, giving matching powers without matching coefficients.
- **Source pointers:** [Sharpness: Feedback gain](../science/sharpness.md#feedback-gain) and [Connected correlations are linear in the weak link](../science/sharpness.md#connected-correlations-are-linear-in-the-weak-link); [Correlation bounds: The quadratic correlation bound](../science/correlation_bounds.md#3-the-quadratic-correlation-bound).

<a id="m27"></a>

### M27. What the two sharpness examples establish

- **Central question:** Which conclusions follow from the examples, and which parameters must be held fixed when comparing powers?
- **Understanding target:** Distinguish a small-record-information limit from a small-ground-state-correlation limit. Explain why the examples establish sharp information and correlation powers, while neither an optimal coefficient nor an optimal spatial decay rate follows. Keep the critical local-stiffness certificate distinct from both sharpness arguments.
- **Dependencies and story role:** Integrates [M16](#m16), [M19](#m19), [M22](#m22), [M24](#m24), and [M26](#m26). It joins the separate examples to the corresponding parts of the universal result.
- **Conceptual connection:** A matching law requires the upper and lower bounds to concern the same varying quantity and the same controlled resources.
- **Source pointers:** [Exact examples and sharp exponents](../science/sharpness.md); [Interpretation: What the correlation bound adds](../science/interpretation.md#what-the-correlation-bound-adds) and [Relation to established results](../science/interpretation.md#relation-to-established-results).

<a id="m28"></a>

### M28. The physical energy ledger and protocol boundaries

- **Central question:** What physical energy and resources does the complete theorem account for?
- **Understanding target:** Explain the difference between total system-energy reduction, bare onsite energy, ideal unitary work extraction, and a full apparatus energy balance. Identify the role of independent local ancillas in the channel model and the separate accounting needed for preparation, resets, finite propagation time, additional shared resources, or multiple rounds.
- **Dependencies and story role:** Depends on [M10](#m10), [M16](#m16), [M19](#m19), [M22](#m22), and [M27](#m27). It integrates the conclusions with the physical task and its consequential boundaries.
- **Conceptual connection:** Broadening feedback from unitaries to channels strengthens the system-energy ceiling while requiring care about the thermodynamic interpretation of the extracted quantity.
- **Source pointers:** [Interpretation: The energy ledger](../science/interpretation.md#the-energy-ledger); [Model: Feedback and the extraction observable](../science/model.md#feedback-and-the-extraction-observable) and [Support parameters and scope](../science/model.md#support-parameters-and-scope).

<a id="m29"></a>

### M29. Established ingredients and the added response estimate

- **Central question:** Which parts of the argument are established foundations, and what additional claim does this project supply?
- **Understanding target:** Attribute channel representations, information inequalities, local passivity, clustering, and specified-protocol quadratic response to their sources. Identify the additional support-aware response estimate, its combination with retained reference cost, and its universal quantifiers. Compare nearby energy-information results under their actual energy observables and assumptions.
- **Dependencies and story role:** Depends on [M15](#m15), [M16](#m16), [M18](#m18), [M22](#m22), and [M27](#m27). It places the connected result in its scientific context without treating familiar ingredients as newly introduced facts.
- **Conceptual connection:** The advance lies in a uniform relation between useful response and energetic disturbance, together with its consequences across the declared operation class.
- **Source pointers:** [Energy and information: Relation to existing results](../science/energy_information.md#relation-to-existing-results), [Interpretation: Relation to established results](../science/interpretation.md#relation-to-established-results), and [Related work and attribution](../references/RELATED_WORK.md); [Project-specific steps](ANCHOR_AND_BRIDGE.md#project-specific-steps).

<a id="m30"></a>

### M30. The complete energy–information argument

- **Central question:** How do the local proof, universal bounds, examples, and physical qualifications form one scientific conclusion?
- **Understanding target:** Explain the full chain from local stiffness and occupied support to a disturbance-dependent response, then to a quadratic conditional-energy bound, a linear information ceiling, and a squared correlation envelope. Connect the two sharpness examples to their respective powers and the critical Ising family to the finite local coefficient, while retaining the energy ledger and uniformity assumptions.
- **Dependencies and story role:** Integrates [M16](#m16), [M18](#m18), [M19](#m19), [M22](#m22), and [M27](#m27) through [M29](#m29), including their earlier dependencies. This is the narrative phase's synthesis and the endpoint of the complete map.
- **Conceptual connection:** Ground-state correlations supply information for feedback, but local energetic resistance constrains how that information can become an average energy reduction. Universality, sharp powers, and applicability at criticality are supported by different parts of the same account.
- **Source pointers:** [Theorem 1](../science/energy_information.md#theorem-1-conditional-distinguishability-and-information), [The quadratic correlation bound](../science/correlation_bounds.md#3-the-quadratic-correlation-bound), [Local excitation stiffness](../science/local_stiffness.md), [Sharp exponents](../science/sharpness.md), and [Physical interpretation](../science/interpretation.md); [Anchor and bridge](ANCHOR_AND_BRIDGE.md#reading-route).
