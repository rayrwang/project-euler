import numba
import numpy as np

MOD = 10**9 + 9

@numba.jit(cache=True)
def longest_run_sum(n: int, mod: int) -> int:
    """f(n) = sum of L(S) over all n^n n-sequences, mod `mod`.

    f(n) = sum_{k=1}^{n} #{L >= k} = n * n^n - sum_{m=1}^{n-1} N_m, where
    N_m counts sequences whose runs all have length <= m. Decomposing a
    sequence into j runs gives n (n-1)^{j-1} colour choices times the
    compositions of n into j parts of size <= m, so per length the
    generating function is rational:
        N_m = n [x^n] (x - x^{m+1}) / (1 - n x + (n-1) x^{m+1}),
    and expanding the geometric series of the denominator,
        [x^t] = sum_i (-1)^i (n-1)^i C(t - i m, i) n^{t - i(m+1)}.
    Each coefficient needs about t/(m+1) terms, so the whole sum over m
    costs O(n log n) with precomputed factorial and power tables.
    """
    # factorials, inverse factorials, powers of n and n-1
    fact = np.empty(n + 1, dtype=np.int64)
    inv_fact = np.empty(n + 1, dtype=np.int64)
    pw_n = np.empty(n + 1, dtype=np.int64)
    pw_n1 = np.empty(n + 1, dtype=np.int64)
    fact[0] = 1
    pw_n[0] = 1
    pw_n1[0] = 1
    nm = n % mod
    n1m = (n - 1) % mod
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
        pw_n[i] = pw_n[i - 1] * nm % mod
        pw_n1[i] = pw_n1[i - 1] * n1m % mod
    inv = 1
    b = fact[n]
    e = mod - 2
    while e > 0:
        if e & 1:
            inv = inv * b % mod
        b = b * b % mod
        e >>= 1
    inv_fact[n] = inv
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod

    total_n_m = 0
    for m in range(1, n):
        # coefficient of x^(n-1) minus coefficient of x^(n-1-m)
        coef = 0
        for sign in range(2):
            t = n - 1 if sign == 0 else n - 1 - m
            if t < 0:
                continue
            i = 0
            acc = 0
            while t - i * m >= i:
                top = t - i * m
                c = fact[top] * inv_fact[i] % mod * inv_fact[top - i] % mod
                term = c * pw_n1[i] % mod * pw_n[t - i * (m + 1)] % mod
                if i % 2 == 0:
                    acc = (acc + term) % mod
                else:
                    acc = (acc - term) % mod
                i += 1
            if sign == 0:
                coef = (coef + acc) % mod
            else:
                coef = (coef - acc) % mod
        total_n_m = (total_n_m + nm * coef) % mod
    return (nm * pw_n[n] - total_n_m) % mod

def brute(n: int) -> int:
    total = 0
    for s in range(n**n):
        prev = -1
        run = best = 0
        x = s
        for _ in range(n):
            d = x % n
            x //= n
            run = run + 1 if d == prev else 1
            prev = d
            if run > best:
                best = run
        total += best
    return total

if __name__ == "__main__":
    assert longest_run_sum(3, MOD) == brute(3) == 45  # given
    assert longest_run_sum(5, MOD) == brute(5)
    assert longest_run_sum(7, MOD) == 1403689  # given
    assert longest_run_sum(11, MOD) == 481496895121 % MOD  # given
    print(longest_run_sum(7_500_000, MOD))  # 97138867
