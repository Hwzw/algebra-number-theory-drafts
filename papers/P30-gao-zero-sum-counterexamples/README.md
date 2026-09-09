# Counterexamples to Gao's zero-sum invariant conjecture

**Henry Zweiman** · September 9, 2026

[Complete paper in Markdown](manuscript.md) · [Four-page PDF](manuscript.pdf) · [LaTeX source](manuscript.tex)

For every odd integer n >= 3, this paper proposes the exact value nu(C2^3 + C2n) = d(C2^3 + C2n) = 2n+2, contradicting Gao's universal conjecture nu(G)=d(G)-1. A uniform zero-sum-free sequence of length d(G)-1 has exactly six omitted nonzero sums. Their differences prevent containment in any coset excluding zero. The proof covers arbitrary subgroups, not only index-two subgroups.

The Davenport constant is classical and credited to Baayen. Explicit extremal extensions, the local invariant, and the parity limit of the construction are included in this same paper. No complete classification for even n or all finite abelian groups is claimed.

The [source and significance assessment](ASSESSMENT.md) records two primary conjecture statements and the scope of the literature search. The [internal review](REVIEW.md) records the proof obligations. Run `python3 check.py` for 50 exact family checks and a separate enumeration of all 127 nonempty subsequences in the smallest example; [stored results](check-results.json) accompany the hand proof.

The PDF was rendered and all four pages visually inspected. Full Markdown passed semantic roundtrip and mathematical-rendering checks. [Artifact QA](artifact-qa.json) and a [SHA-256 manifest](manifest.json) are included.

This is an AI-generated, internally checked proposed result. No human or separate-agent review, journal acceptance, or exhaustive historical-priority certification is claimed. Its publication adds one manuscript, not an automatically certified significant solution toward the research goal.
