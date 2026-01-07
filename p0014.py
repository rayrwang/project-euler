
import numba

@numba.jit
def collatz_len(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        length += 1
    return length

if __name__ == "__main__":
    n_max = None
    max_len = float("-inf")
    for n in range(1, 1_000_000):
        length = collatz_len(n)
        if length > max_len:
            n_max = n
            max_len = length
    print(n_max)  # 837799
