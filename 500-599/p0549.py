"""Project Euler Problem 549: Divisibility of Factorials.

s(n) = smallest m with n | m!.  S(n) = sum_{i=2}^n s(i).  Find S(10^8).

If n = prod p^e then s(n) = max over the prime powers of s(p^e), because m! must
absorb every p^e independently and the binding constraint is the largest required
factorial.  And s(p^e) is the smallest multiple m of p for which the exponent of p
in m! reaches e (v_p(m!) only increases at multiples of p).

We compute all s(i) with one modified sieve: for each prime p (detected because its
slot is still 0), walk m = p, 2p, 3p, ... accumulating c = v_p(m!); whenever c rises
past an integer k, the value s(p^k) equals the current m, and we raise s[j] to m for
every multiple j of p^k.  Summing the array gives S(N).  S(100) = 2012 is the check.
"""

import numpy as np
import numba


@numba.jit(cache=True)
def _S(N: int) -> int:
    s = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if s[p] != 0:
            continue  # composite, already updated by a smaller prime
        # p is prime: enumerate s(p^k) and propagate to multiples of p^k
        m = 0
        c = 0          # v_p(m!) so far
        k_done = 0
        pk = p         # p^(k_done+1)
        running = True
        while running:
            m += p
            t = m
            while t % p == 0:
                c += 1
                t //= p
            # for every k in (k_done, c], s(p^k) = m
            while k_done < c:
                k_done += 1
                # pk currently = p^k_done
                j = pk
                while j <= N:
                    if m > s[j]:
                        s[j] = m
                    j += pk
                if pk > N // p:  # next power p^(k_done+1) would exceed N
                    running = False
                    break
                pk *= p
    total = 0
    for i in range(2, N + 1):
        total += s[i]
    return total


def S(N: int) -> int:
    return int(_S(N))


if __name__ == "__main__":
    assert S(100) == 2012, S(100)
    print(S(10**8))  # 476001479068717
