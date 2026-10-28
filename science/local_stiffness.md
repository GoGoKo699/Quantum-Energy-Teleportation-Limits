# Local excitation stiffness

The energy–information bound depends on the energetic cost of an operation near Bob. For a unique ground state, a global spectral gap supplies one lower bound on that cost. A finite matrix of local expectation values can supply a stronger bound, including in a critical system whose global gap closes.

This note defines that matrix without discarding physical zero modes, explains its role for arbitrary local quantum channels, and evaluates it exactly for a single receiver site in the periodic critical Ising chain. The main energy–information proof is in [energy_information.md](energy_information.md).

## 1. Definition on all local operators

Let $H$ be a finite-dimensional Hamiltonian and let $|\Omega\rangle$ be a normalized pure ground state with energy $E_0$. Write $\widetilde H=H-E_0I\geq0$. Expectation brackets refer to $|\Omega\rangle$. For arbitrary, possibly non-Hermitian operators $O_1,O_2$ on Bob's region $B$, define

$$
G_B(O_1,O_2)=\langle O_1^\dagger O_2\rangle
-\langle O_1^\dagger\rangle\langle O_2\rangle,
\qquad
K_B(O_1,O_2)=\langle O_1^\dagger\widetilde H O_2\rangle.
$$

Both are positive semidefinite Hermitian forms. They are the Gram forms of the vectors

$$
(O-\langle O\rangle)|\Omega\rangle,
\qquad
\widetilde H^{1/2}O|\Omega\rangle,
$$

respectively. The local excitation stiffness is

$$
\boxed{\displaystyle
\kappa_B=\inf_{O:\,G_B(O,O)>0}
\frac{K_B(O,O)}{G_B(O,O)}.}
\tag{1}
$$

The optimization includes complex coefficients in a local operator basis. Restricting $O$ to Hermitian generators can give a larger constant that need not be valid for the Kraus operators of a channel. If $G_B$ is identically zero, all local operations are trivial on the reference vector; the inequality below holds with any positive constant. Otherwise the infimum is a minimum because the quotient space is finite dimensional.

### The quotient and its kernel

Let $P_B=\operatorname{supp}\omega_B$, where $\omega_B$ is the ground-state marginal. A Schmidt decomposition across $B$ and its complement gives

$$
G_B(O,O)=0
\quad\Longleftrightarrow\quad
O|\Omega\rangle=\langle O\rangle|\Omega\rangle
\quad\Longleftrightarrow\quad
OP_B=\langle O\rangle P_B.
\tag{2}
$$

Every such direction is also in the kernel of $K_B$. Thus $K_B$ descends to the quotient by $\ker G_B$. Only these zero-variance directions are removed. A direction with $G_B(O,O)>0$ and $K_B(O,O)=0$ remains in the quotient and makes $\kappa_B=0$. This can happen when a local operator takes the reference state into a different ground state.

Rank deficiency of $\omega_B$ does not justify restricting the output of $O$ to $P_B$. Operators taking $P_B$ into $P_B^\perp$ can have positive variance and excitation energy, and they are included in (1). Equation (2) removes operators that are scalar on the occupied input support, including operators that annihilate that support.

For a unique ground state with gap $\Delta>0$,

$$
\widetilde H\geq\Delta(I-|\Omega\rangle\langle\Omega|)
\quad\Longrightarrow\quad K_B\geq\Delta G_B,
\quad\text{so}\quad \kappa_B\geq\Delta.
\tag{3}
$$

A positive $\kappa_B$ can also hold without a unique global ground state. Its defining requirement is that no nontrivial local operator on $B$ creates a different zero-energy vector from the chosen reference state. In a finite system this requirement is equivalent to $\ker K_B=\ker G_B$.

### Generalized eigenvalue computation

Choose any spanning local operator basis $\{F_i\}$, with complex coefficients allowed. Set

$$
G_{ij}=G_B(F_i,F_j),\qquad K_{ij}=K_B(F_i,F_j).
$$

Let $R$ be an isometry onto the positive-eigenvalue subspace of $G$, and put $G_+=R^\dagger GR$, $K_+=R^\dagger KR$. Then

$$
\kappa_B=\lambda_{\min}\!\left(G_+^{-1/2}K_+G_+^{-1/2}\right).
\tag{4}
$$

The minimum in (4) includes zero eigenvalues of the displayed matrix. Taking its smallest *positive* eigenvalue would change the claim. Null directions of $G$ cause no ambiguity because they are also null directions of $K$. A change of operator basis changes the matrices but not the Rayleigh quotient (1).

Write $H=H_B+H_{\rm rest}$, where $H_{\rm rest}$ acts trivially on $B$ and $H_B$ contains the Hamiltonian terms that Bob can change. If $C$ contains their support, then

$$
K_{ij}=\langle F_i^\dagger[H,F_j]\rangle
=\langle F_i^\dagger[H_B,F_j]\rangle.
\tag{5}
$$

Consequently $G$ depends only on $\omega_B$, and $K$ depends only on $\omega_C$ and $H_B$. The commutator expression is Hermitian as a matrix of expectation values because it equals the positive form in its definition.

## 2. Why the same constant applies to a channel

Let a channel on $B$ have Kraus operators $V_j$, with $\sum_jV_j^\dagger V_j=I$. Define

$$
c_j=\langle V_j\rangle,
\qquad q^2=1-\sum_j|c_j|^2
=\sum_jG_B(V_j,V_j).
$$

Its energy cost on the reference state is

$$
Q=\sum_j\langle V_j^\dagger\widetilde H V_j\rangle
=\sum_jK_B(V_j,V_j)\geq\kappa_Bq^2.
\tag{6}
$$

This is the restoring-cost inequality used in the main proof. With $\lambda_B=\lambda_{\min}^+(\omega_B)$ and the centered local norm

$$
h_B=\inf_{a\in\mathbb R}\|H_B-aI\|
=\frac{\lambda_{\max}(H_B)-\lambda_{\min}(H_B)}2,
$$

that proof gives

$$
E_{\rm ext}\leq
\frac{h_B^2}{\kappa_B\lambda_B}
\sum_m p_m\|\sigma_m-\omega_C\|_1^2
\leq\frac{2h_B^2}{\kappa_B\lambda_B}I(M:C).
\tag{7}
$$

Here Alice acts outside $C$, $\sigma_m$ is the conditional state on $C$, and Bob may choose any channel on $B$ after receiving outcome $m$. The quantity $E_{\rm ext}$ is the decrease in system energy caused by Bob. The energetic cost of his controller is a separate ledger.

## 3. A periodic critical Ising chain

Consider every integer $N\geq4$, including odd $N$, with periodic boundary conditions:

$$
H_N(h)=-J\sum_{j=0}^{N-1}X_jX_{j+1}
-h\sum_{j=0}^{N-1}Z_j,
\qquad X_N=X_0,\qquad J,h>0.
\tag{8}
$$

The critical point is $h=J$. The exact Ising solution supplies the dispersion and critical local correlators [Pfeuty1970](../references/RELATED_WORK.md#pfeuty1970). We retain the fermion parity condition below to derive the finite-ring formulas rather than applying a thermodynamic boundary approximation.

### Unique ground state and parity

In the simultaneous $X$ basis, the interaction in (8) is diagonal and each $-hZ_j$ flips one basis spin with a strictly negative matrix element. These flips connect the entire basis graph. Perron–Frobenius, applied after a scalar shift to a nonnegative irreducible matrix, therefore gives a unique ground state with strictly positive coefficients in that basis.

The spin parity $\mathcal P=\prod_jZ_j$ commutes with $H_N$ and permutes each $X$-basis configuration with its global flip. Uniqueness makes the ground state a parity eigenvector. Positivity of its coefficients excludes eigenvalue $-1$, so its parity is $+1$.

Define Jordan–Wigner fermions by

$$
c_j=\left(\prod_{\ell<j}Z_\ell\right)\frac{X_j+iY_j}{2},
\qquad n_j=c_j^\dagger c_j=\frac{I-Z_j}{2}.
$$

For a nonboundary bond, $X_jX_{j+1}=(c_j^\dagger-c_j)(c_{j+1}^\dagger+c_{j+1})$. The boundary bond carries the factor $-\mathcal P$, so the same quadratic expression applies to all bonds with $c_N=-\mathcal P c_0$. In a fixed parity sector,

$$
H_N=-J\sum_{j=0}^{N-1}(c_j^\dagger-c_j)(c_{j+1}^\dagger+c_{j+1})
-Nh+2h\sum_{j=0}^{N-1}n_j.
$$

Thus the even-parity sector has antiperiodic momenta

$$
\mathcal K_+=\left\{\frac{(2n+1)\pi}{N}:n=0,\ldots,N-1\right\},
\qquad
\epsilon_k(h)=2\sqrt{J^2+h^2-2Jh\cos k}.
\tag{9}
$$

Modes at $k$ and $-k$ are paired by the Bogoliubov transformation and contribute even fermion parity in their vacuum. When $N$ is odd, $\mathcal K_+$ also contains the unpaired mode $k=\pi$; its coefficient $h+J$ is positive, so it is empty in the vacuum. This vacuum has even parity for both even and odd $N$ and is the unique ground state identified above. Its energy is

$$
E_+(h)=-\frac12\sum_{k\in\mathcal K_+}\epsilon_k(h)
=-\sum_{n=0}^{N-1}\sqrt{J^2+h^2-2Jh\cos\frac{(2n+1)\pi}{N}}.
\tag{10}
$$

### Critical energy, gap, and local means

Put $x_N=\pi/(2N)$. At $h=J$, the elementary sums

$$
\sum_{n=0}^{N-1}\sin[(2n+1)x_N]=\csc x_N,
\qquad
\sum_{n=0}^{N-1}\sin(2nx_N)=\cot x_N
$$

give

$$
E_+(J)=-2J\csc x_N.
\tag{11}
$$

The odd-parity sector has periodic momenta $2\pi n/N$. Its $k=0$ mode has zero energy at criticality and can be occupied to satisfy odd parity. Its lowest energy is therefore $E_-(J)=-2J\cot x_N$. Excitations within the even sector require two quasiparticles; their lowest cost is $8J\sin x_N$, which exceeds $E_--E_+$. The global gap is consequently

$$
\Delta_N=E_-(J)-E_+(J)
=2J\tan\frac{\pi}{4N}\longrightarrow0.
\tag{12}
$$

Translation symmetry and Hellmann–Feynman differentiation of (10) give

$$
m_N=\langle Z_b\rangle
=-\frac1N\left.\frac{\partial E_+(h)}{\partial h}\right|_{h=J}
=\frac{1}{N\sin(\pi/(2N))}.
\tag{13}
$$

The dispersion is symmetric in $h,J$, so differentiation with respect to $J$, holding $h$ fixed before setting $h=J$, also gives

$$
\langle X_bX_{b+1}\rangle=m_N.
\tag{14}
$$

Ground-state parity gives $\langle X_b\rangle=\langle Y_b\rangle=0$. All these formulas hold for odd and even rings. In the limit,

$$
m_N\longrightarrow m_0=\frac2\pi.
\tag{15}
$$

### Exact all-operator stiffness

Let Bob control site $b$. All local operators have the form

$$
O=aI+v_xX_b+v_yY_b+v_zZ_b,
\qquad a,v_x,v_y,v_z\in\mathbb C.
$$

The scalar component lies in $\ker G_B$. On the remaining Pauli basis, equations (5), (13), and (14) give

$$
G_N=\begin{pmatrix}
1&im_N&0\\
-im_N&1&0\\
0&0&1-m_N^2
\end{pmatrix},
\qquad
K_N=J\begin{pmatrix}
2m_N&2i&0\\
-2i&6m_N&0\\
0&0&4m_N
\end{pmatrix}.
\tag{16}
$$

For instance,

$$
[H_B,Y_b]=-2iJ(X_{b-1}Z_b+Z_bX_{b+1})+2iJX_b.
$$

Multiplication by $Y_b$ gives $K_{yy}=6Jm_N$. Multiplication by $X_b$ gives $K_{xy}=2iJ$: the remaining expectations contain a single $Y$ and vanish because the ground state can be chosen real. The $xz$ and $yz$ entries vanish by parity. This accounts for the complex entries, which matter for non-Hermitian Kraus operators.

The eigenvalues of $G_N$ are $1\pm m_N$ and $1-m_N^2$, all positive. The three generalized eigenvalues are

$$
\kappa_\pm(m_N)=
\frac{2J\left[m_N\pm\sqrt{1-3m_N^2+3m_N^4}\right]}{1-m_N^2},
\qquad
\kappa_z(m_N)=\frac{4Jm_N}{1-m_N^2}.
\tag{17}
$$

The local stiffness is their minimum, $\kappa_N=\kappa_-(m_N)$. Its limit is

$$
\boxed{\displaystyle
\kappa_*=
\frac{2J\left[2/\pi-\sqrt{1-12/\pi^2+48/\pi^4}\right]}{1-4/\pi^2}
=0.37125191\ldots\,J>0.}
\tag{18}
$$

For unitary feedback alone one can use a larger constant. Writing $U=e^{i\alpha}(\cos\theta\,I+i\sin\theta\,\boldsymbol n\cdot\boldsymbol\sigma)$ with a real unit vector $\boldsymbol n$, its variance and cost are

$$
G_B(U,U)=\sin^2\theta(1-m_N^2n_z^2),
\quad
K_B(U,U)=2Jm_N\sin^2\theta(n_x^2+3n_y^2+2n_z^2).
$$

Their minimum ratio is $2Jm_N$, attained for $\boldsymbol n$ along $x$. The channel bound uses the smaller all-operator value (17).

### A uniform bound for every $N\geq4$

Since $x/\sin x$ increases for $0<x<\pi/2$,

$$
m_0<m_N\leq m_4=\frac{1}{4\sin(\pi/8)}<1.
\tag{19}
$$

Set $\eta=\kappa_*/J$. At $m=m_0$, the determinant of the $xy$ block of $K/J-\eta G$ is zero. At general $m$ that determinant is

$$
F(m,\eta)=(12-\eta^2)m^2-4\eta m+\eta^2-4.
\tag{20}
$$

One has $0<\eta<2m_0<2$. Positivity follows from

$$
m_0^2-(1-3m_0^2+3m_0^4)
=(1-m_0^2)(3m_0^2-1)>0;
$$

the upper bound follows from

$$
1-3m_0^2+3m_0^4-m_0^6=(1-m_0^2)^3>0.
$$

For $m\geq m_0$,

$$
\partial_mF=2(12-\eta^2)m-4\eta
>16m_0-8m_0>0.
$$

The leading diagonal entry $2m-\eta$ is positive, and the $z$ entry $4m-\eta(1-m^2)$ is positive. Thus $K_N-\kappa_*G_N\geq0$ for every $N\geq4$, proving the uniform bound

$$
\kappa_N\geq\kappa_*>0.
\tag{21}
$$

### Local norm and support conditioning

The energy Bob can change is

$$
H_B=-JZ_b-JX_b(X_{b-1}+X_{b+1}),
\qquad C=\{b-1,b,b+1\}.
$$

The two neighbors are distinct for $N\geq4$. Their $X$ operators commute, and the two Pauli components on $b$ anticommute. The spectrum of $H_B$ is symmetric about zero. Therefore

$$
H_B^2=J^2\big[I+(X_{b-1}+X_{b+1})^2\big],
\qquad h_B=\|H_B\|=\sqrt5\,J.
\tag{22}
$$

Also $\omega_B=(I+m_NZ_b)/2$, so

$$
\lambda_{B,N}=\frac{1-m_N}{2}
\geq\frac{1-m_4}{2}>0,
\qquad
\lambda_{B,N}\longrightarrow\frac{1-2/\pi}{2}=0.18169011\ldots.
\tag{23}
$$

Equations (21)–(23) make the coefficient in (7) uniformly finite across all rings. Its exact limiting value is

$$
\frac{2h_B^2}{\kappa_*\lambda_{B,\infty}}
=\frac{10J^2}{\kappa_*[(1-2/\pi)/2]}.
\tag{24}
$$

The global-gap coefficient obtained by replacing $\kappa_N$ with $\Delta_N$ instead diverges with $N$.

## 4. Thermodynamic scope and verification

The result is a uniform sequence of finite-volume inequalities. For fixed finite Alice and Bob regions, any thermodynamic limit of their reduced states preserves (7): local energy expectations converge, and the mutual information of the fixed-dimensional classical–quantum output of any fixed finite-outcome instrument is continuous. Thus the limiting Ising state inherits a finite energy–information coefficient without requiring a gapped infinite-volume Hamiltonian.

This calculation establishes the local coefficient. A consequence for spatial decay additionally requires a correlation envelope for the full operator classes on Alice's region and $C$; see [correlation_bounds.md](correlation_bounds.md). A single spin correlator does not establish that envelope.

The standalone [check_critical_ising.py](../verification/check_critical_ising.py) uses only NumPy. It diagonalizes rings of sizes $4,5,6,8$, including an odd ring to check the parity boundary condition. It compares the ground energy, exact gap, parity, local reduced spectrum, local matrices, and generalized eigenvalues with the formulas above. It also checks the three-site norm in (22) and the uniform matrix inequality (21). The script prints one JSON object and exits nonzero on a failed check. Its output is a normalization and boundary-condition check; the all-$N$ claims follow from the analytic derivation.
