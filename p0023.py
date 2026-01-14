
import numba

from funcs import sum_proper_divisors

@numba.jit
def is_abundant(n):
    return sum_proper_divisors(n) > n

@numba.jit
def count_non_abundant():
    s = 0
    for n in range(28123+1):
        for i in range(n//2 + 1):
            if is_abundant(i) and is_abundant(n-i):
                break
        else:
            s += n
    return s

if __name__ == "__main__":
    print(count_non_abundant())  # 4179871
