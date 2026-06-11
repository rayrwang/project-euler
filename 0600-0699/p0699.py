from bisect import bisect_right
from math import isqrt

from funcs import is_prime, prime_sieve_int

# n = 3^a * m (3 not dividing m) has sigma(n)/n with denominator a positive
# power of 3 exactly when m | sigma(n) and the 3-adic valuation of sigma(n)
# is below a. Since sigma is multiplicative over the components q^f of n,
# each prime q != 3 in m must have its full exponent covered by the sigma
# contributions of the *other* components (sigma(q^f) is never divisible by
# q). A DFS over factorizations builds n from the root 3^a outward: while
# some component prime is uncovered, branch on the new component q^f that
# covers the largest uncovered prime p (p | sigma(q^f)); when everything is
# covered, record n if v3(sigma(n)) < a, and branch on free extensions
# (new primes dividing sigma(n)) and on mutually-covering "cycle seeds"
# q * w^g with q | sigma(w^g), q > w, g >= 2, which are exactly the ways a
# new covered cluster disconnected from sigma(n) can appear (a g = 1 seed
# would force w = q - 1, which is even and so never a new prime pair).
# sigma(w)/w < 7 for all w <= 1e14 bounds how much future multiplication an
# uncovered prime p can be granted: a node is dead once n*max(p/7, 2)
# exceeds the limit, and an uncovered new prime q needs q^2 <= 7 * limit/n.

LIMIT = 10**14

C = 7  # sigma(w) < C*w for all w <= 1e14

PRIMES = prime_sieve_int(16_000_000)  # > isqrt(7 * LIMIT / 3)
PRIMES_LIST = [int(p) for p in PRIMES]
PRIMES_SMALL = PRIMES_LIST[: bisect_right(PRIMES_LIST, 100_000)]


def gcd_int(a, b):
    while b:
        a, b = b, a % b
    return a


def pollard_rho(n):
    if n % 2 == 0:
        return 2
    c = 1
    while True:
        x = y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd_int(abs(x - y), n)
        if d != n:
            return d
        c += 1


FACT_CACHE = {}


def factorize(n):
    if n in FACT_CACHE:
        return FACT_CACHE[n]
    orig = n
    out = {}
    for p in PRIMES_SMALL:
        if p * p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    stack = [n] if n > 1 else []
    while stack:
        v = stack.pop()
        if v == 1:
            continue
        if is_prime(v):
            out[v] = out.get(v, 0) + 1
        else:
            d = pollard_rho(v)
            stack += [d, v // d]
    FACT_CACHE[orig] = out
    return out


def sigma_pp(q, f):
    return (q ** (f + 1) - 1) // (q - 1)


def iroot(x, n):
    r = int(round(x ** (1.0 / n)))
    while r > 0 and r**n > x:
        r -= 1
    while (r + 1) ** n <= x:
        r += 1
    return r


def cycle_seeds(maxb):
    out = []
    for w in PRIMES_LIST:
        if w**3 > maxb:
            break
        g = 2
        while w ** (g + 1) <= maxb:
            for q in factorize(sigma_pp(w, g)):
                if q > w and q != 3 and q * w**g <= maxb:
                    out.append((q * w**g, w, g, q))
            g += 1
    out.sort()
    return out


def search(limit):
    seeds = cycle_seeds(limit // 3)
    visited = set()
    stack = []

    def push(n, comps, s):
        if n > limit or n in visited:
            return
        visited.add(n)
        resid_max = 0
        for q, f in comps.items():
            if q != 3 and f > s.get(q, 0):
                if q > resid_max:
                    resid_max = q
        if resid_max and n * max((resid_max + C - 1) // C, 2) > limit:
            return
        stack.append((n, comps, s))

    p3, a = 3, 1
    while p3 <= limit:
        push(p3, {3: a}, dict(factorize(sigma_pp(3, a))))
        a += 1
        p3 *= 3

    def merge(s, extra):
        out = dict(s)
        for q, f in extra.items():
            out[q] = out.get(q, 0) + f
        return out

    def add(n, comps, s, q, f):
        comps2 = dict(comps)
        comps2[q] = f
        push(n * q**f, comps2, merge(s, factorize(sigma_pp(q, f))))

    total = 0
    sols = []
    while stack:
        n, comps, s = stack.pop()
        B = limit // n
        resid = [q for q, f in comps.items() if q != 3 and f > s.get(q, 0)]
        if not resid:
            if s.get(3, 0) < comps[3]:
                total += n
                sols.append(n)
            for q in list(s):
                if q == 3 or q in comps or q > B:
                    continue
                qf, f = q, 1
                while qf <= B:
                    add(n, comps, s, q, f)
                    f += 1
                    qf *= q
            for base, w, g, q in seeds:
                if base > B:
                    break
                if q in s or q in comps or w in comps:
                    continue
                sig_w = factorize(sigma_pp(w, g))
                qf, f = q, 1
                wg = w**g
                while qf * wg <= B:
                    comps2 = dict(comps)
                    comps2[q] = f
                    comps2[w] = g
                    s2 = merge(merge(s, sig_w), factorize(sigma_pp(q, f)))
                    push(n * qf * wg, comps2, s2)
                    f += 1
                    qf *= q
        else:
            p = max(resid)
            # f = 1 coverers: primes q with q + 1 ≡ 0 (mod p), q <= lim1,
            # plus already-covered primes of s up to B.
            lim1 = min(isqrt(C * B), B)
            if p < 1000:
                sub = PRIMES[: bisect_right(PRIMES_LIST, lim1)]
                cand = sub[(sub + 1) % p == 0]
                for q in cand.tolist():
                    if q != 3 and q not in comps:
                        add(n, comps, s, q, 1)
            else:
                w = p - 1
                while w <= lim1:
                    if w != 3 and w not in comps and is_prime(w):
                        add(n, comps, s, w, 1)
                    w += p
            for q in list(s):
                if q > lim1 and q <= B and q not in comps and (q + 1) % p == 0:
                    add(n, comps, s, q, 1)
            # f >= 2 coverers: q <= (C*B)^(1/(f+1)), sigma(q^f) ≡ 0 (mod p),
            # plus fully pre-covered primes of s with q^f <= B.
            f = 2
            while 2**f <= B:
                cb = C * B
                if 2 ** (f + 1) <= cb:
                    limf = iroot(cb, f + 1)
                    for q in PRIMES_LIST[: bisect_right(PRIMES_LIST, limf)]:
                        if q == 3 or q in comps or q**f > B:
                            continue
                        h = 1
                        for _ in range(f):
                            h = (h * q + 1) % p
                        if h == 0:
                            add(n, comps, s, q, f)
                else:
                    limf = 1
                for q in list(s):
                    if q > limf and q != 3 and q not in comps \
                            and s[q] >= f and q**f <= B:
                        h = 1
                        for _ in range(f):
                            h = (h * q + 1) % p
                        if h == 0:
                            add(n, comps, s, q, f)
                f += 1
    return total, sols


if __name__ == "__main__":
    assert search(100)[0] == 270
    assert search(10**6)[0] == 26089287

    print(search(LIMIT)[0])  # 37010438774467572
