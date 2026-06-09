from itertools import combinations, product

import numba
import numpy as np

K = 50000
MAXLEN = 15

def gen_duodigits(maxlen):
    """All positive integers whose decimal form uses at most two distinct
    digits and has at most maxlen digits, returned sorted (fits in int64)."""
    s = set()
    for a, b in combinations(range(10), 2):
        for length in range(1, maxlen + 1):
            for tup in product((a, b), repeat=length):
                if tup[0] == 0:
                    continue
                v = 0
                for d in tup:
                    v = v * 10 + d
                s.add(v)
    for a in range(1, 10):
        v = 0
        for _ in range(maxlen):
            v = v * 10 + a
            s.add(v)
    return np.array(sorted(s), dtype=np.int64)

@numba.njit(cache=True)
def scan_nonmult(arr, k, dn):
    """For each n in 1..k not divisible by 10, store the smallest duodigit
    multiple (the first divisible entry of the sorted array)."""
    for n in range(1, k + 1):
        if n % 10 == 0:
            continue
        for i in range(arr.shape[0]):
            if arr[i] % n == 0:
                dn[n] = arr[i]
                break

@numba.njit(cache=True)
def bfs_mult(n, x):
    """Shortest, then lexicographically smallest number with digits in {0, x},
    leading digit x, divisible by n. Returns parent arrays over residues."""
    par_res = np.full(n, np.int64(-1))
    par_dig = np.full(n, np.int8(-1))
    visited = np.zeros(n, np.uint8)
    q = np.empty(n + 5, np.int64)
    head = 0
    tail = 0
    start = x % n
    visited[start] = 1
    par_res[start] = -2
    par_dig[start] = x
    q[tail] = start
    tail += 1
    while head < tail:
        r = q[head]
        head += 1
        if r == 0:
            break
        for d in (0, x):
            nr = (r * 10 + d) % n
            if not visited[nr]:
                visited[nr] = 1
                par_res[nr] = r
                par_dig[nr] = d
                q[tail] = nr
                tail += 1
    return par_res, par_dig

def dmult(n):
    """Smallest duodigit multiple of n when 10 | n (its digit set is {0, x})."""
    best = None
    for x in range(1, 10):
        par_res, par_dig = bfs_mult(n, x)
        if par_res[0] == -1:
            continue
        digs = []
        r = 0
        while True:
            d = par_dig[r]
            if d < 0:
                break
            digs.append(int(d))
            pr = par_res[r]
            if pr == -2:
                break
            r = pr
        digs.reverse()
        v = 0
        for d in digs:
            v = v * 10 + d
        if v > 0 and v % n == 0 and (best is None or v < best):
            best = v
    return best

def sci(num, sig=13):
    s = str(num)
    exp = len(s) - 1
    if len(s) <= sig:
        digits = s.ljust(sig, "0")
    elif s[sig] >= "5":
        kept = str(int(s[:sig]) + 1)
        if len(kept) > sig:
            kept = kept[:sig]
            exp += 1
        digits = kept
    else:
        digits = s[:sig]
    return f"{digits[0]}.{digits[1:]}e{exp}"

def solve(k):
    arr = gen_duodigits(MAXLEN)
    dn = np.zeros(k + 1, np.int64)
    scan_nonmult(arr, k, dn)
    total = 0
    for n in range(1, k + 1):
        total += dmult(n) if n % 10 == 0 else int(dn[n])
    return total

if __name__ == "__main__":
    print(sci(solve(K)))  # 2.452767775565e20
