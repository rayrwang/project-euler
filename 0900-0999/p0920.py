"""Project Euler 920: Tau Numbers.

m(k) is the least x with tau(x) = k and k | x.  Writing
x = prod p_i^{e_i}, the multiset {e_i + 1} is a factorization of k into
parts >= 2.  The divisibility constraint says v_p(x) >= v_p(k) for
every prime p | k, so each such "required" prime must occupy one
exponent slot of size >= v_p(k); all remaining exponents are assigned,
in decreasing order, to the smallest primes not dividing k -- optimal
by the rearrangement inequality once the required assignment is fixed,
which is searched exhaustively (with pruning by the current best).
This explains shapes like m(5) = 5^4 = 625, where the constraint
forces the prime 5 instead of 2.

Since k | x implies m(k) >= k, only k <= 10^n matter, and
tau(x) <= 41472 for all x <= 10^16 (the largest highly composite
number below 10^16 is ~8.09 * 10^15 with 41472 divisors), so k <= 50000
is an exhaustive range for M(16).  The construction is verified against
a direct tau sieve up to 10^6 -- both the m(k) values found there and
the non-existence of others -- and reproduces the given M(3) = 3189
along with m(8) = 24, m(12) = 60, m(16) = 384.
"""

LIMIT_PRIMES = 10**5
_sieve = bytearray([1]) * (LIMIT_PRIMES + 1)
_sieve[0:2] = b"\x00\x00"
for _i in range(2, int(LIMIT_PRIMES**0.5) + 1):
    if _sieve[_i]:
        _sieve[_i * _i :: _i] = b"\x00" * len(_sieve[_i * _i :: _i])
PRIMES = [i for i in range(LIMIT_PRIMES + 1) if _sieve[i]]


def _factorint(k: int) -> dict[int, int]:
    f: dict[int, int] = {}
    for p in PRIMES:
        if p * p > k:
            break
        while k % p == 0:
            f[p] = f.get(p, 0) + 1
            k //= p
    if k > 1:
        f[k] = f.get(k, 0) + 1
    return f


def _divisors(k: int) -> list[int]:
    divs = [1]
    for p, e in _factorint(k).items():
        divs = [d * p**j for d in divs for j in range(e + 1)]
    return sorted(divs, reverse=True)


def _factorizations(k: int) -> list[list[int]]:
    """non-increasing part lists (parts >= 2) with product k."""
    divs = _divisors(k)
    res: list[list[int]] = []

    def rec(rem: int, mx: int, cur: list[int]) -> None:
        if rem == 1:
            res.append(list(cur))
            return
        for d in divs:
            if d > mx or d > rem or d < 2:
                continue
            if rem % d == 0:
                cur.append(d)
                rec(rem // d, d, cur)
                cur.pop()

    rec(k, k, [])
    return res


def m_of_k(k: int, limit: int):
    if k == 1:
        return 1
    req = _factorint(k)
    req_primes = sorted(req)
    rp = set(req_primes)
    best = [limit + 1]

    for parts in _factorizations(k):
        exps = [p - 1 for p in parts]
        t = len(exps)
        if t < len(req_primes):
            continue
        used = [False] * t

        def assign(i: int, prod: int, exps=exps, used=used, t=t) -> None:
            if prod >= best[0]:
                return
            if i == len(req_primes):
                x = prod
                pi = 0
                for j in range(t):
                    if used[j]:
                        continue
                    while PRIMES[pi] in rp:
                        pi += 1
                    p = PRIMES[pi]
                    pi += 1
                    for _ in range(exps[j]):
                        x *= p
                        if x >= best[0]:
                            return
                best[0] = x
                return
            p = req_primes[i]
            need = req[p]
            seen: set[int] = set()
            for j in range(t):
                if used[j] or exps[j] < need or exps[j] in seen:
                    continue
                seen.add(exps[j])
                used[j] = True
                nxt = prod * p ** exps[j]
                if nxt < best[0]:
                    assign(i + 1, nxt)
                used[j] = False

        assign(0, 1)
    return best[0] if best[0] <= limit else None


def big_m(n: int) -> int:
    limit = 10**n
    total = 0
    for k in range(1, min(limit, 50000) + 1):
        v = m_of_k(k, limit)
        if v is not None:
            total += v
    return total


if __name__ == "__main__":
    import numpy as np

    assert m_of_k(8, 10**6) == 24
    assert m_of_k(12, 10**6) == 60
    assert m_of_k(16, 10**6) == 384
    n_brute = 10**6
    tau = np.zeros(n_brute + 1, dtype=np.int32)
    for d in range(1, n_brute + 1):
        tau[d::d] += 1
    mk: dict[int, int] = {}
    for x in range(1, n_brute + 1):
        t = int(tau[x])
        if x % t == 0 and t not in mk:
            mk[t] = x
    for k, v in mk.items():
        assert m_of_k(k, n_brute) == v, k
    for k in range(1, 200):
        if k not in mk:
            assert m_of_k(k, n_brute) is None, k
    assert big_m(3) == 3189
    print(big_m(16))  # 1154027691000533893
