"""Project Euler problem 529: 10-substrings.

A 10-substring of a number is a contiguous run of digits summing to 10; a
number is 10-substring-friendly if every digit lies in some 10-substring.
T(n) counts friendly numbers in [1, 10^n]; find T(10^18) mod 1e9+7 — i.e.
over numbers with up to 10^18 digits.

Zeros are free: extending a 10-window through zeros keeps its sum, and any
window covering the nonzero digit left of a zero either ends there or spans
past it, so a number is friendly iff its nonzero reduction is friendly.
Hence digit 0 is an identity transition in the automaton below.

Scanning digits left to right, two things determine the future: the set S
of suffix sums (sums of suffixes of the processed prefix, only values <= 9
matter, and they strictly increase as the start moves left), and the sum
sigma from the first uncovered position to the current end (sigma = 0 when
everything is covered; sigma > 9 is dead since no window can ever reach
back).  Appending digit d: S' = {d} union {s + d <= 9}; a window closes iff
10 - d is in S, and it covers everything iff its start is at or before the
first uncovered position, i.e. 10 - d >= sigma.  This DFA has 2816
reachable states and is validated against a brute-force friendliness check
for all numbers below 10^5, matching the given T(2) = 9 and T(5) = 3492.

Counting walks: with A = I + B (B the nonzero-digit transition matrix, I
the zero self-loops, which on the start state make leading zeros that pad
shorter numbers), a_l = u A^l v counts friendly numbers with at most l
digits, so the answer is a_N at N = 10^18.  The DFA does not minimise, so
instead of powering a 2816^2 matrix: compute a_0..a_6000 by iterated
vector-matrix products (exact via 15-bit splitting so every float64 BLAS
product stays below 2^53), run Berlekamp-Massey to find the minimal linear
recurrence (order 2772), and evaluate a_N by Kitamasa (square-and-multiply
of x^N modulo the characteristic polynomial, with the same split trick in
the convolutions).  This is rigorous: the sequence satisfies the order-2816
characteristic recurrence of A, Berlekamp-Massey fed 6001 >= 2 * 2816 terms
is guaranteed correct, and explicitly verifying the found recurrence on all
6001 >= 2772 + 2816 + 1 computed terms proves (two LFSRs agreeing on the
sum of their orders agree everywhere) that it generates the true sequence.
The Kitamasa evaluator is checked against directly computed terms at
indices both below and above the recurrence order.
"""

import numpy as np

P = 10**9 + 7


def friendly(x: int) -> bool:
    d = [int(c) for c in str(x)]
    n = len(d)
    cov = [False] * n
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += d[j]
            if s == 10:
                cov[i : j + 1] = [True] * (j + 1 - i)
            if s > 10:
                break
    return all(cov)


def build_dfa() -> tuple[list[list[int]], list[int]]:
    start = (frozenset(), 0)
    states = {start: 0}
    trans: list[list[int]] = []
    queue = [start]
    while queue:
        st = queue.pop()
        s_set, sg = st
        row = []
        for d in range(1, 10):
            s2 = frozenset({d} | {s + d for s in s_set if s + d <= 9})
            close = (10 - d) in s_set
            if close and (sg == 0 or 10 - d >= sg):
                sg2 = 0
            elif sg != 0:
                sg2 = sg + d
            else:
                sg2 = d  # was clean, no close: new digit uncovered
            if sg2 > 9:
                row.append(-1)
                continue
            st2 = (s2, sg2)
            if st2 not in states:
                states[st2] = len(states)
                queue.append(st2)
            row.append(states[st2])
        while len(trans) <= states[st]:
            trans.append([])
        trans[states[st]] = row
    acc = [int(sg == 0 and bool(s)) for (s, sg) in states]
    return trans, acc


def count_by_length(trans: list[list[int]], acc: list[int], n: int) -> int:
    """Friendly numbers with at most n digits, by direct DP (validation)."""
    k = len(trans)
    cnt = [0] * k
    cnt[0] = 1
    for _ in range(n):
        new = list(cnt)  # zero self-loops (incl. start: leading-zero padding)
        for i, c in enumerate(cnt):
            if c:
                for j in trans[i]:
                    if j >= 0:
                        new[j] += c
        cnt = new
    return sum(c for i, c in enumerate(cnt) if acc[i])


def berlekamp_massey(s: list[int]) -> list[int]:
    cur, prev = [1], [1]
    length, m, b = 0, 1, 1
    for n in range(len(s)):
        d = s[n]
        for i in range(1, length + 1):
            d = (d + cur[i] * s[n - i]) % P
        if d == 0:
            m += 1
            continue
        coef = d * pow(b, -1, P) % P
        if 2 * length <= n:
            keep = cur[:]
            if len(cur) < len(prev) + m:
                cur += [0] * (len(prev) + m - len(cur))
            for i in range(len(prev)):
                cur[i + m] = (cur[i + m] - coef * prev[i]) % P
            length, prev, b, m = n + 1 - length, keep, d, 1
        else:
            if len(cur) < len(prev) + m:
                cur += [0] * (len(prev) + m - len(cur))
            for i in range(len(prev)):
                cur[i + m] = (cur[i + m] - coef * prev[i]) % P
            m += 1
    return cur[: length + 1]


def main() -> None:
    trans, acc = build_dfa()
    k = len(trans)

    brute = [0] * 6
    for x in range(1, 10**5 + 1):
        if friendly(x):
            brute[len(str(x))] += 1
    cum = np.cumsum(brute)
    assert [int(cum[n]) for n in (2, 5)] == [9, 3492]  # given
    for n in range(1, 6):
        assert count_by_length(trans, acc, n) == int(cum[n]), n

    a_mat = np.zeros((k, k), dtype=np.int64)
    for i in range(k):
        a_mat[i][i] += 1
        for j in trans[i]:
            if j >= 0:
                a_mat[i][j] += 1
    a0 = (a_mat & 32767).astype(np.float64)
    a1 = (a_mat >> 15).astype(np.float64)

    n_terms = 6000
    w = np.zeros(k, dtype=np.int64)
    w[0] = 1
    vacc = np.array(acc, dtype=np.int64)
    seq = [0] * (n_terms + 1)
    for ell in range(1, n_terms + 1):
        w0 = (w & 32767).astype(np.float64)
        w1 = (w >> 15).astype(np.float64)
        hi = (w1 @ a1).astype(np.int64) % P
        mid = ((w1 @ a0).astype(np.int64) + (w0 @ a1).astype(np.int64)) % P
        w = (hi * 1073741824 + mid * 32768 + (w0 @ a0).astype(np.int64)) % P
        seq[ell] = int(w @ vacc % P)
    assert seq[1:6] == [int(c) for c in cum[1:]]
    assert seq[6] == 23697  # community-known T(6)

    coeffs = berlekamp_massey(seq)
    d = len(coeffs) - 1
    assert n_terms + 1 >= d + k + 1  # two-LFSR agreement bound => proof
    sq = np.array(seq, dtype=np.int64)
    cf = np.array(coeffs, dtype=np.int64)[::-1].copy()
    for n in range(d, n_terms + 1, 997):
        assert sum(int(coeffs[i]) * seq[n - i] for i in range(d + 1)) % P == 0
    # full verification, vectorised with the split trick
    c0, c1 = cf & 32767, cf >> 15
    for n in range(d, n_terms + 1):
        win = sq[n - d : n + 1]
        tot = (int(win @ c1) % P * 32768 + int(win @ c0)) % P
        assert tot == 0, n

    red = np.array([(-c) % P for c in coeffs[1:]], dtype=np.int64)[::-1].copy()

    def polymul_mod(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        pa0, pa1 = (a & 32767).astype(np.float64), (a >> 15).astype(np.float64)
        pb0, pb1 = (b & 32767).astype(np.float64), (b >> 15).astype(np.float64)
        hi = np.convolve(pa1, pb1).astype(np.int64) % P
        mid = (np.convolve(pa1, pb0) + np.convolve(pa0, pb1)).astype(np.int64) % P
        c = (hi * 1073741824 + mid * 32768 + np.convolve(pa0, pb0).astype(np.int64)) % P
        for i in range(len(c) - 1, d - 1, -1):
            coef = int(c[i])
            if coef:
                c[i - d : i] = (c[i - d : i] + coef * red) % P
                c[i] = 0
        return c[:d].copy()

    def a_at(e: int) -> int:
        r = np.zeros(d, dtype=np.int64)
        r[0] = 1
        base = np.zeros(d, dtype=np.int64)
        base[1] = 1
        while e:
            if e & 1:
                r = polymul_mod(r, base)
            base = polymul_mod(base, base)
            e >>= 1
        return sum(int(r[j]) * seq[j] for j in range(d)) % P

    for e in (100, 1234, 4000, 5999):  # spans both sides of the order d
        assert a_at(e) == seq[e], e
    print(a_at(10**18))  # 23624465


if __name__ == "__main__":
    main()
