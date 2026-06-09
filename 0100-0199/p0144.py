def solve() -> int:
    # Beam in the ellipse 4x^2 + y^2 = 100. At each contact the normal is
    # parallel to (4x, y); reflect the incoming direction about it, then find
    # the far intersection with the ellipse. Count contacts until the beam
    # leaves through the gap |x| <= 0.01, y > 0.
    x0, y0 = 0.0, 10.1
    x, y = 1.4, -9.6           # first impact
    dx, dy = x - x0, y - y0    # incoming direction
    count = 0
    while not (abs(x) <= 0.01 and y > 0):
        count += 1
        nx, ny = 4 * x, y      # normal direction (~ gradient/2)
        dot = dx * nx + dy * ny
        nn = nx * nx + ny * ny
        rx = dx - 2 * dot / nn * nx
        ry = dy - 2 * dot / nn * ny
        t = -(8 * x * rx + 2 * y * ry) / (4 * rx * rx + ry * ry)
        x, y = x + t * rx, y + t * ry
        dx, dy = rx, ry
    return count


if __name__ == "__main__":
    print(solve())  # 354
