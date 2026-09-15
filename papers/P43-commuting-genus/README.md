# P43: A genus obstruction for commuting boundary operators

Henry Zweiman. September 15, 2026.

**AI-assisted research preprint. Not peer reviewed or independently verified.**

The manuscript proves that a compact connected oriented smooth surface whose Dirichlet-to-Neumann map commutes with its boundary Laplacian has genus zero. It gives a negative answer to both cases of Speciel's final Open Problem 1.6 and, combined with his existing genus-zero theorem, completes the oriented classification. The proof uses finite periods, multiplication of holomorphic Fourier traces, and conformal disk capping.

- [Full Markdown manuscript](manuscript.md)
- [Nine-page PDF](manuscript.pdf)
- [Portable LaTeX](manuscript.tex)
- [Priority and significance assessment](ASSESSMENT.md)
- [Internal proof review](REVIEW.md)
- [Source audit](source-audit.json), [download metadata](source-downloads.json), [artifact checks](artifact-check.json), and [checksums](SHA256SUMS.txt)

The genus-zero models and their classification are credited to Speciel. The finite-period obstruction and smooth conformal sewing are prior tools, whose needed forms are proved or precisely sourced. The new contribution is the genus obstruction and its reduction from several boundary components. These results comprise one paper. Quantitative stability, nonorientable surfaces and rough boundaries are outside the theorem.

To rebuild, install Pandoc and Tectonic on PATH and run `python3 build.py`. The authoritative source is manuscript.md. Local mathematical-expression parsing and PDF rendering establish artifact integrity, not mathematical correctness or historical priority. The source record specifies which primary texts and version histories were checked.
