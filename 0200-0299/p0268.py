from math import comb

# Counting integers below N divisible by at least m distinct primes from a
# fixed set uses the weighted inclusion-exclusion
#     sum over subsets S, |S| >= m of (-1)^(|S| - m) C(|S| - 1, m - 1)
#         floor((N - 1) / prod S):
# each integer with exactly t >= m qualifying primes is counted
# sum_k (-1)^(k - m) C(k - 1, m - 1) C(t, k) = 1. A DFS over the 25 primes
# below 100 visits only subsets whose product stays below N. Verified
# against the stated 23 below 1000 and direct counting below 10^5.


def solve(n: int = 10**16, m: int = 4) -> int:
    primes = [p for p in range(2, 100) if all(p % q for q in range(2, p))]
    total = 0

    def dfs(start: int, k: int, prod: int) -> None:
        nonlocal total
        if k >= m:
            total += (-1) ** (k - m) * comb(k - 1, m - 1) * ((n - 1) // prod)
        for j in range(start, len(primes)):
            if prod * primes[j] >= n:
                break
            dfs(j + 1, k + 1, prod * primes[j])

    dfs(0, 0, 1)
    return total


if __name__ == "__main__":
    print(solve())  # 785478606870985
