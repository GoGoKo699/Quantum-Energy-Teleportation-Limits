# Energy extraction, information, and correlations

Remote information can reveal a favorable local energy fluctuation, but exploiting that information also requires disturbing a passive ground state. The key estimate below relates the size of the conditional energy response to the square root of the unconditional disturbance cost. Retaining both terms gives a bound linear in the information available to Bob and quadratic in the connected correlations between Alice and Bob's energy neighborhood.

The model, energy accounting, and all-operator stiffness hypothesis are specified in [Model](model.md). Throughout, $\langle\cdot\rangle$ denotes the pure ground-state expectation, $\delta_m=\sigma_m-\omega_C$, and logarithms are natural.

## Theorem 1: conditional distinguishability and information

Assume the model hypotheses and a constant $\kappa_B\gt 0$ satisfying

$$
\langle O^\dagger H O\rangle
\ge\kappa_B\left(\langle O^\dagger O\rangle-|\langle O\rangle|^2\right)
\quad\text{for every local operator }O\text{ on }B.
\qquad\text{(1)}
$$

For every local instrument on $A$, and every outcome-dependent local CPTP feedback map on $B$,

$$
\boxed{
\begin{aligned}
E_{\mathrm{ext}}
&\le\frac{h_B^2}{\kappa_B\lambda_B}
\sum_m p_m\Vert\sigma_m-\omega_C\Vert_1^2\\
&\le\frac{2h_B^2}{\kappa_B\lambda_B}I(M:C)\\
&\le\frac{2h_B^2}{\kappa_B\lambda_B}I(A:C)_\omega.
\end{aligned}
}
\qquad\text{(2)}
$$

The coefficient does not depend on the number of outcomes, a minimum outcome probability, or the Kraus rank of the feedback. Neither $\omega_A$ nor $\omega_B$ is required to be full rank. With a unique ground state and gap $\Delta\gt 0$, the same statement holds with $\kappa_B$ replaced by $\Delta$.

The proof establishes a bound for each branch before averaging. A branch may have negative extraction, and no conditioning on successful outcomes is implicit in (2).

## Proof

### 1. Conditional support

Write $P=P_B$, extended by the identity on other regions. Positivity and
$\sum_m p_m(\sigma_m)_B=\omega_B$ imply

$$
\mathrm{Tr}[(I_B-P)(\sigma_m)_B]=0
\quad\text{for every }p_m\gt 0.
$$

For a positive matrix, zero trace against a projection means that its range is orthogonal to that projection. Therefore

$$
\sigma_m=P\sigma_mP,\qquad \omega_C=P\omega_CP,
\qquad\text{(3)}
$$

where $P$ now acts on $C$. This is the only support restriction imposed on the pre-feedback conditional states. Bob's operations themselves need not preserve $P$.

### 2. A channel's ground-state cost

Fix one feedback channel, suppress the outcome index, and write its Kraus operators as $K_j$. Use the standard channel representation described in [Watrous](../references/RELATED_WORK.md#watrous2018) and introduce a Stinespring isometry

$$
V|\psi\rangle=\sum_jK_j|\psi\rangle\otimes|j\rangle,
\qquad V^\dagger V=I_B.
$$

Let

$$
a_j=\langle K_j\rangle,
\qquad |a\rangle=\sum_j a_j|j\rangle,
\qquad q^2=1-\sum_j|a_j|^2.
\qquad\text{(4)}
$$

Cauchy-Schwarz and trace preservation give $0\le q^2\le1$. The energy cost of applying this channel to the ground state is

$$
Q=\sum_j\langle K_j^\dagger H K_j\rangle
\ge\kappa_B\sum_j
\left(\langle K_j^\dagger K_j\rangle-|\langle K_j\rangle|^2\right)
=\kappa_Bq^2.
\qquad\text{(5)}
$$

This is where the all-operator hypothesis is needed. It is applied to every Kraus operator, including non-Hermitian operators.

Define the rectangular local operator

$$
W=(V-I_B\otimes|a\rangle)P.
\qquad\text{(6)}
$$

Here $I_B\otimes|a\rangle$ maps $|\psi\rangle$ to $|\psi\rangle\otimes|a\rangle$. Since $P|\Omega\rangle=|\Omega\rangle$,

$$
\mathrm{Tr}(\omega_BW^\dagger W)
=\Vert W|\Omega\rangle\Vert^2=q^2.
$$

The inequality $\omega_B\ge\lambda_BP$, together with $W=WP$, yields

$$
q^2\ge\lambda_B\mathrm{Tr}(W^\dagger W)
\ge\lambda_B\Vert W\Vert^2,
\qquad
\Vert W\Vert\le q/\sqrt{\lambda_B}.
\qquad\text{(7)}
$$

The output of $W$ may lie outside the support of $\omega_B$; (7) does not discard those directions.

### 3. A local representative of every conditioned energy change

Consider the operator on the system

$$
L=P V^\dagger
\left[(H\otimes I_E)W-WH\right]P.
\qquad\text{(8)}
$$

Operators supported away from $B$ intertwine with the local map $W$. Thus the bracket in (8) equals

$$
(H_B\otimes I_E)W-WH_B,
$$

and $L$ is supported on $C$. Since $\Vert V\Vert=1$, any scalar shift of $H_B$ cancels from this bracket, and (7) gives

$$
\Vert L\Vert\le2h_B\Vert W\Vert
\le\frac{2h_Bq}{\sqrt{\lambda_B}}.
\qquad\text{(9)}
$$

The purpose of $L$ is an expectation identity, not an operator identity with the channel's full energy-change observable. For every operator $X$ supported on Alice's region,

$$
\langle XL\rangle
=\left\langle X\left(\mathcal E^{\ast}(H)-H\right)\right\rangle.
\qquad\text{(10)}
$$

To verify (10), first remove the exterior support projectors in the expectation using $P|\Omega\rangle=|\Omega\rangle$ and $[X,P]=0$. Next use

$$
W|\Omega\rangle
=V|\Omega\rangle-|\Omega\rangle\otimes|a\rangle,
\qquad H|\Omega\rangle=0.
$$

The right-hand action of the bracket in (8) is then
$(H\otimes I_E)V|\Omega\rangle$. Consequently,

$$
\langle XL\rangle
=\langle XV^\dagger(H\otimes I_E)V\rangle
=\left\langle X\sum_jK_j^\dagger HK_j\right\rangle.
$$

Subtracting $\langle XH\rangle=0$ establishes (10). Although $H$ itself can overlap Alice, its channel-induced difference is supported on $C$, which is disjoint from Alice. This is why the actual postmeasurement energy change can be represented by (10).

Taking $X=I$ gives $\mathrm{Tr}(\omega_CL)=Q$. Taking $X=E_m$, using the conditional-state identity in the model, gives

$$
\mathrm{Tr}(\sigma_mL)
=\mathrm{Tr}\left[\rho_m\left(\mathcal E^{\ast}(H)-H\right)\right].
\qquad\text{(11)}
$$

The operator $L$ need not be Hermitian. The specific expectations in (11) are real because they equal physical energy changes. Equivalently, one can use $(L+L^\dagger)/2$, whose norm is no larger than $\Vert L\Vert$.

### 4. Optimize cost against response

Apply (5), (9), and (11) to the channel chosen in outcome $m$. Hölder's inequality gives

$$
\begin{aligned}
g_m
&=-Q-\mathrm{Re}\mathrm{Tr}(\delta_mL)\\
&\le-\kappa_Bq^2+
\frac{2h_B}{\sqrt{\lambda_B}}\Vert\delta_m\Vert_1q\\
&\le\frac{h_B^2}{\kappa_B\lambda_B}\Vert\delta_m\Vert_1^2.
\end{aligned}
\qquad\text{(12)}
$$

The last line maximizes a concave quadratic over $q\ge0$. Allowing $q\gt 1$ only enlarges the upper bound. If $q=0$, then $W=0$, and the same identity shows that the channel produces no conditioned energy change. Thus zero-cost directions associated with an unoccupied local subspace do not create a linear-response loophole.

Averaging (12) proves the first inequality in (2). Quantum Pinsker's inequality, with natural logarithms, states

$$
\Vert\sigma_m-\omega_C\Vert_1^2
\le2D(\sigma_m\Vert\omega_C).
$$

The weighted sum of these relative entropies is $I(M:C)$. Finally, the measurement map on $A$ is a local channel from $A$ to the classical record $M$, so data processing gives
$I(M:C)\le I(A:C)_\omega$. These standard information inequalities are reviewed in [Watrous](../references/RELATED_WORK.md#watrous2018). This proves (2).

## Consequences for connected correlations and spatial decay

The conditional trace-norm estimate also controls the energy through the square of the ground state's bounded-observable connected correlation $\mathcal C(A:C)$. Let $r_A=\mathrm{rank}(\omega_A)$ and $\lambda_A=\lambda_{\min}^{+}(\omega_A)$. The support-compressed effect argument in [Correlation bounds](correlation_bounds.md) gives

$$
E_{\mathrm{ext}}
\le\frac{h_B^2r_A}{\kappa_B\lambda_A\lambda_B}\mathcal C(A:C)^2.
$$

This result has no minimum measurement-outcome probability. With a uniform envelope $\mathcal C(A:C)\le C_0e^{-d(A,C)/\xi}$ and uniformly controlled coefficients, it squares that envelope. The complete definition, proof, and qualifications are given in the linked document. In particular, the claim concerns a supplied valid envelope, not an identified optimal physical correlation length.

## Relation to existing results

The mathematical derivation in this document is the contribution presented here. Its ingredients include established quantum-channel representations, local passivity, trace-norm duality, Pinsker's inequality, and data processing. The specific additional estimate is the support-compressed response bound (9), combined with the retained energy cost (5).

[Hotta's general information bound](../references/RELATED_WORK.md#hotta2013) already retains an unconditional feedback cost but bounds the relevant energy observable by a fixed norm. It yields a square-root-information upper bound on extracted energy. Earlier [two-qubit results](../references/RELATED_WORK.md#hotta2010) already relate extraction linearly to a model-specific consumed-entanglement quantity, and standard optimized QET rotations already produce quadratic weak-signal formulas. The claim here is the universal record-information and connected-correlation converse under the stated stiffness and support conditions.

[Alhambra et al.](../references/RELATED_WORK.md#alhambra2019) establish and characterize CP-local passivity. Their gap and Schmidt-spectrum considerations are structural predecessors of the present argument. [Haque's clustering bound](../references/RELATED_WORK.md#haque2026) treats general local measurements and unitary feedback and discards the nonpositive ground-state cost at an intermediate step. The retained-cost estimate here produces the squared-correlation consequence under explicit stiffness and local-conditioning hypotheses, and applies to CPTP feedback.

The effective-thermodynamic bound of [Itoh et al.](../references/RELATED_WORK.md#itoh2026) contains an additive athermality term as well as an information term. That additive term need not vanish when the remote record becomes independent. Equation (2) instead has zero offset because it uses global ground-state passivity. These comparisons do not imply that the different information quantities, energy observables, or hypotheses are interchangeable.
