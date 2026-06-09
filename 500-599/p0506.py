"""Project Euler Problem 506: Clock sequence.

The "clock" digit stream repeats 1,2,3,4,3,2 with period 6.  We chop it into
consecutive integers v_n whose decimal digit-sum equals n, and want
S(N) = sum_{n=1..N} v_n  modulo M = 123454321 for N = 10**14.

Let T(n) = n(n+1)/2 be the cumulative digit-sum target.  Walking the period-6
stream, the stream position after emitting v_1..v_n is

    e(n) = 6*(T(n)//15) + jindex[T(n) % 15],

since one full period (6 digits) contributes digit-sum 15.  The value v_n is the
block of stream digits strictly between positions e(n-1) and e(n).

Writing the infinite stream's prefix value modulo M with a geometric helper, one
finds a clean closed form for v_n modulo M:

    v_n == gval(n) - gval(n-1) * 10**L_n      (mod M),   L_n = e(n) - e(n-1),

where gval(n) = Pr0[r] - C*10**r with r = jindex[T(n) % 15], C = 123432/999999.
gval is periodic in n with period 30, and L_{n+30} = L_n + 12.  Hence

    S(N) = Sigma1 - Sigma2,
    Sigma1 = sum gval(n)                 (periodic mod 30 -> block sum),
    Sigma2 = sum gval(n-1)*10**L_n       (30 geometric series, ratio 10**12).

Everything is O(1) after a 30-term setup.
"""

M = 123454321  # = 11111**2

T = [0] * 31
for _n in range(1, 31):
    T[_n] = _n * (_n + 1) // 2

JINDEX = {0: 0, 1: 1, 3: 2, 6: 3, 10: 4, 13: 5}
PR0 = [0, 1, 12, 123, 1234, 12343]

INV66 = pow(999999, -1, M)
C = 123432 * INV66 % M


def _t(n: int) -> int:
    return n * (n + 1) // 2


def e(n: int) -> int:
    """Stream position (number of digits consumed) after emitting v_1..v_n."""
    t = _t(n)
    return 6 * (t // 15) + JINDEX[t % 15]


def gval(n: int) -> int:
    """The periodic-prefix helper g_n modulo M (period 30 in n)."""
    r = JINDEX[_t(n) % 15]
    return (PR0[r] - C * pow(10, r, M)) % M


def S(N: int) -> int:
    if N <= 0:
        return 0

    # ---- Sigma1 = sum_{n=1..N} gval(n), period 30 ----
    block = [gval(c + 1) for c in range(30)]  # gval(1..30)
    blocksum = sum(block) % M
    full = N // 30
    part = N % 30
    sigma1 = (full * blocksum + sum(block[:part])) % M

    # ---- Sigma2 = sum_{n=1..N} gval(n-1) * 10**L_n, grouped by n mod 30 ----
    R = pow(10, 12, M)  # ratio: L_{n+30} = L_n + 12
    inv_Rm1 = pow(R - 1, -1, M)  # R-1 is a unit mod M
    sigma2 = 0
    for n0 in range(1, 31):
        if n0 > N:
            break
        count = (N - n0) // 30 + 1
        a = gval(n0 - 1) * pow(10, e(n0) - e(n0 - 1), M) % M
        # a * (R^0 + R^1 + ... + R^{count-1})
        geo = (pow(R, count, M) - 1) * inv_Rm1 % M
        sigma2 = (sigma2 + a * geo) % M

    return (sigma1 - sigma2) % M


if __name__ == "__main__":
    # Given checks.  S(11) = 36120 exactly; reduce mod M for comparison.
    assert S(11) == 36120 % M, S(11)
    assert S(1000) == 18232686, S(1000)
    print(S(10**14))  # 18934502
