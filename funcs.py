
import numba

@numba.jit
def is_prime(n):
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
def is_square(n):
    return (int(n**0.5))**2 == n

@numba.jit
def gcd(x, y):
    """Greatest common divisor using Euclid's algorithm"""
    a = max(x, y)
    b = min(x, y)
    rem = a % b
    while rem != 0:
        a, b = b, rem
        rem = a % b
    return b
