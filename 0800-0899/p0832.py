"""Project Euler 832: Mex Sequence.

Simulating the process reveals its algebraic skeleton: round k writes
the triple (a, 2 (x) a, 3 (x) a) under nim-multiplication, where a runs
through the positive integers whose leading base-4 digit is 1 (the
blocks [4^j, 2 * 4^j)).  Indeed, nim-multiplying by 2 acts digitwise
on base-4 digits as the GF(4) map 0,1,2,3 -> 0,2,3,1, and the three
triples {a, 2 (x) a, 3 (x) a} tile each block [4^j, 4^(j+1)) into its
three quarters, matching the simulated triples exactly.

For any nonzero GF(4) digit d, d + 2 (x) d + 3 (x) d = 1 + 2 + 3 = 6,
so each triple sums to 6 * sum of 4^i over the nonzero base-4 digit
positions of a.  M(n) is therefore 6 times a digit-counting sum: full
blocks contribute 16^j + 4^(j-1)(4^j - 1) in closed form, and the
partial block is a standard per-position count of nonzero digits below
a bound.  Everything is exact integer arithmetic, validated against
direct simulation for n <= 1500 (including M(10) = 642 and
M(1000) = 5432148), with the final reduction modulo 10^9 + 7.
"""

from __future__ import annotations

MOD = 10**9 + 7


def nonzero_digit_weight_sum(r: int) -> int:
    """sum_{s=0}^{r-1} (sum of 4^i over nonzero base-4 digits of s)."""
    total = 0
    i = 0
    while 4**i < max(r, 1):
        block = 4 ** (i + 1)
        hi, rem = divmod(r, block)
        cnt = hi * 3 * 4**i + max(0, rem - 4**i)
        total += cnt * 4**i
        i += 1
    return total


def mex_total(n: int) -> int:
    total = 0
    rem = n
    j = 0
    while rem > 0:
        take = min(rem, 4**j)
        total += take * 4**j + nonzero_digit_weight_sum(take)
        rem -= take
        j += 1
    return 6 * total


def simulate(rounds: int) -> list[int]:
    used: set[int] = set()
    sums = []
    running = 0
    a = 1
    for _ in range(rounds):
        while a in used:
            a += 1
        b = a + 1
        while b in used or (a ^ b) in used:
            b += 1
        used.update((a, b, a ^ b))
        running += a + b + (a ^ b)
        sums.append(running)
    return sums


def main() -> None:
    sums = simulate(1500)
    for n in (1, 2, 5, 10, 100, 777, 1000, 1500):
        assert mex_total(n) == sums[n - 1]
    assert mex_total(10) == 642
    assert mex_total(1000) == 5432148
    print(mex_total(10**18) % MOD)  # 552839586


if __name__ == "__main__":
    main()
