
import numba

from funcs import is_prime

@numba.jit
def calc_sum():
    s = 0
    for n in range(2, 100_000_000, 2):
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if not is_prime(i + n//i):
                    break
        else:
            s += n
    return s

if __name__ == "__main__":
    print(1+calc_sum())  # 1739023853137
