P = 10**9 + 7


def xor_mul(a: int, b: int) -> int:
    """Carry-less (GF(2)[x]) product of a and b as bitmasks."""
    result = 0
    while b:
        low = b & (-b)
        result ^= a * low  # a << shift
        b ^= low
    return result


def xor_pow(a: int, e: int) -> int:
    result = 1
    while e:
        if e & 1:
            result = xor_mul(result, a)
        a = xor_mul(a, a)
        e >>= 1
    return result


def p_mod(two_exp: int, three_exp: int) -> int:
    """P(2^two_exp * 3^three_exp) mod P.

    The XOR-product is multiplication in GF(2)[x], with 11 = x^3 + x + 1.
    Squaring is the Frobenius f(x) -> f(x^2), so
        11^(x) (n = 2^a * m)  =  g(x^(2^a)) with g = 11^(x) m.
    Computing g = (x^3 + x + 1)^(3^8) exactly (degree ~2 * 10^4) and
    substituting x -> x^(2^a) turns each monomial x^k into 2^(k 2^a) mod P.
    """
    g = xor_pow(0b1011, 3**three_exp)
    shift = pow(2, two_exp, P - 1)  # 2^(k * 2^a) = 2^(k * shift) mod P (Fermat)
    total = 0
    k = 0
    while g:
        if g & 1:
            total = (total + pow(2, k * shift, P)) % P
        g >>= 1
        k += 1
    return total


if __name__ == "__main__":
    assert xor_pow(0b1011, 2) == 69
    print(p_mod(52, 8))  # 14063639
    # since 8^12 * 12^8 = 2^36 * 2^16 * 3^8 = 2^52 * 3^8
