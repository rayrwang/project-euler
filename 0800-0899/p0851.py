"""Project Euler 851: SOP and POS.

R_n(M) sums prod (u_i + v_i) over pairs of positive n-tuples with
sum u_i v_i = M.  Coordinates are independent, so R_n(M) is the q^M
coefficient of F(q)^n with F(q) = sum_{u,v>=1} (u+v) q^(uv); pairing
each divisor d of m with m/d gives F = 2 sum sigma(m) q^m, i.e.
F = 2 (1 - E_2)/24 with the weight-2 Eisenstein series E_2.  Hence
F^n is a (mixed-weight) quasimodular form of depth n.

By the Kaneko-Zagier structure theorem, every quasimodular form for
SL_2(Z) is a unique combination of derivatives of modular forms and
derivatives of E_2.  For n = 6 the relevant space is spanned by the 23
series D^i E_k (k = 2, 4, 6, 8, 10, with the appropriate i), E_12, the
cusp form Delta and the constant; the exact rational coefficients are
found once by Gaussian elimination on 41 power-series coefficients and
verified on all of them.  Since [q^M] D^i g = M^i [q^M] g, the q^M
coefficient of F^n becomes an explicit combination of sigma_k(M) for
k = 1, 3, 5, 7, 9, 11 and of Ramanujan's tau(M).

For M = 10000! the prime exponents come from Legendre's formula, each
sigma_k(M) is a product of geometric series modulo 10^9 + 7, and
tau(M) follows from multiplicativity and the Hecke recursion
tau(p^(e+1)) = tau(p) tau(p^e) - p^11 tau(p^(e-1)), seeded by tau(p)
for p <= 10000 read off Delta = q (eta^3)^8, where eta^3 is Jacobi's
sparse series and the squarings use Kronecker substitution.  The code
reproduces R_1(10) = 36, R_2(100) = 1873044 and R_2(100!) = 446575636
before printing R_6(10000!).
"""

from __future__ import annotations

from fractions import Fraction

MOD = 10**9 + 7
TERMS = 40  # power-series length used for the exact linear algebra


# --- exact power series over Q -------------------------------------------


def sigma_table(k: int, n: int) -> list[int]:
    s = [0] * (n + 1)
    for d in range(1, n + 1):
        dk = d**k
        for m in range(d, n + 1, d):
            s[m] += dk
    return s


def eisenstein(k: int, const: Fraction | int) -> list[Fraction]:
    s = sigma_table(k - 1, TERMS)
    return [Fraction(1)] + [Fraction(const) * s[m] for m in range(1, TERMS + 1)]


def series_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    c = [Fraction(0)] * (TERMS + 1)
    for i, ai in enumerate(a):
        if ai:
            for j in range(TERMS + 1 - i):
                if b[j]:
                    c[i + j] += ai * b[j]
    return c


def series_pow(a: list[Fraction], e: int) -> list[Fraction]:
    r = [Fraction(1)] + [Fraction(0)] * TERMS
    for _ in range(e):
        r = series_mul(r, a)
    return r


def derivative(a: list[Fraction], times: int = 1) -> list[Fraction]:
    for _ in range(times):
        a = [Fraction(m) * a[m] for m in range(len(a))]
    return a


def express(target: list[Fraction], basis: list[list[Fraction]]) -> list[Fraction]:
    """Exact coefficients with target = sum c_i basis_i, verified fully."""
    nb = len(basis)
    rows = [
        list(b) + [Fraction(int(j == i)) for j in range(nb)]
        for i, b in enumerate(basis)
    ]
    piv_cols: list[int] = []
    piv = 0
    for col in range(TERMS + 1):
        sel = next((r for r in range(piv, nb) if rows[r][col] != 0), None)
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = 1 / rows[piv][col]
        rows[piv] = [v * inv for v in rows[piv]]
        for r in range(nb):
            if r != piv and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [a - f * b for a, b in zip(rows[r], rows[piv])]
        piv_cols.append(col)
        piv += 1
    t = list(target) + [Fraction(0)] * nb
    for r, col in enumerate(piv_cols):
        if t[col] != 0:
            f = t[col]
            t = [a - f * b for a, b in zip(t, rows[r])]
    assert all(t[m] == 0 for m in range(TERMS + 1)), "target not in span"
    coeffs = [-t[TERMS + 1 + i] for i in range(nb)]
    for m in range(TERMS + 1):
        assert sum(c * basis[i][m] for i, c in enumerate(coeffs)) == target[m]
    return coeffs


def quasimodular_decomposition() -> tuple[list, list[Fraction], list[Fraction]]:
    e2 = eisenstein(2, -24)
    e4 = eisenstein(4, 240)
    e6 = eisenstein(6, -504)
    e8 = eisenstein(8, 480)
    e10 = eisenstein(10, -264)
    e12 = eisenstein(12, Fraction(65520, 691))
    delta = [(a - b) / 1728 for a, b in zip(series_pow(e4, 3), series_pow(e6, 2))]
    one = [Fraction(1)] + [Fraction(0)] * TERMS
    items: list[tuple[str, list[Fraction], int | str, Fraction | int, int]] = [
        ("const", one, 0, 0, 0)
    ]
    for series, order, const, max_d in (
        (e2, 1, -24, 5),
        (e4, 3, 240, 4),
        (e6, 5, -504, 3),
        (e8, 7, 480, 2),
        (e10, 9, -264, 1),
    ):
        for i in range(max_d + 1):
            items.append((f"D{i}", derivative(series, i), order, const, i))
    items.append(("E12", e12, 11, Fraction(65520, 691), 0))
    items.append(("Delta", delta, "tau", 1, 0))
    base = [Fraction(0)] + [-x / 24 for x in e2[1:]]  # sum sigma(m) q^m
    basis = [it[1] for it in items]
    return (
        items,
        express(series_pow(base, 6), basis),
        express(series_pow(base, 2), basis),
    )


# --- coefficient extraction at huge M -------------------------------------


def primes_upto(n: int) -> list[int]:
    flags = bytearray([1]) * (n + 1)
    flags[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if flags[i]:
            flags[i * i :: i] = b"\x00" * len(flags[i * i :: i])
    return [i for i in range(2, n + 1) if flags[i]]


def tau_series(n: int) -> list[int]:
    """tau(1..n) mod MOD from Delta = q (eta^3)^8 with Jacobi's eta^3."""
    cubes = [0] * (n + 1)
    k = 0
    while k * (k + 1) // 2 <= n:
        cubes[k * (k + 1) // 2] = (-1) ** k * (2 * k + 1) % MOD
        k += 1

    def square(a: list[int]) -> list[int]:
        x = 0
        for c in reversed(a):
            x = (x << 128) | c
        y = x * x
        mask = (1 << 128) - 1
        out = [0] * (n + 1)
        for m in range(n + 1):
            out[m] = (y & mask) % MOD
            y >>= 128
        return out

    eta24 = square(square(square(cubes)))
    return [0] + eta24[:n]


def evaluate_at_factorial(
    items: list, coeffs: list[Fraction], fact_n: int, power_of_two: int
) -> int:
    """2^power_of_two * [q^M] sum c_i item_i at M = fact_n! mod MOD."""
    expo: dict[int, int] = {}
    for p in primes_upto(fact_n):
        e, q = 0, p
        while q <= fact_n:
            e += fact_n // q
            q *= p
        expo[p] = e
    m_mod = 1
    for i in range(2, fact_n + 1):
        m_mod = m_mod * i % MOD

    def sigma_mod(k: int) -> int:
        r = 1
        for p, e in expo.items():
            x = pow(p, k, MOD)
            if x == 1:
                r = r * ((e + 1) % MOD) % MOD
            else:
                r = r * (pow(x, e + 1, MOD) - 1) % MOD
                r = r * pow(x - 1, MOD - 2, MOD) % MOD
        return r

    sig_cache: dict[int, int] = {}
    tau_value: int | None = None
    total = 0
    for (name, _, order, const, deriv_order), coef in zip(items, coeffs):
        if not coef or name == "const":
            continue
        c_mod = coef.numerator % MOD * pow(coef.denominator, MOD - 2, MOD) % MOD
        if order == "tau":
            if tau_value is None:
                ts = tau_series(fact_n)
                tau_value = 1
                for p, e in expo.items():
                    a, b = 1, ts[p]
                    p11 = pow(p, 11, MOD)
                    for _ in range(e - 1):
                        a, b = b, (ts[p] * b - p11 * a) % MOD
                    tau_value = tau_value * b % MOD
            val = tau_value
        else:
            assert isinstance(order, int)
            if order not in sig_cache:
                sig_cache[order] = sigma_mod(order)
            k_mod = (
                Fraction(const).numerator
                % MOD
                * pow(Fraction(const).denominator, MOD - 2, MOD)
                % MOD
            )
            val = k_mod * pow(m_mod, deriv_order, MOD) % MOD
            val = val * sig_cache[order] % MOD
        total = (total + c_mod * val) % MOD
    return total * pow(2, power_of_two, MOD) % MOD


def main() -> None:
    items, c6, c2 = quasimodular_decomposition()
    # R_1(10) = 2 sigma(10) = 36 and R_2(100) by direct convolution.
    sig = sigma_table(1, 100)
    assert 2 * sig[10] == 36
    assert sum(4 * sig[i] * sig[100 - i] for i in range(1, 100)) == 1873044
    assert evaluate_at_factorial(items, c2, 100, 2) == 446575636
    print(evaluate_at_factorial(items, c6, 10000, 6))  # 726358482


if __name__ == "__main__":
    main()
