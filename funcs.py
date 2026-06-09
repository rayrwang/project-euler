import numpy as np

from functools import cache

# TODO add arbitrary precision int for numba
import numba

def inf_range_py(start: int = 0, step: int = 1):
    return range(start, 1<<62, step)

@numba.jit(cache=True)
def inf_range(start: int = 0, step: int = 1):
    return range(start, 1<<62, step)

first_primes = (2, 3, 5, 7, 11, 13, 17, 19)  # Optimal number

@numba.jit(cache=True)
def mul_mod_bounded(a: int, b: int, mod: int, /) -> int:
    """(a * b) % mod without 64-bit overflow. Valid for mod < 2**62."""
    result = 0
    a %= mod
    while b > 0:
        if b & 1:
            result = (result + a) % mod
        a = (a + a) % mod
        b >>= 1
    return result

@numba.jit(cache=True)
def mod_exp_mulmod_bounded(a: int, b: int, mod: int, /) -> int:
    """(a ** b) % mod using overflow-safe mulmod. Valid for mod < 2**62."""
    prod = 1
    a %= mod
    while b > 0:
        if b & 1:
            prod = mul_mod_bounded(prod, a, mod)
        b //= 2
        a = mul_mod_bounded(a, a, mod)
    return prod

@numba.jit(cache=True)
def is_prime(n: int, /) -> bool:
    """
    Deterministic Miller-Rabin test

    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants

    https://miller-rabin.appspot.com/
    """
    if n <= 1:
        return False
    for p in first_primes:
        if n == p:
            return True
    for p in first_primes:
        if n % p == 0:
            return False

    # n-1 = 2^s * d
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    if n < 38_010_307:
        bases = [2, 9332593]
    elif n < 4_759_123_141:
        bases = [2, 7, 61]
    elif n < 1_122_004_669_633:
        bases = [2, 13, 23, 1662803]
    elif n < 2_152_302_898_747:
        bases = [2, 3, 5, 7, 11]
    elif n < 3_474_749_660_383:
        bases = [2, 3, 5, 7, 11, 13]
    elif n < 341_550_071_728_321:
        bases = [2, 3, 5, 7, 11, 13, 17]
    else:
        # Deterministic up to 3.3e24, far beyond the 2**62 mulmod limit below.
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Direct int64 squaring overflows once x*x can exceed 2**63 (n >= ~3.04e9),
    # which silently breaks the test. For larger n use overflow-safe mulmod,
    # which is correct as long as n < 2**62.
    assert n < (1 << 62), "is_prime is only valid for n < 2**62 in int64"
    use_mulmod = n >= 3_037_000_500

    for a in bases:
        if a % n == 0:
            return True
        if use_mulmod:
            x = mod_exp_mulmod_bounded(a, d, n)
        else:
            x = mod_exp_bounded(a, d, n)
        y = x
        for _ in range(s):
            if use_mulmod:
                y = mul_mod_bounded(x, x, n)
            else:
                y = (x*x) % n
            if y == 1 and x != 1 and x != n-1:
                return False
            x = y
        if y != 1:
            return False
    return True

@numba.jit(cache=True)
def prime_sieve_bool(n: int, /) -> np.ndarray:
    is_prime_array = np.full(n, True)
    is_prime_array[0] = False
    is_prime_array[1] = False
    for n in range(2, int(n**0.5)+1):
        if is_prime_array[n]:  # Not already done by lower numbers
            is_prime_array[n**2::n] = False
    return is_prime_array

@numba.jit(cache=True)
def prime_sieve_int(n: int, /) -> np.ndarray:
    return np.arange(n, dtype=np.int64)[prime_sieve_bool(n)]

@numba.jit(cache=True)
def totient_sieve(n: int, /) -> np.ndarray:
    """Euler's totient phi(i) for all 0 <= i < n. phi[0]=0, phi[1]=1."""
    phi = np.arange(n, dtype=np.int64)
    for p in range(2, n):
        if phi[p] == p:  # p is prime (untouched so far)
            for k in range(p, n, p):
                phi[k] -= phi[k] // p
    return phi

@numba.jit(cache=True)
def is_square(n: int, /) -> bool:
    if n < 0:
        return False
    r = int(n**0.5)
    # int(n**0.5) can be off by one from float error; check neighbours.
    for c in (r - 1, r, r + 1):
        if c >= 0 and c*c == n:
            return True
    return False

@numba.jit(cache=True)
def gcd(x: int, y: int, /) -> int:
    """Greatest common divisor using Euclid's algorithm"""
    a = max(abs(x), abs(y))
    b = min(abs(x), abs(y))
    while b != 0:
        a, b = b, a % b
    return a

@numba.jit(cache=True)
def lcm(a: int, b: int, /) -> int:
    return min(a, b) * (max(a, b) // gcd(a, b))

@numba.jit(cache=True)
def lcm_list(xs: list[int], /) -> int:
    lcm_acc = xs[0]
    for x in xs[1:]:
        lcm_acc = lcm(lcm_acc, x)
    return int(lcm_acc)

fact_cache = {}
def fact(n: int, /) -> int:
    prod = 1
    for i in range(n, 1, -1):
        if i in fact_cache:
            prod *= fact_cache[i]
            break
        else:
            prod *= i
    fact_cache[n] = prod
    return prod

@numba.jit(cache=True)
def fact_bounded(n: int, /) -> int:
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

@cache
def nCr(n: int, r: int, /) -> int:
    """n! / (r!(n-r)!)"""
    prod = 1
    for i in range(max(r, n-r)+1, n+1):
        prod *= i
    return prod // fact(min(r, n-r))

@numba.jit(cache=True)
def divisors(n: int, /) -> list[int]:
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i**2 != n:
                divisors.append(n // i)
    return divisors

@numba.jit(cache=True)
def count_divisors(n: int, /) -> int:
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                divisors += 1
            else:
                divisors += 2
    return divisors

@numba.jit(cache=True)
def sum_proper_divisors(n: int, /) -> int:
    s = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                s += i
            else:
                s += i
                s += n // i
    return s - n

@numba.jit(cache=True)
def find_prime_factors_list(n: int, /) -> list[int]:
    if n <= 1:
        return [n][:0]  # empty list[int]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors_list(i) + find_prime_factors_list(n//i)
    return [n]

@numba.jit(cache=True)
def find_prime_factors_set(n: int, /) -> set[int]:
    if n <= 1:
        s = {n}
        s.discard(n)  # empty set[int]
        return s
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors_set(i) | find_prime_factors_set(n//i)
    return {n}

@numba.jit(cache=True)
def find_prime_factors_dict(n: int, /) -> dict[int, int]:
    prime_factors = find_prime_factors_list(n)
    occurrences = {}
    for p in prime_factors:
        if p in occurrences:
            occurrences[p] += 1
        else:
            occurrences[p] = 1
    return occurrences

@numba.jit(cache=True)
def totient(n: int, /) -> int:
    prod = 1
    for (p, k) in find_prime_factors_dict(n).items():
        prod *= p**(k-1)*(p-1)
    return prod

def reverse(n: int, /) -> int:
    return int("".join(reversed(str(n))))

@numba.jit(cache=True)
def reverse_bounded(n: int, /) -> int:
    r = 0
    place = count_digits_bounded(n) - 1
    while n != 0:
        digit = n % 10
        r += digit * 10 ** place
        place -= 1
        n = n // 10
    return r

def is_palindrome(n: int, /) -> bool:
    return n == reverse(n)

@numba.jit(cache=True)
def is_palindrome_bounded(n: int, /) -> bool:
    return n == reverse_bounded(n)

def count_digits(n):
    return len(str(abs(n)))

@numba.jit(cache=True)
def count_digits_bounded(n):
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

@numba.jit(cache=True)
def slice_number(n, start, stop):
    return (n // (10**(count_digits_bounded(n) - stop))) % 10**(stop-start)

def mod_exp(a, b, mod):
    prod = 1
    while b > 0:
        if b % 2 == 1:
            prod = (prod * a) % mod
        b //= 2
        a = (a * a) % mod
    return prod

@numba.jit(cache=True)
def mod_exp_bounded(a, b, mod):
    prod = 1
    while b > 0:
        if b % 2 == 1:
            prod = (prod * a) % mod
        b //= 2
        a = (a * a) % mod
    return prod

def mod_add(a: int, b: int, mod: int, /):
    return ((a % mod) + (b % mod)) % mod

def mod_sub(a: int, b: int, mod: int, /):
    return ((a % mod) - (b % mod)) % mod

def mod_mul(a: int, b: int, mod: int, /):
    return ((a % mod) * (b % mod)) % mod
    