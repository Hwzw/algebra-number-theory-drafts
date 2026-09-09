# Internal proof review

Date: September 9, 2026. Review performed within the same Codex task; no independent human or external-agent review is claimed.

## Polynomial evaluation and quantifiers

The theorem is uniform over all prescriptions on a fixed r-dimensional subspace. It does not say every individual prescription fails below the threshold. E(f) is a maximum of minimum root multiplicities. Algebraic closure ensures every fiber is nonempty; characteristic zero makes the critical-value set finite. The derivative count proves that at most one fiber lacks a simple point.

For N a nilpotent Jordan block, f(alpha I+N)-lambda I=N^e g(N) with g(N) invertible and commuting with N. Equality of the nullity sequence establishes the Jordan type. The packet of size e(d-1)+1 has one block d and e-1 blocks d-1. Similarity transports the f-preimage to the desired direct sum and preserves the prescribed action on the original invariant block.

## Partial-operator decomposition

The filtration is U_-1=V, U_0=U and U_(j+1)=L^-1(U_j) inside U. It is descending and stabilizes at an invariant subspace. The injection U_j/U_(j+1) into U_(j-1)/U_j is well defined: the image of the denominator lies in U_j, and its kernel is precisely U_(j+1).

Choosing representatives downwards and retaining actual images gives exact chain equations, not merely equations modulo the invariant part. Quotient bases certify independence of all observed chain vectors; the final injection gives independence of the tail vectors modulo U. This addresses possible hidden coupling between the regular and chain parts. The classical decomposition is credited rather than treated as new.

## Dimension accounting

Open chains use one already-existing free tail each. With a invariant dimensions and c chains, c <= r-a. Only regular Jordan blocks with size at least two and minimum multiplicity at least two need padding. If any such block exists, the total cost is at most (E-1)(a-1). The inequality n >= E(r-1)+1 gives n-r-c >= (E-1)(a-1)+(E-2)(r-a), so those unused vectors suffice. If a is zero or one, no padding is needed. Rank zero and E=1 are handled separately.

## Sharpness and coefficients

Prescribing a single invariant J_r(lambda) forces the minimal polynomial of any extension to contain (t-lambda)^r. Every lambda block of f(X) has size at most ceil(n/E), since every scalar preimage of that chosen lambda has multiplicity at least E. This proves the strict boundary.

For Af(X)=D, transposition defines L on im A^T by L(A^T v)=D^T v. The condition im D contained in im A is exactly what makes this well defined. Every partial map arises. For a direct sum of coefficient images, the components of a target are unique, so componentwise necessity as well as sufficiency follows. This argument cannot be carried to overlapping images without new work. Density and finite-dimensional closedness supply the vector-space criterion.

## Exact checks and artifact QA

The standard-library program verifies 729 exhaustive partial operators over F3 and 924 additional operators over F7. It classifies all 19,683 matrices over F3 by roots over the algebraic closure and checks 729 versus 721 reachable two-row prescriptions for squares versus fourth powers. It checks 98,800 padding inequalities and 406 Jordan packet identities. Finite-field diagnostic cases are not used as a characteristic-zero proof.

The six-page PDF compiled without TeX warnings. All six final rendered pages were individually inspected. The complete Markdown conversion preserves theorem/proof structure and references; all 269 rendered mathematical expressions passed the math-rendering check. File hashes are in the manifest.
