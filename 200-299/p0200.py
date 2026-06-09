import numpy as np


def _primes_up_to(n: int) -> np.ndarray:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.nonzero(sieve)[0]


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
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _prime_proof(v: int) -> bool:
    s = str(v)
    for i in range(len(s)):
        for digit in "0123456789":
            if digit != s[i] and _is_prime(int(s[:i] + digit + s[i + 1 :])):
                return False
    return True


def solve(nth: int = 200, substring: str = "200", bound: int = 10**12) -> int:
    # A sqube is p^2 q^3 (distinct primes). Generate squbes up to a bound, keep
    # those containing the substring that are prime-proof (no single-digit change
    # yields a prime), and return the nth in increasing order.
    primes = _primes_up_to(10**6)
    squbes = set()
    for q in primes:
        q3 = int(q) ** 3
        if q3 > bound:
            break
        cap = bound // q3
        for p in primes:
            if p * p > cap:
                break
            if p != q:
                squbes.add(p * p * q3)
    count = 0
    for value in sorted(squbes):
        if substring in str(value) and _prime_proof(value):
            count += 1
            if count == nth:
                return value
    raise RuntimeError("not enough qualifying squbes; raise the bound")


if __name__ == "__main__":
    print(solve())  # 229161792008
