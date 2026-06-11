import random

import sympy

def second_player_win_probability() -> sympy.Expr:
    """Exact P(y > x) for the dishwashing wager.

    Renewal facts for sums of independent U(0,1): the density that some
    partial sum sits at level s < 1 (before crossing) is e^s, plus an
    atom of weight 1 at s = 0 (no draws yet). Player 1 crosses level 1:
    the joint density of her last draw x and overshoot t = S - 1 is
    e^(1 + t - x) on 0 < t < x < 1 (the pre-sum was 1 + t - x). Player 2
    then crosses a fresh gap c = 1 - t in (0, 1): given c, the last draw
    y has density 1_{y > c} (zero pre-draws) + e^c - e^(max(0, c - y))
    (pre-sum u > c - y). Integrating P(y > x) against the joint law
    gives the answer in closed form.
    """
    x, t, y = sympy.symbols("x t y", positive=True)
    c = 1 - t
    # P(y > x | c): integrate g2(y | c) over y in (x, 1)
    # g2(y | c) = [y > c] + e^c - e^(max(0, c - y)), y in (0, 1)
    # split at y = c (relative position of x vs c handled by Piecewise)
    g2_low = sympy.exp(c) - sympy.exp(c - y)   # y < c
    g2_high = 1 + sympy.exp(c) - 1             # y > c: atom + e^c - e^0
    p_tail_if_x_below_c = (sympy.integrate(g2_low, (y, x, c))
                           + sympy.integrate(g2_high, (y, c, 1)))
    p_tail_if_x_above_c = sympy.integrate(g2_high, (y, x, 1))
    joint = sympy.exp(1 + t - x)  # density of (x, t), 0 < t < x < 1
    # x vs c = 1 - t: x > 1 - t <=> t > 1 - x
    inner_below = sympy.integrate(
        joint * p_tail_if_x_below_c, (t, 0, sympy.Min(x, 1 - x)))
    # region where t < x and t > 1 - x (only when x > 1/2)
    inner_above = sympy.integrate(
        joint * p_tail_if_x_above_c, (t, 1 - x, x))
    total = (sympy.integrate(inner_below, (x, 0, 1))
             + sympy.integrate(inner_above, (x, sympy.Rational(1, 2), 1)))
    return sympy.simplify(total)

def monte_carlo(trials: int) -> float:
    wins = 0
    for _ in range(trials):
        s = 0.0
        while s <= 1.0:
            x = random.random()
            s += x
        while s <= 2.0:
            y = random.random()
            s += y
        if y > x:
            wins += 1
    return wins / trials

if __name__ == "__main__":
    p = second_player_win_probability()
    val = float(p)
    mc = monte_carlo(400_000)
    assert abs(val - mc) < 0.005, (val, mc)
    from decimal import Decimal
    d = Decimal(str(sympy.N(p, 25))).quantize(Decimal("0.0000000001"))
    print(d)  # 0.5276662759
