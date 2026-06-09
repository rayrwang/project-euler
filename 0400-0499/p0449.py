import math

def simpson(f, x0: float, x1: float, n: int) -> float:
    h = (x1 - x0) / n
    s = f(x0) + f(x1)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(x0 + i * h)
    return s * h / 3

def chocolate(a: float, b: float, n: int = 200000) -> float:
    """Volume of a uniform 1mm coat on the spheroid x^2/a^2+y^2/a^2+z^2/b^2=1.

    The coat is the Minkowski parallel body at distance t=1, so by the Steiner
    tube formula its volume above the candy is S + M + 4*pi/3, where S is the
    surface area and M = integral of mean curvature. Both are integrals over the
    profile (r,z) = (a sin u, b cos u), u in [0, pi], with line element
    W = sqrt(a^2 cos^2 u + b^2 sin^2 u):
        S = 2*pi*a * int sin u * W du,
        M = pi * int sin u * (a^2 b / W^2 + b) du."""
    def w(u: float) -> float:
        return math.sqrt(a * a * math.cos(u) ** 2 + b * b * math.sin(u) ** 2)

    surface = 2 * math.pi * a * simpson(lambda u: math.sin(u) * w(u), 0.0, math.pi, n)
    mean_curv = math.pi * simpson(
        lambda u: math.sin(u) * (a * a * b / w(u) ** 2 + b), 0.0, math.pi, n
    )
    return surface + mean_curv + 4 * math.pi / 3

if __name__ == "__main__":
    assert abs(chocolate(1, 1) - 28 * math.pi / 3) < 1e-9
    assert abs(chocolate(2, 1) - 60.35475635) < 1e-7
    print(f"{chocolate(3, 1):.8f}")  # 103.37870096
