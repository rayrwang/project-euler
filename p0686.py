
import math

import numba

@numba.jit
def find_p():
    p = 0
    log_10_2 = math.log10(2)
    lower = math.log10(1.23)
    upper = math.log10(1.24)
    for j in range(1<<62):
        if lower < (j*log_10_2 % 1) < upper:
            p += 1
        if p == 678910:
            return j

if __name__ == "__main__":
    print(find_p())  # 193060223
