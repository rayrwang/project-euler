import heapq
from math import comb, sqrt

# Squares are packed greedily under y = 1/x (x >= 1): each placed square has
# its lower-left corner at the corner (x0, y0) of some rectangular region
# against the hyperbola, with side s solving (x0 + s)(y0 + s) = 1, and it
# spawns two child regions - to its right, index (left + 1, below), and on
# top, index (left, below + 1). A max-heap on side length replays the greedy
# order exactly. Exactly C(6, 3) = 20 squares ever receive the index (3, 3)
# (one per lattice path from (0, 0)), so pop until the twentieth such square
# appears; its position in the order is the answer. Adjacent side lengths
# differ by far more than double-precision error at this depth, so floats
# order the heap correctly.


def solve(target: tuple[int, int] = (3, 3)) -> int:
    def side(x: float, y: float) -> float:
        return (-(x + y) + sqrt((x - y) * (x - y) + 4)) / 2

    ta, tb = target
    remaining = comb(ta + tb, ta)
    heap: list[tuple[float, float, float, int, int]] = []
    heapq.heappush(heap, (-side(1.0, 0.0), 1.0, 0.0, 0, 0))
    n = 0
    while True:
        neg_s, x, y, a, b = heapq.heappop(heap)
        s = -neg_s
        n += 1
        if (a, b) == target:
            remaining -= 1
            if remaining == 0:
                return n
        heapq.heappush(heap, (-side(x + s, y), x + s, y, a + 1, b))
        heapq.heappush(heap, (-side(x, y + s), x, y + s, a, b + 1))


if __name__ == "__main__":
    print(solve())  # 782252
