
import math

import numba

@numba.jit
def all_odd(n):
    while n != 0:
        if (n % 10) % 2 == 0:  # If last digit is even
            return False
        n = n // 10
    return True

@numba.jit
def reverse(n):
    r = 0
    place = math.floor(math.log(n) / math.log(10))
    while n != 0:
        digit = n % 10
        r += digit * 10 ** place
        place -= 1
        n = n // 10
    return r

@numba.jit
def count_reversible():
    count = 0
    for n in range(1_000_000_000):
        if n % 10 != 0 and all_odd(n + reverse(n)):
            count += 1
    return count

if __name__ == "__main__":
    print(count_reversible())  # 608720
