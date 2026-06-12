MOD = 10**9
BASE_L = 16

# A_n is the n-th smallest integer whose binary expansion occurs in the
# Thue-Morse word t (A_0 = 0); we need sum A_(10^k) for k = 1..18 mod 1e9.
# A positive integer belongs iff its expansion (leading 1) is a factor of t.
#
# Every factor of length >= 4 occurs at positions of a single parity, which
# splits the length-l factors into an even class w = mu(z) truncated to l
# letters, z a factor of length ceil(l/2), and an odd class
# w = (1 - z_0) mu(z_1:) truncated, z of length floor(l/2) + 1 - both
# bijections (whence the complexity recursion p(l) = p(ceil(l/2)) +
# p(floor(l/2) + 1) and its closed piecewise-linear form), and both
# order-preserving once the first four letters of w - which already pin
# down the class, as the conflicting pattern would force the cube 111 - are fixed.
# Counting factors below a prefix and selecting the r-th factor of a length
# therefore descend one scale per step.  The value mod 1e9 follows the same
# chain bottom-up: a mu-pair contributes z_i (b - 1) + 1 at weight b^2, so
# each level is a geometric series plus (b - 1) times the child's value at
# base b^2, peeling at most one letter from each end.

def tm_prefix(n):
    bits = [0] * n
    for i in range(1, n):
        bits[i] = bits[i >> 1] ^ (i & 1)
    return bits

TM = tm_prefix(1 << 16)
FACTORS = {}  # length -> sorted list of factor tuples, for length <= 16
BASE_COUNT = {}  # (length, prefix tuple) -> count, |prefix| <= 4
for ell in range(1, BASE_L + 1):
    fs = sorted({tuple(TM[i : i + ell]) for i in range(len(TM) - ell)})
    FACTORS[ell] = fs
    for f in fs:
        for k in range(min(4, ell) + 1):
            key = ell, f[:k]
            BASE_COUNT[key] = BASE_COUNT.get(key, 0) + 1

def half_complexity(j):
    # p(j)/2, the number of length-j factors starting with a fixed letter
    if j <= 2:
        return j
    r = (j - 1).bit_length() - 1
    q = j - 1 - (1 << r)
    if q < 1 << (r - 1):
        return (3 << (r - 1)) + 2 * q
    return (1 << (r + 1)) + q

def cumulative(ell):
    # sum of p(j)/2 for j = 1..ell
    if ell <= 0:
        return 0
    total = min(ell, 2) * (min(ell, 2) + 1) // 2
    r = 1
    while (1 << r) < ell:
        half = 1 << (r - 1)
        hi = min(ell - (1 << r) - 1, 2 * half - 1)  # largest q in this block
        if hi >= 0:
            a = min(hi, half - 1)
            total += (a + 1) * (3 * half) + a * (a + 1)
            if hi >= half:
                total += (hi - half + 1) * (1 << (r + 1))
                total += (half + hi) * (hi - half + 1) // 2
        r += 1
    return total

def count(ell, prefix):
    # number of length-ell factors beginning with the given letters
    if ell <= BASE_L:
        return BASE_COUNT.get((ell, prefix), 0)
    if len(prefix) < 4:
        return count(ell, prefix + (0,)) + count(ell, prefix + (1,))
    key = ell, prefix
    if key in MEMO:
        return MEMO[key]
    a, b, c, d = prefix
    res = 0
    if b == 1 - a and d == 1 - c:  # even class: z starts (a, c)
        res += count((ell + 1) // 2, (a, c))
    if c == 1 - b:  # odd class: z starts (1 - a, b, d)
        res += count(ell // 2 + 1, (1 - a, b, d))
    MEMO[key] = res
    return res

MEMO = {}

def powgeo(base, k):
    # (base^k, 1 + base + ... + base^(k-1)) mod MOD
    p, g = 1, 0
    for bit in bin(k)[2:]:
        p, g = p * p % MOD, g * (p + 1) % MOD
        if bit == "1":
            p, g = p * base % MOD, (g * base + 1) % MOD
    return p, g

def descend(ell, prefix, r, base):
    # (value of w[:-1] mod MOD in the given base, last letter of w), where
    # w is the r-th smallest length-ell factor starting with the prefix
    if ell <= BASE_L:
        for f in FACTORS[ell]:
            if f[: len(prefix)] == prefix:
                r -= 1
                if r == 0:
                    val = 0
                    for letter in f[:-1]:
                        val = (val * base + letter) % MOD
                    return val, f[-1]
        raise AssertionError("rank out of range")
    for ext in range(1 << (4 - len(prefix))):
        full = prefix + tuple(
            (ext >> i) & 1 for i in range(3 - len(prefix), -1, -1)
        )
        n_here = count(ell, full)
        if r > n_here:
            r -= n_here
            continue
        a, b, c, d = full
        base2 = base * base % MOD
        if b == 1 - a and d == 1 - c:  # even class
            m = (ell + 1) // 2
            pz, tz = descend(m, (a, c), r, base2)
            _, geo = powgeo(base2, m - 1)
            pw = ((base - 1) * pz + geo) % MOD
            if ell == 2 * m:  # one extra letter of the last pair
                pw = (pw * base + tz) % MOD
                return pw, 1 - tz
            return pw, tz
        m = ell // 2 + 1  # odd class: w = (1 - z_0) mu(z_1:) truncated
        pz, tz = descend(m, (1 - a, b, d), r, base2)
        pk, geo = powgeo(base2, m - 2)
        q = (pz - (1 - a) * pk) % MOD  # value of z[1:-1] in base base2
        core = (a * pk + (base - 1) * q + geo) % MOD  # a, then mu(z[1:-1])
        if ell == 2 * m - 1:
            return (core * base + tz) % MOD, 1 - tz
        return core, tz
    raise AssertionError("rank exceeds factor count")

def a_value(n):
    # A_n mod MOD for n >= 1
    lo, hi = 1, 1 << 32
    while lo < hi:
        mid = (lo + hi) // 2
        if cumulative(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    r = n - cumulative(lo - 1)
    p, t = descend(lo, (1,), r, 2)
    return (2 * p + t) % MOD

if __name__ == "__main__":
    assert a_value(100) == 3251
    assert a_value(1000) == 80852364498 % MOD
    print(sum(a_value(10**k) for k in range(1, 19)) % MOD)  # 178476944
