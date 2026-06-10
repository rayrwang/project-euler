import math
from functools import lru_cache

from sympy import factorint, primerange

MOD = 409120391
_PRIME_LIMIT = 200_000
PRIMES_1 = [p for p in primerange(3, _PRIME_LIMIT) if p % 4 == 1]
PRIMES_3 = [p for p in primerange(3, _PRIME_LIMIT) if p % 4 == 3]
LOG_1 = [math.log(p) for p in PRIMES_1]
LOG_3 = [math.log(p) for p in PRIMES_3]

_factor_cache: dict[int, dict[int, int]] = {}


def _factorize(value: int) -> dict[int, int]:
    if value not in _factor_cache:
        _factor_cache[value] = factorint(value)
    return _factor_cache[value]


def _divisors(prime_factors: dict[int, int]) -> list[int]:
    divisors = [1]
    for prime, exp in prime_factors.items():
        divisors = [d * prime**i for d in divisors for i in range(exp + 1)]
    return divisors


def _odd_factorizations(value: int) -> set[tuple[int, ...]]:
    """All factorizations of odd `value` into integer factors > 1 (unordered)."""
    divisors = _divisors(_factorize(value))
    result: set[tuple[int, ...]] = set()

    def recurse(remaining: int, min_factor: int, chosen: list[int]) -> None:
        if remaining == 1:
            result.add(tuple(sorted(chosen)))
            return
        for d in divisors:
            if d >= max(min_factor, 2) and remaining % d == 0:
                recurse(remaining // d, d, chosen + [d])

    recurse(value, 2, [])
    return result


@lru_cache(maxsize=None)
def _best_pool(value: int, residue_one: bool) -> tuple[float, int] | None:
    """Minimal prime^exponent product realizing a (2a+1)-product equal to `value`.

    Each odd factor f >= 3 of `value` corresponds to a prime power with exponent
    (f - 1) / 2 on a prime of the chosen residue class (1 or 3 mod 4); to minimise
    the resulting integer the largest exponents go on the smallest primes.
    Returns (log of the integer, integer mod MOD), or None if it needs more
    primes than are tabulated.
    """
    if value == 1:
        return (0.0, 1)
    primes, logs = (PRIMES_1, LOG_1) if residue_one else (PRIMES_3, LOG_3)
    best: tuple[float, int] | None = None
    for parts in _odd_factorizations(value):
        if any(f % 2 == 0 for f in parts):
            continue
        exps = sorted(((f - 1) // 2 for f in parts), reverse=True)
        if len(exps) > len(primes):
            continue
        log_val = sum(a * logs[i] for i, a in enumerate(exps))
        if best is None or log_val < best[0]:
            mod_val = 1
            for i, a in enumerate(exps):
                mod_val = mod_val * pow(primes[i], a, MOD) % MOD
            best = (log_val, mod_val)
    return best


def smallest_occurrence(n: int) -> tuple[float, int]:
    """Q(n) as (log, value mod MOD): least N in exactly n Pythagorean triples.

    The number of triples a<b<c containing N splits into "N is a leg" and "N is
    the hypotenuse". Writing N = 2^s * prod p^a and grouping the odd primes by
    residue mod 4 into M1 = prod (2a+1) over p == 1 and M3 = prod (2a+1) over
    p == 3 (so M = M1 * M3 = tau(odd part of N^2)):
        legs  = (M - 1)/2          if s = 0,  ((2s - 1) M - 1)/2  if s >= 1,
        hyps  = (M1 - 1)/2.
    Hence count(N) = n means  M1 * ((2s - 1) M3 + 1) = 2n + 2  for s >= 1, and
    M1 * (M3 + 1) = 2n + 2 for s = 0. (Verified against brute force for N < 3000.)

    To minimise N we let M1 range over odd divisors of T = 2n + 2; for each, the
    cofactor G = T / M1 must equal (2s - 1) M3 + 1, so (2s - 1) M3 = G - 1 splits
    over odd divisors of G - 1 (plus the s = 0 and empty-M3 cases). Each M1 and
    M3 is realised on the smallest 1-mod-4 / 3-mod-4 primes, the factor of 2^s
    is free, and we keep the assignment of least real value (compared via logs,
    reported modulo MOD).
    """
    target = 2 * n + 2
    odd_part = {p: e for p, e in _factorize(target).items() if p != 2}
    best = (float("inf"), 0)
    for m1 in _divisors(odd_part):
        cofactor = target // m1
        pool1 = _best_pool(m1, True)
        if pool1 is None:
            continue
        candidates: list[tuple[int, int]] = []
        residual = cofactor - 1
        if residual >= 1 and residual % 2 == 1:
            candidates.append((0, residual))  # s = 0, odd N
            for u in _divisors(_factorize(residual)):  # (2s-1) = u, M3 = residual / u
                candidates.append(((u + 1) // 2, residual // u))
        if cofactor % 2 == 0 and cofactor // 2 >= 1:
            candidates.append((cofactor // 2, 1))  # empty M3
        for s, m3 in candidates:
            pool3 = _best_pool(m3, False)
            if pool3 is None:
                continue
            log_n = pool1[0] + pool3[0] + s * math.log(2)
            if log_n < best[0]:
                mod_n = pool1[1] * pool3[1] % MOD * pow(2, s, MOD) % MOD
                best = (log_n, mod_n)
    return best


def sum_of_q_powers() -> int:
    return sum(smallest_occurrence(10**k)[1] for k in range(1, 19)) % MOD


if __name__ == "__main__":
    assert smallest_occurrence(5)[1] == 15
    assert smallest_occurrence(10)[1] == 48
    assert smallest_occurrence(1000)[1] == 8064000
    print(sum_of_q_powers())  # 397289979
