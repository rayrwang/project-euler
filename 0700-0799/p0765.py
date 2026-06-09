from math import comb

def solve(rounds, start, target, digits=10):
    """Maximum probability of turning `start` grams into at least `target`
    in `rounds` bets of a p = 0.6 double-or-lose coin, betting any amount up
    to current wealth each round.

    Key reduction: wins and losses change wealth by +b and -b, so the wealth
    process is a nonnegative martingale under the FAIR (1/2) measure,
    whatever the strategy. Conversely, any nonnegative binary martingale is
    realisable by legal bets. The minimal capital that guarantees wealth
    >= target on a set S of outcome sequences is therefore
    target * (|S| / 2^rounds) (take the conditional-expectation martingale of
    target * 1_S). Hence a success set S is achievable iff
    |S| <= k = floor(start * 2^rounds / target), and the optimum simply takes
    the k sequences with the most wins:
        V = sum of the k largest p^w q^(rounds-w).
    This was verified to agree exactly with the full Bellman recursion on
    every dyadic state for all horizons up to 11 (bold play, by contrast, is
    strictly suboptimal here since the coin is favourable).

    Evaluate exactly: V = N / 10^rounds with N an integer built from
    6^w 4^(rounds-w) terms, then round to `digits` decimals.
    """
    k = start * 2**rounds // target
    numerator = 0
    remaining = k
    for w in range(rounds, -1, -1):
        c = comb(rounds, w)
        take = min(c, remaining)
        numerator += take * 6**w * 4 ** (rounds - w)
        remaining -= take
        if remaining == 0:
            break
    # Round N / 10^rounds to `digits` decimal places, half-up.
    scaled = numerator * 10**digits
    denom = 10**rounds
    rounded = (scaled * 2 + denom) // (2 * denom)
    return f"0.{rounded:0{digits}d}"

if __name__ == "__main__":
    print(solve(1000, 1, 10**12))  # 0.2429251641
