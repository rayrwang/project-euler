MOD = 10**9 + 9

def digit_counts(m, j):
    """How many x in [0, m] have digit value v at decimal position j,
    for v = 0..9 (numbers padded with leading zeros)."""
    p = 10**j
    high, cur, low = m // (10 * p), m // p % 10, m % p
    out = []
    for v in range(10):
        c = high * p
        if v < cur:
            c += p
        elif v == cur:
            c += low + 1
        out.append(c % MOD)
    return out

def mul_convolve(u, v):
    out = [0] * 10
    for p in range(10):
        if u[p]:
            for q in range(10):
                out[p * q % 10] = (out[p * q % 10] + u[p] * v[q]) % MOD
    return out

def F(r, m):
    """Sum of x_1 [x] ... [x] x_R over all tuples with 0 <= x_i <= m.

    The freshman's product works digit-by-digit, so position j of the result
    depends only on the j-th digits of the x_i, which are independent across
    positions only in their *joint distribution per position*: summing over
    all tuples, position j contributes 10^j * sum_w w * N_j[w], where N_j[w]
    counts tuples whose j-th digits multiply to w modulo 10. N_j is the
    R-fold convolution of the digit-count vector of [0, m] at position j
    under the multiplication monoid mod 10, computed by binary powering of
    10-vectors (100 multiplications per convolution).
    """
    total = 0
    digits = len(str(m))
    for j in range(digits):
        cnt = digit_counts(m, j)
        # cnt to the R-th convolution power.
        result = [0] * 10
        result[1] = 1  # multiplicative identity distribution
        base = cnt
        e = r
        while e:
            if e & 1:
                result = mul_convolve(result, base)
            base = mul_convolve(base, base)
            e >>= 1
        total = (total + pow(10, j, MOD) * sum(w * result[w] for w in range(10))) % MOD
    return total

if __name__ == "__main__":
    assert F(2, 7) == 204
    assert F(23, 76) == 5870548
    print(F(234567, 765432))  # 146133880
