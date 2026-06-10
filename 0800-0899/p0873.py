import numba
import numpy as np

MOD = 1_000_000_007


@numba.jit(cache=True)
def _mod_pow(a: int, e: int, mod: int) -> int:
    r = 1
    a %= mod
    while e:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r


@numba.jit(cache=True)
def w_count(p: int, q: int, r: int) -> int:
    """Words with p A's, q B's, r C's, every A/B pair split by >= 2 C's.

    Strip the C's: what remains is a binary string whose runs alternate;
    if it has a runs of A and b runs of B then |a - b| <= 1, it can be
    built in C(p-1, a-1) C(q-1, b-1) ways (twice that when a = b, for the
    two starting letters), and it has t = a + b - 1 type changes.  Only
    those t internal gaps need C's -- two each -- so distributing the
    remaining r - 2t C's freely over all p + q + 1 gaps gives
    C(r - 2t + p + q, p + q) insertions.  The big binomial slides from
    t to t + 1 by a rational factor, with the denominators inverted in
    one batch pass.
    """
    t_max = min(2 * min(p, q) + 1, r // 2)
    n = max(p, q) + 1
    fact = np.empty(n, dtype=np.int64)
    fact[0] = 1
    for i in range(1, n):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = np.empty(n, dtype=np.int64)
    inv_fact[n - 1] = _mod_pow(fact[n - 1], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    # binom[t] = C(r - 2t + p + q, p + q) for t = 0..t_max
    m_top = r + p + q
    k = p + q
    c = 1  # C(m_top, k) via a direct product of k factors over k!
    for i in range(k):
        c = c * ((m_top - i) % MOD) % MOD
    kf = 1
    for i in range(2, k + 1):
        kf = kf * i % MOD
    c = c * _mod_pow(kf, MOD - 2, MOD) % MOD

    denom = np.empty(2 * t_max, dtype=np.int64)
    for t in range(t_max):
        denom[2 * t] = (m_top - 2 * t) % MOD
        denom[2 * t + 1] = (m_top - 2 * t - 1) % MOD
    prefix = np.empty(2 * t_max + 1, dtype=np.int64)
    prefix[0] = 1
    for i in range(2 * t_max):
        prefix[i + 1] = prefix[i] * denom[i] % MOD
    inv_all = _mod_pow(prefix[2 * t_max], MOD - 2, MOD)
    inv_denom = np.empty(2 * t_max, dtype=np.int64)
    for i in range(2 * t_max - 1, -1, -1):
        inv_denom[i] = inv_all * prefix[i] % MOD
        inv_all = inv_all * denom[i] % MOD

    binom = np.empty(t_max + 1, dtype=np.int64)
    binom[0] = c
    for t in range(t_max):
        c = c * ((m_top - 2 * t - k) % MOD) % MOD
        c = c * ((m_top - 2 * t - 1 - k) % MOD) % MOD
        c = c * inv_denom[2 * t] % MOD * inv_denom[2 * t + 1] % MOD
        binom[t + 1] = c

    total = 0
    for a in range(1, p + 1):
        ca = fact[p - 1] * inv_fact[a - 1] % MOD * inv_fact[p - a] % MOD
        for b in range(max(1, a - 1), min(q, a + 1) + 1):
            t = a + b - 1
            if 2 * t > r:
                continue
            m = ca * fact[q - 1] % MOD * inv_fact[b - 1] % MOD
            m = m * inv_fact[q - b] % MOD
            if a == b:
                m = m * 2 % MOD
            total = (total + m * binom[t]) % MOD
    return total


if __name__ == "__main__":
    assert w_count(2, 2, 4) == 32  # given
    assert w_count(4, 4, 44) == 13908607644 % MOD  # given
    print(w_count(10**6, 10**7, 10**8))  # 735131856
