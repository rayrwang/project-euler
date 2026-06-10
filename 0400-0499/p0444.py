from decimal import Decimal, getcontext

GAMMA = Decimal("0.577215664901532860606512090082402431042")

def harmonic_exact(n: int) -> Decimal:
    getcontext().prec = 60
    total = Decimal(0)
    for i in range(1, n + 1):
        total += Decimal(1) / i
    return total

def harmonic_asymptotic(n: int) -> Decimal:
    """H_n = ln n + gamma + 1/(2n) - 1/(12n^2) + 1/(120n^4) - ..."""
    getcontext().prec = 60
    dn = Decimal(n)
    return (dn.ln() + GAMMA + 1 / (2 * dn) - 1 / (12 * dn * dn)
            + 1 / (120 * dn**4))

def s_k(n: int, k: int) -> Decimal:
    """S_k(N) = binom(N + k, k) * (H_{N+k} - H_k).

    With optimal play the expected number of players remaining is the
    harmonic number, E(p) = H_p (verified by hand for p = 1, 2, against
    the given E(111) = 5.2912, and through the problem's own ten-digit
    S_3(100) example below). Iterated prefix sums multiply the generating
    function -ln(1-x)/(1-x) by 1/(1-x)^k, and the coefficient of x^N in
    -ln(1-x)/(1-x)^(k+1) is the classical binom(N+k, k)(H_{N+k} - H_k).
    """
    getcontext().prec = 60
    binom = 1
    for i in range(1, k + 1):
        binom = binom * (n + i)
    for i in range(1, k + 1):
        binom //= i
    h_big = (harmonic_asymptotic(n + k) if n + k > 10**6
             else harmonic_exact(n + k))
    return Decimal(binom) * (h_big - harmonic_exact(k))

def sci(d: Decimal, sig: int) -> str:
    getcontext().prec = 60
    exp = int(d.log10().to_integral_value(rounding="ROUND_FLOOR"))
    mant = d / Decimal(10) ** exp
    q = mant.quantize(Decimal(1).scaleb(-(sig - 1)))
    if q >= 10:
        q = (q / 10).quantize(Decimal(1).scaleb(-(sig - 1)))
        exp += 1
    return f"{q}e{exp}"

if __name__ == "__main__":
    # E(p) = H_p: hand-checked for p = 1, 2; given E(111) = 5.2912
    assert abs(harmonic_exact(111) - Decimal("5.2912")) < Decimal("5e-5")
    # the problem's own example: S_3(100) = 5.983679014e5
    assert sci(s_k(100, 3), 10) == "5.983679014e5"
    # asymptotic and exact harmonic agree deep past 10 digits
    assert abs(harmonic_asymptotic(10**6) - harmonic_exact(10**6)) < Decimal("1e-30")
    print(sci(s_k(10**14, 20), 10))  # 1.200856722e263
