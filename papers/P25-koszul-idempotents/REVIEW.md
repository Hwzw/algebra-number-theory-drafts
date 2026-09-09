# Internal proof review

The proof was checked within this research session. No independent human referee or separate agent reviewed it.

1. **Presentation and hypotheses.** The quadrics have coprime leading monomials in lex order b>c>a>z. Distinct standard monomials map to distinct monomials in k[s,t], proving the presentation is a domain. Freeness over k[a,z] proves dimension two; height two gives the regular sequence. The classical quadratic Groebner criterion and the stated graded Morita functor establish Koszulness of the matrix algebra.
2. **Idempotence.** A determinant-one matrix over Z[x] gives the identity before substitution. Its square-through-fifth powers lie in R under x=st^3 z^r. Thus the identity descends to R in every characteristic. Exact checks also verify it directly in the quotient, independently of conjugation in the larger ring.
3. **Primitive complete system.** Both complementary images of the two-by-two matrix have rank one. Their endomorphism rings are R, so they are indecomposable over the domain. Embedding in larger matrices preserves this, and the remaining diagonal units complete the system.
4. **Tensor obstruction.** The two auxiliary base changes have explicitly known frames differing by 1+d z^r in k[z,d]/(d^2). If a tensor power were free, its base-change frames would differ by units of B and k[z], both nonzero constants. Comparing the nilpotent coefficient gives the contradiction. This does not require flat base change, normalization, patching descent, or a Picard-group calculation.
5. **Arbitrary automorphisms.** Inverse images of matrix units give R-linear isomorphisms among all n image modules. Their determinant forces L^(tensor n) to be free. This argument remains valid when the automorphism moves the center. The condition n nonzero in k is essential to this particular obstruction and is explicitly stated.
6. **Homogeneity.** A nonzero homogeneous idempotent has degree zero. A primitive constant matrix has rank one and is conjugate over k to E_11. Thus excluding E_11 excludes every homogeneous target, including permutations of a complete system.
7. **Finite jets and completion.** The first nonzero degree of e_r-E_11 is 2r+2. The explicit W satisfies W E_11=e_r W and W=1 modulo that degree. It is a unit after completion and in every finite quotient; no claim that it is a unit in the original algebra is made.

Exact reproducible checks are in `check.py` and `check-results.json`. They use integer arithmetic and Python's standard library. Finite checks are supporting certificates; the general proof covers every r, every allowed n, and every field.

The cited comparison results are separated from the new construction. No unsupported claim of first-ever nonhomogenizable idempotents is made. Publication hosting is not journal acceptance.
