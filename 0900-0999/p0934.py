"""Project Euler 934: Unlucky Primes.

u(n) > p means n mod q is a multiple of 7 for every prime q <= p.  For
q in {2, 3, 5, 7} the only multiple of 7 in [0, q) is 0, so 210 | n.
Writing n = 7j (with 30 | j), for q > 7:

    n mod q in 7Z  <=>  7j = 7t (mod q), 7t < q  <=>  j mod q <= (q-1)//7,

an initial interval.  So with X = floor(N/7) and A_p(N) = #{j <= X :
30 | j and j mod q <= m_q for all 7 < q <= p}, telescoping the sum over
the value of u gives

    U(N) = 2N + sum_p (nextprime(p) - p) * A_p(N).

The allowed residues form CRT classes; a DFS over primes 11, 13, ...
accumulates exact class counts floor((X - r)/L) + 1 per level while the
class count stays small (6.35 million classes through q = 43, where the
modulus L ~ 1.9e15 nears X ~ 1.4e16).  Past that, every class has only
a handful of members <= X (about 5e7 integers in total); these are
enumerated explicitly and streamed through the remaining primes until
the survivor count hits zero (around q ~ 90), giving every deeper A_p
exactly.

Validated against a per-n brute force for N = 1470 (given U = 4293) and
N = 10^5 .. 10^8.
"""

import numpy as np
from numba import njit

PRIMES = np.array([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                   67, 71, 73, 79, 83, 89, 97, 101, 103, 107], dtype=np.int64)
NEXTP = {2: 3, 3: 5, 5: 7, 7: 11}
for _i in range(len(PRIMES) - 1):
    NEXTP[int(PRIMES[_i])] = int(PRIMES[_i + 1])

BRUTE_PRIMES = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                         43, 47, 53, 59, 61, 67, 71, 73, 79], dtype=np.int64)


@njit(cache=True)
def _dfs_count(x, primes, kmax, counts):
    stack_r = np.zeros(kmax + 2, dtype=np.int64)
    stack_l = np.zeros(kmax + 2, dtype=np.int64)
    stack_c = np.zeros(kmax + 2, dtype=np.int64)
    lvl = 0
    stack_l[0] = 30
    while lvl >= 0:
        r = stack_r[lvl]
        ll = stack_l[lvl]
        c = stack_c[lvl]
        q = primes[lvl]
        if c > (q - 1) // 7:
            lvl -= 1
            if lvl >= 0:
                stack_c[lvl] += 1
            continue
        linv = 1
        b = ll % q
        e = q - 2
        while e:
            if e & 1:
                linv = linv * b % q
            b = b * b % q
            e >>= 1
        r2 = r + ll * ((c - r) % q * linv % q)
        l2 = ll * q
        if r2 == 0:
            cnt = x // l2
        elif r2 <= x:
            cnt = (x - r2) // l2 + 1
        else:
            cnt = 0
        counts[lvl + 1] += cnt
        if cnt == 0:
            stack_c[lvl] += 1
            continue
        if lvl + 1 == kmax:
            j = r2 if r2 >= 1 else l2
            while j <= x:
                k = kmax
                while k < len(primes):
                    q2 = primes[k]
                    if j % q2 > (q2 - 1) // 7:
                        break
                    counts[k + 1] += 1
                    k += 1
                j += l2
            stack_c[lvl] += 1
        else:
            lvl += 1
            stack_r[lvl] = r2
            stack_l[lvl] = l2
            stack_c[lvl] = 0


def solve(n: int) -> int:
    x = n // 7
    kmax = 0
    ll = 30
    cls = 1
    while kmax < len(PRIMES):
        q = int(PRIMES[kmax])
        if (ll * q > max(x, 1) and cls > 10**5) \
                or cls * ((q - 1) // 7 + 1) > 2 * 10**7:
            break
        ll *= q
        cls *= (q - 1) // 7 + 1
        kmax += 1
        if ll > max(x, 1):
            break
    kmax = max(kmax, 1)
    counts = np.zeros(len(PRIMES) + 1, dtype=np.int64)
    _dfs_count(x, PRIMES, kmax, counts)
    total = 2 * n + (n // 2) + 2 * (n // 6) + 2 * (n // 30) + 4 * (n // 210)
    for i in range(len(PRIMES)):
        a = int(counts[i + 1])
        if a == 0:
            break
        p = int(PRIMES[i])
        total += (NEXTP[p] - p) * a
    else:
        raise RuntimeError("prime list too short")
    return total


@njit(cache=True)
def _brute(n: int) -> int:
    tot = 0
    for m in range(1, n + 1):
        for i in range(len(BRUTE_PRIMES)):
            p = BRUTE_PRIMES[i]
            if (m % p) % 7 != 0:
                tot += p
                break
    return tot


if __name__ == "__main__":
    assert solve(1470) == 4293  # given
    for n_chk in (1470, 10**5, 10**6, 10**7):
        assert solve(n_chk) == _brute(n_chk), n_chk
    print(solve(10**17))  # 292137809490441370
