from fractions import Fraction

Poly = list[dict[int, Fraction]]  # b-polynomial; coeffs are Laurent polys in z


def _add(d: dict[int, Fraction], e: dict[int, Fraction], scale: int = 1) -> None:
    for k, v in e.items():
        d[k] = d.get(k, Fraction(0)) + v * scale


def _integrate(poly: Poly) -> Poly:
    out: Poly = [{} for _ in range(len(poly) + 1)]
    for i, c in enumerate(poly):
        for k, v in c.items():
            out[i + 1][k] = v / (i + 1)
    return out


def _shift_z(poly: Poly, dz: int) -> Poly:
    return [{k + dz: v for k, v in c.items()} for c in poly]


def _padd(a: Poly, b: Poly, scale: int = 1) -> Poly:
    out: Poly = [{} for _ in range(max(len(a), len(b)))]
    for i, c in enumerate(a):
        _add(out[i], c)
    for i, c in enumerate(b):
        _add(out[i], c, scale)
    return out


def _mul_b(a: Poly) -> Poly:
    return [{}] + [dict(c) for c in a]


def _eval_at_1(poly: Poly) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for c in poly:
        _add(out, c)
    return out


def separation_probability(n: int) -> Fraction:
    """P(n): probability that the red and blue rope loops can be separated.

    Because every rope lies above all previous ones, each loop is a height-
    monotone arc closed by a vertical strand at R_0 (resp. B_0) on the
    boundary; the two monotone arcs form a pure braid on two strands, whose
    boundary closure is the (2, 2k) torus link with k the red/blue linking
    number. The loops therefore separate iff lk = 0.

    Blue rope j lies above red rope i iff j >= i, so lk is the sum over j of
    the signed crossings of blue rope j with the red path R_0..R_j. Signed
    crossings with a chord telescope to a difference of side indicators, so
    lk = sum_{j=1}^{n-1} s_j, where s_j = +/-1 when chord B_{j-1}B_j
    separates R_0 from R_j (sign from orientation) and 0 otherwise. (The
    j = n term vanishes since the full red loop is closed.)

    Fixing R_0 = 0, the factors couple only through consecutive B's, so
    E[z^lk] = E[prod_j g(B_{j-1}, B_j)] with
        g(b, b') = 1 + (b' - b)(z - 1)        if b < b',
        g(b, b') = 1 + (b - b')(1/z - 1)      if b > b',
    since R_j is uniform and independent. Iterating the transfer operator
    (Tf)(b') = integral of g(b, b') f(b) db on exact b-polynomials with
    Laurent-in-z coefficients gives E[z^lk] exactly; P(n) is the z^0 term.
    """
    f: Poly = [{0: Fraction(1)}]
    for _ in range(n - 1):
        big_f = _integrate(f)
        big_g = _integrate(_mul_b(f))
        f1 = _eval_at_1(big_f)
        g1 = _eval_at_1(big_g)
        b_f = _mul_b(big_f)
        # (z - 1) * (b F(b) - G(b))
        a = _padd(b_f, big_g, -1)
        term_a = _padd(_shift_z(a, 1), a, -1)
        # (1/z - 1) * (G1 - G(b) - b F1 + b F(b))
        b = _padd(_padd([g1], big_g, -1), _padd(b_f, [{}, f1], -1))
        term_b = _padd(_shift_z(b, -1), b, -1)
        f = _padd(_padd([f1], term_a), term_b)
    return _eval_at_1(_integrate(f)).get(0, Fraction(0))


if __name__ == "__main__":
    assert separation_probability(3) == Fraction(11, 20)
    p = separation_probability(80)
    scaled = p.numerator * 10**11 // p.denominator  # 11 digits, then round
    print(f"0.{(scaled + 5) // 10:010d}")  # 0.1091523673
