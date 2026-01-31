
import itertools

from funcs import is_prime, mod_exp

if __name__ == "__main__":
    n = 0
    for p in itertools.count():
        if is_prime(p):
            n += 1
            r = (mod_exp(p-1, n, p**2) + mod_exp(p+1, n, p**2)) % p**2
            if r > 10_000_000_000:
                break
    print(n)  # 21035
