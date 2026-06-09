MOD = 10**9 + 7
PM1 = MOD - 1
W = 199
NTERMS = 199

def gf2mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return r

def gf2mod(a, m):
    dm = m.bit_length() - 1
    while a and a.bit_length() - 1 >= dm:
        a ^= m << (a.bit_length() - 1 - dm)
    return a

def gf2gcd(a, b):
    while b:
        a, b = b, gf2mod(a, b)
    return a

def charpoly(w):
    """Characteristic polynomial over F_2 of the w x w tridiagonal all-ones
    matrix M, via D_k = (x + 1) D_(k-1) + D_(k-2), D_0 = 1, D_1 = x + 1."""
    if w == 0:
        return 1
    d0, d1, xp1 = 1, 0b11, 0b11
    for _ in range(2, w + 1):
        d0, d1 = d1, gf2mul(xp1, d1) ^ d0
    return d1

def pn_mod(h, chi):
    """P_(h+1)(x) mod chi, where P_(m+1) = x P_m + P_(m-1); this is the top-left
    entry of [[x, 1], [1, 0]]^h over F_2[x] / (chi)."""
    def mul(m, n):
        a, b, c, d = m
        e, f, g, hh = n
        return (gf2mod(gf2mul(a, e) ^ gf2mul(b, g), chi),
                gf2mod(gf2mul(a, f) ^ gf2mul(b, hh), chi),
                gf2mod(gf2mul(c, e) ^ gf2mul(d, g), chi),
                gf2mod(gf2mul(c, f) ^ gf2mul(d, hh), chi))
    mat = (0b10, 1, 1, 0)  # [[x, 1], [1, 0]]
    res = (1, 0, 0, 1)
    while h:
        if h & 1:
            res = mul(res, mat)
        mat = mul(mat, mat)
        h >>= 1
    return res[0]

def solve(w, n):
    """S(w, n) = sum_{k=1}^n F(w, f_k), F(w, h) = 2^(w h - d(w, h)) where the
    nullity d(w, h) = deg gcd(P_(h+1), chi_w) (the tridiagonal M is nonderogatory,
    so its only invariant factor is chi_w and multiplication by P_(h+1) on
    F_2[x] / (chi_w) has kernel of that dimension). Exponents are reduced via
    Fermat since 2 and MOD are coprime."""
    fib = [0, 1, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    chi = charpoly(w)
    dchi = chi.bit_length() - 1
    total = 0
    for k in range(1, n + 1):
        h = fib[k]
        g = pn_mod(h, chi)
        d = dchi if g == 0 else gf2gcd(g, chi).bit_length() - 1
        e = (w * (h % PM1) - d) % PM1
        total = (total + pow(2, e, MOD)) % MOD
    return total

if __name__ == "__main__":
    print(solve(W, NTERMS))  # 652907799
