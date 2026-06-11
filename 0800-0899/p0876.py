from collections import deque
from math import gcd, isqrt

# Each operation is a Vieta flip preserving Q = (c - a - b)^2 - 4ab, which
# is exactly the discriminant of the binary form F(X, Y) = a X^2 +
# (c - a - b) X Y + b Y^2.  In Conway's topograph the triple (a, b, c) is
# the set of values around one vertex of the superbase tree and a move is a
# step across an edge (the edge relation r + r' = 2(p + q) is our rule), so
# "some number becomes zero" means arriving at a vertex touching a region
# of value 0.  Zero regions exist iff Q is a perfect square s^2 — giving
# finitely many c per (a, b), namely c = a + b ± (d + e) over factorisations
# d e = ab — and correspond to the primitive root directions
# (x : y) = (-h ± s : 2a) of F.  The number of steps to the first vertex
# touching a region v is v's depth in the Stern–Brocot subdivision of the
# base sectors: the sum of the continued-fraction quotients of its sector
# coordinates minus one (mixed-sign coordinates (X, Y), X > 0 > Y, become
# (X - Y, -Y) in the adjacent sector).  Hence
#     f(a, b, c) = min over the two roots of that depth,
# and F(a, b) sums it over the candidate c.

EXPECT = {(6, 10): 17, (36, 100): 179}


def qsum(p: int, q: int) -> int:
    """Sum of the continued-fraction quotients of p/q (coprime, positive)."""
    s = 0
    while q:
        s += p // q
        p, q = q, p % q
    return s


def depth(x: int, y: int) -> int:
    """Steps from the base vertex until region (x, y) appears."""
    if y < 0:
        x, y = -x, -y
    if x > 0:
        return qsum(x, y) - 1  # inside sector (e1, e2)
    return qsum(y - x, y) - 1  # mixed signs: sector (e1, e3)


def f(a: int, b: int, c: int) -> int:
    h = c - a - b
    disc = h * h - 4 * a * b
    if disc < 0:
        return 0
    s = isqrt(disc)
    if s * s != disc:
        return 0
    best = 0
    for sg in (1,) if s == 0 else (1, -1):
        x0, y0 = -h + sg * s, 2 * a
        g = gcd(abs(x0), y0)
        d = depth(x0 // g, y0 // g)
        if best == 0 or d < best:
            best = d
    return best


def big_f(a: int, b: int, divisors: list[int]) -> int:
    ab = a * b
    total = 0
    for d in divisors:
        e = ab // d
        if d > e:
            continue
        for c in (a + b + d + e, a + b - d - e):
            if c >= 1:
                total += f(a, b, c)
    return total


def divisors_of(n: int) -> list[int]:
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return out


def divisors_60k(k: int) -> list[int]:
    out = []
    p2 = 1
    for _ in range(2 * k + 1):
        p3 = p2
        for _ in range(k + 1):
            p5 = p3
            for _ in range(k + 1):
                out.append(p5)
                p5 *= 5
            p3 *= 3
        p2 *= 2
    return out


def f_bfs(a: int, b: int, c: int, maxdepth: int, cap: int) -> int:
    start = (a, b, c)
    seen = {start}
    queue = deque([(start, 0)])
    while queue:
        (x, y, z), d = queue.popleft()
        if d >= maxdepth:
            continue
        for nt in (
            (2 * (y + z) - x, y, z),
            (x, 2 * (z + x) - y, z),
            (x, y, 2 * (x + y) - z),
        ):
            if 0 in nt:
                return d + 1
            if max(abs(v) for v in nt) <= cap and nt not in seen:
                seen.add(nt)
                queue.append((nt, d + 1))
    return 0


if __name__ == "__main__":
    assert f(6, 10, 35) == 3 and f(6, 10, 36) == 0  # given examples
    for (a, b), want in EXPECT.items():
        assert big_f(a, b, divisors_of(a * b)) == want  # given
    # cross-check the topograph depth against breadth-first search wherever
    # the latter is feasible, including a zero-discriminant case (4, 9, 25)
    for a, b in [(6, 10), (4, 9), (2, 3), (5, 8), (12, 25)]:
        for d in divisors_of(a * b):
            e = a * b // d
            for c in (a + b + d + e, a + b - d - e):
                if c >= 1:
                    val = f(a, b, c)
                    if val <= 8:
                        assert f_bfs(a, b, c, val + 1, 10**7) == val, (a, b, c)
    answer = sum(big_f(6**k, 10**k, divisors_60k(k)) for k in range(1, 19))
    print(answer)  # 457019806569269
