MOD = 1_000_000_007

def count_dominating_below(N):
    """D(N): dominating numbers below 10^N, modulo MOD.

    A d-digit number is dominating when one digit value occupies more than half
    the d places. At most one value can do so, so summing over the count k of
    that value (k > d/2) avoids double counting. After cancelling the
    leading-zero corrections, the number of d-digit dominating numbers is
        A(d) = sum_{k > d/2} C(d, k) * 9^(d - k + 1),
    and D(N) = sum_{d=1}^{N} A(d).
    """
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    pow9 = [1] * (N + 2)
    for i in range(1, N + 2):
        pow9[i] = pow9[i - 1] * 9 % MOD

    def comb(n, r):
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    total = 0
    for d in range(1, N + 1):
        for k in range(d // 2 + 1, d + 1):
            total = (total + comb(d, k) * pow9[d - k + 1]) % MOD
    return total

if __name__ == "__main__":
    print(count_dominating_below(2022))  # 471745499
