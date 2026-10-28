# Model and energy accounting

The result concerns one round of quantum energy teleportation in a finite quantum system. A measurement in Alice's region produces a classical record, and Bob uses that record to choose a local operation before energy propagates from Alice to Bob. The quantity bounded is the reduction in the system's total energy caused by Bob's operation. The bound includes interaction energy and averages over every measurement outcome.

The central hypothesis is a positive energy cost for local departures from the ground state. A nondegenerate global spectral gap guarantees this hypothesis, but a local stiffness can remain positive when the global gap becomes small. The proof and its information and correlation consequences are in [Energy and information](energy_information.md). The two independent meanings of a sharp exponent are established in [Sharpness](sharpness.md).

## System, state, and local energy

Let the system have finite-dimensional Hilbert space

$$
\mathcal H=\bigotimes_{x\in\Lambda}\mathcal H_x
$$

and Hamiltonian $H$. Subtract its ground energy, so that

$$
H\ge0,\qquad H|\Omega\rangle=0,\qquad
\omega=|\Omega\rangle\langle\Omega|.
$$

Expectation brackets refer to this pure ground state. The primary theorem does not require global ground-state uniqueness; it requires the local stiffness defined below. Uniqueness enters the spectral-gap corollary.

Bob controls a region $B$. Assume a decomposition

$$
H=H_B+H_{\mathrm{out}},
$$

where $H_{\mathrm{out}}$ acts trivially on $B$, and $H_B$ is supported on a neighborhood $C\supseteq B$. For a finite-range interaction Hamiltonian, one may take $H_B$ to be the sum of all interaction terms intersecting $B$, and $C$ to contain the union of their supports. All energy that a local operation on $B$ can change is then represented by $H_B$.

Use the centered operator-norm scale

$$
h_B=\inf_{c\in\mathbb R}\Vert H_B-cI_C\Vert
=\frac{\lambda_{\max}(H_B)-\lambda_{\min}(H_B)}{2}.
$$

One may instead insert any larger certified norm bound. Centering changes neither energy differences under trace-preserving maps nor the commutators used in the proof. The chosen decomposition and neighborhood are part of the model. The theorem does not silently replace an interaction Hamiltonian by Bob's bare on-site Hamiltonian.

Alice controls a region $A$ with

$$
A\cap C=\varnothing.
$$

The protocol is instantaneous in the following precise sense: there is no intervening free evolution between Alice's measurement and Bob's operation. The separation excludes direct action by Alice on an energy term that Bob can change. It does not assert that classical communication takes zero physical time. Applying the result to an experimental time window requires that propagation effects be negligible or be bounded separately.

## Local stiffness over all operators

For every operator $O$ supported on $B$, including a non-Hermitian operator, define

$$
\mathrm{Var}_{\omega}(O)
=\langle O^\dagger O\rangle-|\langle O\rangle|^2.
$$

Assume there is a constant $\kappa_B\gt 0$ such that

$$
\boxed{
\langle O^\dagger H O\rangle
\ge\kappa_B\mathrm{Var}_{\omega}(O)
\quad\text{for every }O\text{ on }B.
}
\qquad\text{(M1)}
$$

The largest valid constant is

$$
\kappa_B^{\mathrm{opt}}
=\inf_{\mathrm{Var}_{\omega}(O)\gt 0}
\frac{\langle O^\dagger H O\rangle}
{\mathrm{Var}_{\omega}(O)}.
$$

A smaller positive lower bound is sufficient. A condition quantified only over unitary operators would suffice for a unitary-only version of the theorem, but it does not by itself establish the result for arbitrary channels. The all-operator quantifier in (M1) permits the inequality to be summed over Kraus operators.

The stiffness is a finite-dimensional generalized eigenvalue problem. For any basis $\lbrace F_\alpha\rbrace $ of all operators on $B$, form

$$
\mathsf A_{\alpha\beta}
=\langle F_\alpha^\dagger H F_\beta\rangle,
\qquad
\mathsf S_{\alpha\beta}
=\langle F_\alpha^\dagger F_\beta\rangle
-\overline{\langle F_\alpha\rangle}\langle F_\beta\rangle.
$$

On the range of $\mathsf S$, whiten its positive spectrum and take the least eigenvalue of the resulting $\mathsf A$ matrix. Only zero-variance directions are removed. A zero-energy eigenvector with nonzero variance makes the stiffness zero and must not be discarded. Directions that map the support of $\omega_B$ into its orthogonal complement must also remain in the operator basis.

This quotient is legitimate because zero variance means
$O|\Omega\rangle=\langle O\rangle|\Omega\rangle$, which also has zero energy cost and zero cross terms in $\mathsf A$. The locality decomposition gives the useful alternative expression

$$
\langle O^\dagger H O\rangle
=\langle O^\dagger[H_B,O]\rangle.
$$

Consequently, the matrices can be evaluated from operators supported on $C$, even though the stiffness is defined through the total Hamiltonian.

If the ground state is unique and the excitation gap is $\Delta\gt 0$, then

$$
H\ge\Delta(I-\omega)
\quad\Longrightarrow\quad
\langle O^\dagger H O\rangle
\ge\Delta\mathrm{Var}_{\omega}(O).
$$

Thus $\kappa_B=\Delta$ is always a valid choice in a finite gapped system. A lower bound uniform in system size is a separate requirement when taking a family or thermodynamic limit. Local passivity and the role of ground-state entanglement have substantial precedent in [Alhambra et al.](../references/RELATED_WORK.md#alhambra2019); the present work uses the quantitative condition (M1) to control feedback that depends on a remote measurement record.

## Measurement and conditional states

An instrument on $A$ has Kraus operators $M_{m\alpha}$, where $m$ labels the communicated outcome and $\alpha$ labels an unobserved refinement. Its effects are

$$
E_m=\sum_\alpha M_{m\alpha}^\dagger M_{m\alpha},
\qquad E_m\ge0,\qquad\sum_m E_m=I_A.
$$

For $p_m=\langle E_m\rangle\gt 0$, define

$$
\rho_m=
\frac{1}{p_m}\sum_\alpha M_{m\alpha}\omega M_{m\alpha}^\dagger,
\qquad
\sigma_m=\mathrm{Tr}_{\Lambda\setminus C}\rho_m.
$$

Because Alice is disjoint from $C$, every operator $Y_C$ obeys

$$
p_m\mathrm{Tr}(\sigma_mY_C)=\langle E_mY_C\rangle,
\qquad
\sum_m p_m\sigma_m=\omega_C.
\qquad\text{(M2)}
$$

Thus the effect $E_m$, rather than the details of its local implementation, determines the conditional state relevant to Bob's energy change. The record-neighborhood state is

$$
\omega_{MC}=\sum_m p_m|m\rangle\langle m|\otimes\sigma_m.
$$

All information quantities use natural logarithms. In particular,

$$
I(M:C)=\sum_m p_mD(\sigma_m\Vert\omega_C),
$$

where $D$ is quantum relative entropy. The averaged state in (M2) ensures that the conditional supports lie within the support of $\omega_C$.

## Feedback and the extraction observable

For each outcome, Bob chooses an arbitrary completely positive trace-preserving map on $B$,

$$
\mathcal E_m(\tau)=\sum_j K_{mj}\tau K_{mj}^\dagger,
\qquad \sum_jK_{mj}^\dagger K_{mj}=I_B.
$$

The total system energy change caused by this feedback is localized:

$$
\mathcal E_m^{\ast}(H)-H
=\mathcal E_m^{\ast}(H_B)-H_B.
\qquad\text{(M3)}
$$

Equation (M3) holds because the map is trace preserving and $H_{\mathrm{out}}$ acts trivially on $B$. Define

$$
g_m=
\mathrm{Tr}(H\rho_m)
-\mathrm{Tr}\left[H(\mathcal E_m\otimes\mathrm{id})(\rho_m)\right],
\qquad
E_{\mathrm{ext}}=\sum_m p_m g_m.
$$

Positive $g_m$ means that Bob lowers the system energy in that branch. Negative and failed branches remain in the average. Doing nothing is an admissible feedback operation. The energy injected by Alice is not subtracted in this observable, so $E_{\mathrm{ext}}$ is not the net energy balance of the entire measurement-and-feedback cycle.

A unitary feedback operation has the usual ideal-control interpretation of energy transferred out of the system. A general channel can exchange both energy and entropy with a local apparatus. The theorem then bounds the system's energy decrease; it does not identify all of that decrease with useful work after accounting for apparatus preparation, discarded ancillas, or memory reset. Independent ancillary systems are already allowed through local CPTP maps. A previously correlated quantum resource outside the declared Bob region requires a larger model.

This distinction also separates the present observable from a bound on the reduction of a chosen bare subsystem Hamiltonian, such as an effective-thermodynamic extraction bound in [Itoh et al.](../references/RELATED_WORK.md#itoh2026).

## Support parameters and scope

Let

$$
P_B=\mathrm{supp}(\omega_B),
\qquad
\lambda_B=\lambda_{\min}^{+}(\omega_B)\gt 0.
$$

Full rank is not assumed. The theorem explicitly tracks the smallest positive eigenvalue because the cost-to-response estimate converts a state-weighted norm into an operator norm on the occupied support. Conditional states remain on that support before Bob acts, while Bob's channel may map them outside it.

The main result applies to finite instruments, and the same proof applies to countable instruments by summation. A continuous-outcome instrument can be written using an effect density with respect to a dominating measure, replacing sums by integrals; the support and quadratic bounds hold almost everywhere. No lower bound on outcome probabilities and no bound on the number of outcomes appears in the result.

Uniform spatial consequences require control of $h_B$, $\kappa_B$, and the relevant support eigenvalues throughout the family. The theorem does not assert a uniform coefficient when these parameters vanish or diverge, and it does not include propagation during feedback, multiple communication rounds, or infinite-dimensional local systems without additional assumptions.

## Connected reading route

| Scientific question | Authoritative account |
|---|---|
| Why must weak steering give a quadratic energy response? | [General information theorem and proof](energy_information.md) |
| What local energy scale replaces the bulk gap? | [Local stiffness and the critical Ising certificate](local_stiffness.md) |
| How does a spatial correlation envelope constrain extraction? | [Correlation bounds](correlation_bounds.md) |
| Can the information and correlation powers be improved? | [Exact sharpness examples](sharpness.md) |
| What energy and resources do the statements describe? | [Physical interpretation](interpretation.md) |

The [related-work account](../references/RELATED_WORK.md) identifies inherited results and the precise comparisons. The [verification guide](../verification/README.md) connects the finite checks to their analytical claims.
