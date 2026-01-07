
import itertools

import numba

from funcs import is_prime

if __name__ == "__main__":
    s = 0
    count = 0
    for n in itertools.count():
        if count >= 50:
            break
        if is_prime(n):
            square = n**2
            rev_square = int(''.join(reversed(str(square))))
            if square != rev_square \
                    and (root_rev := int(rev_square**0.5))**2 == rev_square:
                if is_prime(root_rev):
                    count += 1
                    s += square
    print(s)  # 3807504276997394
