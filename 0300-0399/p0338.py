import math

import numba

# The only two-piece dissections of one rectangle into another are the
# staircase cuts: w x h with k | w and (k+1) | h becomes
# (w (k+1) / k) x (h k / (k+1)), plus the same with the roles of the sides
# swapped.  Writing the first family as (k a, (k+1) b) -> ((k+1) a, k b)
# and the second as ((k+1) c, j d) -> (j c, (j+1) d), F(w, h) counts the
# distinct non-congruent targets, so G(N) = RAW - DUP - ORIG over sheets
# h <= w <= N, where RAW counts all (sheet, k, direction) triples, DUP the
# coinciding pairs of operations, and ORIG the sheets reachable to
# themselves (exactly those with w / h = (j+1) / j, once each).
#
# Two operations collide only in pairs: solving the simultaneous equations
# shows a first-family k and second-family j coincide exactly on the sheets
# (k (j+1) m, (k+1) j m) with k >= j (k = j giving the squares), and two
# second-family j < j' coincide exactly on ((j+1)(j'+1) m, j j' m).  With
# J = j + 1, K = k these two families together count
#   #{J >= 2, K >= J-1, J K m <= N} + #{2 <= J < J', J J' m <= N}
# = D_3(N) - 2 D(N) + N + sum_{J >= 2} floor(N / (J (J-1))),
# where D and D_3 are the 2- and 3-dimensional divisor summatories: the
# symmetrisation halves cancel.  Everything is validated component by
# component against brute-force operation enumeration for N <= 60.
#
# RAW needs sum_k sum_{a <= N/k} floor(a k / (k+1)) and the swapped
# analogue: closed forms in O(1) per k below sqrt(N) and divisor blocks
# above (where the inner floor degenerates), D_3 runs in O(N^(2/3)), and
# all arithmetic is kept modulo 10^8 with pre-reduced factors.

MOD = 10**8

@numba.jit(cache=True)
def tri(n):
    # n (n + 1) / 2 mod MOD
    return (n % (2 * MOD)) * ((n + 1) % (2 * MOD)) % (2 * MOD) // 2 % MOD

@numba.jit(cache=True)
def divisor_blocks(n, start):
    # sum of floor(n / j) for j = start..n, mod MOD
    total = 0
    j = start
    while j <= n:
        v = n // j
        last = n // v
        total = (total + v % MOD * ((last - j + 1) % MOD)) % MOD
        j = last + 1
    return total

@numba.jit(cache=True)
def d3(n):
    # number of triples a b c <= n (exact, fits int64 for n = 1e12)
    total = 0
    a = 1
    while a * a * a <= n:
        na = n // a
        total += 3 * (na // a) - 3 * a + 1  # b = a row: c from a..na/a, perms
        b = a + 1
        while b * b <= na:
            cmax = na // b
            total += 6 * (cmax - b) + 3  # c > b and c = b
            b += 1
        a += 1
    return total

@numba.jit(cache=True)
def raw_sums(n):
    # sum over k of #{(a, b): k a <= n, (k+1) b <= k a} plus the swapped
    # family #{(c, d): (k+1) c <= n, k d <= (k+1) c}, mod MOD
    root = int(math.sqrt(n))
    while root * root > n:
        root -= 1
    while (root + 1) * (root + 1) <= n:
        root += 1
    total = 0
    for k in range(1, root + 1):
        amax = n // k
        u, v = divmod(amax, k + 1)
        ceil_sum = ((k + 1) % MOD * tri(u) + (u + 1) % MOD * (v % MOD)) % MOD
        total = (total + tri(amax) - ceil_sum) % MOD  # sum floor(a k/(k+1))
        cmax = n // (k + 1)
        u, v = divmod(cmax, k)
        floor_sum = (k % MOD * tri(u - 1) + u % MOD * ((v + 1) % MOD)) % MOD
        total = (total + tri(cmax) + floor_sum) % MOD  # sum floor((k+1)c/k)
    # tails: k > root has floor(N/k) <= k, so ceil(a/(k+1)) = 1 throughout,
    # and the swapped family has floor(c/k) = 0 throughout
    k = root + 1
    while k <= n:
        a = n // k
        last = n // a
        cnt = (last - k + 1) % MOD
        total = (total + (tri(a) - a) % MOD * cnt) % MOD
        k = last + 1
    j = root + 2  # j + 1 ranges over blocks; j = n + 1 contributes nothing
    while j <= n:
        c = n // j
        last = n // c
        cnt = (last - j + 1) % MOD
        total = (total + tri(c) * cnt) % MOD
        j = last + 1
    return total

@numba.jit(cache=True)
def grid_paper(n):
    raw = raw_sums(n)
    dup = (d3(n) - 2 * divisor_blocks(n, 1) + n) % MOD
    j = 2
    while j * (j - 1) <= n:
        dup = (dup + n // (j * (j - 1))) % MOD
        j += 1
    orig = divisor_blocks(n, 2)
    return (raw - dup - orig) % MOD

if __name__ == "__main__":
    assert grid_paper(10) == 55
    assert grid_paper(100) == 8670
    assert grid_paper(1000) == 971745
    assert grid_paper(10**5) == 9992617687 % MOD
    print(grid_paper(10**12))  # 15614292
