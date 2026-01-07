
import numba

from funcs import is_prime

if __name__ == "__main__":
    s = 0
    for n in range(3, 2_000_000, 2):
        if is_prime(n):
            s += n
    print(2+s)  # 142913828922
