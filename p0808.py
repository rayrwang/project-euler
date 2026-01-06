
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
