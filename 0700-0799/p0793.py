import numba
import numpy as np

@numba.njit(cache=True)
def count_at_most(a, x):
    """Number of pairs i < j (in sorted order) with a[i] * a[j] <= x."""
    n = len(a)
    count = 0
    j = n - 1
    for i in range(n):
        if j <= i:
            break
        while j > i and a[i] * a[j] > x:
            j -= 1
        count += j - i if j > i else 0
    return count

@numba.njit(cache=True)
def M(n):
    """Median of the pairwise products S_i S_j, 0 <= i < j < n, with
    S_0 = 290797 and S_(i+1) = S_i^2 mod 50515093.

    Binary search the answer: count_at_most(x) counts pairs with product at
    most x by a linear two-pointer sweep over the sorted values (as i grows,
    the largest admissible partner index only shrinks). The number of pairs
    n(n-1)/2 is odd here, so the median is the value of rank
    (n(n-1)/2 + 1)/2; the search converges to the smallest x whose count
    reaches that rank, which is itself an attained product.
    """
    s = np.empty(n, dtype=np.int64)
    v = 290797
    for i in range(n):
        s[i] = v
        v = v * v % 50515093
    s.sort()
    pairs = n * (n - 1) // 2
    rank = (pairs + 1) // 2  # 1-indexed median rank (pairs is odd)
    lo = s[0] * s[1]
    hi = s[-1] * s[-2]
    while lo < hi:
        mid = (lo + hi) // 2
        if count_at_most(s, mid) >= rank:
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == "__main__":
    assert M(3) == 3878983057768
    assert M(103) == 492700616748525
    print(M(1_000_003))  # 475808650131120
