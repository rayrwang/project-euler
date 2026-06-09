def m_cards(c: int, rooms: int) -> int:
    """Minimum cards dispensed to pass `rooms` rooms carrying at most `c`.

    Passing R rooms means passing R + 1 doors, each consuming one card per
    passage in either direction. Let N(d) be the number of cards needed in
    hand (or stashed at the current position) to get through d more doors.
    If d <= c the cards can simply be carried: N(d) = d. Otherwise the
    N(d - 1) cards required beyond the next door must be ferried through
    it: a round trip costs two passages and delivers c - 2 cards (carry c,
    one for the door in, keep one for the door out), while the final
    one-way trip costs one passage and delivers c - 1. With k trips chosen
    minimally so that (k - 1)(c - 2) + (c - 1) >= N(d - 1), the door
    consumes 2k - 1 extra cards: N(d) = N(d - 1) + 2k - 1. The dispenser at
    the start makes N(R + 1) exactly the number of cards drawn.
    """
    doors = rooms + 1
    n = min(doors, c)
    for _ in range(c + 1, doors + 1):
        deficit = n - (c - 1)
        k = 1 + -(-deficit // (c - 2))  # ceiling division
        n += 2 * k - 1
    return n


def solve(c_lo: int, c_hi: int, rooms: int) -> int:
    return sum(m_cards(c, rooms) for c in range(c_lo, c_hi + 1))


if __name__ == "__main__":
    assert m_cards(3, 6) == 123
    assert m_cards(4, 6) == 23
    assert solve(3, 10, 10) == 10382
    print(solve(3, 40, 30))  # 34315549139516
