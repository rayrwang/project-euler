
import numba

from funcs import count_digits

@numba.jit
def T():
    s = 0
    for root in range(2, 1_000_000+1):
        square = root**2
        n_digits = count_digits(square)
        for split_pattern in range(2**(n_digits-1)):  # len(digits) - 1 possible split locations
            split_sum = 0
            prev_split = 0
            rem = square
            for i in range(1, n_digits+1):
                # Go from right to left
                bit = split_pattern % 2
                split_pattern //= 2
                if bit == 1:
                    split_sum += rem % 10**(i-prev_split)
                    rem //= 10**(i-prev_split)
                    prev_split = i
            split_sum += rem
            if split_sum == root:
                s += square
                break
    return s

if __name__ == "__main__":
    print(T())  # 128088830547982
