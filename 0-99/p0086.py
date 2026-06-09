import numba

@numba.jit(cache=True)
def _is_square(v):
    r = int(v**0.5)
    for cand in (r - 1, r, r + 1):
        if cand >= 0 and cand * cand == v:
            return True
    return False

@numba.jit(cache=True)
def count_up_to(m):
    """Number of cuboids a <= b <= c <= m whose shortest surface route is integer."""
    total = 0
    for c in range(1, m + 1):
        for s in range(2, 2 * c + 1):           # s = a + b
            if _is_square(s * s + c * c):
                # count pairs (a, b) with 1 <= a <= b <= c and a + b = s
                if s <= c + 1:
                    total += s // 2
                else:
                    total += s // 2 - (s - c) + 1
    return total

@numba.jit(cache=True)
def solve(target):
    total = 0
    c = 0
    while total <= target:
        c += 1
        for s in range(2, 2 * c + 1):
            if _is_square(s * s + c * c):
                if s <= c + 1:
                    total += s // 2
                else:
                    total += s // 2 - (s - c) + 1
    return c

if __name__ == "__main__":
    print(solve(1_000_000))  # 1818
