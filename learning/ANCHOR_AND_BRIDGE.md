# From quantum channels to a limit on energy extraction

Imagine a chain of interacting spins in its ground state. Alice measures one part of the chain and sends the outcome to Bob, who controls a distant part. The outcome can tell Bob which local operation will lower the system's energy. The question is how much energy any such feedback can remove when Alice's record carries little information about Bob's surroundings.

The project answers this question for arbitrary local quantum channels, with explicit assumptions on the ground state and its local excitation cost. Its educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The book supplies the language of states, measurements, channels, distinguishability, and entropy. The bridge below explains how those objects enter the energy problem and where the project supplies additional physics and estimates.

The [30-milestone map](MILESTONES.md) organizes the complete scientific story. This page supports that map; the authoritative assumptions and proofs remain in [the model](../science/model.md) and [the energy-information theorem](../science/energy_information.md).

<a id="reading-route"></a>

## 1. A focused route through the anchor

The [author's book page](https://jhwatrous.github.io/books-and-courses.html) provides the complete manuscript, individual chapters, and errata. The locations below were checked in the author's standard-layout chapter PDFs on 28 October 2026. These are the author-posted manuscript of the 2018 book. The [published-book errata](https://jhwatrous.github.io/TQI.errata.pdf), dated 23 July 2025, do not change the four numbered channel, discrimination, and entropy results used below.

| Project question | Watrous location | Role in this project |
|---|---|---|
| What does a subsystem state describe? | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Sections 2.1.2 and 2.1.3 | Density matrices, mixtures, and reduced states; [M01](MILESTONES.md#m01) and [M02](MILESTONES.md#m02). |
| What operations may Bob perform? | Chapter 2, Sections 2.2.1 and 2.2.2, especially **Corollary 2.27** | Kraus and isometric representations of a channel; [M03](MILESTONES.md#m03) and [M12](MILESTONES.md#m12). |
| What is Alice's classical record? | Chapter 2, Sections 2.3.1 and 2.3.2 | Measurement effects and operations with a retained quantum output; [M04](MILESTONES.md#m04). |
| How different are two conditional states? | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Section 3.1.1, especially **Theorem 3.4** | Operational meaning of the trace norm through binary state discrimination; [M07](MILESTONES.md#m07). |
| How is distinguishability controlled by information? | [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf), Section 5.2.1 and Section 5.2.3, especially **Theorems 5.35 and 5.38** | Relative entropy, data processing, and Pinsker's inequality; [M08](MILESTONES.md#m08) and [M16](MILESTONES.md#m16). |

Start with the explanations on this page and consult those sections where a definition or proof needs more detail. Chapter 5's proof of joint convexity is a substantial mathematical result; the energy argument uses its stated consequences. Understanding the application does not require rederiving that theorem first.

Research papers supporting passivity, QET comparisons, the exact Ising solution, and clustering are attributed in [Related work](../references/RELATED_WORK.md). They serve as research dependencies and attribution. Watrous remains the single educational anchor.

<a id="notation"></a>

## 2. Translate the notation before using the theorems

| In Watrous | In this project |
|---|---|
| A register and its associated complex Euclidean space | A spatial region, such as $A$, $B$, or $C$, and its finite-dimensional Hilbert space. |
| $\rho[X]$, the state reduced to register $X$ | $\omega_B$ for the ground-state marginal, or $\sigma_m$ for the conditional state on $C$. |
| $\Phi$, a channel | $\mathcal E_m$, Bob's feedback channel after outcome $m$. |
| $A_a$ in a Kraus representation, and $A$ for an isometry | $K_j$ and $V$, respectively. The letter $A$ already names Alice's region here. |
| $X^{\ast}$ for an operator adjoint | $X^\dagger$. The notation $\mathcal E_m^{\ast}$ still denotes the adjoint **map**. |
| $\mu(m)$, a positive measurement effect | $E_m$. The implementation can have several Kraus operators $M_{m\alpha}$ for one recorded outcome. |
| $H(\rho)$, an entropy | $S(\rho)$ when entropy is written explicitly below. The symbol $H$ denotes the physical Hamiltonian in the project. |
| Base-two logarithms in entropies | Natural logarithms, so information is measured in nats. |

The symbol $\omega$ denotes the reference ground state here; it does not imply that the state is maximally mixed. Write $\langle O\rangle=\mathrm{Tr}(\omega O)$. The norm $\lVert O\rVert$ is the operator norm, while $\lVert O\rVert_1=\mathrm{Tr}\sqrt{O^\dagger O}$ is the trace norm. In particular, the trace distance convention with a factor $1/2$ is different from the unhalved norm used in the energy bound.

Alice acts on $A$, Bob acts on $B$, and $C$ contains every Hamiltonian term Bob can change. Usually $C$ is larger than $B$ because it includes interaction partners. The separation assumption is $A\cap C=\varnothing$. There is no free Hamiltonian evolution between Alice's measurement and Bob's feedback in this model. The instantaneous description specifies the mathematical protocol; its use in an experiment requires a time window in which propagation is negligible or separately controlled. See [M05](MILESTONES.md#m05) and [the locality assumptions](../science/model.md#system-state-and-local-energy).

<a id="states-and-records"></a>

## 3. From a measurement to a useful conditional state

Alice's instrument has effects

$$
E_m=\sum_\alpha M_{m\alpha}^\dagger M_{m\alpha},
\qquad \sum_m E_m=I_A.
$$

The probability of outcome $m$ is $p_m=\langle E_m\rangle$. For $p_m\gt 0$, let $\sigma_m$ be the state on $C$ conditional on that outcome. Since Alice acts outside $C$, any observable $Y_C$ satisfies

$$
p_m\mathrm{Tr}(\sigma_mY_C)=\langle E_mY_C\rangle,
\qquad
\sum_m p_m\sigma_m=\omega_C.
$$

These are the project's application of the measurement framework in [Watrous, Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Sections 2.3.1 and 2.3.2. The second identity says that a reader who does not receive Alice's outcome sees the original marginal on $C$. Receiving the outcome identifies a particular member of an ensemble whose average is that marginal. This distinction is the resource used by feedback.

Package the record and conditional state together as

$$
\omega_{MC}=\sum_m p_m\lvert m\rangle\langle m\rvert\otimes\sigma_m.
$$

The orthogonal states $\lvert m\rangle$ represent an ordinary classical record. Define $\delta_m=\sigma_m-\omega_C$ and $d_m=\lVert\delta_m\rVert_1$. If all $d_m$ vanish, the outcome gives no information about any observable on $C$.

The positivity of the conditional states also controls their support. A vector in the kernel of $\omega_C=\sum_m p_m\sigma_m$ has zero expectation against every positive term with $p_m\gt 0$. It is therefore in the kernel of every such $\sigma_m$. Consequently $D(\sigma_m\Vert\omega_C)$ is finite even when $\omega_C$ has zero eigenvalues. The same reasoning on $B$ establishes the support statement used in [M11](MILESTONES.md#m11).

Theorem 3.4 of [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf) makes the trace norm operational: for two density matrices given with equal prior probabilities, the optimal probability of identifying them is

$$
p_{\mathrm{guess}}
=\frac12+\frac14\lVert\rho_0-\rho_1\rVert_1.
$$

Applied to $\sigma_m$ and $\omega_C$, this quantifies how an observer with access to $C$ could distinguish the conditioned state from the average. It is an interpretation of $d_m$; Bob's allowed operation is still confined to $B$.

<a id="channels-and-disturbance"></a>

## 4. From a general channel to its ground-state cost

Corollary 2.27 in [Chapter 2, Section 2.2.2](https://jhwatrous.github.io/TQI.2.pdf) applies to finite-dimensional completely positive trace-preserving maps. Its Kraus and isometric representations give, for one of Bob's channels,

$$
\begin{aligned}
\mathcal E(\rho)&=\sum_jK_j\rho K_j^\dagger,
&\sum_jK_j^\dagger K_j&=I_B,\\
V\lvert\psi\rangle&=\sum_jK_j\lvert\psi\rangle\otimes\lvert j\rangle,
&V^\dagger V&=I_B.
\end{aligned}
$$

The auxiliary register records a representation of the discarded environment. This allows noisy feedback, ancillary systems, and discarding within a local channel. The corollary imposes no Hamiltonian or energy constraint. Those enter through the project's model.

Shift the ground energy to zero, so $H\ge0$ and $H\lvert\Omega\rangle=0$. Let

$$
a_j=\langle K_j\rangle,
\qquad q^2=1-\sum_j\lvert a_j\rvert^2.
$$

The quantity $q^2$ lies between zero and one. In fact, it is one minus the overlap of the channel's output on the full ground state with that same ground state. It measures disturbance relative to the reference state, including the surrounding degrees of freedom.

The physical hypothesis is a positive constant $\kappa_B$ such that, for **every** operator $O$ on $B$,

$$
\langle O^\dagger HO\rangle
\ge\kappa_B
\left(\langle O^\dagger O\rangle-\lvert\langle O\rangle\rvert^2\right).
$$

This is stronger than saying that an operation cannot lower the ground energy. It gives a quantitative cost for creating an excitation. Because Kraus operators need not be Hermitian or unitary, the quantifier over all operators is necessary. Summing this inequality over the $K_j$ gives

$$
Q=\sum_j\langle K_j^\dagger HK_j\rangle
\ge\kappa_Bq^2.
$$

Here $Q$ is the energy increase produced by that channel on the unconditioned ground state. A unique ground state with gap $\Delta\gt 0$ guarantees the hypothesis with $\kappa_B=\Delta$. The [local-stiffness calculation](../science/local_stiffness.md) can give a stronger constant; it removes only zero-variance directions and keeps all other local operators. These are the connections developed in [M06](MILESTONES.md#m06), [M12](MILESTONES.md#m12), and [M20](MILESTONES.md#m20).

<a id="information-and-energy"></a>

## 5. The extra estimate that turns information into an energy ceiling

### Support converts a weighted estimate into a uniform one

Let $P_B$ project onto the support of $\omega_B$, and let $\lambda_B\gt 0$ be its smallest positive eigenvalue. Thus $\omega_B\ge\lambda_BP_B$. Define $\lvert a\rangle=\sum_j a_j\lvert j\rangle$ and

$$
W=(V-I_B\otimes\lvert a\rangle)P_B.
$$

The representation above yields

$$
\begin{aligned}
q^2&=\mathrm{Tr}(\omega_BW^\dagger W)\\
&\ge\lambda_B\mathrm{Tr}(W^\dagger W)\\
&\ge\lambda_B\lVert W\rVert^2.
\end{aligned}
$$

The first expression is an average weighted by the ground marginal. The last controls the largest action on any occupied input direction. The factor $1/\lambda_B$ is the price of that conversion. Bob may send occupied inputs outside the support; the definition restricts only the input of $W$. In particular, $q=0$ says that the channel is trivial on the reference state, without asserting that it is the identity on every possible input.

### A response competes with a positive cost

Write $H=H_B+H_{\mathrm{out}}$, where $H_{\mathrm{out}}$ acts trivially on $B$, and use the centered norm

$$
h_B=\inf_{c\in\mathbb R}\lVert H_B-cI_C\rVert.
$$

The project's proof constructs an operator $L$ on $C$ that represents the channel-induced energy change in the conditional expectations. Its key estimate is

$$
\lVert L\rVert\le\frac{2h_Bq}{\sqrt{\lambda_B}}.
$$

This step uses the locality of a commutator, the ground-state equation, and the conditional support. It is supplied in [the construction of the local response operator](../science/energy_information.md#3-a-local-representative-of-every-conditioned-energy-change), rather than by a channel representation alone. The operator may be non-Hermitian; its relevant expectations are real, and its Hermitian part obeys the same norm bound.

For the channel selected in outcome $m$, let $g_m$ be the decrease in total system energy. Trace/operator norm duality and the retained cost give

$$
\begin{aligned}
g_m
&\le-\kappa_Bq^2+
\frac{2h_B}{\sqrt{\lambda_B}}d_mq\\
&\le\frac{h_B^2}{\kappa_B\lambda_B}d_m^2.
\end{aligned}
$$

The last step completes a square. Its meaning is concrete: a larger feedback disturbance can exploit a larger conditional signal, but it also costs energy even in the ground state. Optimizing their competition makes the gain quadratic in distinguishability. The inequality applies branch by branch; averaging includes negative-gain and failed branches. See [M13](MILESTONES.md#m13) through [M15](MILESTONES.md#m15).

### Convert distinguishability into information, with the correct units

Theorem 5.38 of [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf) holds for density matrices and uses base-two relative entropy. The project's natural-log convention gives

$$
\begin{aligned}
D_{\mathrm{nat}}(\rho\Vert\sigma)
&=(\ln2)D_{\mathrm{bit}}(\rho\Vert\sigma),\\
D_{\mathrm{bit}}(\rho\Vert\sigma)
&\ge\frac{1}{2\ln2}\lVert\rho-\sigma\rVert_1^2,\\
D_{\mathrm{nat}}(\rho\Vert\sigma)
&\ge\frac12\lVert\rho-\sigma\rVert_1^2.
\end{aligned}
$$

No commutation or full-rank assumption is required. For our conditional ensemble, support containment makes every term finite. Direct evaluation of the classical blocks gives

$$
\begin{aligned}
I(M:C)
&=S(\omega_C)-\sum_m p_mS(\sigma_m)\\
&=\sum_m p_mD_{\mathrm{nat}}(\sigma_m\Vert\omega_C).
\end{aligned}
$$

One way to check the second equality is to expand each relative entropy and use $\sum_m p_m\sigma_m=\omega_C$ in the term containing $\ln\omega_C$. Averaging the energy estimate and applying Pinsker now gives

$$
\begin{aligned}
E_{\mathrm{ext}}
&\le\frac{h_B^2}{\kappa_B\lambda_B}
\sum_m p_m d_m^2\\
&\le\frac{2h_B^2}{\kappa_B\lambda_B}I(M:C).
\end{aligned}
$$

Finally, Theorem 5.35 applies relative-entropy monotonicity to finite-dimensional positive operators under a channel. Use the measurement channel from $A$ to $M$, tensored with the identity on $C$, on the pair $\omega_{AC}$ and $\omega_A\otimes\omega_C$. Their images are $\omega_{MC}$ and $\omega_M\otimes\omega_C$, so

$$
I(M:C)\le I(A:C)_\omega.
$$

The information in the actual record can therefore be replaced by the ground-state mutual information for an upper bound. These are different quantities: a weak measurement may reveal little information even when the ground-state correlations remain fixed. This completes the bridge to [Theorem 1](../science/energy_information.md#theorem-1-conditional-distinguishability-and-information) and [M16](MILESTONES.md#m16).

<a id="worked-example"></a>

## 6. A complete three-qubit example

Take qubits $A,R,B$ and standard Pauli operators $X,Y,Z$. Put $n=(I-Z)/2$ and choose $J\gt 0$. The [first exact example](../science/sharpness.md#1-linear-dependence-on-record-information) uses

$$
\begin{aligned}
H_{\mathrm{phys}}
&=\frac{J}{\sqrt2}(n_A+n_R+n_B)\\
&\quad-\frac J2(X_AX_R+Y_AY_R)\\
&\quad-\frac J2(X_RX_B+Y_RY_B).
\end{aligned}
$$

Its unique ground state and gap are

$$
\begin{aligned}
\lvert\Omega\rangle
&=\frac{\lvert100\rangle+\sqrt2\lvert010\rangle+\lvert001\rangle}{2},\\
E_0&=-J/\sqrt2,
\qquad \Delta=J/\sqrt2.
\end{aligned}
$$

Alice controls the first qubit, Bob controls the last, and $C=\lbrace R,B\rbrace $. In particular, Alice is outside Bob's energy neighborhood. Bob changes

$$
H_B=\frac J{\sqrt2}n_B-\frac J2(X_RX_B+Y_RY_B).
$$

For a measurement strength $0\le t\le1$, Alice implements the two Kraus operators $\sqrt{E_s}$ with

$$
E_s=\frac{I+s tX_A}{2},
\qquad s\in\lbrace -1,+1\rbrace .
$$

Both outcomes have probability $1/2$, and Alice communicates the sign $s$. The support of the marginal on $C$ is spanned by

$$
\lvert u\rangle=\frac{\sqrt2\lvert10\rangle+\lvert01\rangle}{\sqrt3},
\qquad
\lvert v\rangle=\lvert00\rangle.
$$

In this basis, the conditional state is

$$
\sigma_s=
\begin{pmatrix}
3/4&s\sqrt3t/4\\
s\sqrt3t/4&1/4
\end{pmatrix},
\qquad
\omega_C=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}.
$$

The two conditional coherences cancel when the record is ignored. The eigenvalues of $\sigma_s-\omega_C$ are $\pm\sqrt3t/4$, so $d_s=\sqrt3t/2$. The conditional-state eigenvalues and record information are

$$
\begin{aligned}
\nu_\pm(t)&=\frac{1\pm\sqrt{1/4+3t^2/4}}{2},\\
I(M:C)&=b(3/4)-b(\nu_+(t)),\\
b(x)&=-x\ln x-(1-x)\ln(1-x).
\end{aligned}
$$

Bob applies the local unitary

$$
U_s=e^{is\theta_{\ast}Y_B},
\qquad
\theta_{\ast}=-\frac12\arctan(t/3).
$$

The rotation calculation in the exact example gives the same extracted energy in each branch:

$$
E_{\mathrm{ext}}(t)
=\frac{J}{4\sqrt2}\left(\sqrt{9+t^2}-3\right).
$$

For a concrete choice $t=1/2$, this protocol gives

| Quantity | Value |
|---|---|
| Probability of each communicated sign | $1/2$ |
| Conditional trace norm $d_s$ | $\sqrt3/4\approx0.433013$ |
| Record information | $I(M:C)\approx0.107590695$ nats |
| Feedback angle | $\theta_{\ast}\approx-0.082574339$ radians |
| Average energy decrease | $E_{\mathrm{ext}}/J\approx0.0073152433$ |

The theorem applies with $\kappa_B=\Delta=J/\sqrt2$, $\lambda_B=1/4$, and the centered norm $h_B=3J/(2\sqrt2)$. It gives $E_{\mathrm{ext}}\le9\sqrt2\,J I(M:C)$, which is about $1.36941J$ at this measurement strength. The explicit protocol lies below that general bound; the theorem's coefficient need not be optimal for this particular Hamiltonian.

As $t$ tends to zero, the same exact formulas give

$$
\begin{aligned}
I(M:C)&=\frac{3\ln3}{8}t^2+O(t^4),\\
E_{\mathrm{ext}}(t)&=\frac{J}{24\sqrt2}t^2+O(t^4).
\end{aligned}
$$

The state and its gap stay fixed while the measurement becomes less informative. Both information and achieved energy vanish at the same order. This is the meaning of information sharpness in [M24](MILESTONES.md#m24); it does not assert an optimal coefficient or a spatial decay exponent. The [verification guide](../verification/README.md) links the numerical checks of the states, spectra, and energy changes, while the exact derivation remains in the scientific account.

<a id="project-specific-steps"></a>

## 7. What the project adds beyond the anchor

The full argument joins several ingredients with different roles. The book establishes the quantum-information framework. The project derives the quantitative response estimate and connects it to a specified energy observable. Its broader consequences require further hypotheses, recorded in the corresponding scientific files.

| Additional step | Why it is needed | Canonical account |
|---|---|---|
| Identify all energy changed by Bob | Interaction terms can make $C$ larger than $B$. A bound on a bare on-site energy would answer a different physical question. | [Model](../science/model.md); [M05](MILESTONES.md#m05). |
| Compare response with excitation cost | The support estimate and local operator $L$ retain a restoring cost and yield the quadratic optimization. | [Energy-information proof](../science/energy_information.md); [M11](MILESTONES.md#m11) through [M16](MILESTONES.md#m16). |
| Control rare outcomes and connected correlations | Positivity and the occupied support of Alice's marginal control effect norms, giving a squared-correlation bound without a minimum outcome probability. Uniform spatial statements need uniform coefficients and a suitable correlation envelope. | [Correlation bounds](../science/correlation_bounds.md); [M17](MILESTONES.md#m17) through [M19](MILESTONES.md#m19). |
| Keep a local coefficient at criticality | An exact generalized eigenvalue calculation shows that all-operator local stiffness can stay positive while the finite-ring global gap closes. | [Local stiffness](../science/local_stiffness.md); [M20](MILESTONES.md#m20) through [M22](MILESTONES.md#m22). |
| Establish what the powers mean | Separate exact families establish sharp dependence on record information and on state correlations. They do not establish a sharp distance exponent. | [Sharpness](../science/sharpness.md); [M23](MILESTONES.md#m23) through [M27](MILESTONES.md#m27). |

The coefficient depends on $h_B$, $\kappa_B$, and $\lambda_B$. Its uniformity is an explicit condition when comparing a family of systems. The theorem treats the average decrease in **total interacting system energy during Bob's feedback**. For a general channel, this decrease can include energy and entropy exchanged with an apparatus; the cost of preparing, controlling, and resetting that apparatus is not included in $E_{\mathrm{ext}}$. The [physical interpretation](../science/interpretation.md), [M28](MILESTONES.md#m28), and [M30](MILESTONES.md#m30) connect that accounting to the theorem's operational meaning.

