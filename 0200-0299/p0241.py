from fractions import Fraction
from math import gcd, isqrt

# sigma(n)/n = k + 1/2 means n is "hemiperfect". Search by building n from
# prime powers: track the remaining abundancy target r (so sigma(m)/m = r is
# still required of the unbuilt coprime part m). If r has denominator d > 1,
# the largest prime factor of d must divide m, which forces the next branch;
# if r is an integer >= 2, branch on the smallest prime of m, pruning when
# even every remaining prime within the budget cannot lift the abundancy to
# r. Abundancy never decreases when primes are added, so r < 1 prunes too.

_LIMIT = 10**18


def _sieve(n: int) -> list[int]:
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i :: i] = bytes(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


_PRIMES = _sieve(100000)


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _largest_prime_factor(n: int) -> int:
    best = 1
    stack = [n]
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if _is_prime(m):
            best = max(best, m)
            continue
        f = next((p for p in _PRIMES[:1000] if m % p == 0), None)
        if f is None:  # deterministic Brent-Pollard rho
            c = 1
            while True:
                x = y = 2
                d = 1
                while d == 1:
                    x = (x * x + c) % m
                    y = (y * y + c) % m
                    y = (y * y + c) % m
                    d = gcd(abs(x - y), m)
                if d != m:
                    f = d
                    break
                c += 1
        stack.append(f)
        stack.append(m // f)
    return best


def _max_gain(p_idx: int, budget: int) -> Fraction:
    # Upper bound on the abundancy factor obtainable from distinct primes
    # >= PRIMES[p_idx] whose product stays within the budget.
    g = Fraction(1)
    i, b = p_idx, budget
    while i < len(_PRIMES) and _PRIMES[i] <= b:
        q = _PRIMES[i]
        g *= Fraction(q, q - 1)
        b //= q
        i += 1
    if i >= len(_PRIMES) and b > _PRIMES[-1]:
        g *= Fraction(11, 10)  # generous slack for primes beyond the table
    return g


def solve(limit: int = _LIMIT) -> int:
    solutions: set[int] = set()

    def sigma_pe(p: int, e: int) -> int:
        return (p ** (e + 1) - 1) // (p - 1)

    def dfs(n: int, r: Fraction, used: frozenset[int], next_idx: int) -> None:
        if r == 1:
            solutions.add(n)
            return
        if r < 1:
            return
        budget = limit // n
        if budget < 2:
            return
        den = r.denominator
        if den > 1:
            p = _largest_prime_factor(den)
            if p in used or p > budget:
                return
            e, pe = 1, p
            while n * pe <= limit:
                dfs(n * pe, r * Fraction(pe, sigma_pe(p, e)), used | {p}, next_idx)
                e += 1
                pe *= p
            return
        i = next_idx
        while i < len(_PRIMES):
            p = _PRIMES[i]
            if p > budget:
                return
            if p in used:
                i += 1
                continue
            if _max_gain(i, budget) < r:
                return
            e, pe = 1, p
            while n * pe <= limit:
                dfs(n * pe, r * Fraction(pe, sigma_pe(p, e)), used | {p}, i + 1)
                e += 1
                pe *= p
            i += 1

    for k in range(1, 7):  # abundancy of n <= 10^18 stays well below 13/2
        dfs(1, Fraction(2 * k + 1, 2), frozenset(), 0)
    return sum(solutions)


if __name__ == "__main__":
    print(solve())  # 482316491800641154
