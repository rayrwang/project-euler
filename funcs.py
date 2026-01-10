
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
