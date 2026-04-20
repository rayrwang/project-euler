
import math
from functools import cache

# TODO add arbitrary precision int for numba
import numba

def inf_range_py(start: int = 0, step: int = 1):
    return range(start, 1<<62, step)

@numba.jit
def inf_range(start: int = 0, step: int = 1):
    return range(start, 1<<62, step)

first_primes = (2, 3, 5, 7, 11, 13, 17, 19)  # Optimal number
@numba.jit
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
        # TODO Fix overflow issues if use the 7 set
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if a % n == 0:
            return True
        x = mod_exp_bounded(a, d, n)
        for _ in range(s):  
            y = (x*x) % n
            if y == 1 and x != 1 and x != n-1:
                return False
            x = y
        if y != 1:
            return False
    return True

@numba.jit
def is_square(n: int, /) -> bool:
    return (int(n**0.5))**2 == n

@numba.jit
def gcd(x: int, y: int, /) -> int:
    """Greatest common divisor using Euclid's algorithm"""
    a = max(x, y)
    b = min(x, y)
    rem = a % b
    while rem != 0:
        a, b = b, rem
        rem = a % b
    return b

@numba.jit
def lcm(a: int, b: int, /) -> int:
    return min(a, b) * (max(a, b) // gcd(a, b))

@numba.jit
def lcm_list(xs: list[int], /) -> int:
    lcm_acc = lcm(xs[0], xs[1])
    for x in xs[2:]:
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

@numba.jit
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

@numba.jit
def divisors(n: int, /) -> list[int]:
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i**2 != n:
                divisors.append(n // i)
    return divisors

@numba.jit
def count_divisors(n: int, /) -> int:
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                divisors += 1
            else:
                divisors += 2
    return divisors

@numba.jit
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

@numba.jit
def find_prime_factors_list(n: int, /) -> list[int]:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors_list(i) + find_prime_factors_list(n//i)
    return [n]

@numba.jit
def find_prime_factors_set(n: int, /) -> set[int]:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors_set(i) | find_prime_factors_set(n//i)
    return {n}

@numba.jit
def find_prime_factors_dict(n: int, /) -> dict[int, int]:
    prime_factors = find_prime_factors_list(n)
    occurrences = {}
    for p in prime_factors:
        if p in occurrences:
            occurrences[p] += 1
        else:
            occurrences[p] = 1
    return occurrences

@numba.jit
def totient(n: int, /) -> int:
    prod = 1
    for (p, k) in find_prime_factors_dict(n).items():
        prod *= p**(k-1)*(p-1)
    return prod

def reverse(n: int, /) -> int:
    return int("".join(reversed(str(n))))

@numba.jit
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

@numba.jit
def is_palindrome_bounded(n: int, /) -> bool:
    return n == reverse_bounded(n)

def count_digits(n):
    return int(math.log10(n)) + 1

@numba.jit
def count_digits_bounded(n):
    return int(math.log10(n)) + 1

@numba.jit
def slice_number(n, start, stop):
    return (n // (10**(count_digits(n) - stop))) % 10**(stop-start)

def mod_exp(a, b, mod):
    prod = 1
    while b > 0:
        if b % 2 == 1:
            prod = (prod * a) % mod
        b //= 2
        a = (a * a) % mod
    return prod

@numba.jit
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
