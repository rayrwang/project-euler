def occupant(f: int, r: int) -> int:
    """P(f, r): the person occupying room r on floor f.

    Simulating the assignment reveals the structure. Within any floor the
    occupants a_1, a_2, ... satisfy a_i + a_(i+1) = (i + b)^2, where the floors
    pair up: floor 1 has b = 1, and floors 2k, 2k+1 (k >= 1) share b = 2k.
    The first occupant is a_1 = P(f, 1):
        f = 1            -> a_1 = 1,        b = 1
        f = 2k (even)    -> a_1 = f^2 / 2,  b = f
        f = 2k+1 (odd)   -> a_1 = 2k(k+1),  b = f - 1
    Solving the alternating recurrence a_(i+1) = (i+b)^2 - a_i and using the
    alternating square sum  sum_(k=1)^n (-1)^(n-k) k^2 = n(n+1)/2  gives
        P(f, r) = (-1)^(r-1) ( a_1 - b(b+1)/2 ) + (b+r-1)(b+r)/2.
    """
    if f == 1:
        b, a1 = 1, 1
    elif f % 2 == 0:
        b, a1 = f, f * f // 2
    else:
        k = (f - 1) // 2
        b, a1 = f - 1, 2 * k * (k + 1)
    sign = 1 if (r - 1) % 2 == 0 else -1
    return sign * (a1 - b * (b + 1) // 2) + (b + r - 1) * (b + r) // 2


def solve() -> int:
    # 71328803586048 = 2^27 * 3^12; sum P(f, r) over all f*r = N, last 8 digits.
    total = 0
    for a in range(28):
        for e in range(13):
            f = 2**a * 3**e
            r = 71328803586048 // f
            total += occupant(f, r)
    return total % 10**8


if __name__ == "__main__":
    assert occupant(10, 20) == 440
    assert occupant(25, 75) == 4863
    assert occupant(99, 100) == 19454
    print(solve())  # 40632119
