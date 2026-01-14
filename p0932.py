
"""typst
= Problem 932: $2025$

Let $d$ be the number of digits in $b$. We have:

$
10^d a + b = (a+b)^2 \
b^2 + (2a - 1)b + a^2 - 10^d a = 0 \
b = (1 - 2a + sqrt(4 dot 10^d a - 4a + 1)) / 2
$
"""

import numba

from funcs import is_square

@numba.jit
def T(max_digits):
    s = 0
    for shorter_len in range(1, max_digits//2 + 1):
        # longer_len = max_digits - shorter_len
        for n in range(int(10**(shorter_len-1)), int(10**shorter_len)):
            for longer_len in range(1, max_digits - shorter_len + 1):
                # Case 1
                # n is a (shorter), find b (longer)
                a = n
                disc = 4*10**longer_len*a - 4*a + 1
                if is_square(disc):
                    b = int((1 - 2*a + disc**0.5) / 2)
                    if b > 0 and len(str(b)) == longer_len:
                        ab = a*10**longer_len + b
                        if ab == (a+b)**2:
                            s += ab

                # Case 2: (happens to be unnecessary)
                # n is b (shorter), find a (longer)
                b = n
                disc = 10**(2*shorter_len) - 4*10**shorter_len*b - 4*b
                if is_square(disc):
                    a = int(((10**shorter_len) - 2*b + disc**0.5) / 2)
                    if a > 0 and len(str(a)) == longer_len:
                        ab = a*10**shorter_len + b
                        if ab == (a+b)**2:
                            s += ab
    return s

if __name__ == "__main__":
    print(T(16))  # 72673459417881349
