# A finite-parameter principle and the exact resolution of Guadalupe's congruences

Status: complete candidate proof, awaiting independent review. All finite checks below are certified by an existing theorem, not extrapolation from numerical data.

## 1. Statements

Put f_j(q)=product_{n>=1}(1-q^{jn}), H=f_2/f_1^3, and D_k=H^k/f_1=sum d_k(n)q^n. All series have integer coefficients and constant term 1.

For every c,n>=0 the following congruences hold:

| k | index | modulus |
|---|---|---|
|125c+58|25n+16|125|
|125c+83|125n+41,91|125|
|125c+100|125n+124|125|
|125c+5|125n+69,119|125|
|125c+30|125n+69|125|
|125c+60|125n+14,64,89,114|125|
|125c+58|125n+91|625|
|125c+58|125n+66,116|625|

Moreover, for a fixed c>=0, either (equivalently, both) of the assertions

    d_(125c+58)(125n+66)=0 mod3125 for every n>=0,
    d_(125c+58)(125n+116)=0 mod3125 for every n>=0

holds if and only if c=0 or2 mod5. Thus the first seven lines of Guadalupe [G, Conjecture7.1] are proved. Its last line, which asserts the 3125 congruences without the condition on c, is false and is replaced by an exact classification. The counterexample c=1,n=0 has d_183(66)=2500 mod3125.

This is one coherent paper, not a separate paper for each congruence.

## 2. Finite-parameter principle

Let p be prime, s,v positive integers, m>=1, r in [0,m), and R=Z[[q]]. Let F,A be in R and B in 1+q^m Z[[q^m]]. Suppose A/B=1+p^v C for C in R. Put L=ceil(s/v). If the coefficients in degrees congruent to r modulo m of F A^j vanish modulo p^s for every j=0,...,L-1, then they vanish for every j>=0.

Proof. Multiplication by B or B^(-1) preserves the submodule of series whose r-th residue component is zero modulo p^s. Consequently the hypothesis holds for F(A/B)^j. By the integer binomial identity it holds for F(A/B-1)^j for all j<L. For j>=L, this entire series is divisible by p^s. For every c>=0 expand F(A/B)^c by the binomial theorem and multiply by B^c. Every summand has zero r-th residue component. This proves the assertion. No division by j! or any nonunit occurs.

Applications: Freshman's dream, valid coefficientwise for any integer unit series H, gives H(q)^125/H(q^125)=1 mod5. Therefore for the modulus5^s and either m=25 or125, the parameter progression k=a+125c requires only c=0,...,s-1. For k=a+625c and m=125, choose A=H^625, B=H(q^125)^5. Writing H^125/H(q^125)=1+5C, the binomial theorem gives A/B=(1+5C)^5=1 mod25. Consequently only c=0,1,2 are required modulo3125.

## 3. Exact finite criterion used for the base cases

The following is the Radu–Sellers finite criterion, as stated in Tang [T, Lemma7]. Its full admissibility conditions are [B, Definition4.1]. The criterion and cusp representative assertion also appear together in [B, Lemmas4.2--4.3]. We specify them to make the certificate independently auditable.

For r=(r_delta) indexed by divisors of M, define c_r(n) by product f_delta^r_delta=sum c_r(n)q^n, put kappa=gcd(m²-1,24), and

    P_(m,r)(t)={ ts+(s-1)/24 sum delta*r_delta mod m :
                  s is a unit square modulo24m }.

Every such s is1 mod24, so the displayed quotient is integral. The set is represented in [0,m).

A tuple (m,M,N,t,r) belongs to Delta* if (1) every prime divisor of m divides N; (2) every delta>1 with r_delta!=0 divides mN; (3) kappa*N*sum r_delta*(m*N/delta)=0 mod24; (4) kappa*N*sum r_delta=0 mod8; (5) 24m/gcd(kappa*(-24t-sum delta*r_delta),24m) divides N; and (6) the additional even-m alternative in [B]. Here m is odd, so (6) is vacuous.

For gamma=[[a,b],[c,d]], set

    p_(m,r)(gamma) = min_(0<=lambda<m) (1/24)
       sum r_delta*gcd(delta*(a+kappa*lambda*c),m*c)^2/(delta*m),
    p*_a(gamma) = (1/24) sum a_delta*gcd(delta,c)^2/delta.

Let gamma_i represent Gamma_0(N)\SL_2(Z)/Gamma_infinity. If a is an integer exponent vector with p_(m,r)(gamma_i)+p*_a(gamma_i)>=0 at every representative, put

    nu = ((sum r_delta+sum a_delta)*index(Gamma_0(N))
           -sum delta*a_delta)/24
           -sum delta*r_delta/(24m)-min(P)/m.

If c_r(mn+t')=0 mod u for every t' in P and 0<=n<=floor(nu), then the congruence holds for all n>=0 and every t' in P. The modulus u can be any positive integer, in particular a prime power.

Our use has M=N=10, index18, and the four representatives gamma_c=[[1,0],[c,1]] for c=1,2,5,10. The squarefree-N representative result is [B, Lemma4.3], credited there to Radu--Sellers.

For a requested coefficient modulus u=5^s, take J=ceil((3k+1)/u) and

    r=(uJ-3k-1, k, -uJ/5, 0), indexed by1,2,5,10.

Then f_1^u=f_5^(u/5) modulo u implies c_r(n)=d_k(n) modulo u for every n. This binomial congruence for products and inverses follows from (1-X)^(5^s)=(1-X^5)^(5^(s-1)) mod5^s, by induction. Its use introduces no rational coefficients.

We have sum delta*r_delta=-k-1. Conditions1--4 above hold immediately because kappa=24 and M=N=10. For condition5, it is enough and necessary here that m/gcd(24t-k-1,m) divides10. Every base row passes this exact integer check; in fact m=25 or125 and 24t-k-1 is divisible by25.

The four scaled minima have the following closed forms (in cusp order1,2,5,10):

    24p = ( -m(5k+2)/50, -m(k+1)/25,
             -(5k+2)/(2m), -(k+1)/m ).

For cusp1 let g=gcd(1+24lambda,m). If g<m, then gcd(5(1+24lambda),m)=5g, so the scaled sum is -g²(5k+2)/(2m), minimized at g=m/5. If g=m, the scaled sum is m((24/25)uJ-(5k+2)/2), positive since uJ>=3k+1 and k>=1. The same argument at cusp2, using that1+48lambda is odd, gives -g²(k+1)/m for g<m and a positive value for g=m. At cusps5,10 the number1+24lambda*c is coprime to5, giving the last two values directly. Each extremizing g=m/5 occurs because24 (respectively48) is a unit modulo m. The most negative entry is the first, hence A=ceil(m(5k+2)/50).

The code computes all four minima as exact Fractions over all m possible lambda. It sets a=(A,0,0,0), where A=max(0,ceil(-24 min p_(m,r))). Then p*_a=A/24, proving every cusp inequality by construction. For these rows, the resulting A also equals ceil(m(5k+2)/50). All nu and floors are computed as exact rational numbers, not floating point.

The complete records are check-results.json, including the exponent vector, orbit P, all four scaled cusp minima, A, exact nu, bound, largest checked coefficient, and zero-test counts. The script certificates.py independently rebuilds each certificate from k,m,t,s.

## 4. Base cases and complete sufficiency proof

For the first six displayed rows, use the three k values a,a+125,a+250, modulus125. For the seventh and eighth rows, use a=58 and four values58,183,308,433, modulus625. For the exact3125 classification use the two families k=58+625c and k=308+625c, each at c=0,1,2. Their orbits P are {66,116}; every required base series is zero in these progressions through its Radu bound. Thus the criterion proves all base cases for every coefficient. Section2 then proves the infinite parameter families.

The executable proof check is check_congruences.py. It computes Euler's series exactly by the pentagonal theorem, in the finite ring (Z/uZ)[q]/(q^L), forms its inverse using constant coefficient1, computes H and then D_k, and tests exactly the coefficients required by the criterion. All arithmetic is integer modular arithmetic using python-flint0.9.0. No floating point arithmetic is used in the mathematical check. The largest coefficient index is1,901,366. No numerical truncation assumption is made: multiplication, inversion and exponentiation in the quotient ring give precisely the first L coefficients of the infinite formal series.

## 5. Necessity and the exact obstruction (credited to Patel)

The two identities and counterexample in this section appeared in a MathDB solution by Shivam Patel [P], found during the final novelty audit. We independently checked them and include the argument for completeness, without claiming priority. The new content is the converse for all n and the other infinite congruences.

Let a(c)=d_(125c+58)(66) and b(c)=d_(125c+58)(116). Since these degrees are less than125, the factor H(q^125)^c is identically1 through the relevant degrees. Write V=H^125/H(q^125)=1+5C. Modulo3125, a(c) and b(c) are therefore integer linear combinations of binomial(c,j), 0<=j<=4. The five values at c=0,...,4 uniquely determine such a combination over Z/3125Z: the binomial evaluation matrix is unit lower triangular.

Independent exact-integer coefficient evaluation gives:

|c|a(c) mod3125|b(c) mod3125|
|--|--|--|
|0|0|0|
|1|2500|625|
|2|0|0|
|3|1875|1250|
|4|1875|1250|

These are respectively the values of625c(c-2) and -625c(c-2) modulo3125. Both polynomials lie in the indicated binomial span (c(c-2)=2 binomial(c,2)-binomial(c,1)). Consequently these identities hold for every c>=0. Either universal3125 congruence forces a(c)=0 or b(c)=0, and therefore forces c(c-2)=0 mod5. This gives c=0 or2 mod5. Section4 proves sufficiency, completing both equivalences.

For transparency, the five values are obtained without FLINT and without modular division by the exact integer recurrence

    d_k(0)=1,
    n*d_k(n)=sum_(j=1)^n ((3k+1)*sigma_1(j)
                       - 2k*1_(2|j)*sigma_1(j/2))*d_k(n-j).

It follows by formal logarithmic differentiation of D_k. The numerator is divided by n in Z, and divisibility is checked at every step. See check_initial.py and initial-checks.json, which save the complete integer values.

## Sources

[G] Russelle Guadalupe, The k-elongated plane partition function modulo small powers of5, arXiv:2504.08627v2 (2025), Conjecture7.1. https://arxiv.org/html/2504.08627v2 . Primary PDF saved as guadalupe-2025.pdf. The absence of a condition on c in the last line is confirmed in both HTML and PDF.

[T] Dazhao Tang, New Congruences for Broken k-Diamond Partitions, Journal of Integer Sequences21 (2018), Article18.5.8, Lemma7 and Section2.2. https://cs.uwaterloo.ca/journals/JIS/VOL21/Tang/tang13.pdf .

[B] Liuquan Wang, Arithmetic properties of (k,l)-regular bipartitions, Bulletin of the Australian Mathematical Society95 (2017),353--364, Definition4.1 and Lemmas4.2--4.3, DOI10.1017/S0004972716000964. https://doi.org/10.1017/S0004972716000964 .

[RS] S. Radu and J. A. Sellers, Parity results for broken k-diamond partitions and (2k+1)-cores, Acta Arithmetica146 (2011),43--52, Lemma1.8. Primary article https://www.impan.pl/shop/en/publication/transaction/download/product/82220 . This differs from their pod-function paper cited as reference10 in [T].

[R] S. Radu, An algorithmic approach to Ramanujan's congruences, Ramanujan Journal20 (2009),215--251. Primary 2008 preprint URL appeared in search but direct retrieval returned404; do not claim that inaccessible file was read.

[P] Shivam Patel, Counterexample, solution attached to the MathDB entry Conjectural congruences for the k-elongated plane partition function modulo powers of5, displayed as posted one day before access on2026-09-08. https://mathdb.com/p/382381/conjectural-congruences-for-the-k-elongated-plane-partition . Primary author-posted proof of the two initial coefficient identities; no proof of the remaining conjectures or sufficiency for the surviving c classes.
