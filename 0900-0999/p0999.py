"""Project Euler 999.

The sequence is defined by a_1 = a_2 = a_3 = 1, a_4 = 2 and the alternating
quadratic relation

    a_n**2 = a_{n+2} a_{n-2} + u * a_{n+1} a_{n-1},   u = 1 (n even), 2 (n odd),

so a_{n+2} = (a_n**2 - u a_{n+1} a_{n-1}) / a_{n-2}.  The terms grow like
exp(c n**2): this is an elliptic divisibility / Somos-4 type sequence, and no
linear recurrence exists, so we need a genuinely sub-linear evaluation of
a_N for N = 10**18 + 3 modulo the prime P = 1234567891.

Normalisation.  Writing a_n = g(n) W_n peels the alternating coefficient into a
gauge factor and leaves a *constant-coefficient* normalised EDS W with W_0 = 0,
W_1 = 1 and the clean recurrence

    W_{n+2} = (-sqrt(2) * W_{n+1} W_{n-1} + W_n**2) / W_{n-2}.

The gauge is g(n) = i**(n-1) for odd n and i**(n-1) * 2**(-1/4) for even n
(derived from a_n = kappa rho**n sigma**(n**2) omega**((-1)**n) W_n with
rho = i, omega = 2**(-1/8)).  Seeds: W_2 = -i 2**(1/4), W_3 = -1,
W_4 = 2 i 2**(1/4), and W_5 = -3 from the recurrence.  For odd n the eighth-root
cancels, so a_n = i**(n-1) W_n with W_n landing in F_p; verified for n = 1..20.

Working field.  Let theta = i * 2**(1/4); then theta**4 = 2, W_2 = -theta,
sqrt(2) = -theta**2.  Every value met here is a + b theta + c theta**2 + d
theta**3 over F_p with theta**4 = 2, so arithmetic is polynomial multiplication
reduced mod (theta**4 - 2, P).  Odd-index W_n are pure constants; even-index are
multiples of theta.  The block-doubling step divides only by W_2 = -theta, and
theta is a unit (theta**-1 = theta**3 / 2), so no field-irreducibility is needed.

Block doubling.  Keep the window V = [W_{c-3}, ..., W_{c+4}] (W_c at index 3).
From the EDS duplication identities one window at center c maps to nine values
T_j = W_{2c+j} (j = -3..5); reading bit b of N picks the length-8 sub-window
T[0:8] (c -> 2c) or T[1:9] (c -> 2c+1).  Starting from c = 1 and scanning the
bits of N below the leading one reaches c = N in O(log N) products, matching the
direct recurrence on every tested N.

For N = 10**18 + 3 (odd), N - 1 = 10**18 + 2 == 2 (mod 4) so i**(N-1) = -1 and
a_N = -W_N.  Checks: a_13 = 23321 and a_1003 == 231906014 (mod P) reproduce.
"""

P = 1234567891
INV2 = pow(2, P - 2, P)

# Field K = F_P[theta]/(theta**4 - 2): elements are 4-tuples
# (a, b, c, d) = a + b*theta + c*theta**2 + d*theta**3.
Elem = tuple[int, int, int, int]


def mul(x: Elem, y: Elem) -> Elem:
    """Multiply in K, reducing theta**4 = 2."""
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    c0 = a0 * b0
    c1 = a0 * b1 + a1 * b0
    c2 = a0 * b2 + a1 * b1 + a2 * b0
    c3 = a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
    c4 = a1 * b3 + a2 * b2 + a3 * b1
    c5 = a2 * b3 + a3 * b2
    c6 = a3 * b3
    return (
        (c0 + 2 * c4) % P,
        (c1 + 2 * c5) % P,
        (c2 + 2 * c6) % P,
        c3 % P,
    )


def sub(x: Elem, y: Elem) -> Elem:
    return ((x[0] - y[0]) % P, (x[1] - y[1]) % P, (x[2] - y[2]) % P, (x[3] - y[3]) % P)


def scal(x: Elem, s: int) -> Elem:
    s %= P
    return ((x[0] * s) % P, (x[1] * s) % P, (x[2] * s) % P, (x[3] * s) % P)


def sq(x: Elem) -> Elem:
    return mul(x, x)


def cube(x: Elem) -> Elem:
    return mul(sq(x), x)


# theta**-1 = theta**3 * INV2, so dividing by W_2 = -theta is mult by -theta**-1.
_TH_INV = scal((0, 0, 0, 1), INV2)


def div_w2(x: Elem) -> Elem:
    return scal(mul(x, _TH_INV), -1)


# Normalised-EDS seeds as elements of K.
W0: Elem = (0, 0, 0, 0)
W1: Elem = (1, 0, 0, 0)
W2: Elem = (0, -1 % P, 0, 0)  # -theta
W3: Elem = (-1 % P, 0, 0, 0)
W4: Elem = (0, 2, 0, 0)  # 2 theta
W5: Elem = (-3 % P, 0, 0, 0)
WM1: Elem = (-1 % P, 0, 0, 0)  # -W1  (antisymmetry W_{-n} = -W_n)
WM2: Elem = (0, 1, 0, 0)  # -W2


def doubling_window(v: list[Elem]) -> list[Elem]:
    """Map window [W_{c-3}..W_{c+4}] to [W_{2c-3}..W_{2c+5}]."""
    v0, v1, v2, v3, v4, v5, v6, v7 = v
    return [
        sub(mul(v3, cube(v1)), mul(v0, cube(v2))),
        div_w2(sub(mul(mul(v4, v2), sq(v1)), mul(mul(v0, v2), sq(v3)))),
        sub(mul(v4, cube(v2)), mul(v1, cube(v3))),
        div_w2(sub(mul(mul(v5, v3), sq(v2)), mul(mul(v1, v3), sq(v4)))),
        sub(mul(v5, cube(v3)), mul(v2, cube(v4))),
        div_w2(sub(mul(mul(v6, v4), sq(v3)), mul(mul(v2, v4), sq(v5)))),
        sub(mul(v6, cube(v4)), mul(v3, cube(v5))),
        div_w2(sub(mul(mul(v7, v5), sq(v4)), mul(mul(v3, v5), sq(v6)))),
        sub(mul(v7, cube(v5)), mul(v4, cube(v6))),
    ]


def w_n(n: int) -> Elem:
    """Normalised EDS value W_n in K via block doubling (n >= 1)."""
    v = [WM2, WM1, W0, W1, W2, W3, W4, W5]  # window centred at c = 1
    c = 1
    for b in bin(n)[3:]:
        t = doubling_window(v)
        if b == "0":
            v, c = t[0:8], 2 * c
        else:
            v, c = t[1:9], 2 * c + 1
    assert c == n, (c, n)
    return v[3]


def a_n(n: int) -> int:
    """a_n mod P for odd n: a_n = i**(n-1) * W_n with W_n a pure F_p constant."""
    w = w_n(n)
    assert w[1] == w[2] == w[3] == 0, "W_n not a constant for odd n"
    sign = 1 if ((n - 1) // 2) % 2 == 0 else -1
    return (sign * w[0]) % P


if __name__ == "__main__":
    assert a_n(13) == 23321, "checkpoint a_13"
    assert a_n(1003) == 231906014, "checkpoint a_1003"
    print(a_n(10**18 + 3))  # 801096743
