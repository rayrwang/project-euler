
import numba

from funcs import count_divisors

@numba.jit
def count_same_divisors():
    count = 0
    prev_divisors = count_divisors(1)
    for n_plus_one in range(2, int(1e7)+1):
        divisors = count_divisors(n_plus_one)
        if prev_divisors == divisors:
            count += 1
        prev_divisors = divisors
    return count

if __name__ == "__main__":
    print(count_same_divisors())  # 986262
