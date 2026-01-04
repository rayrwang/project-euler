
import itertools
import math

import numba

@numba.jit
def inf_range():
    x = 0
    while True:
        x += 1
        yield x

@numba.jit
def find_smallest_multiple():
    for n in inf_range():
        all_divisible = True
        for i in range(2, 20+1):
            if n % i != 0:
                all_divisible = False
                break
        if all_divisible:
            return n

if __name__ == "__main__":
    print(find_smallest_multiple())  # 232792560
