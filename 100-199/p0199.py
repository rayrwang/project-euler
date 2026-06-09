from math import sqrt


def solve(iterations: int = 10) -> float:
    # Apollonian gasket: an outer circle (curvature -1) holds three equal mutually
    # tangent circles; each gap bounded by three tangent circles is filled by a
    # Soddy circle of curvature a+b+c+2*sqrt(ab+bc+ca). Track the covered fraction.
    k0 = 1 + 2 / sqrt(3)
    covered = 3 * (1 / k0) ** 2

    def fill(a: float, b: float, c: float, depth: int) -> None:
        nonlocal covered
        if depth == 0:
            return
        d = a + b + c + 2 * sqrt(a * b + b * c + c * a)
        covered += (1 / d) ** 2
        fill(a, b, d, depth - 1)
        fill(a, c, d, depth - 1)
        fill(b, c, d, depth - 1)

    fill(k0, k0, k0, iterations)            # central gap
    for _ in range(3):                      # three gaps against the outer circle
        fill(-1, k0, k0, iterations)
    return round(1 - covered, 8)


if __name__ == "__main__":
    print(solve())  # 0.00396087
