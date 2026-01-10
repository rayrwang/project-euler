
from funcs import is_prime

if __name__ == "__main__":
    s = 0
    primes = 0
    for n in range(11, 1<<62):
        if is_prime(n):
            truncatable = True

            mask = 10
            while mask < n:  # Truncate from left to right, in reverse
                if not is_prime(n % mask):
                    truncatable = False
                    break
                mask = mask * 10

            if not truncatable:
                continue

            n_trl = n
            while n_trl != 0:  # Truncate from right to left
                if not is_prime(n_trl):
                    truncatable = False
                    break
                n_trl = n_trl // 10

            if not truncatable:
                continue

            s += n
            primes += 1
            if primes == 11:
                break
    print(s)  # 748317
