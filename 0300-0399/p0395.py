import heapq
import math

# Each square is encoded by its base edge A -> B (side s); the square has
# corners A, B, B + n, A + n with n = rot90ccw(B - A).  The 3-4-5 triangle
# sits on the far side A'B' (A' = A + n) with apex C = A' + 0.64 v + 0.48 n,
# so the child squares have bases A' -> C (scale 4/5) and C -> B' (scale
# 3/5), the smaller one on the right as the problem requires.
#
# Each side of the bounding box is the supremum of a fixed linear functional
# over the tree, found by best-first branch and bound.  A subtree lies
# within R * s of its square's centre, where R = 5.71 satisfies
# R >= max(1.141 + 0.8 R, 1.077 + 0.6 R) (distance to each child's centre
# plus that child's own reach, the square's own corners being nearer).

R = 5.71

def supremum(ux, uy, tol):
    # largest projection onto (ux, uy) over the whole tree
    def bounds(ax, ay, vx, vy):
        nx, ny = -vy, vx
        s = math.hypot(vx, vy)
        upper = (ax + 0.5 * (vx + nx)) * ux + (ay + 0.5 * (vy + ny)) * uy + R * s
        corner = max(
            ax * ux + ay * uy,
            (ax + vx) * ux + (ay + vy) * uy,
            (ax + vx + nx) * ux + (ay + vy + ny) * uy,
            (ax + nx) * ux + (ay + ny) * uy,
        )
        return upper, corner

    upper, best = bounds(0.0, 0.0, 1.0, 0.0)
    heap = [(-upper, 0.0, 0.0, 1.0, 0.0)]
    while heap:
        neg_upper, ax, ay, vx, vy = heapq.heappop(heap)
        if -neg_upper <= best + tol:
            return best
        nx, ny = -vy, vx
        apx, apy = ax + nx, ay + ny
        cx = apx + 0.64 * vx + 0.48 * nx
        cy = apy + 0.64 * vy + 0.48 * ny
        for qx, qy, wx, wy in (
            (apx, apy, cx - apx, cy - apy),
            (cx, cy, ax + vx + nx - cx, ay + vy + ny - cy),
        ):
            upper, corner = bounds(qx, qy, wx, wy)
            best = max(best, corner)
            if upper > best + tol:
                heapq.heappush(heap, (-upper, qx, qy, wx, wy))
    return best

if __name__ == "__main__":
    width = supremum(1.0, 0.0, 1e-12) + supremum(-1.0, 0.0, 1e-12)
    height = supremum(0.0, 1.0, 1e-12) + supremum(0.0, -1.0, 1e-12)
    print(f"{width * height:.10f}")  # 28.2453753155
