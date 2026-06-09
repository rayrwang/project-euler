def count_reversible(max_digits):
    """Count reversible numbers with up to `max_digits` digits.

    Adding n to its reverse and demanding every output digit be odd pins down
    the per-column structure, giving a closed form per digit length d:
      * even d            -> no carries; each symmetric digit pair sums to an
                             odd value below 10. The outer pair (no leading
                             zeros) has 20 choices, every inner pair has 30,
                             so 20 * 30**(d/2 - 1).
      * odd  d, d % 4 == 3 -> the middle column needs a carry-in, which forces
                             a self-consistent cascade: 100 * 500**((d - 3)/4).
      * odd  d, d % 4 == 1 -> the carry parity is contradictory: 0.
    """
    total = 0
    for d in range(1, max_digits + 1):
        if d % 2 == 0:
            total += 20 * 30 ** (d // 2 - 1)
        elif d % 4 == 3:
            total += 100 * 500 ** ((d - 3) // 4)
    return total

if __name__ == "__main__":
    # Numbers below 10^9 have at most 9 digits.
    print(count_reversible(9))  # 608720
