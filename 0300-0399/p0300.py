import numpy as np
from numba import njit

LENGTH = 15
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def _contact_shapes(n: int) -> list[frozenset[tuple[int, int]]]:
    """Distinct sets of *non-consecutive* contact pairs over all foldings (self-avoiding
    walks) of length n. The first step is fixed to (1, 0): contacts are indexed by chain
    position, so they are invariant under the rotation this removes, cutting the work 4x."""
    shapes: set[frozenset[tuple[int, int]]] = set()
    path = [(0, 0), (1, 0)]
    occupied = {(0, 0), (1, 0)}

    def walk() -> None:
        if len(path) == n:
            index = {pt: i for i, pt in enumerate(path)}
            pairs = frozenset(
                (min(i, index[(x + dx, y + dy)]), max(i, index[(x + dx, y + dy)]))
                for i, (x, y) in enumerate(path)
                for dx, dy in DIRS
                if (x + dx, y + dy) in index and abs(index[(x + dx, y + dy)] - i) >= 2
            )
            shapes.add(pairs)
            return
        x, y = path[-1]
        for dx, dy in DIRS:
            nxt = (x + dx, y + dy)
            if nxt not in occupied:
                occupied.add(nxt)
                path.append(nxt)
                walk()
                path.pop()
                occupied.remove(nxt)

    walk()
    return list(shapes)


@njit(cache=True)
def _total_contacts(pi: np.ndarray, pj: np.ndarray, n: int) -> int:
    """Sum over all 2^n strings of the optimal H-H contact count: the always-present
    consecutive H-H bonds plus the best non-consecutive contacts achievable by folding."""
    num_shapes, max_pairs = pi.shape
    total = 0
    for bits in range(1 << n):
        base = 0
        for i in range(n - 1):
            if (bits >> i) & 1 and (bits >> (i + 1)) & 1:
                base += 1
        best = 0
        for k in range(num_shapes):
            count = 0
            for m in range(max_pairs):
                i = pi[k, m]
                if i < 0:
                    break
                j = pj[k, m]
                if (bits >> i) & 1 and (bits >> j) & 1:
                    count += 1
            if count > best:
                best = count
        total += base + best
    return total


def solve(n: int = LENGTH) -> float:
    """Average optimal number of H-H contact points over all 2^n proteins of length n.

    A folding is a self-avoiding walk; an H-H contact is a pair of H elements occupying
    lattice-adjacent cells. Consecutive H-H pairs are always in contact, so for each string
    the optimum is that fixed baseline plus the maximum, over all walk shapes, of the
    non-consecutive adjacent H-H pairs. The distinct contact-pair sets are enumerated once,
    then every string is scored by bit operations. The length-8 case averages 850/256 =
    3.3203125, confirming the model.
    """
    shapes = _contact_shapes(n)
    max_pairs = max(len(s) for s in shapes)
    pi = np.full((len(shapes), max_pairs), -1, dtype=np.int8)
    pj = np.full((len(shapes), max_pairs), -1, dtype=np.int8)
    for k, shape in enumerate(shapes):
        for m, (i, j) in enumerate(shape):
            pi[k, m] = i
            pj[k, m] = j
    total = _total_contacts(pi, pj, n)
    return total / (1 << n)


if __name__ == "__main__":
    assert solve(8) == 850 / 256
    print(solve())  # 8.0540771484375
