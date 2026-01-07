
import itertools

import numba

from funcs import is_prime

if __name__ == "__main__":
    for n in itertools.count(start=3, step=2):
        if not is_prime(n):
            for i in range(1, int(n**0.5)+1):
                if is_prime(n - (2*i**2)):
                    break
            else:
                break
    print(n)  # 5777
