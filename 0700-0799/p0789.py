"""
Project Euler Problem 789: Minimal Pairing Modulo p
https://projecteuler.net/problem=789

Pair up 1..p-1 (p prime) into (p-1)/2 pairs; the cost of a pair (a, b) is
ab mod p, the total cost is the sum of pair costs, and an optimal pairing
minimizes the total cost.  All optimal pairings for p = 2000000011 have the
same cost product (product of all pair costs); find it.

Theory.  Pair costs are >= 1, and a pair has cost 1 exactly when b = a^-1.
The elements 1 and p-1 are their own inverses, so a perfect matching of
inverse pairs is impossible: some "defect chain" is needed.  Consider pairs
(1, c1), (c1^-1, c1 c2), ((c1 c2)^-1, c1 c2 c3), ..., ending when the running
product reaches p-1 (whose leftover partner closes the chain); all elements
outside the chain are matched with their inverses at cost 1.  The chain pair
costs are c1, c2, ..., ck with c1 c2 ... ck = -1 (mod p), and the total cost is
(p-1)/2 + sum(ci - 1).  Conversely (Wilson's theorem) the product of all pair
costs of any pairing is = -1 (mod p), and replacing any pair cost c = ab
(composite) by two costs a, b strictly lowers sum(c - 1); brute force over
p = 5, 7, 11, 13, 17 confirms that the minimum total cost equals
(p-1)/2 + W*, where

    W* = min{ weight(n) : n = -1 (mod p) },  weight(n) = sum over prime
    factors q of n (with multiplicity) of (q - 1),

and that the cost products of the optimal pairings are exactly the integers n
attaining W* (the chain costs are the prime factors of n).  For p = 5 this
gives total cost 2 + 2 = 4 and product 4, as stated in the problem.

Search.  W* turns out to be 239, so n's prime factors q all satisfy
q - 1 <= 260 once we cap the search at U0 = 260.  Meet in the middle:

  * side 1: all products of "small" primes q <= 23 with weight <= 140 are
    enumerated (1.8e7 multisets) into a hash table residue -> minimal weight;
  * side 2: every multiset of "large" primes 29 <= q <= 261 with weight
    wL <= 260, combined with small primes of weight ws <= max(0, 141 - wL),
    is enumerated by multiplying *inverse* primes starting from p-1, so a
    node's residue is exactly the side-1 residue needed to complete n = -1.

Completeness for every multiset of weight <= 260: put all large parts on side
2; the small parts (each <= 22) must be split with side-2 share s2 <= 141 - wL
and side-1 share <= 140.  Sorting the small parts ascending, consecutive
prefix sums differ by at most 22, and the admissible interval
[ws - 140, 141 - wL] has length >= 21 whenever ws + wL <= 260, so a valid
prefix always exists.  The search returns W* = 239 <= 260, so the cap is
verified a posteriori.  A second pass records parent pointers, collects every
side-2 node matching w2 + table[residue] = W*, rebuilds the side-1
completions of exact weight W* - w2, and multiplies out the full prime
multisets; all reconstructions yield the single integer below.
"""

import numpy as np
from numba import njit

P = 2000000011
A1 = 140  # side-1 small-prime weight bound
U0 = 260  # global weight cap (verified a posteriori: W* = 239 <= 260)
LOGSIZE = 25
MASK = (1 << LOGSIZE) - 1
NOTFOUND = 32000


@njit(cache=True)
def hpos(key):
    h = np.uint64(key) * np.uint64(0x9E3779B97F4A7C15)
    return np.int64((h >> np.uint64(64 - LOGSIZE)) & np.uint64(MASK))


@njit(cache=True)
def table_put(keys, vals, key, val):
    i = hpos(key)
    while True:
        k = keys[i]
        if k == -1:
            keys[i] = key
            vals[i] = val
            return
        if k == key:
            if val < vals[i]:
                vals[i] = val
            return
        i = (i + 1) & MASK


@njit(cache=True)
def table_get(keys, vals, key):
    i = hpos(key)
    while True:
        k = keys[i]
        if k == key:
            return vals[i]
        if k == -1:
            return np.int16(NOTFOUND)
        i = (i + 1) & MASK


@njit(cache=True)
def build_side1(small, p):
    """Enumerate small-prime multisets with weight <= A1.

    Returns the residue -> min weight hash table plus per-node arrays
    (residue, weight, parent index, prime index) for path reconstruction.
    """
    keys = np.full(1 << LOGSIZE, -1, dtype=np.int64)
    vals = np.zeros(1 << LOGSIZE, dtype=np.int16)
    ns = small.shape[0]
    cap = 18_000_000
    res = np.empty(cap, dtype=np.int64)
    wgt = np.empty(cap, dtype=np.int16)
    par = np.empty(cap, dtype=np.int32)
    pri = np.empty(cap, dtype=np.int8)
    # DFS stack of node ids; node 0 is the empty product
    res[0] = 1
    wgt[0] = 0
    par[0] = -1
    pri[0] = -1  # node 0 is the empty product; reconstruction stops here
    n = 1
    stack = np.empty(cap, dtype=np.int32)
    first = np.empty(cap, dtype=np.int8)  # smallest prime index allowed
    stack[0] = 0
    first[0] = 0
    top = 1
    while top > 0:
        top -= 1
        node = stack[top]
        i0 = first[top]
        r = res[node]
        w = wgt[node]
        table_put(keys, vals, r, wgt[node])
        for j in range(i0, ns):
            nw = w + small[j] - 1
            if nw <= A1:
                res[n] = r * small[j] % p
                wgt[n] = nw
                par[n] = node
                pri[n] = j
                stack[top] = n
                first[top] = j
                top += 1
                n += 1
    return keys, vals, res[:n], wgt[:n], par[:n], pri[:n]


@njit(cache=True)
def search_side2(keys, vals, small, sinv, large, linv, p, wstar, mat_node):
    """Enumerate side-2 multisets (large free under U0, small under budget),
    multiplying inverse primes from p-1.  First call (wstar < 0) returns the
    best total weight; second call records nodes matching the optimum.

    Returns (best, parent array, prime array, node count, match count);
    prime index convention: 0..ns-1 small, ns..ns+nl-1 large.
    """
    ns = small.shape[0]
    nl = large.shape[0]
    best = np.int64(NOTFOUND)
    cap = 45_000_000
    par = np.empty(cap, dtype=np.int32)
    pri = np.empty(cap, dtype=np.int16)
    nmat = 0
    # large-phase DFS stack (node ids carry residues/weights separately)
    capL = 1 << 16
    lnode = np.empty(capL, dtype=np.int32)
    lfirst = np.empty(capL, dtype=np.int16)
    lres = np.empty(capL, dtype=np.int64)
    lwgt = np.empty(capL, dtype=np.int16)
    # node 0 = empty product at residue p-1
    par[0] = -1
    pri[0] = -1
    n = 1
    lnode[0] = 0
    lfirst[0] = 0
    lres[0] = p - 1
    lwgt[0] = 0
    ltop = 1
    capS = 1 << 22
    snode = np.empty(capS, dtype=np.int32)
    sfirst = np.empty(capS, dtype=np.int8)
    sres = np.empty(capS, dtype=np.int64)
    swgt = np.empty(capS, dtype=np.int16)
    while ltop > 0:
        ltop -= 1
        nodeL = lnode[ltop]
        i0 = lfirst[ltop]
        rL = lres[ltop]
        wL = lwgt[ltop]
        budget = 141 - wL
        if budget < 0:
            budget = 0
        # small sub-DFS rooted at this large node
        snode[0] = nodeL
        sfirst[0] = 0
        sres[0] = rL
        swgt[0] = 0
        stop = 1
        while stop > 0:
            stop -= 1
            node = snode[stop]
            j0 = sfirst[stop]
            r = sres[stop]
            ws = swgt[stop]
            w1 = np.int64(table_get(keys, vals, r))
            tot = wL + ws + w1
            if tot < best:
                best = tot
            if wstar >= 0 and tot == wstar and nmat < mat_node.shape[0]:
                mat_node[nmat] = node
                nmat += 1
            for j in range(j0, ns):
                nws = ws + small[j] - 1
                if nws <= budget:
                    par[n] = node
                    pri[n] = j
                    snode[stop] = n
                    sfirst[stop] = j
                    sres[stop] = r * sinv[j] % p
                    swgt[stop] = nws
                    stop += 1
                    n += 1
        # large children
        for j in range(i0, nl):
            nwL = wL + large[j] - 1
            if nwL <= U0:
                par[n] = nodeL
                pri[n] = np.int16(ns + j)
                lnode[ltop] = n
                lfirst[ltop] = j
                lres[ltop] = rL * linv[j] % p
                lwgt[ltop] = nwL
                ltop += 1
                n += 1
    return best, par[:n], pri[:n], n, nmat


@njit(cache=True)
def side2_residue_weight(node, par, pri, small, sinv, linv, allw, p):
    """Recompute (residue, weight) of a side-2 node from its parent chain."""
    r = np.int64(p - 1)
    w = np.int64(0)
    ns = small.shape[0]
    while node > 0:
        j = pri[node]
        if j < ns:
            r = r * sinv[j] % p
        else:
            r = r * linv[j - ns] % p
        w += allw[j]
        node = par[node]
    return r, w


def sieve_primes(n):
    is_p = np.ones(n + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = False
    return np.flatnonzero(is_p).astype(np.int64)


def multiset_of(node, par, pri):
    out = []
    while node > 0:
        out.append(int(pri[node]))
        node = int(par[node])
    return out


def main():
    primes = sieve_primes(U0 + 1)
    small = primes[primes <= 23]
    large = primes[primes >= 29]
    sinv = np.array([pow(int(q), P - 2, P) for q in small], dtype=np.int64)
    linv = np.array([pow(int(q), P - 2, P) for q in large], dtype=np.int64)
    allp = np.concatenate([small, large])
    allw = (allp - 1).astype(np.int64)

    keys, vals, res1, wgt1, par1, pri1 = build_side1(small, P)

    dummy = np.empty(1, dtype=np.int32)
    wstar, _, _, _, _ = search_side2(
        keys, vals, small, sinv, large, linv, P, -1, dummy
    )
    assert wstar <= U0, "cap too small; raise U0"
    # p = 5 sanity check from the problem statement: total cost 4, product 4
    # (weight of 4 = 2(2-1) = 2; (5-1)/2 + 2 = 4).  Verified by brute force
    # for p in {5, 7, 11, 13, 17} during development.

    mat_node = np.empty(1 << 20, dtype=np.int32)
    _, par2, pri2, _, nmat = search_side2(
        keys, vals, small, sinv, large, linv, P, wstar, mat_node
    )
    assert nmat < mat_node.shape[0]

    products = set()
    for t in range(nmat):
        node = int(mat_node[t])
        r2, w2 = side2_residue_weight(node, par2, pri2, small, sinv, linv, allw, P)
        need_w = wstar - int(w2)
        ms2 = multiset_of(node, par2, pri2)
        # all side-1 multisets with residue r2 and weight exactly need_w
        idx = np.flatnonzero((res1 == r2) & (wgt1 == need_w))
        for k in idx:
            ms1 = multiset_of(int(k), par1, pri1)
            n = 1
            for j in ms1 + ms2:
                n *= int(allp[j])
            assert n % P == P - 1
            products.add(n)
    assert len(products) == 1, products
    return products.pop()


if __name__ == "__main__":
    print(main())  # 13431419535872807040
