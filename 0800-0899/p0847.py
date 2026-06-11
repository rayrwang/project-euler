"""Project Euler 847: Jack's Bean.

A question reveals whether the magic bean lies in a chosen subset of a
single plate; a "yes" leaves a one-plate instance needing plain binary
search.  Solvability in d questions therefore means the question with
t answers remaining may peel at most 2^(t-1) beans from one plate, and
peeling min(cap, plate) greedily is optimal by monotonicity.  Because
the caps 2^(d-1), ..., 1 are distinct powers, a triple is solvable in
d questions iff the powers below 2^d can be split into three disjoint
groups whose sums cover a, b, c with total shortfall at most one --
equivalently, iff there exist x, y, z with pairwise disjoint binary
supports inside d bits and a slack of one unit on at most one plate
with x >= a, y >= b, z >= c.

That existential is decided by a most-significant-bit-first automaton
whose witness records, per plate, whether the cover is still tight,
already strictly above, or has deviated one below (which commits the
plate to owning every remaining bit while its own bits must vanish,
and consumes the single slack).  A subset construction over these
witness states makes the test deterministic in the digits of
(a, b, c), so a standard digit DP -- also carrying the clipped deficit
of a + b + c against the bound -- counts the triples with sum at most
N that are NOT solvable in d questions, once per d.  Summing the
unsolvable counts over d (triples with sum exceeding 2^d are
unsolvable outright) gives H(N) = sum of h without any case analysis.
The automaton is verified against the game recursion exhaustively for
small sizes, and the code reproduces H(6) = 203, H(20) = 7718 and
H(R_3) = 1634144 before computing H(R_19) modulo 10^9 + 7.
"""

from __future__ import annotations

from functools import lru_cache

MOD = 10**9 + 7
START = frozenset({("T", "T", "T", 0)})
DIGITS = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]


def step_witness(w: tuple, bits: tuple[int, int, int], own_allowed: bool) -> set[tuple]:
    """Successor witness states for one bit; statuses T/F/S, slack flag."""
    s1, s2, s3, slack = w
    sts = [s1, s2, s3]
    out: set[tuple] = set()
    s_idx = [i for i in range(3) if sts[i] == "S"]
    if s_idx:
        i = s_idx[0]
        if bits[i] == 1 or not own_allowed:
            return out
        if all(not (j != i and sts[j] == "T" and bits[j] == 1) for j in range(3)):
            out.add(w)
        return out
    owners: list[int | None] = [None]
    if own_allowed:
        owners += [i for i in range(3) if sts[i] == "T"]
    for o in owners:
        nst = sts[:]
        if o is not None:
            nst[o] = "T" if bits[o] == 1 else "F"
        pending = [j for j in range(3) if j != o and nst[j] == "T" and bits[j] == 1]
        if not pending:
            out.add((nst[0], nst[1], nst[2], slack))
        elif len(pending) == 1 and slack == 0:
            nst[pending[0]] = "S"
            out.add((nst[0], nst[1], nst[2], 1))
    return out


@lru_cache(maxsize=None)
def wstep(wset: frozenset, bits: tuple, own: bool) -> frozenset:
    out: set[tuple] = set()
    for w in wset:
        out |= step_witness(w, bits, own)
    return frozenset(out)


def solvable_auto(a: int, b: int, c: int, d: int) -> bool:
    width = max(d, max(a, b, c).bit_length())
    wset = START
    for k in range(width - 1, -1, -1):
        bits = ((a >> k) & 1, (b >> k) & 1, (c >> k) & 1)
        wset = wstep(wset, bits, k < d)
        if not wset:
            return False
    return True


@lru_cache(maxsize=None)
def solvable_game(d: int, state: tuple[int, int, int]) -> bool:
    if sum(state) <= 1:
        return True
    if d == 0:
        return False
    cap = 1 << (d - 1)
    for i in range(3):
        if state[i] == 0:
            continue
        ns = list(state)
        ns[i] -= min(cap, ns[i])
        if solvable_game(d - 1, tuple(sorted(ns, reverse=True))):
            return True
    return False


def count_unsolvable(d: int, m: int) -> int:
    """Triples with a + b + c <= m not solvable in d questions, mod MOD."""
    width = max(d, m.bit_length(), 1)

    @lru_cache(maxsize=None)
    def dp(k: int, t: int, wset: frozenset) -> int:
        if k < 0:
            return 1 if not wset else 0
        total = 0
        mk = (m >> k) & 1
        own = k < d
        for bits in DIGITS:
            nt = 2 * t + mk - sum(bits)
            if nt < 0:
                continue
            total += dp(k - 1, min(nt, 4), wstep(wset, bits, own))
        return total % MOD

    result = dp(width - 1, 0, START)
    dp.cache_clear()
    return result


def triples_up_to(m: int) -> int:
    return (m + 1) * (m + 2) * (m + 3) // 6 if m >= 0 else 0


def question_sum(n: int) -> int:
    total = 0
    d = 0
    while True:
        cap = 1 << d
        u = count_unsolvable(d, min(cap, n))
        extra = (triples_up_to(n) - triples_up_to(cap)) % MOD if cap < n else 0
        total = (total + u + extra) % MOD
        if u == 0 and cap >= n:
            return total
        d += 1


def main() -> None:
    for a in range(16):
        for b in range(16):
            for c in range(16):
                for d in range(6):
                    game = solvable_game(d, tuple(sorted((a, b, c), reverse=True)))
                    assert solvable_auto(a, b, c, d) == game
    assert question_sum(6) == 203
    assert question_sum(20) == 7718
    assert question_sum(111) == 1634144
    print(question_sum((10**19 - 1) // 9))  # 381868244


if __name__ == "__main__":
    main()
