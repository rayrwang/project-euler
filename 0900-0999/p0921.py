"""Project Euler 921: Golden Recurrence.

The map x -> x(x^4 + 10x^2 + 5)/(5x^4 + 10x^2 + 1) is the
quintuple-argument formula for coth: coth(5t) equals that rational
function of c = coth(t).  Writing coth t = (u + 1)/(u - 1) with
u = e^{2t}, quintupling t means u -> u^5.  Since
a_0 = phi = (phi^3 + 1)/(phi^3 - 1) (using phi + 1 = phi^2), we get
u_0 = phi^3 and

    a_n = (phi^m + 1)/(phi^m - 1),     m = 3 * 5^n.

With phi^m = (L_m + F_m sqrt5)/2 and L_m^2 - 5 F_m^2 = -4 (m odd),
rationalising gives a_n = (F_m sqrt5 + 2)/L_m = (p_n sqrt5 + 1)/q_n
with p_n = F_m / 2 and q_n = L_m / 2 (both integers since 3 | m).
Check: m = 3 gives (1 sqrt5 + 1)/2 = phi and s(0) = 1 + 32 = 33.  The
closed form is verified below against the literal recurrence by exact
arithmetic in Q(sqrt5), and the modular pipeline against exact big-int
Fibonacci values for F_i <= 8.

s(F_i) needs F and L at index k = 3 * 5^{F_i} modulo M = 398874989 (a
prime).  The Pisano period is pi(M) = 199437494 = 2 * 99718747, coprime
to 5, so k mod pi(M) = 3 * 5^{F_i mod ord} where ord is the
multiplicative order of 5 modulo pi(M).  A single pass over
i = 2..1618034 carries F_i modulo ord and evaluates each term by
fast-doubling Fibonacci mod M.
"""

from fractions import Fraction
from math import gcd

M = 398874989


def _factor(x: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def fib_pair(n: int, mod: int) -> tuple[int, int]:
    """(F_n, F_{n+1}) mod mod by fast doubling."""
    if n == 0:
        return (0, 1 % mod)
    a, b = fib_pair(n >> 1, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    return (d, (c + d) % mod) if n & 1 else (c, d)


def _pisano_prime(p: int) -> int:
    if p == 5:
        return 20
    bound = p - 1 if p % 5 in (1, 4) else 2 * (p + 1)
    divs = sorted({d for i in range(1, int(bound**0.5) + 1)
                   if bound % i == 0 for d in (i, bound // i)})
    for d in divs:
        f, f1 = fib_pair(d, p)
        if f == 0 and f1 == 1:
            return d
    raise RuntimeError(p)


def pisano(n: int) -> int:
    res = 1
    for p, e in _factor(n).items():
        pp = _pisano_prime(p) * p ** (e - 1)
        res = res * pp // gcd(res, pp)
    f, f1 = fib_pair(res, n)
    assert f == 0 and f1 == 1
    return res


def _mult_order(a: int, n: int) -> int:
    lam = 1
    for p, e in _factor(n).items():
        lp = (p - 1) * p ** (e - 1)
        lam = lam * lp // gcd(lam, lp)
    o = lam
    for p in _factor(lam):
        while o % p == 0 and pow(a, o // p, n) == 1:
            o //= p
    return o


def solve(m: int) -> int:
    pi_m = pisano(M)
    assert pi_m % 5 != 0  # so 5^x mod pi_m reduces via the order of 5
    order = _mult_order(5, pi_m)
    inv2 = pow(2, -1, M)
    total = 0
    fa, fb = 1, 1  # F_1, F_2 modulo `order`
    for _ in range(2, m + 1):
        k = 3 * pow(5, fb, pi_m) % pi_m
        f, f1 = fib_pair(k, M)
        lk = (2 * f1 - f) % M
        p = f * inv2 % M
        q = lk * inv2 % M
        total = (total + pow(p, 5, M) + pow(q, 5, M)) % M
        fa, fb = fb, (fa + fb) % order
    return total


def _s_exact(fi: int) -> int:
    def fp(n: int) -> tuple[int, int]:
        if n == 0:
            return (0, 1)
        x, y = fp(n >> 1)
        c = x * (2 * y - x)
        d = x * x + y * y
        return (d, c + d) if n & 1 else (c, d)

    f, f1 = fp(3 * 5**fi)
    return ((f // 2) ** 5 + ((2 * f1 - f) // 2) ** 5) % M


if __name__ == "__main__":
    # closed form vs literal recurrence, exactly in Q(sqrt5)
    def fp_exact(n):
        if n == 0:
            return (0, 1)
        x, y = fp_exact(n >> 1)
        c = x * (2 * y - x)
        d = x * x + y * y
        return (d, c + d) if n & 1 else (c, d)

    x, y = Fraction(1, 2), Fraction(1, 2)  # a_0 = (1 + sqrt5)/2 = x + y*sqrt5
    for n in range(4):
        f, f1 = fp_exact(3 * 5**n)
        lm = 2 * f1 - f
        assert (x, y) == (Fraction(2, lm), Fraction(f, lm)), n
        # apply the recurrence in Q(sqrt5): represent a = x + y sqrt5
        def mul(a, b):
            return (a[0] * b[0] + 5 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])
        a = (x, y)
        a2 = mul(a, a)
        a4 = mul(a2, a2)
        num = mul(a, (a4[0] + 10 * a2[0] + 5, a4[1] + 10 * a2[1]))
        den = (5 * a4[0] + 10 * a2[0] + 1, 5 * a4[1] + 10 * a2[1])
        dnorm = den[0] ** 2 - 5 * den[1] ** 2
        x = (num[0] * den[0] - 5 * num[1] * den[1]) / dnorm
        y = (num[1] * den[0] - num[0] * den[1]) / dnorm
    assert _s_exact(0) == 33
    # modular pipeline vs exact big-int values for small F_i: terms of S
    pi_m = pisano(M)
    order = _mult_order(5, pi_m)
    inv2 = pow(2, -1, M)
    for fi in (1, 2, 3, 5, 8):
        k = 3 * pow(5, fi % order, pi_m) % pi_m
        f, f1 = fib_pair(k, M)
        lk = (2 * f1 - f) % M
        got = (pow(f * inv2 % M, 5, M) + pow(lk * inv2 % M, 5, M)) % M
        assert got == _s_exact(fi), fi
    print(solve(1618034))  # 378401935
