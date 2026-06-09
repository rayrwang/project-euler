import numba
import numpy as np

@numba.njit(cache=True)
def count_pairs(limit):
    """Number of pairs x <= y with x(x+1) * y(y+1) <= limit."""
    total = 0
    x = 1
    while x * (x + 1) * x * (x + 1) <= limit:
        cap = limit // (x * (x + 1))
        y = x
        while y * (y + 1) <= cap:
            total += 1
            y += 1
        x += 1
    return total

@numba.njit(cache=True)
def fill_values(limit, out):
    """Write all products x(x+1) * y(y+1) <= limit (x <= y) into out."""
    i = 0
    x = 1
    while x * (x + 1) * x * (x + 1) <= limit:
        f = x * (x + 1)
        cap = limit // f
        y = x
        while y * (y + 1) <= cap:
            out[i] = f * y * (y + 1)
            i += 1
            y += 1
        x += 1
    return i

def stealthy_count(limit):
    """N is stealthy iff N = x(x+1) y(y+1) for positive x, y.

    Sufficiency: (a, b) = (x y, (x+1)(y+1)) and (c, d) = (x(y+1), y(x+1))
    both multiply to N, with a + b = 2 x y + x + y + 1 = (c + d) + 1.
    Necessity follows from a discriminant argument (see the writeup).
    Enumerate all such products up to the limit, sort, and count distinct.
    """
    n = count_pairs(limit)
    values = np.empty(n, dtype=np.int64)
    fill_values(limit, values)
    values.sort()
    return 1 + int(np.count_nonzero(values[1:] != values[:-1]))

if __name__ == "__main__":
    assert stealthy_count(10**6) == 2851
    print(stealthy_count(10**14))  # 75737353
