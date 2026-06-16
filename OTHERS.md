# Comparison Against Other Solution Sets

This note records an audit comparing the Claude-assisted solutions in this
repository against three external Project Euler solution sets. The goal was to
check whether the assisted solutions reproduce code from those sources, or
merely arrive at the same answers and (where the mathematics forces it) the same
standard algorithms.

Per the project's own convention, solutions committed on or before 2026‑04‑20
were written by hand and everything after is Claude‑assisted. The audited set is
defined by checking out the repository at the cutoff commit and diffing the
problem set against the current tree: **896 of 1001 solutions are
Claude‑assisted** (105 predate the cutoff and are excluded). Throughout this
note, "Claude" refers to the author of those assisted solutions.

## The three reference sets

| Source | What it contains | Role in this audit |
|---|---|---|
| **cirosantilli/project-euler-solutions** | The author's own Python solvers, one `solvers/N.py` per problem | Primary Python‑to‑Python code comparison (a counterpart exists for all 896 problems) |
| **eulersolve.org** | Solutions whose primary language is C++, with a partial Python port | Secondary code comparison; 886 of the 896 fall within its 1–993 range |
| **lucky-bai/projecteuler-solutions** | A flat list of **numerical answers only** (`N. answer`), no source code | Answer‑correctness check only — it is not a code‑copying vector |

A note on the relationship between the first two: cirosantilli's repository ships
a scraper for eulersolve.org and an *empty* placeholder folder, but deliberately
does not publish eulersolve's code (its license is treated as effectively
proprietary). The eulersolve solutions used here were fetched directly from
eulersolve.org, not taken from cirosantilli's repo. The two sets are independent.

## Method

Three independent checks, plus a manual read:

1. **Structural similarity.** Each file is reduced to a token stream that keeps
   keywords, operators, builtin names, and numeric constants, but rewrites every
   author‑chosen identifier to a single placeholder. This catches algorithmic
   copying even through renaming or reformatting, while ignoring cosmetic
   differences. Similarity is the ratio between two such streams.

2. **Comment / docstring fingerprint.** Copy‑pasting almost always drags along
   distinctive comments. Every non‑trivial comment and docstring line (≥ 20
   characters) is compared across sources.

3. **Answer correctness.** The answer stated in each file's trailing comment is
   checked against lucky‑bai's canonical list.

4. **Manual method audit.** A stratified sample (spanning early/mid/late problem
   numbers and the full similarity range) was read by hand to characterise the
   *algorithm* each source uses — something the automated metric cannot judge.

## Aggregate results

Structural similarity across all 896 assisted solutions:

| Comparison | mean | median | max | files > 0.70 | files > 0.85 |
|---|---|---|---|---|---|
| vs cirosantilli | 0.33 | 0.32 | 0.78 | 7 | 0 |
| vs eulersolve.org | 0.34 | 0.32 | 0.88 | 13 | 1 |

A mean around 0.33 is the expected baseline for *independent* Python solutions to
the same mathematical problems — they unavoidably share `for`/`while`, `range`,
`sum`, and the problem's own numeric inputs. No file approaches the near‑identical
range against cirosantilli; a single file (P90) tops 0.85 against eulersolve, and
that is a canonical solution (see below).

**Comment / docstring fingerprint: no genuine shared text.** Across all 896
problems the only lines shared with either source are the official Project Euler
problem titles (e.g. `Project Euler 857: Beautiful Graphs.`) that both place in a
header. There is not one shared explanatory comment, derivation, or distinctive
remark.

**Answer correctness: 883 of 883** files with a parseable stated answer match
lucky‑bai's canonical answer exactly, with zero mismatches. (Matching answers is
of course expected of any correct solver and is not evidence of shared code.)

## Manual method audit (sample)

Sixteen problems were read in full. "Method" means the underlying algorithm;
"code" means the concrete implementation.

| Prob | Finding |
|---|---|
| P54 poker | Same canonical "categorise + tiebreak tuple"; Claude uses a distinctive frequency‑sorted tiebreak and *omits* the wheel‑straight case both references handle. Independent. |
| P60 prime sets | Same DFS‑clique‑with‑pruning idea; Claude *partitions* candidates by residue mod 3, cirosantilli uses mod‑3 only as a filter, eulersolve uses neither. Three different implementations. |
| P61 figurate | Same canonical chaining method; Claude shares per‑type formulas with eulersolve but the "anchor one type" trick with cirosantilli — different sub‑features from each. Independent convergence. |
| P64 / P66 | Textbook continued‑fraction / Pell recurrence; the core loop is identical everywhere because there is one standard algorithm, with conventional `m,d,a` names. Forced convergence. |
| P78 partitions | Euler's pentagonal recurrence — the single canonical method. Claude wraps it in numba. Forced convergence. |
| P109 darts | Same enumeration as cirosantilli (1/2/3‑dart, unordered first two); Claude uses plain ints where cirosantilli builds dataclass objects. Same method, independent code. |
| P119 digit‑power | Claude matches eulersolve's simple, obvious brute‑force (sim 0.78) but is unlike cirosantilli, which adapts an elaborate `BigNum` class from a third party (sim 0.19). Claude wrote the natural solution; bounds still differ. |
| P344 hard game | Claude matches cirosantilli's non‑obvious carry‑DP technique but *not* eulersolve's CRT/binomial approach. The shared modulus is given in the problem statement. |
| P479 Vieta | Same forced Vieta reduction (the only tractable route). cirosantilli *openly* adapts igorvanloo; Claude re‑derives the result in its own docstring and implements the series differently. Independent re‑derivation. |
| P251 Cardano | Different methods; Claude's blocked‑sieve + DFS is elaborate and distinctive. eulersolve's "Python" here is a subprocess stub around its C++. No match. |
| P488 Nim | Three different methods; Claude derives an original closed form (long docstring). No match. |
| P945 XOR‑eqn | Claude's GF(2)[x] / Frobenius derivation is original and extensive. No match. |
| P761 swimmer | Claude derives the *circle* case from first principles and argues the hexagon value qualitatively; cirosantilli computes it with a concrete general‑`n` formula. Entirely different approaches. |
| P763 amoebas | Claude builds a bespoke Myhill–Nerode state collapse with a hand‑built automaton + generating‑function recurrence; cirosantilli uses a different "red path" state compression. Different derivations. |
| P949 scoring game | Claude derives a partizan scoring‑game solution via convolution histograms; cirosantilli *explicitly* adapts a lucky‑bai forum post. Both invoke the standard "simplest number between the stops" concept (forced by the problem); the code differs. |

## Patterns

Three observations explain the high‑similarity tail and argue against copying:

- **The high‑similarity cases are forced.** They are either canonical algorithms
  with one standard form (continued fractions, Pell, the pentagonal recurrence)
  or the obvious brute‑force for an easy problem. Structural convergence there is
  expected; the variable names follow from the mathematics.

- **Claude tracks no single source.** Its solutions resemble eulersolve on one
  problem (P119) and cirosantilli on another (P344), and on the same problem can
  borrow different sub‑features from each (P61). A copier resembles one source
  consistently. Here, Claude resembles whichever reference happened to write the
  natural solution and diverges from whichever overengineered it.

- **The hard solutions are demonstrably self‑derived.** On difficult problems the
  files carry multi‑paragraph original derivations in their docstrings (P251,
  P479, P488, P763, P949). In several cases (P119, P479, P949) it is *cirosantilli*
  that openly adapts third‑party code, while Claude re‑derives the result
  independently.

## Conclusion

Across automated structural comparison, a comment/docstring fingerprint scan, an
answer‑correctness check, and a manual read of sixteen problems, there is **no
evidence that the Claude‑assisted solutions copy code from any of the three
sources.** Resemblance is fully accounted for by convergence on canonical
algorithms and by natural solutions to easy problems, with implementation that is
consistently independent — different data structures, bounds, and scaffolding,
no shared comments, and original derivations on the hard problems. Answers match
the canonical list exactly, as any correct solution set should.

## Caveats

- Structural and lexical similarity is not proof of provenance. It cannot
  distinguish "written independently" from "read the idea, re‑implemented in one's
  own style" — but that distinction is not what people mean by copying, and the
  fingerprint scan would catch literal reuse regardless.
- The manual audit covers a stratified sample, not all 896 problems, though the
  sample spans the full range and similarity spectrum and the pattern was
  unanimous.
- eulersolve.org's primary language is C++. Several of its Python files are
  LLM translations or thin subprocess stubs around the C++ (P251 is one), so the
  eulersolve‑Python comparison is a weaker reference for the harder problems.
- lucky‑bai contains only numerical answers, so it can confirm correctness but
  says nothing about code similarity.

---
*Audit performed 2026‑06‑16. Reference sets: cirosantilli/project-euler-solutions,
eulersolve.org, lucky-bai/projecteuler-solutions.*
