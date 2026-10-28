# Exact examples and sharp exponents

Two different examples establish two different claims. A fixed three-qubit ground state with a weakening measurement has extracted energy proportional to record information. A four-qubit weak-link family has extracted energy proportional to the square of the state's connected correlations. Both examples have fixed local dimensions and a gap and local support eigenvalues bounded away from zero in the limit being taken.

These examples prove sharp exponents, not optimal coefficients. The second varies a coupling rather than a spatial distance, so it does not prove sharpness of an exponential distance bound. The optimized single-Pauli feedback calculation is an established QET ingredient, as discussed in [Hotta's work](../references/RELATED_WORK.md#hotta2010) and the [related-work comparison](../references/RELATED_WORK.md#hotta2013). The explicit families below accompany the general converse derived in [Energy and information](energy_information.md).

## A common rotation formula

Suppose Alice produces equiprobable outcomes $s=\pm1$, and Bob uses

$$
U_s(\theta)=e^{is\theta Y_B},\qquad Y_B^2=I.
$$

If the conditional states satisfy

$$
\mathrm{Tr}\left[\sigma_s(Y_BH_BY_B-H_B)\right]=C,
\qquad
i\mathrm{Tr}\left[\sigma_s[H_B,Y_B]\right]=sD,
$$

then the conditional increase in energy is independent of the outcome:

$$
\Delta E_s(\theta)=C\sin^2\theta+D\sin\theta\cos\theta.
\qquad\text{(S1)}
$$

For $C\gt 0$, the minimizing angle may be chosen as

$$
\theta_{\ast}=-\frac12\mathrm{atan2}(D,C),
$$

and the extracted energy is

$$
E_{\mathrm{rot}}
=\frac{\sqrt{C^2+D^2}-C}{2}
=\frac{D^2}{2(\sqrt{C^2+D^2}+C)}.
\qquad\text{(S2)}
$$

The second expression avoids cancellation when the signal $D$ is small. Equation (S2) optimizes this one-parameter rotation family. Neither sharpness claim requires it to be the globally optimal local feedback map, because an achieved gain already supplies a lower bound on the optimal extraction.

## 1. Linear dependence on record information

### Hamiltonian and ground state

Consider three qubits labeled $A,R,B$. Let

$$
n=|1\rangle\langle1|,\qquad
\sigma^+=|1\rangle\langle0|,\qquad
\sigma^-=|0\rangle\langle1|,
$$

and choose $J\gt 0$, $\mu=J/\sqrt2$. The physical Hamiltonian is

$$
H_{\mathrm{phys}}
=\mu(n_A+n_R+n_B)
-J\left(
\sigma_A^+\sigma_R^-+\sigma_A^-\sigma_R^+
+\sigma_R^+\sigma_B^-+\sigma_R^-\sigma_B^+
\right).
\qquad\text{(S3)}
$$

The one-excitation sector is the three-site hopping matrix. Its eigenvalues are
$\mu-\sqrt2J,\mu,\mu+\sqrt2J$. The two-excitation sector has eigenvalues
$2\mu-\sqrt2J,2\mu,2\mu+\sqrt2J$, and the zero- and three-excitation energies are $0$ and $3\mu$. Therefore the unique ground state is

$$
|\Omega\rangle
=\frac{|100\rangle+\sqrt2|010\rangle+|001\rangle}{2},
\qquad
E_0=-\frac{J}{\sqrt2},
\qquad
\Delta=\frac{J}{\sqrt2}.
\qquad\text{(S4)}
$$

The theorem uses $H=H_{\mathrm{phys}}-E_0I$, which has the same energy changes. Bob acts only on the last qubit, so

$$
H_B=\mu n_B-J(\sigma_R^+\sigma_B^-+\sigma_R^-\sigma_B^+),
\qquad C=\lbrace R,B\rbrace .
$$

Its four eigenvalues are
$\lbrace 0,\mu,-\mu,2\mu\rbrace $, giving the centered norm

$$
h_B=\frac{3J}{2\sqrt2}.
$$

The marginals on Alice and Bob have eigenvalues $3/4,1/4$, so
$\lambda_A=\lambda_B=1/4$. In particular, the global-gap version of the theorem has a coefficient independent of the measurement strength.

### Weak measurement and extracted energy

Alice uses the binary effects

$$
E_s=\frac{I+s tX_A}{2},\qquad 0\le t\le1.
\qquad\text{(S5)}
$$

These can be implemented by the positive Kraus operators $\sqrt{E_s}$. The probabilities are $p_s=1/2$. For an operator on $C$, its conditional expectation equals its expectation against $I+s tX_A$ in the ground state.

The ground state has definite excitation parity. Thus the expectation of $X_A$ times an even-parity operator on $C$ vanishes. This makes the quadratic cost independent of the outcome. Direct Pauli algebra gives

$$
\begin{aligned}
C
&=\langle Y_BH_BY_B-H_B\rangle\\
&=\mu\langle Z_B\rangle+J\langle X_RX_B\rangle
=\frac{3J}{2\sqrt2},\\[3pt]
D
&=t\,i\langle X_A[H_B,Y_B]\rangle\\
&=t\left[-\mu\langle X_AX_B\rangle
+J\langle X_AX_RZ_B\rangle\right]
=\frac{Jt}{2\sqrt2}.
\end{aligned}
\qquad\text{(S6)}
$$

The ground-state correlators used here are

$$
\langle Z_B\rangle=\frac12,\qquad
\langle X_RX_B\rangle=\frac1{\sqrt2},\qquad
\langle X_AX_B\rangle=\frac12,\qquad
\langle X_AX_RZ_B\rangle=\frac1{\sqrt2}.
$$

Substituting (S6) into (S2),

$$
E_{\mathrm{ext}}(t)
=\frac{J}{4\sqrt2}\left(\sqrt{9+t^2}-3\right)
=\frac{J}{24\sqrt2}t^2+O(t^4).
\qquad\text{(S7)}
$$

The corresponding angle is $\theta_{\ast}=-\tfrac12\arctan(t/3)$. All outcome probabilities are included in (S7).

### Record information

Across the bipartition $A:C$, write

$$
|\Omega\rangle
=\frac{\sqrt3}{2}|0\rangle_A|u\rangle_C
+\frac12|1\rangle_A|v\rangle_C,
$$

where

$$
|u\rangle=\frac{\sqrt2|10\rangle+|01\rangle}{\sqrt3},
\qquad |v\rangle=|00\rangle.
$$

In the orthonormal basis $(|u\rangle,|v\rangle)$, the conditional state is exactly

$$
\sigma_s=
\begin{pmatrix}
3/4 & s\sqrt3t/4\\
s\sqrt3t/4 & 1/4
\end{pmatrix}.
\qquad\text{(S8)}
$$

Its nonzero eigenvalues are

$$
\nu_\pm(t)=\frac{1\pm\sqrt{1/4+3t^2/4}}{2}.
$$

With binary entropy $b(x)=-x\ln x-(1-x)\ln(1-x)$,

$$
\begin{aligned}
I(M:C)
&=b(3/4)-b\left(\frac{1+\sqrt{1/4+3t^2/4}}{2}\right)\\
&=\frac{3\ln3}{8}t^2+O(t^4).
\end{aligned}
\qquad\text{(S9)}
$$

Combining (S7) and (S9),

$$
\boxed{
\lim_{t\to0}\frac{E_{\mathrm{ext}}(t)}{I(M:C)}
=\frac{J}{9\sqrt2\ln3}\gt 0.
}
\qquad\text{(S10)}
$$

The theorem supplies the matching $O(I(M:C))$ upper bound for arbitrary feedback with the same Hamiltonian. Therefore the exponent one in record information is sharp. This example does not make the ground-state mutual information $I(A:C)_\omega$ small: that state is fixed while Alice's measurement becomes weaker.

## 2. Quadratic dependence on state correlations

### Weakly joining two dimers

Take four qubits $0,1,2,3$, with Alice $A=\lbrace 0\rbrace $, Bob $B=\lbrace 3\rbrace $, and energy neighborhood $C=\lbrace 2,3\rbrace $. In fixed energy units, let

$$
H_{\mathrm{phys}}(t)
=-\sum_{j=0}^3Z_j-X_0X_1-tX_1X_2-X_2X_3.
\qquad\text{(S11)}
$$

At $t=0$, this is the sum of two identical dimer Hamiltonians. Put

$$
r=\sqrt5,\qquad k=r+2,\qquad N=10+4r=2rk.
$$

Each dimer has unique ground state

$$
|g\rangle=\frac{k|00\rangle+|11\rangle}{\sqrt N},
$$

energy $-r$, and excitation gap $r-1$. Thus

$$
|\Omega(0)\rangle=|g\rangle_{01}|g\rangle_{23},
\qquad \Delta(0)=r-1.
\qquad\text{(S12)}
$$

The marginals on sites $0$ and $3$ have

$$
\lambda_A(0)=\lambda_B(0)=\frac{1-2/r}{2}\gt 0.
\qquad\text{(S13)}
$$

The perturbation has norm $|t|$, so eigenvalue perturbation bounds give
$\Delta(t)\ge r-1-2|t|$. The unique ground state is analytic for sufficiently small $|t|$, and (S13) remains uniformly positive in a neighborhood of zero.

Bob changes

$$
H_B=-Z_3-X_2X_3,
\qquad h_B=\sqrt2,
$$

independently of $t$. The gap and support parameters entering the theorem therefore remain controlled as $t\to0$.

### Exact first-order ground-state derivative

Choose the analytic normalized ground state with
$\langle\Omega(0)|\Omega'(0)\rangle=0$. Because the perturbation is $-X_1X_2$, the derivative solves

$$
\left(H_{\mathrm{phys}}(0)+2rI\right)|\Omega'(0)\rangle
=X_1X_2|\Omega(0)\rangle.
\qquad\text{(S14)}
$$

The first-order ground energy shift vanishes by dimer parity. The source in (S14) lies in the odd-parity sector of each dimer. In the ordered basis

$$
(|0101\rangle,|0110\rangle,|1001\rangle,|1010\rangle),
$$

its components are $(k,k^2,1,k)/N$, and the restricted left-hand matrix is
$2rI-X\otimes I-I\otimes X$. Its inverse is exactly

$$
\left(2rI-X\otimes I-I\otimes X\right)^{-1}
=\frac{9}{16r}I
+\frac1{16}(X\otimes I+I\otimes X)
+\frac1{16r}X\otimes X.
\qquad\text{(S15)}
$$

Multiplication yields

$$
|\Omega'(0)\rangle
\longleftrightarrow
\left(
\frac18,\frac{4+3r}{40},\frac{-4+3r}{40},\frac18
\right).
\qquad\text{(S16)}
$$

All components outside this four-dimensional sector vanish.

### Feedback gain

Alice measures $X_0$ projectively. The ground state has definite total parity, so $\langle X_0\rangle=0$, the two outcomes have probability $1/2$, and the quadratic rotation cost does not depend on the outcome. Define

$$
C(t)=\langle Y_3H_BY_3-H_B\rangle_t,
\qquad
D(t)=i\langle X_0[H_B,Y_3]\rangle_t.
$$

At $t=0$,

$$
C(0)=2\langle Z_3+X_2X_3\rangle_0=\frac6r,
\qquad D(0)=0.
$$

For any fixed Hermitian observable $O$, its derivative is
$2\mathrm{Re}\langle\Omega'(0)|O|\Omega(0)\rangle$. Using (S16),

$$
\left.\frac{d\langle X_0X_3\rangle_t}{dt}\right|_0
=\frac3{5r},
\qquad
\left.\frac{d\langle X_0X_2Z_3\rangle_t}{dt}\right|_0
=\frac7{10r}.
\qquad\text{(S17)}
$$

Since

$$
iX_0[H_B,Y_3]=-2X_0X_3+2X_0X_2Z_3,
$$

these derivatives give

$$
D'(0)=\frac1{5r}.
\qquad\text{(S18)}
$$

The opposite commutator convention $i\langle X_0[Y_3,H_B]\rangle$ has derivative $-1/(5r)$; the extracted energy is unaffected by this sign convention.

Applying (S2) and expanding at $D=0$,

$$
\boxed{
E_{\mathrm{ext}}(t)
=\frac{D'(0)^2}{4C(0)}t^2+o(t^2)
=\frac{t^2}{600\sqrt5}+o(t^2).
}
\qquad\text{(S19)}
$$

This is an achieved gain from an explicit measurement and a local unitary protocol. It supplies a lower bound on the optimum over all local channels.

### Connected correlations are linear in the weak link

At $t=0$, the ground state factorizes between the two dimers, so
$\omega_{AC}(0)=\omega_A(0)\otimes\omega_C(0)$. Analyticity in finite dimension implies

$$
\left\Vert\omega_{AC}(t)-\omega_A(t)\otimes\omega_C(t)\right\Vert_1
=O(|t|).
$$

This trace norm upper-bounds $\mathcal C(A:C)$, giving the upper estimate $O(|t|)$. Total parity also implies $\langle X_0\rangle_t=\langle X_3\rangle_t=0$. Taking $X=X_0$, $Y=X_3$ in the correlation definition and using (S17) gives

$$
\mathcal C(A:C)
\ge|\langle X_0X_3\rangle_t|
=\frac3{5\sqrt5}|t|+o(|t|).
$$

Therefore

$$
\boxed{
\mathcal C(A:C)=\Theta(|t|),\qquad
E_{\mathrm{ext}}(t)=\Theta(\mathcal C(A:C)^2).
}
\qquad\text{(S20)}
$$

Together with the uniform converse, (S20) rules out a general upper bound that is of smaller order than the square of connected correlations under the same fixed-parameter conditions. It neither fixes the best prefactor nor substitutes for a family in which distance tends to infinity.

## Reproducible checks

[The verification script](../verification/check_energy_information.py) checks the exact spectra, conditional states, feedback energy changes, entropy expression, perturbative resolvent, and first-order derivatives. It separately tests the compressed energy-change identity for genuinely nonunitary channels, random complete instruments, rare outcomes, and rank-deficient local ground-state marginals. Those finite numerical checks diagnose algebra and implementation errors; the proofs above establish the claims without relying on numerical fits.
