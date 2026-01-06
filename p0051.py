
import itertools

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

def smallest_prime():
    for n in itertools.count():
        if is_prime(n):
            for mask_int in range(1, 2**(len(str(n)))):
                mask = bin(mask_int)[2:].rjust(len(str(n)), "0")
                n_primes = 0
                for i in range(int(mask[0]), 10):  # Don't replace first digit with 0
                    if is_prime(int("".join([digit if mask_bit == '0' else str(i) for digit, mask_bit in zip(str(n), mask)]))):
                        n_primes += 1
                if n_primes == 8:
                    # Go through the replacements again and return the smallest one
                    for i in range(int(mask[0]), 10):  # Don't replace first digit with 0
                        replacement = int("".join([digit if mask_bit == '0' else str(i) for digit, mask_bit in zip(str(n), mask)]))
                        if is_prime(replacement):
                            return replacement

if __name__ == "__main__":
    print(smallest_prime())  # 121313
