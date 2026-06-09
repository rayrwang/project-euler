from funcs import gcd

def S(n: int) -> int:
    """Sum of r_A + r_B + r_C over integer Descartes triples with r_A <= r_B <= n.

    Two circles tangent to each other and a common line, with a third circle in
    the gap tangent to all three, satisfy 1/sqrt(r_C) = 1/sqrt(r_A) + 1/sqrt(r_B).
    Every integer solution with r_A <= r_B is, uniquely,
        r_A = e * p^2 * (p+q)^2,
        r_B = e * q^2 * (p+q)^2,
        r_C = e * p^2 * q^2,
    for coprime 1 <= p <= q and e >= 1. For fixed (p, q) the scale e runs from 1
    to floor(n / r_B^(1)), and the e-sum of (r_A + r_B + r_C) telescopes to a
    triangular number.
    """
    total = 0
    q = 1
    while q * q * (q + 1) * (q + 1) <= n:  # smallest base r_B at this q is for p=1
        for p in range(1, q + 1):
            if gcd(p, q) != 1:
                continue
            s = (p + q) * (p + q)
            base_rb = q * q * s  # r_B at e = 1
            if base_rb > n:
                continue
            m = n // base_rb
            unit = p * p * s + q * q * s + p * p * q * q  # (r_A+r_B+r_C) at e=1
            total += unit * (m * (m + 1) // 2)
        q += 1
    return total

if __name__ == "__main__":
    assert S(5) == 9
    assert S(100) == 3072
    print(S(10**9))  # 315306518862563689
