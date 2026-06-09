from math import comb

def solve(n):
    """Number of equal-size disjoint subset pairs that actually need an equal-sum
    test, given the size rule already holds.

    For 2k chosen elements split into B and C, the comparison is pre-decided
    exactly when one set element-wise dominates the other -- and the number of
    such dominating splits is the Catalan number C_k. So the pairs that still
    need testing are (all splits) - (dominating splits) = C(2k,k)/2 - C_k.
    """
    total = 0
    for k in range(2, n // 2 + 1):       # k = 1 contributes nothing
        catalan = comb(2 * k, k) // (k + 1)
        need = comb(2 * k, k) // 2 - catalan
        total += comb(n, 2 * k) * need
    return total

if __name__ == "__main__":
    print(solve(12))  # 21384
