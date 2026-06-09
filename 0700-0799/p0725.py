MOD = 10**16
L = 2020
TOP = 19  # digit sums of interest are < 19

def poly_mul(p, q):
    out = [0] * TOP
    for i, pi in enumerate(p):
        if pi:
            for j in range(TOP - i):
                out[i + j] = (out[i + j] + pi * q[j]) % MOD
    return out

def poly_pow(p, e):
    result = [0] * TOP
    result[0] = 1
    while e:
        if e & 1:
            result = poly_mul(result, p)
        p = poly_mul(p, p)
        e >>= 1
    return result

def S(length):
    """Sum of all DS-numbers with at most `length` digits, modulo 10^16.

    A number is a DS-number iff its digit sum equals 2d for some digit d that
    occurs in it (then the other digits sum to d and are automatically <= d).
    Represent every number as a string of exactly `length` digits with leading
    zeros. For a fixed d, the value-sum of qualifying strings is, by symmetry
    over positions, R * sum_v v * (#strings on the remaining positions),
    where R = 111...1 (`length` ones). Inclusion-exclusion removes strings
    with digit sum 2d that avoid the digit d entirely.
    """
    repunit = 0
    for _ in range(length):
        repunit = (repunit * 10 + 1) % MOD

    all_digits = [1] * 10 + [0] * (TOP - 10)
    m_all = poly_pow(all_digits, length - 1)

    total = 0
    for d in range(1, 10):
        target = 2 * d
        without_d = all_digits.copy()
        without_d[d] = 0
        m_avoid = poly_pow(without_d, length - 1)
        for v in range(10):
            if v > target:
                continue
            count = m_all[target - v]
            if v != d:
                count -= m_avoid[target - v]
            total = (total + v * count) % MOD
    return total * repunit % MOD

if __name__ == "__main__":
    assert S(3) == 63270
    assert S(7) == 85499991450
    print(S(L))  # 4598797036650685
