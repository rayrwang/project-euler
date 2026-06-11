"""Project Euler 941: de Bruijn's Combination Lock.

C(10, 12) is the lexicographically smallest linear sequence of length
10^12 + 11 containing all 12-digit combinations: the Fredricksen-Maiorana
de Bruijn cycle (concatenation, in lex order, of all Lyndon words over
{0..9} whose length divides 12) opened at its minimal rotation, with the
first 11 digits repeated at the end. The position of a combination w is
S(L) + i, where L is the Lyndon word in whose canonical occurrence the
window starts, i the offset within it, and S(L) the total length of all
smaller Lyndon words. Since i < |L| and consecutive Lyndon words tile the
sequence, position order is exactly lexicographic order of the key (L, i)
(with the prefix rule for L), so the places p_n need no Lyndon ranking at
all, just a sort of 10^7 small keys.

(L, i) is found per word via the constructive Fredricksen-Maiorana proof
(as formulated by Kociumaka, Radoszewski & Rytter, arXiv:1510.02637).
Write w = (alpha beta)^d with beta alpha the Lyndon root of the minimal
rotation. Unless alpha is a nonempty run of 9s with d = 1, w occurs as a
factor of pred(L) L succ(L)... around L = beta alpha; in the exceptional
case it occurs around L' = the largest Lyndon word less than beta
(= primitive root of the largest self-minimal word below beta 0^|alpha|),
and w = 9^j 0^(12-j) wraps around the seam ...8 9^11, 9 | 0, 0^11 1.
Any match inside a genuine factor of the cycle is the unique occurrence.

Decoder verified by brute force against the explicit de Bruijn sequence
for (n, k) in {(2,3), (4,2), (6,2), (3,4), (4,3), (2,10), (4,4), (6,3)},
and F(2) = 2194210461325, F(10) = 32698850376317 match the given values.
"""

import numba
import numpy as np

N_LEN = 12
K = 10
Z = K - 1
MOD = 1234567891


@numba.njit(cache=True)
def min_rotation(w):
    best = 0
    for r in range(1, N_LEN):
        for i in range(N_LEN):
            a = w[(r + i) % N_LEN]
            b = w[(best + i) % N_LEN]
            if a != b:
                if a < b:
                    best = r
                break
    return best


@numba.njit(cache=True)
def primitive_period(w):
    for p in range(1, N_LEN + 1):
        if N_LEN % p == 0:
            ok = True
            for i in range(N_LEN):
                if w[i] != w[i % p]:
                    ok = False
                    break
            if ok:
                return p
    return N_LEN


@numba.njit(cache=True)
def is_self_minimal(w):
    return min_rotation(w) == 0


@numba.njit(cache=True)
def largest_selfmin_less(v, out):
    """Largest self-minimal length-12 word < v into out; False if none."""
    cand = np.empty(N_LEN, np.int64)
    for j in range(N_LEN - 1, -1, -1):
        if v[j] > 0:
            for i in range(j):
                cand[i] = v[i]
            cand[j] = v[j] - 1
            for i in range(j + 1, N_LEN):
                cand[i] = Z
            if is_self_minimal(cand):
                out[:] = cand
                return True
    return False


@numba.njit(cache=True)
def lyndon_succ(lam, plen, out):
    """Next Lyndon word (length | 12) after lam; returns its length.

    Wraps from [9] to [0].
    """
    t = np.empty(N_LEN, np.int64)
    for i in range(N_LEN):
        t[i] = lam[i % plen]
    while True:
        j = -1
        for i in range(N_LEN - 1, -1, -1):
            if t[i] < Z:
                j = i
                break
        if j == -1:
            out[0] = 0
            return 1
        t[j] += 1
        m = j + 1
        for i in range(m, N_LEN):
            t[i] = t[i % m]
        if N_LEN % m == 0:
            for i in range(m):
                out[i] = t[i]
            return m


@numba.njit(cache=True)
def lyndon_pred(lam, plen, out):
    """Previous Lyndon word (length | 12) before lam; returns its length.

    Wraps from [0] to [9].
    """
    t = np.empty(N_LEN, np.int64)
    for i in range(N_LEN):
        t[i] = lam[i % plen]
    v = np.empty(N_LEN, np.int64)
    if not largest_selfmin_less(t, v):
        out[0] = Z
        return 1
    p = primitive_period(v)
    for i in range(p):
        out[i] = v[i]
    return p


@numba.njit(cache=True)
def decode_key(w):
    """Sort key for the position of w in C(10, 12).

    Key = base-11 encoding of the Lyndon word containing the occurrence
    start (digits + 1, zero-padded on the right, so the prefix rule of
    lexicographic order is preserved), times 16, plus the offset.
    """
    r = min_rotation(w)
    rot = np.empty(N_LEN, np.int64)
    for i in range(N_LEN):
        rot[i] = w[(r + i) % N_LEN]
    p = primitive_period(rot)

    alpha_is_top = True
    for i in range(r):
        if w[i] != Z:
            alpha_is_top = False
            break

    center = np.empty(N_LEN, np.int64)
    clen = p
    for i in range(p):
        center[i] = rot[i]
    seam = False
    if r >= 1 and alpha_is_top and p == N_LEN:
        beta_zero = True
        for i in range(r, N_LEN):
            if w[i] != 0:
                beta_zero = False
                break
        if beta_zero:
            seam = True
        else:
            v = np.empty(N_LEN, np.int64)
            for i in range(N_LEN - r):
                v[i] = w[r + i]
            for i in range(N_LEN - r, N_LEN):
                v[i] = 0
            sv = np.empty(N_LEN, np.int64)
            largest_selfmin_less(v, sv)
            clen = primitive_period(sv)
            for i in range(clen):
                center[i] = sv[i]

    # Build word list around the center (or around the seam ...9|0...).
    words = np.empty((30, N_LEN), np.int64)
    lens = np.empty(30, np.int64)
    if seam:
        top = np.empty(1, np.int64)
        top[0] = Z
        lens[0] = lyndon_pred(top, 1, words[0])
        words[1, 0] = Z
        lens[1] = 1
        words[2, 0] = 0
        lens[2] = 1
        nw = 3
    else:
        lens[0] = lyndon_pred(center, clen, words[0])
        for i in range(clen):
            words[1, i] = center[i]
        lens[1] = clen
        nw = 2
    total = 0
    for i in range(nw):
        total += lens[i]
    need = lens[0] + lens[1] + N_LEN
    while total < need:
        lens[nw] = lyndon_succ(words[nw - 1], lens[nw - 1], words[nw])
        total += lens[nw]
        nw += 1

    # Flatten and search for w.
    text = np.empty(total, np.int64)
    pos = 0
    for i in range(nw):
        for j in range(lens[i]):
            text[pos] = words[i, j]
            pos += 1
    for q in range(total - N_LEN + 1):
        ok = True
        for i in range(N_LEN):
            if text[q + i] != w[i]:
                ok = False
                break
        if ok:
            acc = 0
            for i in range(nw):
                if q < acc + lens[i]:
                    off = q - acc
                    enc = np.int64(0)
                    for j in range(N_LEN):
                        d = words[i, j] + 1 if j < lens[i] else 0
                        enc = enc * 11 + d
                    return enc * 16 + off
                acc += lens[i]
    return np.int64(-1)


@numba.njit(cache=True, parallel=True)
def all_keys(a):
    n = a.shape[0]
    keys = np.empty(n, np.int64)
    for idx in numba.prange(n):  # ty: ignore[not-iterable]
        w = np.empty(N_LEN, np.int64)
        x = a[idx]
        for i in range(N_LEN - 1, -1, -1):
            w[i] = x % 10
            x //= 10
        keys[idx] = decode_key(w)
    return keys


@numba.njit(cache=True)
def lcg_values(n):
    a = np.empty(n, np.int64)
    x = np.int64(0)
    for i in range(n):
        x = (920461 * x + 800217387569) % 10**12
        a[i] = x
    return a


def solve(n_terms: int) -> int:
    a = lcg_values(n_terms)
    keys = all_keys(a)
    assert keys.min() >= 0
    order = np.argsort(keys, kind="stable")
    total = 0
    for place, idx in enumerate(order, start=1):
        total = (total + place * (int(a[idx]) % MOD)) % MOD
    return total


if __name__ == "__main__":
    print(solve(10**7))  # 1068765750
