import math
from functools import lru_cache

from funcs import factorint, isprime, primerange

Shape = tuple  # () for a leaf, (left, right) for an internal node

_PRIMES = primerange(2, 2_000_000)


def _closest_split(prime_factors: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    """Factor pair (a, b), a <= b, of n = prod p^e with b - a minimal."""
    n = 1
    for p, e in prime_factors:
        n *= p**e
    divisors = [1]
    for p, e in prime_factors:
        divisors = [d * p**i for d in divisors for i in range(e + 1)]
    root = math.isqrt(n)
    a = max(d for d in divisors if d <= root)
    return a, n // a


@lru_cache(maxsize=None)
def _shape_of_factored(prime_factors: tuple[tuple[int, int], ...]) -> Shape:
    """Binary factor-tree shape of the number with the given factorization."""
    total_exp = sum(e for _, e in prime_factors)
    if total_exp == 0:
        return ()
    if total_exp == 1:  # prime -> leaf
        return ()
    a, b = _closest_split(prime_factors)
    return (_shape_of_int(a), _shape_of_int(b))


@lru_cache(maxsize=None)
def _shape_of_int(n: int) -> Shape:
    if n == 1 or isprime(n):
        return ()
    return _shape_of_factored(tuple(sorted(factorint(n).items())))


def _double_factorial_shape(n: int) -> Shape:
    factors: dict[int, int] = {}
    k = n
    while k > 1:
        for p, e in factorint(k).items():
            factors[p] = factors.get(p, 0) + e
        k -= 2
    return _shape_of_factored(tuple(sorted(factors.items())))


@lru_cache(maxsize=None)
def _smallest_realisations(shape: Shape, count: int = 80) -> tuple[int, ...]:
    """The `count` smallest integers whose factor tree equals `shape` (ordered).

    A leaf is any prime. An internal node value must be a product v = a * b of
    realisations of its two child shapes whose *closest* factor split is exactly
    (a, b) -- so each candidate product is re-checked against the shape. Keeping
    a pool of the smallest realisations of each subtree lets the parent find its
    own smallest realisations; the pool size is ample for the shapes that arise
    from n!! up to n = 31.
    """
    if shape == ():
        return tuple(_PRIMES[:count])
    left, right = shape
    left_vals = _smallest_realisations(left, count)
    right_vals = _smallest_realisations(right, count)
    products = {a * b for a in left_vals for b in right_vals}
    result = []
    for v in sorted(products):
        if _shape_of_int(v) == shape:
            result.append(v)
            if len(result) >= count:
                break
    return tuple(result)


def smallest_with_shape_of_double_factorial(n: int) -> int:
    """M(n): smallest integer whose factor tree matches that of n!!."""
    shape = _double_factorial_shape(n)
    if shape == ():
        return 2
    return _smallest_realisations(shape)[0]


def sum_of_m() -> int:
    return sum(smallest_with_shape_of_double_factorial(n) for n in range(2, 32))


if __name__ == "__main__":
    assert smallest_with_shape_of_double_factorial(9) == 72
    print(sum_of_m())  # 41768797657018024
