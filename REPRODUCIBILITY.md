# Reproducing the drafts

The scripts are mostly auxiliary checks. P11 uses a rigorous finite modular reduction, so its full coefficient certificates are a claimed part of its proof. Reproducing a computation does not certify the general proof or novelty.

## Working directory and outputs

For each table row, first change into the named directory beneath `papers/`, then run the commands in the stated order. For example, from the workspace root:

```sh
cd papers/P03-local-permutation-polynomials
python3 check.py
```

Equivalently, from the workspace root, prefix each script with its directory, for example `python3 papers/P03-local-permutation-polynomials/check.py`. Local module imports resolve beside their scripts; generated files use the script's location, rather than the shell's working directory. Use a normal Python invocation: `python3 -O` disables the assertions that perform these checks.

Scripts listed as writing JSON overwrite their named result files. Save a copy first if comparing against the recorded results. Compare parsed JSON, rather than whitespace; ignore diagnostic elapsed-time fields in P11. Scripts listed as stdout-only do not update an adjacent JSON file. For those, capture stdout to a new file if desired, for example `python3 check.py > reproduced-results.json` in P03, and compare its parsed JSON with `check-results.json`.

## Python and package requirements

- A Python 3.10-or-newer environment can run the complete collection. P11's pinned `python-flint==0.9.0` explicitly requires Python >=3.10. The other supplied scripts are compatible with Python 3.9, including P12's use of `math.lcm`.
- P01, P07, and P12 require SymPy. The inspected installation has **SymPy 1.14.0**.
- P05's normalization-correction check requires NumPy. The inspected installation has **NumPy 2.0.2**. That check uses floating-point LP-vertex calculations with explicit half-integrality tolerance checks, together with exact matching calculations; it is auxiliary evidence, not the hand proof of normalization.
- P11's two full coefficient passes require **python-flint 0.9.0**, pinned in `P11-partition-congruences/requirements.txt`. Its local `certificates.py` module and input JSON files are included. Install the package in the selected environment; a copied `vendor/` directory is not required. Both independent expressions use the same FLINT library, a limitation recorded in the mathematical review.
- All other published draft check scripts use only Python's standard library. P03 includes both `field_arithmetic.py` and `transfer_experiment.py`. P10's exploratory SciPy/NumPy optimization scripts are excluded from the published draft folder; they are not proof dependencies.

One possible clean environment setup, using an already selected Python >=3.10 interpreter, is:

```sh
python3 -m venv .venv-reproduce
. .venv-reproduce/bin/activate
python -m pip install sympy==1.14.0 numpy==2.0.2 python-flint==0.9.0
```

Run this from the workspace root before entering individual paper directories. In the activated environment, `python3` in the table refers to that environment's interpreter. The environment setup is provided for reproduction; no new environment or dependency installation was performed during the packaging repair.

## Per-paper commands

Commands are relative to the paper directory in the first column. A successful run exits with status zero; failed assertions or missing imports exit nonzero.

| Paper directory | Commands, in order | Dependencies | Output and reference results |
|---|---|---|---|
| `P01-lefschetz-classification` | `python3 verify.py` | SymPy | Writes `verification.json` and prints the same JSON. Deterministic random seed 20260908 is recorded. These are finite graph/witness and exact-rank checks. |
| `P02-recurrence-repair` | `python3 check.py` | Standard library | Stdout-only `PASS ... local Lucas congruences and minimality witnesses`; no output JSON is written. This script checks the Lucas application, not every theorem in the paper. Broader independent review evidence is linked in `README.md`. |
| `P03-local-permutation-polynomials` | `python3 check.py` | Standard library; included local modules `field_arithmetic.py`, `transfer_experiment.py` | Prints JSON; compare with `check-results.json`. Does not overwrite that file. Independent function-value and polynomial-transfer computations are compared. |
| `P04-carlitz-factorization` | `python3 check_small_cases.py` | Standard library | Prints a four-case JSON list; no result file is written. Compare the numerical counts with `validation.md`. The computations use prime fields q=2,3; the proof covers all finite fields. |
| `P05-symbolic-defect` | `python3 verify.py`<br>`python3 verify_correction.py` | First script: standard library. Second: NumPy. | Writes `verification.json` and `correction-verification.json`, respectively, and prints summaries. The second script documents its floating-point tolerance and exact matching comparison. |
| `P06-stirling-repair` | `python3 check_digits.py` | Standard library | Stdout-only `PASS: ... direct Stirling-triangle digit congruences`; no file is written. This is the digit-formula check; other independently reviewed local congruence tests are identified in `README.md`. |
| `P07-irreducible-compositions` | `python3 check_prefix.py` | SymPy | Writes `prefix_checks.json` and prints the same JSON. Checks selected compositions, factorizations, and integer gaps. `proof.md` is also included; the arbitrary-continuation proof is not inferred from these samples. |
| `P08-homological-shift-counterexamples/checks` | `python3 check.py` | Standard library | Writes `results.json` and prints a compact summary. The script is auxiliary; artifact hashes are in the collection manifest. |
| `P09-unique-addition` | No computational script is required or supplied. | None for the hand proof. | Read `manuscript.tex`, `dossier.md`, and the review linked in `README.md`. The absence of a check script is intentional. |
| `P10-restricted-sumsets` | `python3 check.py` | Standard library | Writes `check-results.json` and prints the same report for 1,848 parameter triples. `counterexample.json` preserves the original translated finite witness. Optimization discovery scripts are not included or needed. |
| `P11-partition-congruences` | `python3 certificates.py`<br>`python3 check_congruences.py`<br>`python3 check_initial.py`<br>`python3 check_independent.py --full` | Python >=3.10; python-flint **0.9.0** for `check_congruences.py` and the independent `--full` pass. Other steps use the standard library. | Writes `certificates.json`, `check-results.json`, `initial-checks.json`, and `independent-results.json`. The independent check reads `check-results.json` and `initial-checks.json`, so retain this order. The full passes cover the theorem-required 182,706 modular tests through coefficient index 1,901,366. Omitting `--full` runs only certificate reconstruction and small exact-integer checks; it does not reproduce the full coefficient verification. Runtime `seconds` fields may differ. |
| `P12-arithmetical-critical-groups` | `python3 check_examples.py` | SymPy; Python >=3.9 | Writes `exact_checks.json`; prints `PASS: 8 extremal pairs, primitive kernels, and nonunit star scaling`. Uses exact Smith normal forms, rational arithmetic, and integer kernels. |
| `P13-nilperiod-rings` | `python3 check_corbas.py`<br>`python3 C20_verify.py`<br>`python3 C20_corbas_verify.py` | Standard library | The author check prints per-case and final PASS summaries only. The independent scripts write `C20-verification.json` and `C20-corbas-verification.json`, respectively, and print JSON summaries. All are auxiliary finite multiplication-table/power-map checks of the hand proofs. |

## Build the PDFs

Install a LaTeX distribution or Tectonic (the preparation used Tectonic 0.17.0). From the repository root, for example:

```sh
tectonic --keep-logs papers/P01-lefschetz-classification/manuscript.tex
```

The manuscripts use standard packages declared in their preambles. Rebuilding may change PDF metadata and therefore its hash; the manifest identifies the exact initially uploaded PDF and source bytes. The detailed original AI review logs are not included; those logs were not human peer review. Source papers are cited in the manuscripts rather than redistributed here.
