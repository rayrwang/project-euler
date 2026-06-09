import numba

from funcs import mod_exp_bounded

MOD = 10**9 + 7

@numba.jit(cache=True)
def s(n: int, mod: int) -> int:
    """S(n) = sum_{p=1}^n sum_{k=1}^n (a_k+b_k)^p (b_k+c_k)^p (c_k+a_k)^p mod p.

    The defining equation 1/x = (k/x)^2 (k+x^2) - k x clears to the cubic
    x^3 - k x^2 + (1/k) x - k^2 = 0, whose roots a,b,c satisfy (Vieta)
    a+b+c = k, ab+bc+ca = 1/k, abc = k^2. Then
        (a+b)(b+c)(c+a) = (a+b+c)(ab+bc+ca) - abc = k*(1/k) - k^2 = 1 - k^2,
    so the inner product is just (1-k^2)^p and
        S(n) = sum_{k=1}^n sum_{p=1}^n (1-k^2)^p,
    a geometric series in r = 1 - k^2 for each k.
    """
    total = 0
    for k in range(1, n + 1):
        r = (1 - k * k) % mod
        if r == 0:  # k = 1; the whole geometric series vanishes
            continue
        # sum_{p=1}^n r^p = r (r^n - 1) / (r - 1)
        numerator = r * ((mod_exp_bounded(r, n, mod) - 1) % mod) % mod
        denominator = (r - 1) % mod
        total = (total + numerator * mod_exp_bounded(denominator, mod - 2, mod)) % mod
    return total

if __name__ == "__main__":
    assert s(4, MOD) == 51160
    print(s(10**6, MOD))  # 191541795
