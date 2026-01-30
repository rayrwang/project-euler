
import numba

from funcs import is_palindrome_bounded as is_palindrome, is_square

@numba.jit
def sum_():
    s = 0
    for n in range(1, 100_000_000):
        if is_palindrome(n) and not is_square(n):
            is_sum = False
            for root in range(1, int(n**0.5)+1):
                sum_squares = root**2
                while sum_squares <= n:
                    if sum_squares == n:
                        is_sum = True
                        break
                    root += 1
                    sum_squares += root**2
                if is_sum:
                    break
            if is_sum:
                s += n
    return s

if __name__ == "__main__":
    print(sum_())  # 2906969179
