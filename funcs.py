
import numba

@numba.jit
def is_prime(n):
    if n == 2 or n == 5 or n == 11:
        return True
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 10):
        if n % i == 0:      # 10k + 3
            return False
        if n % (i+4) == 0:  # 10k + 7
            return False
        if n % (i+6) == 0:  # 10k + 9
            return False
        if n % (i+8) == 0:  # 10k + 1
            return False
    return True
