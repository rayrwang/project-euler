from functools import lru_cache

# A hand splits per suit, and sizes mod 3 force exactly one suit to hold the
# pair; within a suit, maximal runs of used numbers are independent and the
# run holding the pair is again forced by its size mod 3. So with
#   A(n, k) = single-suit multisets decomposable into exactly k triples,
#   B(n, k) = single-suit multisets decomposable into k triples + one pair,
# the answer is s * [x^t] B(x) * A(x)^(s-1).
#
# Runs are short (at most 3t + 2 numbers), so A and B come from run profiles:
# count run-multisets of each length once each ("exists a decomposition",
# via a subset construction over the chow/pung scanning NFA), then place g
# ordered runs of total length L among n numbers in C(n - L + 1, g) ways.

MOD = 1_000_000_007
N = 10**8
S = 10**8
T = 30


def nfa_step(state, count):
    """Successors of one NFA state after a position holding `count` tiles.

    State (p, q, used): p chows started two back still need a tile here,
    q chows started one back need a tile here and at the next number, and
    `used` flags whether the pair has been placed. A transition picks r new
    chows (r <= 2 w.l.o.g.: three chows from one start equal three pungs),
    m pungs, and optionally the pair: count = p + q + 3m + r + 2e.
    """
    p, q, used = state
    rem_base = count - p - q
    for e in (0,) if used else (0, 1):
        rem = rem_base - 2 * e
        for r in range(0, min(rem, 2) + 1):
            if (rem - r) % 3 == 0:
                yield (q, r, used | e)


@lru_cache(maxsize=None)
def subset_step(subset, count):
    out = set()
    for state in subset:
        out.update(nfa_step(state, count))
    return frozenset(out)


def run_polys(lmax, kmax):
    """T[l][k] (P[l][k]) = runs of length l decomposable into k triples
    (k triples + one pair), each multiset counted once."""
    dp = {frozenset({(0, 0, 0)}): {0: 1}}  # subset -> {tiles: count}
    triple_runs = [[0] * (kmax + 1) for _ in range(lmax + 1)]
    pair_runs = [[0] * (kmax + 1) for _ in range(lmax + 1)]
    max_tiles = 3 * kmax + 2
    for length in range(1, lmax + 1):
        ndp = {}
        for subset, weights in dp.items():
            for count in (1, 2, 3, 4):
                nsub = subset_step(subset, count)
                if not nsub:
                    continue
                target = ndp.setdefault(nsub, {})
                for tiles, ways in weights.items():
                    if tiles + count <= max_tiles:
                        key = tiles + count
                        target[key] = (target.get(key, 0) + ways) % MOD
        dp = ndp
        for subset, weights in dp.items():
            done_plain = (0, 0, 0) in subset  # no chow extends past the run
            done_pair = (0, 0, 1) in subset
            for tiles, ways in weights.items():
                if done_plain and tiles % 3 == 0 and tiles // 3 <= kmax:
                    row = triple_runs[length]
                    row[tiles // 3] = (row[tiles // 3] + ways) % MOD
                if done_pair and tiles % 3 == 2:
                    row = pair_runs[length]
                    row[(tiles - 2) // 3] = (row[(tiles - 2) // 3] + ways) % MOD
    return triple_runs, pair_runs


def suit_polys(n, kmax):
    """A[k], B[k]: single-suit multiset counts by triple count."""
    lmax = 3 * kmax + 2
    triple_runs, pair_runs = run_polys(lmax, kmax)
    gmax = kmax + 1  # every run holds a triple or the pair

    inv_fact = [1] * (gmax + 1)
    fact = 1
    for i in range(1, gmax + 1):
        fact = fact * i % MOD
    inv_fact[gmax] = pow(fact, MOD - 2, MOD)
    for i in range(gmax, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def placements(total_len, runs):
        """Ordered placements of `runs` runs of total length `total_len`
        among n numbers with gaps: C(n - total_len + 1, runs)."""
        top = n - total_len + 1
        if top < runs:
            return 0
        prod = 1
        for i in range(runs):
            prod = prod * ((top - i) % MOD) % MOD
        return prod * inv_fact[runs] % MOD

    def conv(left, right):
        out = [[0] * (kmax + 1) for _ in range(lmax + 1)]
        for len1 in range(lmax + 1):
            row1 = left[len1]
            for k1 in range(kmax + 1):
                a = row1[k1]
                if not a:
                    continue
                for len2 in range(lmax + 1 - len1):
                    row2 = right[len2]
                    orow = out[len1 + len2]
                    for k2 in range(kmax + 1 - k1):
                        if row2[k2]:
                            orow[k1 + k2] = (orow[k1 + k2] + a * row2[k2]) % MOD
        return out

    suit_a = [0] * (kmax + 1)
    suit_b = [0] * (kmax + 1)
    suit_a[0] = 1  # empty suit

    identity = [[0] * (kmax + 1) for _ in range(lmax + 1)]
    identity[0][0] = 1
    prev = identity  # triple-run profile to the (g-1)-th power
    for g in range(1, gmax + 1):
        cur = conv(prev, triple_runs)
        with_pair = conv(prev, pair_runs)  # one P-run in g slots: factor g
        for total_len in range(lmax + 1):
            ways = placements(total_len, g)
            if not ways:
                continue
            row_a, row_b = cur[total_len], with_pair[total_len]
            for k in range(kmax + 1):
                if row_a[k]:
                    suit_a[k] = (suit_a[k] + row_a[k] * ways) % MOD
                if row_b[k]:
                    suit_b[k] = (suit_b[k] + g * row_b[k] % MOD * ways) % MOD
        prev = cur
    return suit_a, suit_b


def poly_mul(a, b, m):
    out = [0] * m
    for i, x in enumerate(a[:m]):
        if x:
            for j in range(min(len(b), m - i)):
                if b[j]:
                    out[i + j] = (out[i + j] + x * b[j]) % MOD
    return out


def mod_invs(m):
    inv = [0] * (m + 1)
    inv[1] = 1
    for i in range(2, m + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i]) % MOD
    return inv


def poly_pow_big(a, exponent, m):
    """a^exponent mod x^m for a[0] == 1, via exp(exponent * log a)."""
    invs = mod_invs(m)
    # inverse of a
    ainv = [0] * m
    ainv[0] = 1
    for i in range(1, m):
        acc = 0
        for j in range(1, i + 1):
            if j < len(a) and a[j]:
                acc = (acc + a[j] * ainv[i - j]) % MOD
        ainv[i] = (-acc) % MOD
    # log a via integral of a' / a
    deriv = [(i * a[i]) % MOD for i in range(1, m)] + [0]
    quot = poly_mul(deriv, ainv, m)
    log_a = [0] * m
    for i in range(1, m):
        log_a[i] = quot[i - 1] * invs[i] % MOD
    scaled = [c * (exponent % MOD) % MOD for c in log_a]
    # exp via e' = e * (scaled)'
    res = [0] * m
    res[0] = 1
    for i in range(1, m):
        acc = 0
        for j in range(1, i + 1):
            acc = (acc + j * scaled[j] % MOD * res[i - j]) % MOD
        res[i] = acc * invs[i] % MOD
    return res


def w(n, s, t):
    suit_a, suit_b = suit_polys(n, t)
    if s == 1:
        return suit_b[t] % MOD
    others = poly_pow_big(suit_a, s - 1, t + 1)
    return s % MOD * poly_mul(suit_b, others, t + 1)[t] % MOD


if __name__ == "__main__":
    assert w(4, 1, 1) == 20
    assert w(9, 1, 4) == 13259
    assert w(9, 3, 4) == 5237550
    assert w(1000, 1000, 5) == 107662178

    print(w(N, S, T))  # 436944244
