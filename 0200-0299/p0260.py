import numba
import numpy as np

# Wythoff-style three-pile game: a move removes N > 0 stones from one, two or
# all three piles (the same N from each chosen pile). Process sorted
# configurations (x, y, z) in an order compatible with reachability (targets
# are component-wise <= after re-sorting): a position is losing iff no move
# reaches a losing position. Each move type fixes simple invariants, so
# losing positions are recognised with line tables:
#   single-pile moves fix the other two piles -> pair[{p, q}],
#   two-pile moves fix the difference of the pair and the untouched pile
#     -> diff[v - u][w],
#   three-pile moves fix both gaps -> gaps[y - x][z - y].
# Because losing positions form an antichain under moves (if one losing
# position could reach another, it would be winning), each table cell is
# marked by at most one losing position, and at query time only positions
# processed earlier (exactly the reachable ones) have marked it - so boolean
# tables give the exact game value. Verified: n = 100 gives 173895 as stated.


@numba.njit(cache=True)
def _solve(n: int) -> int:
    size = n + 1
    pair = np.zeros((size, size), dtype=np.uint8)
    diff = np.zeros((size, size), dtype=np.uint8)
    gaps = np.zeros((size, size), dtype=np.uint8)
    total = 0
    for z in range(size):
        for y in range(z + 1):
            for x in range(y + 1):
                if (
                    pair[y, z]
                    or pair[x, z]
                    or pair[x, y]
                    or diff[y - x, z]
                    or diff[z - x, y]
                    or diff[z - y, x]
                    or gaps[y - x, z - y]
                ):
                    continue
                total += x + y + z
                pair[y, z] = 1
                pair[x, z] = 1
                pair[x, y] = 1
                diff[y - x, z] = 1
                diff[z - x, y] = 1
                diff[z - y, x] = 1
                gaps[y - x, z - y] = 1
    return total


def solve(n: int = 1000) -> int:
    return int(_solve(n))


if __name__ == "__main__":
    print(solve())  # 167542057
