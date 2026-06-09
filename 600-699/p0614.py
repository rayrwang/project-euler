import numba
import numpy as np

MOD = 10**9 + 7
BLOCK = 1 << 15

def _pent(k: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Generalized pentagonal exponents k*i(3i-1)/2 <= n (ascending) and signs (-1)^i."""
    exps = [0]
    signs = [1]
    i = 1
    while True:
        added = False
        for ii in (i, -i):
            e = k * (ii * (3 * ii - 1) // 2)
            if e <= n:
                exps.append(e)
                signs.append(-1 if i % 2 else 1)
                added = True
        if not added:
            break
        i += 1
    return np.array(exps, dtype=np.int64), np.array(signs, dtype=np.int64)

@numba.jit(cache=True)
def _mul(s: np.ndarray, exps: np.ndarray, signs: np.ndarray) -> np.ndarray:
    """Multiply s by E_k (int32, modular) via one sequential sweep per term."""
    n = len(s) - 1
    res = np.zeros(n + 1, dtype=np.int32)
    for t in range(len(exps)):
        e = exps[t]
        if e > n:
            break
        if signs[t] == 1:
            for j in range(e, n + 1):
                v = res[j] + s[j - e]
                res[j] = v - MOD if v >= MOD else v
        else:
            for j in range(e, n + 1):
                v = res[j] - s[j - e]
                res[j] = v + MOD if v < 0 else v
    return res

@numba.jit(cache=True)
def _div(s: np.ndarray, ne: np.ndarray, ns: np.ndarray, fe: np.ndarray, fs: np.ndarray, bsize: int) -> np.ndarray:
    """Divide s by E_k in place (int32). Far terms via modular sweeps on finalized
    values, near terms via the recurrence inside a cache-resident window."""
    n = len(s) - 1
    nn = len(ne)
    nf = len(fe)
    lo = 0
    while lo <= n:
        hi = min(lo + bsize, n + 1)
        for t in range(nf):
            e = fe[t]
            if e > hi - 1:
                break
            j0 = e if e > lo else lo
            if fs[t] == 1:
                for j in range(j0, hi):
                    v = s[j] - s[j - e]
                    s[j] = v + MOD if v < 0 else v
            else:
                for j in range(j0, hi):
                    v = s[j] + s[j - e]
                    s[j] = v - MOD if v >= MOD else v
        for j in range(lo, hi):
            acc = np.int64(s[j])
            for t in range(nn):
                e = ne[t]
                if e > j:
                    break
                acc -= ns[t] * s[j - e]
            s[j] = acc % MOD
        lo = hi
    return s

def solve(n: int) -> int:
    """sum_{i=1}^n P(i) mod 1e9+7 via G(x) = E2^2 * E8 / (E1 * E4^2)."""
    s = np.zeros(n + 1, dtype=np.int32)
    s[0] = 1
    for k in (2, 2, 8):
        e, sg = _pent(k, n)
        s = _mul(s, e, sg)
    for k in (1, 4, 4):
        e, sg = _pent(k, n)
        near = (e < BLOCK) & (e > 0)
        far = e >= BLOCK
        s = _div(s, e[near], sg[near], e[far], sg[far], BLOCK)
    return (int(s.astype(np.int64).sum() % MOD) - 1) % MOD

if __name__ == "__main__":
    print(solve(10**7))  # 130694090
