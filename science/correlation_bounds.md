# From connected correlations to an energy ceiling

The conditional-distance bound in [energy_information.md](energy_information.md) can be combined with a connected-correlation envelope. This gives a bound proportional to the square of that envelope, provided the ground-state marginals on the fixed measurement and receiver regions have uniform support conditioning. The proof treats rare measurement outcomes without a lower bound on their probabilities.

## 1. State, geometry, and the correlation hypothesis

Let $\omega=|\Omega\rangle\langle\Omega|$ be the reference ground state. Bob acts on $B$. Write $H_B$ for the sum of Hamiltonian terms that Bob can change, and let $C$ contain its support. Alice's region $A$ is disjoint from $C$. Set

$$
P_A=\mathrm{supp}\omega_A,
\qquad r_A=\mathrm{rank}\omega_A,
\qquad \lambda_A=\lambda_{\min}^+(\omega_A),
\qquad
\lambda_B=\lambda_{\min}^+(\omega_B).
$$

The marginal states can be rank deficient. For Hermitian operators $X$ on $A$ and $Y$ on $C$, assume the envelope

$$
\left|\mathrm{Tr}\omega_{AC}(X\otimes Y)
-\mathrm{Tr}(\omega_AX)\mathrm{Tr}(\omega_CY)\right|
\leq f(A,C)\,\Vert X\Vert\,\Vert Y\Vert.
\qquad\text{(1)}
$$

One can use any established upper bound $f(A,C)$; it need not be the smallest possible one. The norms in (1) are operator norms. Both operator classes include all bounded Hermitian operators supported on the stated regions. A bound proved for selected spin components alone does not meet this hypothesis.

Let $h_B=\inf_{a\in\mathbb R}\Vert H_B-aI\Vert$ be the centered local norm, or any larger certified upper bound on it. Let $\kappa_B>0$ be a valid all-operator local stiffness as defined in [local_stiffness.md](local_stiffness.md). The main theorem gives

$$
E_{\rm ext}\leq\frac{h_B^2}{\kappa_B\lambda_B}
\sum_m p_m\Vert\sigma_m-\omega_C\Vert_1^2.
\qquad\text{(2)}
$$

The receiver may use any outcome-dependent CPTP map, and the energy in (2) is the decrease in system energy caused by that map.

## 2. Conditional states depend only on Alice's effects

An arbitrary instrument on $A$ can have several Kraus operators $M_{m\alpha}$ for each recorded outcome $m$. Its effect is

$$
E_m=\sum_\alpha M_{m\alpha}^\dagger M_{m\alpha},
\qquad E_m\geq0,\qquad\sum_mE_m=I_A.
$$

Since $A$ and $C$ are disjoint, tracing out Alice after her operation gives

$$
p_m\mathrm{Tr}(\sigma_mY)
=\mathrm{Tr}\omega_{AC}(E_m\otimes Y),
\qquad p_m=\mathrm{Tr}(\omega_AE_m).
\qquad\text{(3)}
$$

This relation includes instruments that disturb Alice's state and effects of arbitrary rank. Outcomes with $p_m=0$ contribute nothing and can be omitted.

The joint state $\omega_{AC}$ is supported on $P_A\otimes I_C$. To see this, the positive operator $\omega_{AC}$ has zero trace against $(I_A-P_A)\otimes I_C$, so its range lies in the complementary kernel. Thus every expectation in (3) is unchanged when $E_m$ is replaced by

$$
\widetilde E_m=P_AE_mP_A.
$$

This compression does not enlarge Alice's spatial support. Since $\omega_A\geq\lambda_AP_A$ on its support,

$$
p_m=\mathrm{Tr}(\omega_A\widetilde E_m)
\geq\lambda_A\mathrm{Tr}\widetilde E_m
\geq\lambda_A\Vert\widetilde E_m\Vert.
\qquad\text{(4)}
$$

Equation (4) is the needed control of rare outcomes. Their effects shrink in norm in proportion to their probability when the local support spectrum is fixed.

## 3. The quadratic correlation bound

For a Hermitian $Y$ with $\Vert Y\Vert\leq1$, equations (1), (3), and (4) imply

$$
\begin{aligned}
\left|\mathrm{Tr}[(\sigma_m-\omega_C)Y]\right|
&=\frac1{p_m}\left|
\mathrm{Tr}\omega_{AC}(\widetilde E_m\otimes Y)
-p_m\mathrm{Tr}(\omega_CY)\right|\\
&\leq f(A,C)\frac{\Vert\widetilde E_m\Vert}{p_m}
\leq\frac{f(A,C)}{\lambda_A}.
\end{aligned}
$$

Trace-norm duality for the Hermitian operator $\sigma_m-\omega_C$ then gives the branchwise estimate

$$
\Vert\sigma_m-\omega_C\Vert_1\leq\frac{f(A,C)}{\lambda_A}.
\qquad\text{(5)}
$$

Averaging the preceding estimate before replacing the effect norm gives a stronger rank-weighted bound. Equations (1) and (3) first imply $p_m\Vert\sigma_m-\omega_C\Vert_1\leq f(A,C)\Vert\widetilde E_m\Vert$. Since $\sum_m\widetilde E_m=P_A$, equation (4) yields

$$
\begin{aligned}
\sum_m p_m\Vert\sigma_m-\omega_C\Vert_1^2
&\leq f(A,C)^2\sum_{m:p_m>0}
\frac{\Vert\widetilde E_m\Vert^2}{p_m}\\
&\leq\frac{f(A,C)^2}{\lambda_A}\sum_m\Vert\widetilde E_m\Vert\\
&\leq\frac{f(A,C)^2}{\lambda_A}\sum_m\mathrm{Tr}\widetilde E_m
=\frac{r_A}{\lambda_A}f(A,C)^2.
\end{aligned}
\qquad\text{(6)}
$$

Substitution into (2) proves

$$
\boxed{\displaystyle
E_{\rm ext}\leq
\frac{h_B^2r_A}{\kappa_B\lambda_A\lambda_B}
\,f(A,C)^2.}
\qquad\text{(7)}
$$

The number of outcomes and their individual probabilities do not appear. Positivity of the effects supplies the normalization without an outcome-probability floor. Since $r_A\lambda_A\leq1$, equation (7) is at least as strong as the coefficient $1/\lambda_A^2$ obtained by squaring (5) separately on every branch. The elementary bound $\Vert\sigma_m-\omega_C\Vert_1\leq2$ can also be combined with (6) if a bound at small separations is desired.

The theorem requires conditioning on Alice's occupied support. A fixed finite region has $\lambda_A>0$ in each finite system, but this alone does not provide a uniform lower bound across a family of states. The same qualification applies to $\lambda_B$ and $\kappa_B$.

## 4. Exponential clustering in a gapped spin system

For finite-range bounded spin interactions with a unique ground state and a positive spectral gap, exponential-clustering theorems bound connected correlations of bounded local operators. Relevant primary statements are Hastings–Koma, Theorem 2.8 and equation (2.19), specialized to a unique ground state, and Nachtergaele–Sims, Theorem 2 and equations (10)–(12), at zero imaginary time [HastingsKoma2006](../references/RELATED_WORK.md#hastingskoma2006), [NachtergaeleSims2006](../references/RELATED_WORK.md#nachtergaelesims2006). In the latter form, subtracting $\langle Y\rangle I$ satisfies the required ground-state orthogonality conditions; any resulting constant is included in the envelope.

For fixed finite regions and a uniformly bounded interaction family with a uniform gap, these results give an envelope of the form

$$
f(A,C)\leq C_{A,C}\,e^{-d(A,C)/\xi},
\qquad\text{(8)}
$$

with constants controlled by the interaction, gap, geometry, and support sizes. If $h_B$, $r_A$, $\kappa_B^{-1}$, $\lambda_A^{-1}$, $\lambda_B^{-1}$, and the clustering constants are uniformly bounded, equation (7) gives

$$
E_{\rm ext}\leq
\frac{h_B^2r_AC_{A,C}^2}{\kappa_B\lambda_A\lambda_B}
e^{-2d(A,C)/\xi}.
\qquad\text{(9)}
$$

Here the exponent is twice the exponent of the chosen valid clustering envelope. The clustering length $\xi$ need not equal an exact observable correlation length, and the inequality does not establish saturation of the energy exponent.

The natural distance is to $C$, because Bob can change interaction terms involving his neighbors. If every Hamiltonian term has diameter at most $R$ and $C$ is the union of terms meeting $B$, then

$$
d(A,C)\geq d(A,B)-R.
$$

Equation (9) can therefore be written using $d(A,B)$ after multiplying its prefactor by $e^{2R/\xi}$. Fixed $B$, finite interaction range, and bounded lattice coordination keep $C$ finite.

## 5. Scope at criticality

The critical Ising calculation in [local_stiffness.md](local_stiffness.md) proves that $\kappa_B$ and $\lambda_B$ remain bounded away from zero for a single-site receiver while the global gap closes. This keeps the energy–information theorem finite at criticality. A spatial bound at criticality additionally needs an envelope satisfying (1) for every operator on the chosen Alice region and the full interaction neighborhood $C$.

If such an envelope is established as $f(A,C)\leq C_{A,C}d(A,C)^{-\alpha}$, equation (7) gives an energy upper envelope proportional to $d(A,C)^{-2\alpha}$ under the same conditioning assumptions. This is a conditional implication. The present derivation does not replace the full operator-envelope hypothesis with a known asymptotic for one spin correlator, and it does not identify an exact optimal critical QET distance exponent.
