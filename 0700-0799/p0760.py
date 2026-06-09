import sys
from functools import cache

MOD = 10**9 + 7

@cache
def and_sum(n):
    """F(n) = sum of (k AND m) over all pairs k, m >= 0 with k + m <= n,
    modulo MOD.

    Split k = 2k' + i and m = 2m' + j over the low bits i, j: the AND is
    2 (k' AND m') plus (i AND j), and the constraint becomes
    k' + m' <= (n - i - j) // 2. Summing the four (i, j) choices,
        F(n) = 2 [ F(n//2) + 2 F((n-1)//2) + F((n-2)//2) ] + P((n-2)//2),
    where P(M) = (M+1)(M+2)/2 counts the pairs with k' + m' <= M (the i = j
    = 1 case contributes 1 per pair). The arguments are floors n / 2^t up to
    small shifts, so memoisation gives O(log^2 n) states.
    """
    if n <= 1:
        return 0
    a, b, c = n // 2, (n - 1) // 2, (n - 2) // 2
    p = (c + 1) % MOD * ((c + 2) % MOD) % MOD * pow(2, MOD - 2, MOD) % MOD
    return (2 * (and_sum(a) + 2 * and_sum(b) + and_sum(c)) + p) % MOD

def G(n):
    """g(m, n) = XOR + OR + AND = 2(m + n) - 2 (m AND n), using
    XOR = m + n - 2 AND and OR = m + n - AND. Hence
        G(N) = 2 sum_(n<=N) n (n+1) - 2 F(N)
             = 2 N (N+1)(N+2) / 3 - 2 F(N).
    """
    first = n * (n + 1) * (n + 2) // 3 % MOD
    return (2 * first - 2 * and_sum(n)) % MOD

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    assert G(10) == 754
    assert G(10**2) == 583766
    print(G(10**18))  # 172747503
