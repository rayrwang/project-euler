"""Project Euler Problem 628: Open Chess Positions.

A monotone rook path threads through the columns at non-decreasing heights;
analysing how the feasible-height set evolves shows that the only way a
permutation of pawns can block every path is a solid anti-diagonal wall in
a corner: pawns at (r - j, j) for j = 0..r (sealing the lower-left corner)
or the mirror image sealing the upper-right corner.  Walls of different
sizes in the same corner contradict each other (a column can hold only one
pawn), so each family is a disjoint union, and a lower-left wall of size
r + 1 coexists with an upper-right wall of size s + 1 exactly when
r + s <= n - 2 (otherwise they collide, except for the full anti-diagonal,
which is the unique wall belonging to both families).  Inclusion-exclusion:

    blocked(n) = 2 sum_{k=0}^{n-1} k!
               - ( sum_{r+s <= n-2} (n-2-r-s)!  +  1 ).

Writing S(m) = sum_{k<=m} k! and telescoping sum j*j! = (n-1)! - 1:

    f(n) = n! - 2 S(n-1) + (n-1) S(n-2) - (n-1)! + 2,

verified against a brute-force path search for all n <= 9 (in particular
f(3) = 2 and f(5) = 70).  One streaming pass gives n!, S(n-1) and S(n-2)
modulo 1008691207 (no divisions, so primality of the modulus is moot).
"""

import numba

MOD = 1008691207


@numba.jit(cache=True)
def f(n: int) -> int:
    fact = 1  # k!
    s = 1  # S(k) = sum of factorials 0!..k!
    s_nm2 = 1  # S(0), overwritten in the loop for n >= 3
    for k in range(1, n):
        fact = fact * k % MOD
        if k == n - 2:
            s_nm2 = (s + fact) % MOD
        s = (s + fact) % MOD
    fact_nm1 = fact
    fact_n = fact * n % MOD
    return (fact_n - 2 * s + (n - 1) % MOD * s_nm2 - fact_nm1 + 2) % MOD


def f_brute(n: int) -> int:
    from itertools import permutations

    count = 0
    for perm in permutations(range(n)):
        reach = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if perm[c] == r:
                    continue
                if r == 0 and c == 0:
                    reach[0][0] = True
                else:
                    reach[r][c] = (r > 0 and reach[r - 1][c]) or (
                        c > 0 and reach[r][c - 1]
                    )
        count += reach[n - 1][n - 1]
    return count


if __name__ == "__main__":
    assert [f(n) for n in range(2, 9)] == [f_brute(n) for n in range(2, 9)]
    assert f(3) == 2 and f(5) == 70
    print(f(10**8))  # 210286684
