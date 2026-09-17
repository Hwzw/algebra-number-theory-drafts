# A planar comparison argument for radial bound states

Research draft prepared for Henry Zweiman · September 17, 2026 · P55 · Version 0.2

**Unreviewed proof reconstruction. Independent mathematical review pending. No first-proof claim.**

The manuscript gives a candidate shooting proof of uniqueness and classification of radial bound states in the plane for every real $p>1$ and every node count. It reconstructs the comparison method of Cortázar, García-Huidobro, and Yarur, with explicit common-level initialization and a positive weighted-energy gap at infinity. The 2011 theorem already states the whole-plane conclusion, and Zhang–Zhang's June 2026 preprint also claims the planar extension. The correctness and contribution of this reconstruction await expert assessment.

- [Complete Markdown manuscript](manuscript.md)
- [Twelve-page PDF](manuscript.pdf) and [LaTeX source](manuscript.tex)
- [Contribution and prior-work assessment](ASSESSMENT.md)
- [Originating-assistant proof audit](REVIEW.md)
- [Focused expert review brief](expert-review-brief.md)
- [Primary-source retrieval metadata](source-audit.json)
- [Artifact checks](checks/artifact-qa.json), [algebra check](checks/check_identities.py), and [file hashes](SHA256SUMS.txt)
- [Citation metadata](CITATION.cff)

Markdown is authoritative. With Pandoc and Tectonic on PATH, run `python3 build.py` in this folder. With Python and SymPy, run `python3 checks/check_identities.py`; it verifies seven algebraic identities, not the comparison theorem.

Prepared with OpenAI Codex. The audit was performed by the assistant that drafted the proof. Human PDE review is pending. The P55 identifier records public archival publication only; it does not admit a new original theorem to the research program's qualifying-paper count. Finite-disk uniqueness and spectral nondegeneracy are outside this manuscript's claims. Third-party source articles are not redistributed.
