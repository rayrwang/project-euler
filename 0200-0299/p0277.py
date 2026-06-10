# The branch taken at step i depends on a_i mod 3, which is determined by
# a_1 mod 3^i (every map is linear over 3), so the 30-letter prefix pins
# down a_1 modulo 3^30 - and conversely any starting value in that residue
# class produces the same 30 branches. Lift the residue one base-3 digit at
# a time: among the three lifts modulo 3^(k+1), exactly one representative
# reproduces the first k+1 letters when simulated directly. The answer is
# the smallest member of the final class exceeding 10^15, re-verified by
# simulation. The worked example 231 -> "DdDddUUdDD" checks out.


def _sequence(a: int, steps: int) -> str:
    out = []
    for _ in range(steps):
        if a % 3 == 0:
            out.append("D")
            a //= 3
        elif a % 3 == 1:
            out.append("U")
            a = (4 * a + 2) // 3
        else:
            out.append("d")
            a = (2 * a - 1) // 3
    return "".join(out)


def solve(target: str = "UDDDUdddDDUDDddDdDddDDUDDdUUDd", lower: int = 10**15) -> int:
    n = len(target)
    r = 0
    for k in range(n):
        mod = 3**k
        for j in range(4):
            cand = r + j * mod
            if cand > 0 and _sequence(cand, k + 1) == target[: k + 1]:
                r = cand
                break
        else:
            raise AssertionError("no lift found")
    big = 3**n
    a1 = r
    while a1 <= lower:
        a1 += big
    assert _sequence(a1, n) == target
    return a1


if __name__ == "__main__":
    print(solve())  # 1125977393124310
