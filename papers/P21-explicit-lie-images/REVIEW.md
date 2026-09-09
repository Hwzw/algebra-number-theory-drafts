# Proof and reproducibility review

**Reviewer: originating Codex agent, September 9, 2026.** This records internal checking, not a separate-agent or human referee report.

1. **Allowed syntax.** The defining expression contains only two variables, scalar coefficients in F_q, sums, and iterated brackets. The determinant and trace appear in the evaluation identity and proof, not as unauthorized polynomial operations. All coefficients 4^(-k) exist because q is odd.
2. **Double adjoints.** Cayley–Hamilton gives X^2=Q(X)I; polarization gives XY+YX=2B(X,Y)I. Direct multiplication proves ad_X^2(Y)=4(Q(X)Y-B(X,Y)X). Cyclic trace proves B(X,[X,Y])=0. Antisymmetry fixes the minus sign in [C,ad_X^2(Y)]=-4Q(C)X.
3. **All-input identity.** The recurrence ad_X^(2k+2)(Y)=(4Q(X))^k ad_X^2(Y) uses no division by Q(X). Applying 2q-3 adjoints by C produces the factor 4^(q-1)Delta^(q-1), which simplifies to Delta^(q-1). Zero invariants and characteristic three are included.
4. **Interpolation and surjectivity.** The scalar indicator polynomial has degree at most q-1 over any finite field. Nonzero trace-zero matrices are nonscalar and cyclic; their companion form has a partner with commutator diag(1,-1), so every selected output is attained. The proof does not infer surjectivity from a generic or dense locus.
5. **Classes.** The cyclic companion form proves each nonzero Q-fiber is one GL_2 orbit, including the nilpotent fiber. Zero is separately included. No extra distinction between SL_2 and GL_2 nilpotent orbits is introduced.
6. **Degree.** Counting variable occurrences gives 4q+2k-3 for the k-th displayed word, hence at most 6q-5. This is a total Lie degree bound, not a claim about the size of an expanded associative expression.
7. **Fibers.** A nonzero output equals its first input, so no additional input X can contribute to its fiber. The binary form (b-ta)^2-4td^2 yields exactly the three claimed counts. Direct coordinate counts give the three orbit sizes; their products with fiber sizes coincide. Summing over the disjoint selected classes gives the zero fiber.
8. **Lower bound.** On a scalar line through a tuple with nonzero output, f=Q(w) has degree at most 2D and takes only 0,a. Its values at 0 and 1 ensure f(f-a) is a nonzero polynomial. The ordinary root bound gives q<=4D. This applies to any finite number of variables and does not assume homogeneity.
9. **Arity and scope.** A one-generator free Lie algebra is one-dimensional; proper nonzero images require at least two variables. The proposed solution is complete for rank one only. The existence classification and finite-field interpolation are credited existing ingredients.

## Exact checks

The checker first verifies three symbolic identities using generic 2-by-2 matrices over an integer polynomial ring. It independently evaluates the defining nested brackets in finite fields and compares them with the proposed pointwise formula, for each monomial of the scalar polynomial basis.

| Field | Input coverage | Pairs | Basis evaluations |
|---|---|---:|---:|
| F_3 | All pairs | 729 | 2,187 |
| F_5 | All pairs | 15,625 | 78,125 |
| F_7 | Every companion first input, all second inputs | 2,401 | 16,807 |
| F_9 | Every companion first input, all second inputs | 6,561 | 59,049 |
| F_25 | Deterministic sample | 256 | 6,400 |

Total: 25,572 pairs, 162,568 basis evaluations. Every check passes. The extension fields use u^2=2 over F_3 and F_5. Scalar indicator values are checked 5,788 times. Exact nonzero fiber counts are checked for 166 first inputs. All 8+32 subsets over F_3 and F_5 have their full images and zero fibers computed from the bracket basis, with no missing class or extra output.

The script requires Python 3 and SymPy, has fixed sample seeds, and writes deterministic JSON. Finite checks are consistency evidence; the manuscript contains the unrestricted proof. There are no pending computational obligations for the stated theorem.
