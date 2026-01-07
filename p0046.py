
import itertools

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

if __name__ == "__main__":
    for n in itertools.count(start=3, step=2):
        if not is_prime(n):
            for i in range(1, int(n**0.5)+1):
                if is_prime(n - (2*i**2)):
                    break
            else:
                break
    print(n)  # 5777
