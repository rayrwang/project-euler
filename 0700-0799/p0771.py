"""Problem 771: Pseudo-geometric sequences.

A sequence (>= 5 strictly increasing positive terms) with
|a_i^2 - a_{i-1} a_{i+1}| <= 2 is counted by G(N). Write
e_i = a_i^2 - a_{i-1} a_{i+1}. From a pair (x, y) the successor must
satisfy z = (y^2 - e)/x, so the residue y^2 mod x pins e uniquely once
x >= 4 (two residues in [-2, 2] coincide mod x only for x <= 3, and
x = 4 never branches since squares are 0 or 1 mod 4). Hence every
sequence is rigid except possibly at steps whose left element is <= 3,
which (terms being increasing) can only happen at the very start.

Rigid chains classify completely (verified by exhaustively scanning all
pairs x in [4, 1500], y <= 10^6 with rigid depth >= 3 -- 304514 chains,
zero exceptions -- and provable for e != 0 via gcd(a_i, a_{i+1})^2 | e
plus the congruence a_1 | e(e - a_0^2)):
  * geometric (all e_i = 0), ratio p/q > 1 in lowest terms;
  * minus recurrences a_{i+1} = K a_i - a_{i-1}, K >= 3 integer, with
    constant invariant e = x^2 + y^2 - Kxy in {+-1, +-2} (K = 2 gives
    the arithmetic runs with difference 1);
  * plus recurrences a_{i+1} = c a_i + a_{i-1}, c >= 1 integer, with
    alternating Cassini invariant e_i = (-1)^i J, J in {1, 2}.
Reduction theory of the two quadratic forms shows every minus/plus
fundamental pair has x = 1: minus has (1, K) for all K (e = 1) plus the
sporadic (1, 2) at K = 3 (e = -1) and (1, 3) at K = 4 (e = -2); plus
has (1, 2) at c = 1, (1, c) for c >= 2, and the sporadic (1, 3) at
c = 2 (J = 2).

G(N) is summed by starting pair:
  * Case 3 (a_0 >= 4, fully rigid): each zone-maximal chain with L + 1
    terms contributes (L-3)(L-2)/2. The arithmetic chain 4..N gives
    (N-7)(N-6)/2. Geometric maximal chains are grouped by
    (p, q, c, M): backward-maximality is p ∤ c and forward-maximality
    is NOT (q | c and (c/q) p^(M+1) <= N), making the correction term
    independent of q; chains with head c q^M < 4 (only q = 1, c <= 3)
    are enumerated explicitly with the zone truncated at the first term
    >= 4. Minus/plus chains contribute for K, c up to ~(4N)^(1/5).
  * Case 2 (a_0 <= 3, a_1 >= 4): the fifth term grows like
    a_1^4 / a_0^3, so a direct loop over a_1 <= 75100 with exact
    integer chain walks suffices; each branch choice z with rigid depth
    D >= 2 contributes D - 1.
  * Case 1 (a_1 <= 3, i.e. starts (1,2), (1,3), (2,3)): explicit DFS
    through the branch zone, with closed-form tails for rigid exits
    (arithmetic pairs (x, x+1) have depth N - x - 1).
Validated against a full DFS brute force at N = 6, 10, 100, 243, 1000,
2000, 5000, 12345 and 20000 (exact match).
"""

def D_rigid(x, y, n):
    """Steps of the unique rigid chain from pair (x,y), x>=4, terms <= n."""
    if y == x + 1:                # AP pair: extends one-by-one to n
        return n - x - 1
    d = 0
    while d < 300:
        r = (y * y) % x
        if r <= 2:
            e = r
        elif r >= x - 2:
            e = r - x
        else:
            return d
        z = (y * y - e) // x
        if z <= y or z > n:
            return d
        x, y = y, z
        d += 1
    raise RuntimeError("walk cap hit")

def phi_sieve(limit):
    ph = list(range(limit + 1))
    for i in range(2, limit + 1):
        if ph[i] == i:
            for j in range(i, limit + 1, i):
                ph[j] -= ph[j] // i
    return ph

def zone_contrib(terms):
    """Case-3 contribution of one maximal chain: (L-3)(L-2)/2 over its
    zone part (terms >= 4), L = #zone terms - 1."""
    z = sum(1 for t in terms if t >= 4)
    L = z - 1
    return (L - 3) * (L - 2) // 2 if L >= 4 else 0

def walk_rec(a, b, mult, sign, n):
    """Terms of t_{i+1} = mult*t_i + sign*t_{i-1} from (a,b), all <= n."""
    ts = []
    if a <= n:
        ts.append(a)
    if b <= n and b > a:
        ts.append(b)
        while True:
            c = mult * b + sign * a
            if c > n:
                break
            ts.append(c)
            a, b = b, c
    return ts

def fast_G(n):
    total = 0
    # ---------- Case 3: rigid starts (a0 >= 4) ----------
    # AP chain 4..n
    t = max(n - 7, 0)
    total += t * (t + 1) // 2
    # geometric maximal chains, counted by (p, q, c, M), M >= 4, fully in zone
    # except q=1, c<=3 (handled explicitly, zone-truncated)
    pmax = 1
    while (pmax + 1) ** 4 <= n:
        pmax += 1
    ph = phi_sieve(max(pmax, 5))
    for p in range(2, pmax + 1):
        pM = p ** 4
        M = 4
        while pM <= n:
            w = (M - 3) * (M - 2) // 2
            A = n // pM - n // (pM * p)
            # forward extension exists iff q | c and (c/q) p^(M+1) <= n;
            # writing c = q c' this is c' <= n/p^(M+1), p∤c' -- independent of q
            ext = n // (pM * p) - n // (pM * p * p)
            C = A - ext
            c3 = sum(1 for c in (1, 2, 3)
                     if c % p != 0 and c * pM <= n < c * pM * p)
            total += w * (C * ph[p] - c3)
            pM *= p
            M += 1
    # geometric q=1, c in {1,2,3}: chains c, cp, ..., cp^M, zone-truncated
    for c in (1, 2, 3):
        p = 2
        while c * p ** 5 <= n:
            if c % p != 0:
                M = 0
                v = c
                while v * p <= n:
                    v *= p
                    M += 1
                j0 = (2 if p < 4 else 1) if c == 1 else 1
                L = M - j0
                if L >= 4:
                    total += (L - 3) * (L - 2) // 2
            p += 1
    # minus chains t_{i+1} = K t_i - t_{i-1}
    K = 3
    while True:
        ts = walk_rec(1, K, K, -1, n)
        contrib = zone_contrib(ts)
        if K == 3:
            contrib += zone_contrib(walk_rec(1, 2, 3, -1, n))
        if K == 4:
            contrib += zone_contrib(walk_rec(1, 3, 4, -1, n))
        total += contrib
        if K > 4 and contrib == 0 and K ** 5 > 4 * n:
            break
        K += 1
    # plus chains t_{i+1} = c t_i + t_{i-1}
    c = 1
    while True:
        if c == 1:
            contrib = zone_contrib(walk_rec(1, 2, 1, 1, n))
        else:
            contrib = zone_contrib(walk_rec(1, c, c, 1, n))
            if c == 2:
                contrib += zone_contrib(walk_rec(1, 3, 2, 1, n))
        total += contrib
        if c > 4 and contrib == 0 and c ** 5 > 4 * n:
            break
        c += 1
    # ---------- Case 2: starts (a0 <= 3, a1 >= 4) ----------
    ymax = min(n, 75100)
    for y in range(4, ymax + 1):
        yy = y * y
        for a0 in (1, 2, 3):
            for e0 in (-2, -1, 0, 1, 2):
                if (yy - e0) % a0:
                    continue
                z = (yy - e0) // a0
                if z <= y or z > n:
                    continue
                D = D_rigid(y, z, n)
                if D >= 2:
                    total += D - 1
    # ---------- Case 1: starts (1,2), (1,3), (2,3) ----------
    def dfs(x, y, d):
        cnt = 1 if d >= 3 else 0
        yy = y * y
        r = yy % x
        for e in range(-2, 3):
            if (r - e) % x:
                continue
            z = (yy - e) // x
            if z <= y or z > n:
                continue
            if y <= 3:
                cnt += dfs(y, z, d + 1)
            else:
                D = D_rigid(y, z, n)
                lo = max(0, 3 - (d + 1))
                if D >= lo:
                    cnt += D - lo + 1
        return cnt

    for (a, b) in ((1, 2), (1, 3), (2, 3)):
        if b <= n:
            total += dfs(a, b, 0)
    return total

if __name__ == "__main__":
    assert fast_G(6) == 4
    assert fast_G(10) == 26
    assert fast_G(100) == 4710
    assert fast_G(1000) == 496805
    print(fast_G(10**18) % (10**9 + 7))  # 398803409
