
import numba

from funcs import is_square

@numba.jit
def is_pent(P):
    """Whether there's a solution to n(3n-1)/2 = P"""
    if P < 1:
        return False
    det = 1 + 24*P
    if not is_square(det):
        return False
    if (1 + int(det**0.5)) % 6 != 0:
        return False
    return True

@numba.jit
def P(n):
    return n*(3*n-1)/2

@numba.jit
def find_pair():
    D_min = float("inf")
    for j in range(1<<62):
        if P(j) - P(j-1) > D_min:
            # Have found the smallest difference
            return int(D_min)
        for k in range(j-1, 0, -1):
            s = P(j) + P(k)
            d = P(j) - P(k)
            if d >= D_min:
                break
            if d < D_min and is_pent(s) and is_pent(d):
                D_min = d

if __name__ == "__main__":
    print(find_pair())  # 5482660
