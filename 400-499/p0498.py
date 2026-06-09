import math

P = 999999937  # prime; note 10^9 = P + 63

def c_nmd_bruteforce(n: int, m: int, d: int) -> int:
    """|coeff of x^d| in (x^n mod (x-1)^m), by direct expansion (small cases only).

    Substituting t = x-1, the remainder of (t+1)^n by t^m is sum_{i<m} C(n,i) t^i;
    re-expanding each t^i = sum_j C(i,j)(-1)^{i-j} x^j gives the x-coefficients."""
    t_coeff = [math.comb(n, i) for i in range(m)]
    x_coeff = [0] * m
    for i in range(m):
        for j in range(i + 1):
            x_coeff[j] += t_coeff[i] * math.comb(i, j) * (-1) ** (i - j)
    return abs(x_coeff[d])

def c_nmd(n: int, m: int, d: int) -> int:
    """Closed form C(n,m,d) = C(n,d) * C(n-d-1, m-d-1).

    The inner alternating sum sum_{k=0}^{m-d-1} C(n-d,k)(-1)^k telescopes to
    (-1)^{m-d-1} C(n-d-1, m-d-1) by the partial-sum identity for binomials."""
    return math.comb(n, d) * math.comb(n - d - 1, m - d - 1)

def binom_mod_small(a: int, b: int, p: int) -> int:
    """C(a,b) mod p for 0 <= a,b < p."""
    if b < 0 or b > a:
        return 0
    b = min(b, a - b)
    num = den = 1
    for i in range(b):
        num = num * ((a - i) % p) % p
        den = den * ((i + 1) % p) % p
    return num * pow(den, p - 2, p) % p

def binom_mod(n: int, r: int, p: int) -> int:
    """C(n,r) mod prime p via Lucas' theorem."""
    res = 1
    while n > 0 or r > 0:
        res = res * binom_mod_small(n % p, r % p, p) % p
        n //= p
        r //= p
    return res

if __name__ == "__main__":
    # validate the closed form against actual polynomial division
    assert c_nmd_bruteforce(6, 3, 1) == c_nmd(6, 3, 1) == 24
    assert c_nmd_bruteforce(100, 10, 4) == c_nmd(100, 10, 4) == 227197811615775

    n, m, d = 10**13, 10**12, 10**4
    a = binom_mod(n, d, P)
    b = binom_mod(n - d - 1, m - d - 1, P)
    print(a * b % P)  # 472294837
