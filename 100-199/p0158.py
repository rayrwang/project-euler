from math import comb


def solve(alphabet: int = 26) -> int:
    # Choosing n distinct letters fixes their relative order; the number of
    # arrangements with exactly one left-to-right ascent is the Eulerian number
    # <n,1> = 2^n - n - 1. So p(n) = C(26,n)*(2^n - n - 1); take the maximum.
    return max(comb(alphabet, n) * (2**n - n - 1) for n in range(1, alphabet + 1))


if __name__ == "__main__":
    print(solve())  # 409511334375
