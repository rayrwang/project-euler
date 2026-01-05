
import numba

@numba.jit
def is_prime(n):
    if n == 2 or n == 5 or n == 11:
        return True
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 10):
        if n % i == 0:      # 10k + 3
            return False
        if n % (i+4) == 0:  # 10k + 7
            return False
        if n % (i+6) == 0:  # 10k + 9
            return False
        if n % (i+8) == 0:  # 10k + 1
            return False
    return True

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
