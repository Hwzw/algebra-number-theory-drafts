# Revision 1.1 internal proof review

Date: September 16, 2026. Review by the originating AI agent; no independent
review is represented by this document.

## Claim and derivation

Theorem 5.1 evaluates beta_r for every positive r. This answers the explicit
question in Section 5 of version 1. The prior all-genus quasipolynomiality,
parity oscillation, and fixed-r eventual growth proofs remain in place.

1. The full additive equality arrangement includes low-low-low,
   hole-low-hole, and low-low-hole equations. Distinct hyperplanes are
   independent in pairs. Fixing all but two coordinates bounds every
   intersection by O_r(g^(2r-2)); no periodicity of a lower coefficient is
   assumed away.
2. Outside the bulk, the low violation forces 2m in B. A further low sum
   forces a second equality unless it is m+m itself. This gives g/3<m<=g/2,
   other low elements above g-m, and all holes at most g+m. The upper-hole
   violation gives the second region, with forced pair a,a+m and the
   stated constraints on all other low elements and holes. Violating both
   bulk conditions costs two independent equalities.
3. Inside the bulk, only low-low-hole equalities invalidate a tuple. Their
   contributions add at leading order. The pair weights r, (r-1)/2, and
   (r-1)(r-2)/4 include the doubled minimum, doubled other elements, and
   unordered distinct pairs with the correct multiplicities.
4. Every forced coordinate is eliminated with coefficient one. The volume
   calculation therefore uses a lattice-coordinate measure, not Euclidean
   hypersurface area. Factorials account for unordered free sets.
5. The two beta integrals and their difference give the upper positive
   term explicitly. Expanding both falling factorials gives h_r and the
   lower mesh endpoint contributes -C_r/2 to the parity average. Their
   sum gives the displayed beta_r. The special r=1 case is evaluated
   directly and agrees with the same formula.
6. The asymptotic ratio beta_r/A_r follows from the central binomial
   coefficient estimate. It supplies no control of the genus remainder
   when r varies. No all-genus conjecture is declared solved.

## Reproducible finite diagnostics

`check_second.py` uses exact integers and fractions. It checks the candidate
sums against literal tuple enumeration on 17,568 tuples through genus 8.
Every one of the 223 nonzero residuals has at least two distinct primitive
normal vectors, hence two independent additive equalities. This directly
tests the claimed support of the lower-order remainder.

For r=1,...,8, exact Newton interpolation on all twelve tested residue
classes agrees with each candidate sum's proposed leading coefficient and
passes 864 later evaluations. The beta_2 formula independently agrees with
every residue of the source's degree-four formula. These tests corroborate
the proof; their parameter ranges do not establish its universal claim.

The previous `check.py` and its saved diagnostic output are retained from
version 1. No computational result is interpreted as peer review or a
priority certificate.

## Artifact checks

The final PDF has nine pages. Tectonic reported no overfull/underfull boxes
or undefined references. The complete Markdown conversion uses the final
TeX equation/theorem numbers and passes semantic round-trip verification.
Final hashes and numerical artifact counts are recorded in artifact-qa.json
and markdown-math-check.json. Every final PDF page was visually reviewed;
the new proof pages were also inspected individually. Local MathJax checks
do not constitute live GitHub-renderer verification.
