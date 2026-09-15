# P45: Spectral localization and uniform reactive capacitance of thin planar patches

Henry Zweiman. September 15, 2026.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

The manuscript establishes a strong operator limit for thin planar patches around fixed embedded curves. Every fixed eigenvalue is controlled by maximum width, while the input spectral measure converges to the full area-weighted width distribution. This yields vanishing fixed spectral weights for thin ellipses and rhombi, and a capacitance formula with relative error tending to zero uniformly over all positive reactivities.

- [Full Markdown manuscript](manuscript.md)
- [Twelve-page PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The same paper gives an exact criterion for asymptotic accuracy of the standard one-pole approximation, bounded remainders for the two Grebenkov-Maurette tube conjectures on regular center curves, and a connected smooth example with F1>F0. The source's operator, spectral representation, variational principles and approximation are credited prior work. No separate count is assigned to these related consequences.

Sharp spectral corrections, fixed-index weight limits on positive-length maximum sets, and singular or thickness-dependent center curves remain outside the result. The connected weight-reversal example is not asserted to be convex. See the assessment for current-source comparison and its limits.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Formula parsing and visual PDF checks establish artifact integrity, not proof correctness or historical priority.
