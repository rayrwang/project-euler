
import numba

from funcs import is_palindrome_bounded as is_palindrome, is_square

@numba.jit
def find_sum():
    s = 0
    count = 0
    for n in range(1<<62):
        if is_palindrome(n):
            ways = 0
            for cube_root in range(1<<62):
                rem = n - cube_root**3
                if rem <= 0:
                    break
                if is_square(rem):
                    ways += 1
                    if ways == 4:
                        s += n
                        count += 1
        if count == 5:
            return s

if __name__ == "__main__":
    print(find_sum())  # 
