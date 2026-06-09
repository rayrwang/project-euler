import numba
import numpy as np

from funcs import prime_sieve_bool

@numba.jit(cache=True)
def find(parent: np.ndarray, x: int) -> int:
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:       # path compression
        parent[x], x = root, parent[x]
    return root

@numba.jit(cache=True)
def sum_non_relatives(N: int, is_pr: np.ndarray) -> int:
    parent = np.arange(N + 1, dtype=np.int32)
    total = 0
    for p in range(2, N + 1):
        if not is_pr[p]:
            continue
        # digit count and leading place value
        L = 0
        t = p
        while t > 0:
            t //= 10
            L += 1
        # Type 1: same length, change exactly one digit -> union smaller neighbours.
        place = 1
        for j in range(L):
            digit = (p // place) % 10
            lo = 1 if j == L - 1 else 0     # keep leading digit nonzero
            for nd in range(lo, 10):
                if nd == digit:
                    continue
                c = p + (nd - digit) * place
                if c < p and is_pr[c]:
                    ra, rb = find(parent, p), find(parent, c)
                    if ra != rb:
                        parent[ra] = rb
            place *= 10
        # Type 2: drop the leading digit -> (L-1)-digit tail (smaller).
        if L >= 2:
            tail = p % (place // 10)
            if tail >= (place // 100) and is_pr[tail]:   # no leading zero
                ra, rb = find(parent, p), find(parent, tail)
                if ra != rb:
                    parent[ra] = rb
        # P is a 2's relative iff now joined to 2's component.
        if find(parent, p) != find(parent, 2):
            total += p
    return total

if __name__ == "__main__":
    N = 10**7
    is_pr = prime_sieve_bool(N + 1)
    assert sum_non_relatives(10**3, is_pr) == 431
    assert sum_non_relatives(10**4, is_pr) == 78728
    print(sum_non_relatives(N, is_pr))  # 46479497324
