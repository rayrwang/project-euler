
import itertools

import numba

from funcs import is_prime

@numba.jit
def find_longest_sum():
    sums = []
    lengths = []
    for n in range(1_000_000):
        if is_prime(n):
            for i in range(len(sums)):
                if (sums[i]+n) < 1_000_000:
                    sums[i] += n
                    lengths[i] += 1
            sums.append(n)
            lengths.append(1)
    longest_sum = None
    longest_length = 0
    for i, (s, length) in enumerate(zip(sums, lengths)):
        if is_prime(s) and length > longest_length:
            longest_length = length
            longest_sum = s
    return longest_sum

if __name__ == "__main__":
    print(find_longest_sum())  # 997651
