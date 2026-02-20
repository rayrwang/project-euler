
import numba

from funcs import sum_proper_divisors

@numba.jit
def find_longest_smallest():
    longest = 0
    longest_smallest_member = None
    for n in range(1_000_000):
        length = 0
        chain = []
        while True:
            length += 1
            chain.append(n)
            n = sum_proper_divisors(n)
            if (n in chain and n != chain[0]) or n > 1_000_000:
                break
            if n == chain[0]:
                if length > longest:
                    longest = length
                    longest_smallest_member = min(chain)
                break
    return longest_smallest_member

if __name__ == "__main__":
    print(find_longest_smallest())  # 14316
