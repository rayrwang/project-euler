from math import gcd

# Supplied quantities (A, B) per product. Products 2, 3 and 5 all have
# b/a = 59/41 and pool together; product 1 has 5/41 and product 4 has 59/90.
# Totals are 18880 and 15744, whose ratio reduces to 295/246.
_POOL = ((1312, 1888), (2624, 3776), (3936, 5664))


def _feasible(u: int, v: int) -> bool:
    # Spoilage: t_i / b_i = (u/v) s_i / a_i per product, and the overall
    # paradox sum(s) / 18880 = (u/v) sum(t) / 15744. Writing the reduced
    # per-group ratio t/s = p/q gives s = q j, t = p j for a positive integer
    # j, bounded by s <= a and t <= b. The pooled group's multipliers
    # k_2 + k_3 + k_5 = K cover the full interval [3, KM]. The overall
    # condition becomes c1 j1 + c2 K + c4 j4 = 0 with c = 246 v q - 295 u p.
    def red(pn: int, qn: int) -> tuple[int, int]:
        g = gcd(pn, qn)
        return pn // g, qn // g

    p1, q1 = red(5 * u, 41 * v)
    p2, q2 = red(59 * u, 41 * v)
    p4, q4 = red(59 * u, 90 * v)
    j1_max = min(5248 // q1, 640 // p1)
    j4_max = min(5760 // q4, 3776 // p4)
    k_maxs = [min(a // q2, b // p2) for a, b in _POOL]
    if j1_max < 1 or j4_max < 1 or min(k_maxs) < 1:
        return False
    k_top = sum(k_maxs)
    c1 = 246 * v * q1 - 295 * u * p1
    c2 = 246 * v * q2 - 295 * u * p2  # always negative for m > 1
    c4 = 246 * v * q4 - 295 * u * p4
    if c1 <= 0:  # with c2 < 0 the equation would have no positive solution
        return False
    m = -c2
    c4m = c4 % m
    for j1 in range(1, j1_max + 1):
        r = (-c1 * j1) % m
        g = gcd(c4m, m)
        if r % g:
            continue
        step = m // g
        if c4m == 0:
            j4 = 1 if r == 0 else j4_max + 1
        else:
            j4 = (r // g) * pow(c4m // g, -1, step) % step
            if j4 == 0:
                j4 = step
        while j4 <= j4_max:
            val = c1 * j1 + c4 * j4
            if val % m == 0 and 3 <= val // m <= k_top:
                return True
            j4 += step
    return False


def solve() -> str:
    # m = u/v in lowest terms. The overall equation forces
    # m^2 < (246 * 41) / (295 * 5), i.e. m < 2.615. The bound
    # t1 <= 640 forces 5u / gcd(5u, 41v) <= 640; since gcd(u, v) = 1 the gcd
    # divides 205, so either u <= 640 or 41 | u with u <= 26240.
    candidates = [(u, v) for u in range(2, 641) for v in range(u // 3, u)]
    candidates += [
        (41 * u1, v) for u1 in range(16, 641) for v in range(41 * u1 // 3, 41 * u1)
    ]
    best_u, best_v = 1, 1
    for u, v in candidates:
        if u * u * 1475 >= v * v * 10086 or gcd(u, v) != 1:
            continue
        g2 = gcd(59 * u, 41 * v)
        if 59 * u // g2 > 1888 or 41 * v // g2 > 1312:
            continue
        if 5 * u // gcd(5 * u, 41 * v) > 640:
            continue
        g4 = gcd(59 * u, 90 * v)
        if 59 * u // g4 > 3776 or 90 * v // g4 > 5760:
            continue
        if u * best_v <= best_u * v:  # not an improvement
            continue
        if _feasible(u, v):
            best_u, best_v = u, v
    return f"{best_u}/{best_v}"


if __name__ == "__main__":
    print(solve())  # 123/59
