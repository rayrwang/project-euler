import numba

@numba.jit(cache=True)
def can_sum_to(target, m):
    """Can the digits of m be split into contiguous parts summing to target?

    Splitting only lowers the sum, so the maximum achievable is m itself (one
    part); hence m < target is hopeless and m == target succeeds. Otherwise peel
    off the trailing block r (last few digits) and recurse on the prefix.
    """
    if m < target:
        return False
    if m == target:
        return True
    t = 10
    while t < m:
        r = m % t
        if r < target and can_sum_to(target - r, m // t):
            return True
        t *= 10
    return False

@numba.jit(cache=True)
def T(limit):
    total = 0
    root = 2
    while root * root <= limit:
        square = root * root
        # square != root for root >= 2, so any successful split uses >= 2 parts.
        if can_sum_to(root, square):
            total += square
        root += 1
    return total

if __name__ == "__main__":
    print(T(10**12))  # 128088830547982
