"""Project Euler 940: Two-Dimensional Recurrence.

A(0,0) = 0, A(0,1) = 1, A(m+1, n) = A(m, n+1) + A(m, n) and
A(m+1, n+1) = 2 A(m+1, n) + A(m, n).  Eliminating A(m+1, *) between the
two relations forces row 0 to satisfy A(0, n+2) = A(0, n+1) + 3 A(0, n),
and the separable ansatz A = x^m y^n is consistent exactly when

    x = y + 1,   y^2 = y + 3,

so with the two roots y_{1,2} = (1 +- sqrt(13))/2 and x = y + 1 the
boundary values pin down

    A(m, n) = (x_1^m y_1^n - x_2^m y_2^n) / sqrt(13),

a two-dimensional Lucas-style closed form (it reproduces the whole
recurrence table; spot checks A(1,1), A(1,2), A(2,1), A(2,2) =
2, 5, 7, 16 as given).  The double sum then factorises:

    S(k) = [ (sum_i x_1^{f_i})(sum_j y_1^{f_j})
             - (conjugate product) ] / sqrt(13),

and since the second product is the Galois conjugate of the first,
S(k) = 2 * (sqrt(13)-component of the first product).  All arithmetic
lives in F_p[sqrt(13)] with p = 1123581313, represented as pairs
(a, b) = a + b sqrt(13); the Fibonacci exponents up to
f_50 ~ 1.26e10 are handled by ordinary square-and-multiply.  Runs in
milliseconds.  Verified against S(3) = 30 and S(5) = 10396.
"""

MOD = 1123581313


def _mul(u: tuple[int, int], v: tuple[int, int]) -> tuple[int, int]:
    a, b = u
    c, d = v
    return ((a * c + 13 * b * d) % MOD, (a * d + b * c) % MOD)


def _mpow(u: tuple[int, int], e: int) -> tuple[int, int]:
    r = (1, 0)
    while e:
        if e & 1:
            r = _mul(r, u)
        u = _mul(u, u)
        e >>= 1
    return r


def s_value(k: int) -> int:
    inv2 = pow(2, MOD - 2, MOD)
    y1 = (inv2, inv2)
    x1 = (3 * inv2 % MOD, inv2)
    fib = [0, 1]
    for _ in range(2, k + 1):
        fib.append(fib[-1] + fib[-2])
    sx = (0, 0)
    sy = (0, 0)
    for i in range(2, k + 1):
        px = _mpow(x1, fib[i])
        py = _mpow(y1, fib[i])
        sx = ((sx[0] + px[0]) % MOD, (sx[1] + px[1]) % MOD)
        sy = ((sy[0] + py[0]) % MOD, (sy[1] + py[1]) % MOD)
    p1 = _mul(sx, sy)
    return 2 * p1[1] % MOD


def solve() -> int:
    assert s_value(3) == 30
    assert s_value(5) == 10396
    return s_value(50)


if __name__ == "__main__":
    print(solve())  # 969134784
