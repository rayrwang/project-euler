import numba

from funcs import is_square, reverse_bounded

@numba.jit(cache=True)
def count_ways(p):
    """Number of (a, b) with a > 1, b > 1 and a**2 + b**3 == p."""
    ways = 0
    b = 2
    while b * b * b + 4 <= p:      # a**2 = p - b**3 must be at least 2**2
        if is_square(p - b * b * b):  # remainder >= 4, so its root is >= 2
            ways += 1
        b += 1
    return ways

@numba.jit(cache=True)
def find_sum():
    total = 0
    found = 0
    length = 1
    while True:
        h = length // 2
        ten_h = 10 ** h
        if length % 2 == 0:
            lo, hi, odd = ten_h // 10, ten_h, False
        else:
            lo, hi, odd = ten_h, ten_h * 10, True
        for root in range(lo, hi):
            # Mirror the root to build a palindrome; these are produced in
            # strictly increasing order across lengths and roots.
            if odd:
                pal = root * ten_h + reverse_bounded(root // 10)
            else:
                pal = root * ten_h + reverse_bounded(root)
            if count_ways(pal) == 4:
                total += pal
                found += 1
                if found == 5:
                    return total
        length += 1

if __name__ == "__main__":
    print(find_sum())  # 1004195061
