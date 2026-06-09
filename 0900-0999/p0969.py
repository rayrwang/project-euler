"""Project Euler 969: solution via closed form.

H(n) = sum_{j=0}^{n-1} (-1)^j (n-j)^j alpha^{n-j} / j!  with alpha = H(1) = e.
The coefficient of alpha^{n-j} is integral iff j! | (n-j)^j, which holds iff
rad(j!) = (product of primes <= j) divides n - j.

Sum_{n<=N} S(n) = sum_j (-1)^j P_j^j / j! * sum_{t=1}^{floor((N-j)/P_j)} t^j
where P_j = product of primes <= j.
"""

MOD = 10 ** 9 + 7


def power_sum(t: int, j: int) -> int:
    """sum_{i=1}^{t} i^j mod MOD via Lagrange interpolation (degree j+1)."""
    k = j + 2  # number of sample points x = 1..k
    t %= MOD
    ys = []
    acc = 0
    for x in range(1, k + 1):
        acc = (acc + pow(x, j, MOD)) % MOD
        ys.append(acc)
    # prefix[i] = prod_{x=1..i} (t - x), suffix similar
    pre = [1] * (k + 1)
    for i in range(1, k + 1):
        pre[i] = pre[i - 1] * ((t - i) % MOD) % MOD
    suf = [1] * (k + 2)
    for i in range(k, 0, -1):
        suf[i] = suf[i + 1] * ((t - i) % MOD) % MOD
    fact = [1] * (k + 1)
    for i in range(1, k + 1):
        fact[i] = fact[i - 1] * i % MOD
    total = 0
    for x in range(1, k + 1):
        num = pre[x - 1] * suf[x + 1] % MOD
        den = fact[x - 1] * fact[k - x] % MOD
        if (k - x) % 2 == 1:
            den = MOD - den
        total = (total + ys[x - 1] * num % MOD * pow(den, MOD - 2, MOD)) % MOD
    return total


def solve(n_max: int) -> int:
    # primes via tiny sieve up to 60
    sieve = [True] * 61
    sieve[0] = sieve[1] = False
    for i in range(2, 61):
        if sieve[i]:
            for m in range(i * i, 61, i):
                sieve[m] = False
    total = 0
    pj = 1  # product of primes <= j
    fact_j = 1
    j = 0
    while pj <= n_max - j:
        t = (n_max - j) // pj
        if t >= 1:
            term = pow(pj % MOD, j, MOD) * power_sum(t, j) % MOD
            term = term * pow(fact_j % MOD, MOD - 2, MOD) % MOD
            if j % 2 == 1:
                term = MOD - term
            total = (total + term) % MOD
        j += 1
        fact_j *= j
        if sieve[j]:
            pj *= j
    return total


if __name__ == "__main__":
    print(solve(10 ** 18))  # 412543690
