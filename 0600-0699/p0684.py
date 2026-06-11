"""Project Euler Problem 684: Inverse Digit Sum.

s(n), the smallest number with digit sum n, is greedy from the right: as
many trailing 9s as possible, then one leading digit.  Writing n = 9q + r
with 1 <= r <= 9 gives s(n) = (r + 1) * 10^q - 1.

Summing over a complete block r = 1..9 for fixed q gives 54 * 10^q - 9, so
with k = 9Q + R (0 <= R <= 8),

    S(k) = 6 (10^Q - 1) - 9Q + (R (R + 3) / 2) 10^Q - R,

all evaluated modulo 10^9 + 7 with fast modular exponentiation.  The answer
is S summed over the Fibonacci numbers f_2 .. f_90.

Verified: s(10) = 19, S(20) = 1074, and S against brute force for k <= 200.
"""

MOD = 10**9 + 7


def s(n: int) -> int:
    """Smallest number with digit sum n (exact, for the asserts)."""
    q, r = divmod(n - 1, 9)
    return (r + 2) * 10**q - 1


def big_s(k: int, mod: int = MOD) -> int:
    """S(k) = sum of s(n) for n = 1..k, modulo mod."""
    big_q, r = divmod(k, 9)
    ten_q = pow(10, big_q, mod)
    full = (6 * (ten_q - 1) - 9 * big_q) % mod
    partial = (r * (r + 3) // 2 % mod * ten_q - r) % mod
    return (full + partial) % mod


def solve() -> int:
    fib = [0, 1]
    while len(fib) <= 90:
        fib.append(fib[-2] + fib[-1])
    return sum(big_s(fib[i]) for i in range(2, 91)) % MOD


if __name__ == "__main__":
    assert s(10) == 19
    assert all(sum(map(int, str(s(n)))) == n for n in range(1, 1000))
    # Brute-force minimality for small digit sums.
    smallest: dict[int, int] = {}
    for m in range(1, 10**4):
        smallest.setdefault(sum(map(int, str(m))), m)
    assert all(s(n) == smallest[n] for n in range(1, 28))
    assert big_s(20) == 1074
    total = 0
    for n in range(1, 201):
        total += s(n)
        assert big_s(n) == total % MOD
    print(solve())  # 922058210
