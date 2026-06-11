"""Project Euler 823: Factor Shuffle.

View each list entry as its multiset of prime factors.  A round pops
the smallest prime from every column and stacks the pops, sorted, into
a new column — so a column releases its content in increasing order,
the i-th smallest going out i rounds after birth.  The total multiset
of primes (the factorisation of n!) is conserved, and the column-size
dynamics decouples completely: sizes evolve by s -> s - 1 with a new
column of size equal to the current column count, settling into a
short periodic schedule.

Tagged simulation reveals the steady structure: every prime locks to a
fixed height i (its rank among the primes released in the same round)
and is then re-released exactly every i rounds.  Consequently the
steady state is fully described by the map (i, t mod i) -> value of
the height-i prime released at round t, read off a window of recent
rounds, and verified by checking v_i(t) = v_i(t - i) across thousands
of consecutive rounds.  The column born at round u contains, for each
height i, the class-i prime of residue u mod i (when that residue is
in use), so the sum after round m is a double loop over column ages
and heights — about K^2 = 253^2 modular multiplications for n = 10^4.

The formula is validated against direct simulation at distant rounds
for n = 10, 30, 50 and against the given S(5,3) = 21 and
S(10,100) = 257; the steady tables for n = 10^4 emerge after about
65000 simulated rounds, in roughly two seconds.
"""

from __future__ import annotations

MOD = 1234567891


def make_cols(n: int) -> list[list[int]]:
    cols = []
    for k in range(2, n + 1):
        x = k
        fac: list[int] = []
        d = 2
        while d * d <= x:
            while x % d == 0:
                fac.append(d)
                x //= d
            d += 1
        if x > 1:
            fac.append(x)
        cols.append(sorted(fac, reverse=True))
    return cols


def step(cols: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    released = [col.pop() for col in cols]
    cols = [c for c in cols if c]
    released.sort()
    cols.append(released[::-1])
    return cols, released


def simulate_to_steady(
    n: int, min_rounds: int, confirm: int
) -> tuple[int, list[list[int]]]:
    cols = make_cols(n)
    hist: list[list[int]] = []
    t = 0
    while True:
        cols, released = step(cols)
        hist.append(released)
        t += 1
        if t >= min_rounds:
            ok = True
            for j in range(t - confirm, t):
                rel = hist[j]
                for i in range(1, len(rel) + 1):
                    jj = j - i
                    if jj < 0 or i > len(hist[jj]) or hist[jj][i - 1] != rel[i - 1]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return t, hist
            min_rounds = t + confirm
        if t > 500000:
            raise RuntimeError("no steady state found")


def steady_sum(m: int, t_end: int, hist: list[list[int]]) -> int:
    imax = max(len(r) for r in hist[-1000:])
    val: list[dict[int, int]] = [{} for _ in range(imax + 1)]
    for i in range(1, imax + 1):
        for rr in range(t_end - i + 1, t_end + 1):
            rel = hist[rr - 1]
            if i <= len(rel):
                val[i][rr % i] = rel[i - 1]
    total = 0
    for a in range(imax):
        u = m - a
        prod = 1
        empty = True
        for i in range(a + 1, imax + 1):
            v = val[i].get(u % i)
            if v is not None:
                prod = prod * v % MOD
                empty = False
        if not empty:
            total = (total + prod) % MOD
    return total


def direct_sum(n: int, m: int) -> int:
    cols = make_cols(n)
    for _ in range(m):
        cols, _ = step(cols)
    s = 0
    for col in cols:
        v = 1
        for p in col:
            v = v * p % MOD
        s = (s + v) % MOD
    return s


def main() -> None:
    assert direct_sum(5, 3) == 21
    assert direct_sum(10, 100) == 257
    for n in (10, 30, 50):
        t_end, hist = simulate_to_steady(n, 1500, confirm=800)
        for m in (t_end + 7, t_end + 12345):
            assert steady_sum(m, t_end, hist) == direct_sum(n, m), (n, m)
    t_end, hist = simulate_to_steady(10**4, 70000, confirm=5000)
    print(steady_sum(10**16, t_end, hist))  # 865849519


if __name__ == "__main__":
    main()
