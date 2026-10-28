# Related work and attribution

Scientific account: [model](../science/model.md), [energy-information bound](../science/energy_information.md), [correlation bounds](../science/correlation_bounds.md), [local stiffness](../science/local_stiffness.md), and [sharpness examples](../science/sharpness.md).

The result studied here concerns the average decrease of a system's **total interacting energy** during local feedback at Bob, after a spatially separated measurement by Alice and before Hamiltonian propagation. The feedback may be any local completely positive trace-preserving map. With the notation and assumptions of the scientific account, the bound is

$$
E_{\mathrm{ext}}
\leq \frac{h_B^2}{\kappa_B\lambda_B}
\sum_m p_m\|\sigma_m-\omega_C\|_1^2
\leq \frac{2h_B^2}{\kappa_B\lambda_B}I(M:C).
$$

Here $C$ includes the interaction terms changed by Bob, $\lambda_B$ is the smallest positive eigenvalue of the ground-state marginal on $B$, and $\kappa_B$ is a positive local stiffness for all local operators. A positive global spectral gap above a unique ground state is a sufficient choice. These conditions, together with the energy convention, determine the scope of each comparison below.

Linear energy-information relations in specific QET models, quadratic signal response in explicit protocols, strong local passivity, quantum Pinsker, and exponential clustering are established ingredients. The contribution developed here is a nonperturbative bound for the full stated measurement and feedback class, with explicit support conditioning. It implies a squared connected-correlation bound when the additional Alice-side conditioning is controlled. It does not establish an exact distance exponent or a thermodynamic work balance for a controller implementing an irreversible channel.

BibTeX entries are in [references.bib](references.bib). Source versions and theorem locations were checked on 28 October 2026. Where a location is identified as an arXiv equation or appendix, it refers to the explicitly linked version, rather than an assumed identical journal layout.

<a id="hotta2010"></a>

## Hotta (2010): a linear law in the minimal model

**Reference:** M. Hotta, *Energy entanglement relation for quantum energy teleportation*, Physics Letters A **374**, 3416–3421 (2010). [Published article](https://doi.org/10.1016/j.physleta.2010.06.058); [arXiv:1002.0200v2](https://arxiv.org/html/1002.0200v2), 25 June 2010. BibTeX: `Hotta2010`.

Section 2 treats a two-qubit Ising Hamiltonian. Alice's measurement Kraus operators commute with the interaction and have the form $e^{i\delta_m}(m_m+e^{i\alpha_m}l_mX_A)$. Bob's optimization includes all qubit unitaries. Section 3 identifies the consumed ground-state entanglement with the mutual information between the measurement pointer and Bob. Equation (12) upper-bounds optimized extracted energy linearly in that information; Eq. (15) provides a reverse linear bound. The preceding weak-measurement expansion gives proportional energy and information.

Thus a linear information law and its weak-measurement sharpness already hold in this model. The present result concerns general separated regions and arbitrary local CPTP feedback, with constants expressed through stiffness and the local marginal. Its sharpness examples illustrate the general bound; the underlying quadratic feedback mechanism is inherited QET physics.

<a id="hotta2013"></a>

## Hotta (2013): the general entropic converse

**Reference:** M. Hotta, *Ground-state-entanglement bound for quantum energy teleportation of general spin-chain models*, Physical Review A **87**, 032313 (2013). [Published article](https://doi.org/10.1103/PhysRevA.87.032313); [arXiv:1301.0485v2](https://arxiv.org/html/1301.0485v2), 28 February 2013. BibTeX: `Hotta2013`.

Section 3 treats arbitrary local measurements and outcome-dependent local unitaries in a pure, nondegenerate ground state. In the notation used here, the argument proves

$$
I(M:C)\geq
\frac{(E_{\mathrm{ext}}+\overline Q)^2}{2\|H_B\|^2},
\qquad
\overline Q=\sum_m p_m\langle U_m^\dagger H U_m\rangle\geq0.
$$

The pointer-information inequality occurs in the proof following Eq. (32); Eqs. (22), (35), and (36) express the corresponding premeasurement-information and entanglement bounds. The paper also discusses larger regions and higher-dimensional nearest-neighbor lattices.

This yields square-root information dependence without the present quantitative stiffness assumption. The current proof retains the cost $Q_m$ and bounds each useful response by a constant times $\sqrt{Q_m}$. Optimizing their competition gives linear information dependence and extends the feedback class. This is an assumption-dependent strengthening, not a uniform replacement of the earlier bound in every regime.

<a id="alhambra2019"></a>

## Alhambra et al. (2019): CP-local passivity and its quantitative structure

**Reference:** Á. M. Alhambra, G. Styliaris, N. A. Rodríguez-Briones, J. Sikora, and E. Martín-Martínez, *Fundamental Limitations to Local Energy Extraction in Quantum Systems*, Physical Review Letters **123**, 190601 (2019). [Published article](https://doi.org/10.1103/PhysRevLett.123.190601); [arXiv:1902.02357v2](https://arxiv.org/html/1902.02357v2), 6 November 2019, the published author version. BibTeX: `Alhambra2019`.

Theorem 1 characterizes CP-local passivity by a semidefinite condition on a Choi objective. The robustness estimate in Appendix A.1 bounds extractable energy through the negative spectrum of the associated slack matrix. Theorem 2 gives sufficient conditions for passive mixtures involving an excitation gap and ground-state Schmidt coefficients.

The operation class, passivity principle, and gap/Schmidt conditioning are important antecedents. The theorem developed here connects them to a remotely generated conditional ensemble: a support-compressed response operator is controlled by the square root of the unconditional local excitation cost, uniformly over Kraus rank. This gives an explicit information bound with no additive offset and a squared-correlation consequence. The distinction is this operational quantitative statement and its proof, rather than a new passivity principle or new semidefinite-programming method.

<a id="haque2026"></a>

## Haque (2026): a general spatial clustering bound

**Reference:** T. Haque, *Nontrivial bounds on extractable energy in quantum energy teleportation for gapped manybody systems with a unique ground state*, Physics Letters A **584**, 131613 (2026). [Published article](https://doi.org/10.1016/j.physleta.2026.131613); [arXiv:2601.18718v2](https://arxiv.org/html/2601.18718v2), 24 March 2026, accepted version. BibTeX: `Haque2026`.

The paper bounds QET extraction for local POVMs and conditional local unitaries using exponential clustering in a unique, gapped ground state. Its variational decomposition retains a nonpositive ground-state contribution in Eq. (10), then drops that contribution in Eq. (11). Section 4 obtains an energy bound linear in the clustering envelope; Section 5 refines the control of the feedback through commutators.

The present argument instead combines the energetic cost with the size of the useful response. Its squared-envelope consequence has additional explicit hypotheses: fixed supports and uniformly bounded $h_B$, $r_A$, $1/\kappa_B$, $1/\lambda_A$, and $1/\lambda_B$. It also allows CPTP feedback. A supplied estimate $\operatorname{Corr}(A:C)\leq C_0e^{-d/\xi}$ then yields an $e^{-2d/\xi}$ envelope. This does not identify the optimal correlation length or prove that this distance exponent is attained.

<a id="itoh2026"></a>

## Itoh, Masaki, and Matsueda (2026): effective temperature and an additive resource

**Reference:** K. Itoh, Y. Masaki, and H. Matsueda, *Upper bound on locally extractable energy from entangled pure state under feedback control*, Physical Review E **113**, 024108 (2026). [Published article](https://doi.org/10.1103/2mkn-rjff); [published PDF](https://journals.aps.org/pre/pdf/10.1103/2mkn-rjff); [arXiv:2408.11522v2](https://arxiv.org/html/2408.11522v2), 23 August 2024. BibTeX: `Itoh2026`.

The published Secs. II–III define energy reduction relative to a chosen local Hamiltonian $H_S$ and prove, in Eq. (13),

$$
E_{\mathrm{ext}}
\leq
\frac{D(\rho_S\|\sigma_{\mathrm{eff}})+I_{\mathrm{QC}}}{\beta_{\mathrm{eff}}}.
$$

The same formula and equation number occur in the inspected preprint. The state $\sigma_{\mathrm{eff}}$ is Gibbs for $H_S$ at an effective temperature determined from entanglement.

The athermality term generally remains positive when the measurement record carries no information. In the present problem, energy includes all interaction terms affected by Bob. Choosing $S=C$ and $H_S=H_B$ would cover that observable, but would not generally make the ground marginal Gibbs or remove the additive term. The present information bound has zero offset because it uses local passivity of the global ground state together with quantitative stiffness.

<a id="ikeda2026"></a>

## Ikeda (2026): quadratic response in specified protocols

**Reference:** K. Ikeda, *Quantum energy teleportation across a lattice and the continuum*, Physical Review D **114**, 045016 (2026). [Published article](https://doi.org/10.1103/6yq9-7szd); [arXiv:2604.09973v1](https://arxiv.org/html/2604.09973v1), 11 April 2026. BibTeX: `Ikeda2026`.

The inspected author version studies the massive Thirring/sine-Gordon setting and related lattice protocols. Sections 2.4–2.5 obtain $E_B^{\max}=\eta^2/(2\xi)$ for the continuum protocol and identify the leading weak-measurement signal with a current correlator. Section 6 constructs a neutral-current lattice protocol with the corresponding quadratic structure. These formulas demonstrate explicitly how a response competes with a positive local energetic cost.

Such squared-signal behavior in chosen protocols is prior art. The present theorem bounds every measurement and local CPTP feedback in its finite-dimensional model, without expanding a particular feedback generator or assuming weak measurements. Its finite examples establish sharpness of the information and correlation powers under controlled constants. They do not establish sharp distance behavior or extend the theorem to unbounded field operators.

<a id="pfeuty1970"></a>

## Pfeuty (1970): exact Ising input

**Reference:** P. Pfeuty, *The one-dimensional Ising model with a transverse field*, Annals of Physics **57**, 79–90 (1970). [Published article](https://doi.org/10.1016/0003-4916(70)90270-8); [journal PDF hosted at UC Davis](https://www.math.ucdavis.edu/~bxn/pfeuty1970.pdf). BibTeX: `Pfeuty1970`.

The exact fermionic solution supplies the dispersion, ground-state energy, and spin correlations for the transverse-field Ising model. These are inputs to the critical example, not results of this project. In particular, Pauli versus spin-operator normalization and the direction chosen for the field must be translated before using numerical constants.

The local-stiffness analysis constructs energy and variance forms on the full one-site operator space and solves their generalized eigenvalue problem. Its role is to show explicitly why a local energetic stiffness can remain positive while the global gap tends to zero. Finite-ring statements retain their fermion-parity and boundary-condition derivation in the project account; a thermodynamic-limit simplification in the source is not used as a substitute for that finite-size argument.

<a id="hastingskoma2006"></a>

## Hastings and Koma (2006): exponential clustering from a gap

**Reference:** M. B. Hastings and T. Koma, *Spectral Gap and Exponential Decay of Correlations*, Communications in Mathematical Physics **265**, 781–804 (2006). [Published article](https://doi.org/10.1007/s00220-006-0030-4); [arXiv:math-ph/0507008v3](https://arxiv.org/html/math-ph/0507008v3), 16 December 2005. BibTeX: `HastingsKoma2006`.

Theorem 2.8 and Eq. (2.19) give clustering for bounded, compactly supported commuting observables under a uniform gap and appropriate decaying interactions. For a unique ground state, the ground-sector term reduces to the product of expectations, giving the connected-correlation estimate needed here. The decay rate depends on the gap and interaction bounds.

The project imports a valid correlation envelope under those assumptions and then applies its own correlation-squared inequality. It does not derive clustering, assume uniform constants as the gap closes, or equate a theorem's exponential envelope with the exact physical correlation length. Local stiffness can replace the gap in the energy-information theorem; it does not by itself imply a clustering theorem.

<a id="nachtergaelesims2006"></a>

## Nachtergaele and Sims (2006): an explicit clustering formulation

**Reference:** B. Nachtergaele and R. Sims, *Lieb-Robinson Bounds and the Exponential Clustering Theorem*, Communications in Mathematical Physics **265**, 119–130 (2006). [Published article](https://doi.org/10.1007/s00220-006-1556-1); [arXiv:math-ph/0506030v3](https://arxiv.org/html/math-ph/0506030v3), 2 September 2005. BibTeX: `NachtergaeleSims2006`.

Theorem 2, Eqs. (10)–(12), gives exponential clustering from a spectral gap and a Lieb-Robinson bound. At zero imaginary time and for a unique ground state, centering the second observable gives an equal-time connected-correlation bound. The displayed prefactor depends on norms and support size, and its decay rate depends on the gap and interaction norm.

This is a second primary formulation for the spatial input. The project must keep its support and uniformity conditions when taking limits or optimizing observables. The theorem does not supply Alice's or Bob's local marginal conditioning, which is an additional requirement of the squared-envelope corollary here.

<a id="watrous2018"></a>

## Watrous (2018): standard channel and information inequalities

**Reference:** J. Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). [Publisher](https://doi.org/10.1017/9781316848142); [author's book page](https://jhwatrous.github.io/books-and-courses.html). BibTeX: `Watrous2018`.

The author-posted Chapter 2 covers quantum channels and measurements, including the Stinespring characterization in Corollary 2.27. Chapter 3 supplies the operational trace-norm framework. Chapter 5, Theorems 5.35 and 5.38, gives relative-entropy data processing and quantum Pinsker. [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), and [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf) were inspected for these uses.

These are standard mathematical inputs. The source uses base-two entropy, while this project uses natural logarithms. Consequently its Pinsker coefficient $1/(2\ln 2)$ becomes $1/2$ here. The energetic response estimate, support compression, and local-stiffness application are supplied in the project proofs.

## Scope of the comparison

The cited sources establish the relevant prior statements and imported mathematical or physical ingredients. The comparisons above identify the contribution developed in this repository relative to those results. They do not assert that linear information dependence, local passivity, quadratic response, or critical Ising correlations originate here. Any application to growing regions, vanishing local eigenvalues, Hamiltonian evolution during communication, or an unbounded local Hilbert space requires a separate argument.
