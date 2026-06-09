from decimal import Decimal, getcontext

def eulerian(n):
    """Eulerian numbers A(n, 0..n-1) via A(n,j) = (j+1)A(n-1,j) + (n-j)A(n-1,j-1)."""
    a = [1]
    for m in range(2, n + 1):
        a = [
            (j + 1) * (a[j] if j < len(a) else 0)
            + (m - j) * (a[j - 1] if 0 <= j - 1 < len(a) else 0)
            for j in range(m)
        ]
    return a

def E(k, q, digits=12):
    """E_k(q) = sum_n sigma_k(n) q^n in scientific notation with `digits`
    digits after the decimal point.

    Expanding sigma_k as a double sum over divisors, E_k(q) =
    sum_(m>=1) Li_(-k)(q^m), and the negative polylogarithm is the rational
    function Li_(-k)(x) = (sum_j A(k, j) x^(j+1)) / (1 - x)^(k+1) with
    Eulerian numerator coefficients. Near q = 1 the m-th term behaves like
    k! / (m (1-q))^(k+1), so the series converges like sum 1/m^(k+1) and a
    few dozen exactly-evaluated terms (Decimal arithmetic) give full
    precision despite the answer's magnitude of 10^132.
    """
    getcontext().prec = 60
    a = eulerian(k)
    total = Decimal(0)
    m = 1
    while True:
        x = q**m
        numerator = sum(Decimal(c) * x ** (j + 1) for j, c in enumerate(a))
        term = numerator / (1 - x) ** (k + 1)
        total += term
        if term < total * Decimal(10) ** (-digits - 12):
            break
        m += 1
    exp = total.adjusted()
    mantissa = total / Decimal(10) ** exp
    return f"{mantissa:.{digits}f}e{exp}"

if __name__ == "__main__":
    assert E(1, 1 - Decimal(1) / 2**4) == "3.872155809243e2"
    assert E(3, 1 - Decimal(1) / 2**8) == "2.767385314772e10"
    assert E(7, 1 - Decimal(1) / 2**15) == "6.725803486744e39"
    print(E(15, 1 - Decimal(1) / 2**25))  # 3.376792776502e132
