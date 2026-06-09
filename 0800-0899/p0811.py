from math import comb

P = 1_000_062_031


def a_factored_mod(one_bits: list[int], mod: int) -> int:
    """A(x) mod `mod`, given the positions of x's set bits in decreasing order.

    Writing x = y * 2^j with y odd, the recursion turns into
    f_j(y) = sum_a C(j,a) 3^(j-a) 5^a f_(m+a-1)(u) for y = u * 2^m + 1, with
    f_j(1) = 8^j at the leading bit. The binomial transform maps a geometric
    sequence c * alpha^a to c * (3 + 5 alpha)^j, so f stays a single geometric
    term throughout: crossing a gap of z zeros multiplies the coefficient by
    alpha^z and replaces alpha by 3 + 5 alpha. Hence, with 1-bits at positions
    p_1 > ... > p_s and alpha_1 = 8, alpha_(i+1) = 3 + 5 alpha_i,
        A(x) = alpha_1^(p_1 - p_2 - 1) * ... * alpha_(s-1)^(p_(s-1) - p_s - 1)
               * alpha_s^(p_s).
    (Verified against the raw recursion for all x < 3000 and random 40-bit x.)
    """
    alpha, value = 8, 1
    for i in range(len(one_bits) - 1):
        value = value * pow(alpha, one_bits[i] - one_bits[i + 1] - 1, mod) % mod
        alpha = (3 + 5 * alpha) % mod
    return value * pow(alpha, one_bits[-1], mod) % mod


def h(t: int, r: int, mod: int) -> int:
    """H(t, r) = A((2^t + 1)^r) mod `mod`, for t exceeding r's coefficients.

    (2^t + 1)^r = sum_k C(r, k) 2^(t k), and each binomial coefficient fits
    well inside its t-bit block, so the set bits of the power are just the
    set bits of every C(r, k) shifted by t k.
    """
    bits = []
    for k in range(r, -1, -1):
        c = comb(r, k)
        bits.extend(t * k + i for i in range(c.bit_length() - 1, -1, -1)
                    if (c >> i) & 1)
    return a_factored_mod(bits, mod)


if __name__ == "__main__":
    assert h(3, 2, 10**9) == 636056  # A(81)
    print(h(10**14 + 31, 62, P))  # 327287526
