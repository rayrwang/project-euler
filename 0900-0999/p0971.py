import numpy as np
import numba


@numba.njit(cache=True)
def solve(n: int) -> int:
    sieve = np.ones(n + 1, dtype=np.bool_)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i :: i] = False
        i += 1
    total = 0
    for p in range(11, n + 1, 5):  # p ≡ 1 (mod 5)
        if not sieve[p]:
            continue
        e = (p - 1) // 5
        # find a generator of mu_5
        zeta = 1
        a = 2
        while True:
            z = 1
            base = a % p
            ee = e
            while ee:
                if ee & 1:
                    z = z * base % p
                base = base * base % p
                ee >>= 1
            if z != 1:
                zeta = z
                break
            a += 1
        mu = np.empty(5, dtype=np.int64)
        mu[0] = 1
        for i2 in range(1, 5):
            mu[i2] = mu[i2 - 1] * zeta % p
        # next-state map on indices 0..4
        nxt = np.empty(5, dtype=np.int64)
        for i2 in range(5):
            v = mu[i2]
            # chi(1+v) = (1+v)^e mod p
            z = 1
            base = (1 + v) % p
            ee = e
            while ee:
                if ee & 1:
                    z = z * base % p
                base = base * base % p
                ee >>= 1
            w = v * z % p
            for j in range(5):
                if mu[j] == w:
                    nxt[i2] = j
                    break
        # count states on cycles
        t = 0
        for s in range(5):
            # iterate 5 steps to land on a cycle, then check return
            y = s
            for _ in range(5):
                y = nxt[y]
            # y is on a cycle; s is on a cycle iff s reachable from y
            z2 = y
            found = False
            for _ in range(5):
                if z2 == s:
                    found = True
                    break
                z2 = nxt[z2]
            if found:
                t += 1
        total += 1 + t * (p - 1) // 5
    return total


if __name__ == "__main__":
    print(solve(10 ** 8))  # 33626723890930
