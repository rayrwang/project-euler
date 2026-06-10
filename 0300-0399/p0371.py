def solve() -> float:
    """Expected number of licence plates Seth must see until two of them have
    three-digit numbers summing to 1000.

    Only the number 000..999 matters, each equally likely (probability 1/1000).
    Pairing n with 1000 - n: the value 0 has partner 1000 (not a valid plate) so
    it can never make a win; 500 pairs with itself, so two 500s win; and the
    numbers 1..499 pair with 501..999 to give 499 complementary pairs.

    A win happens the moment a drawn number's partner has already been seen. By
    symmetry the state is (k, s): k = how many of the 499 pairs are "half seen"
    (one side seen), and s = whether a 500 has been seen. From state (k, s) a new
    draw is, with probability 1/1000 each: the dead 0 (no change); a 500 (win if
    s = 1, else move to s = 1); the unseen side of a half-seen pair (win, k of
    them); the already-seen side of a half-seen pair (no change, k of them); and
    with probability 2(499 - k)/1000 a fresh pair (k -> k + 1). Writing E[k, s]
    for the expected additional draws and solving the resulting linear equations
    from k = 499 downward gives E[0, 0].
    """
    pairs = 499
    e_seen500 = [0.0] * (pairs + 1)  # E[k, s=1]
    for k in range(pairs, -1, -1):
        p_self = 1 / 1000 + k / 1000  # draw the dead 0, or an already-seen side
        p_fresh = (pairs - k) * 2 / 1000
        nxt = e_seen500[k + 1] if k < pairs else 0.0
        # win (complement of a half-seen pair, or the second 500) contributes 0
        e_seen500[k] = (1 + p_fresh * nxt) / (1 - p_self)

    e_no500 = [0.0] * (pairs + 1)  # E[k, s=0]
    for k in range(pairs, -1, -1):
        p_self = 1 / 1000 + k / 1000
        p_500 = 1 / 1000  # moves to the s=1 state
        p_fresh = (pairs - k) * 2 / 1000
        nxt = e_no500[k + 1] if k < pairs else 0.0
        e_no500[k] = (1 + p_500 * e_seen500[k] + p_fresh * nxt) / (1 - p_self)

    return e_no500[0]


if __name__ == "__main__":
    print(f"{solve():.8f}")  # 40.66368097
