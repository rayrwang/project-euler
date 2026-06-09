from math import isqrt


def solve(amax: int) -> int:
    """Sum of integral areas <= amax of triangles with sides
    sqrt(1+b^2), sqrt(1+c^2), sqrt(b^2+c^2).

    Placing the triangle as O = (0,0), P = (b, 1) and Q on the locus
    forced by the other two side lengths gives area
    (1/2) sqrt(b^2 + c^2 + b^2 c^2) (the example b=2, c=8 yields
    sqrt(324)/2 = 9). So integral area A means
    b^2 + c^2 + b^2 c^2 = (2A)^2 = k^2, and mod 4 this forces b and c
    both even.

    For fixed a, the equation k^2 - (a^2+1) c^2 = a^2 is Pell-like with
    fundamental unit (2a^2+1, 2a), so solutions form chains under
    c -> (2a^2+1) c +/- 2 a k. Vieta-style descent (jumping the larger
    element down strictly reduces the pair, terminating at c = 0) shows
    every solution lives in a tree rooted at the pairs {b, 2b^2}. The
    search walks that tree, taking at each node both jump signs on each
    coordinate, keeping only children whose new element exceeds the
    current maximum (the rejected sign is the parent direction), bounded
    by k <= 2 amax. Only ~1200 triangles exist below 10^10.
    """
    kmax = 2 * amax
    total = 0
    seen: set[tuple[int, int]] = set()
    stack = []
    b = 2
    while b * (2 * b * b + 1) <= kmax:  # root {b, 2b^2} has k = b(2b^2+1)
        stack.append((b, 2 * b * b, b * (2 * b * b + 1)))
        b += 2
    while stack:
        a, c, k = stack.pop()
        if (a, c) in seen:
            continue
        seen.add((a, c))
        total += k // 2
        for cn in ((2 * a * a + 1) * c + 2 * a * k,
                   2 * a * k - (2 * a * a + 1) * c):
            if cn > c:
                kn = isqrt(a * a + cn * cn + a * a * cn * cn)
                if kn <= kmax:
                    stack.append((a, cn, kn))
        for an in ((2 * c * c + 1) * a + 2 * c * k,
                   2 * c * k - (2 * c * c + 1) * a):
            if an > c:
                kn = isqrt(c * c + an * an + c * c * an * an)
                if kn <= kmax:
                    stack.append((c, an, kn))
    return total


def brute(amax: int) -> int:
    total = 0
    for b in range(2, 2 * amax, 2):
        if b * b > 2 * amax:
            break
        for c in range(b + 2, 2 * amax + 2, 2):
            v = b * b + c * c + b * b * c * c
            if v > 4 * amax * amax:
                break
            k = isqrt(v)
            if k * k == v and k % 2 == 0:
                total += k // 2
    return total


if __name__ == "__main__":
    # The example triangle (b=2, c=8) has area 9.
    assert isqrt(2**2 + 8**2 + 2**2 * 8**2) == 18
    assert solve(10**5) == brute(10**5)
    print(solve(10**10))  # 2919133642971
