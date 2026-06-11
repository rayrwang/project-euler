from functools import cache
from math import factorial

# A 123-number uses only digits 1, 2, 3, and the count of each digit that
# appears must itself be a 123-number. The target index is ~1.1e17, so the
# answer has only a few dozen digits; the allowed per-digit counts are then
# the 123-numbers up to ~50, a small fixed set (plus 0 for absent digits).
SMALL_123 = (1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33)
ALLOWED = (0, *SMALL_123)  # valid total count for one digit, 0 = not present


@cache
def valid_totals(length: int) -> tuple[tuple[int, int, int], ...]:
    """All (c1, c2, c3) with each in ALLOWED, c1 + c2 + c3 == length."""
    return tuple(
        (c1, c2, c3)
        for c1 in ALLOWED
        for c2 in ALLOWED
        if (c3 := length - c1 - c2) >= 0 and c3 in ALLOWED
    )


def completions(length: int, used: tuple[int, int, int], remaining: int) -> int:
    """Count ways to finish a number of total digit-length `length`.

    `used` counts digits already placed in the prefix; `remaining` positions
    are still free. Each valid total (c1, c2, c3) >= used componentwise
    contributes a multinomial count of arrangements of the leftover digits.
    """
    total = 0
    for c1, c2, c3 in valid_totals(length):
        r1, r2, r3 = c1 - used[0], c2 - used[1], c3 - used[2]
        if r1 >= 0 and r2 >= 0 and r3 >= 0:
            total += factorial(remaining) // (
                factorial(r1) * factorial(r2) * factorial(r3)
            )
    return total


def count_of_length(length: int) -> int:
    return completions(length, (0, 0, 0), length)


def nth_123_number(n: int) -> int:
    """The n-th 123-number (1-indexed, ascending)."""
    # Shorter numbers are always smaller, so first fix the length.
    length = 1
    while (c := count_of_length(length)) < n:
        n -= c
        length += 1

    # Then choose digits most-significant-first, smallest digit whose
    # subtree of completions reaches the remaining index n.
    used = [0, 0, 0]
    digits = []
    for pos in range(length):
        for d in (1, 2, 3):
            used[d - 1] += 1
            c = completions(
                length, (used[0], used[1], used[2]), length - pos - 1
            )
            if n <= c:
                digits.append(d)
                break
            n -= c
            used[d - 1] -= 1
    return int("".join(map(str, digits)))


def main() -> int:
    assert [nth_123_number(i) for i in (4, 10, 40)] == [11, 31, 1112]
    assert nth_123_number(1000) == 1223321
    assert nth_123_number(6000) == 2333333333323
    return nth_123_number(111_111_111_111_222_333) % 123_123_123


if __name__ == "__main__":
    print(main())  # 57808202
