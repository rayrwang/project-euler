from math import comb


def solve(d: int = 100) -> int:
    # Non-decreasing numbers with up to d digits (digits 1..9): C(d+9,9) - 1.
    # Non-increasing numbers with up to d digits (digits 0..9, minus all-zero
    # per length): C(d+10,10) - 1 - d.
    # Both (repdigits, 9 per length): 9*d. Inclusion-exclusion:
    return comb(d + 9, 9) + comb(d + 10, 10) - 10 * d - 2


if __name__ == "__main__":
    # checkpoints: solve(6) == 12951, solve(10) == 277032
    print(solve())  # 51161058134250
