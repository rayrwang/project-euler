
import math

from collections import Counter

import numba

@numba.jit
def is_prime(n: int, /) -> bool:
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(7, int(n**0.5)+1, 6):
        if n % i == 0:  # 6k + 1
            return False
        elif n % (i+4) == 0:  # 6k + 5
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

def fact(n: int, /) -> int:
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

@numba.jit
def fact_bounded(n: int, /) -> int:
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def nCr(n: int, r: int, /) -> int:
    """n! / (r!(n-r)!)"""
    prod = 1
    for i in range(max(r, n-r)+1, n+1):
        prod *= i
    return int(prod / fact(min(r, n-r)))

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
def find_prime_factors(n: int, /) -> list[int]:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return find_prime_factors(i) + find_prime_factors(n//i)
    return [n]

def totient(n: int, /) -> int:
    prime_factors = find_prime_factors(n)
    prod = 1
    for (p, k) in Counter(prime_factors).items():
        prod *= p**(k-1)*(p-1)
    return prod

@numba.jit
def reverse(n: int, /) -> int:
    r = 0
    place = math.floor(math.log(n) / math.log(10))
    while n != 0:
        digit = n % 10
        r += digit * 10 ** place
        place -= 1
        n = n // 10
    return r

@numba.jit
def is_palindrome(n: int, /) -> bool:
    return n == reverse(n)

@numba.jit
def count_digits(n):
    return int(math.lgo10(n)) + 1

@numba.jit
def slice_number(n, start, stop):
    return (n // (10**(count_digits(n) - stop))) % 10**(stop-start)
