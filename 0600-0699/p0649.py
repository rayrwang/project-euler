"""Project Euler Problem 649: Low-Prime Chessboard Nim.

Each coin is an independent impartial game, itself the sum of two copies of
the 1-D subtraction game with subtraction set {2, 3, 5, 7}.  That game's
Grundy sequence is periodic with period 9: g(x) for x mod 9 = 0..8 is
(0, 0, 1, 1, 2, 2, 3, 3, 4), verified against a direct mex computation.  A
coin on (x, y) has Grundy g(x) XOR g(y), and Alice wins unless the XOR over
all coins is zero.  So

    M(n, c) = n^(2c) - #{arrangements with XOR 0}.

Count the per-coin Grundy distribution cnt2[v] (an XOR-convolution square of
the per-axis distribution), then the c-fold XOR convolution at 0 via the
Walsh-Hadamard transform over (Z/2)^3:

    zero count = (1/8) sum_{s=0}^{7} w_s^c,
    w_s = sum_v (-1)^popcount(s AND v) cnt2[v].

Exact Python integers keep the division by 8 trivial despite the non-prime
modulus 10^9.  Checks: M(3, 1) = 4, M(3, 2) = 40, M(9, 3) = 450304.
"""

PERIOD = (0, 0, 1, 1, 2, 2, 3, 3, 4)


def grundy_check(limit: int) -> None:
    g = []
    for x in range(limit):
        moves = {g[x - s] for s in (2, 3, 5, 7) if x >= s}
        v = 0
        while v in moves:
            v += 1
        g.append(v)
    assert all(g[x] == PERIOD[x % 9] for x in range(limit))


def M(n: int, c: int) -> int:
    axis = [0] * 8
    for r in range(9):
        axis[PERIOD[r]] += n // 9 + (1 if r < n % 9 else 0)
    cnt2 = [0] * 8
    for a in range(8):
        for b in range(8):
            cnt2[a ^ b] += axis[a] * axis[b]
    w = [
        sum(-v if (s & u).bit_count() % 2 else v for u, v in enumerate(cnt2))
        for s in range(8)
    ]
    zeros = sum(ws**c for ws in w)
    assert zeros % 8 == 0
    return n ** (2 * c) - zeros // 8


if __name__ == "__main__":
    grundy_check(1000)
    assert M(3, 1) == 4 and M(3, 2) == 40 and M(9, 3) == 450304
    print(M(10000019, 100) % 10**9)  # 924668016
