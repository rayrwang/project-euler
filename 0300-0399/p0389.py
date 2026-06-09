from fractions import Fraction


def die_stats(sides: int) -> tuple[Fraction, Fraction]:
    """Mean and variance of one fair die with faces 1..sides."""
    mean = Fraction(sides + 1, 2)
    var = Fraction(sides * sides - 1, 12)
    return mean, var


def compound(
    n_mean: Fraction, n_var: Fraction, sides: int
) -> tuple[Fraction, Fraction]:
    """Mean and variance of a sum of N fair dice, N random.

    For S = X_1 + ... + X_N with the X_i iid and independent of N, the laws
    of total expectation and total variance give E[S] = E[N] E[X] and
    Var(S) = E[N] Var(X) + Var(N) E[X]^2.
    """
    x_mean, x_var = die_stats(sides)
    return n_mean * x_mean, n_mean * x_var + n_var * x_mean**2


def solve() -> Fraction:
    mean, var = die_stats(4)  # T
    for sides in (6, 8, 12, 20):  # C, O, D, I
        mean, var = compound(mean, var, sides)
    return var


def brute_first_stage() -> tuple[Fraction, Fraction]:
    """Exact distribution of C (sum of T six-sided dice) by enumeration."""
    dist: dict[int, Fraction] = {}
    for t in range(1, 5):
        # Distribution of the sum of t d6 by convolution.
        sums = {0: Fraction(1)}
        for _ in range(t):
            nxt: dict[int, Fraction] = {}
            for s, p in sums.items():
                for face in range(1, 7):
                    nxt[s + face] = nxt.get(s + face, Fraction(0)) + p / 6
            sums = nxt
        for s, p in sums.items():
            dist[s] = dist.get(s, Fraction(0)) + p / 4
    mean = sum(s * p for s, p in dist.items())
    var = sum(s * s * p for s, p in dist.items()) - mean**2
    return Fraction(mean), Fraction(var)


if __name__ == "__main__":
    # Validate the compound formula against exact enumeration of stage one.
    t_mean, t_var = die_stats(4)
    assert compound(t_mean, t_var, 6) == brute_first_stage()
    print(f"{float(solve()):.4f}")  # 2406376.3623
