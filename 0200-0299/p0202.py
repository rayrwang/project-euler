def _factor(m: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            factors[d] = factors.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return factors


def solve(n: int = 12017639147) -> int:
    # Unfolding the mirror triangle to a triangular lattice, a beam reaching the
    # image (x, y) of C reflects 2(x+y)-3 times, leaves early unless gcd(x,y)=1,
    # and lands on a C-vertex iff x = y (mod 3). With s = x + y = (n+3)/2 this
    # counts x in [1, s) coprime to s (so coprime to x,y) with x = -s (mod 3).
    # A Mobius sum over the squarefree divisors of s evaluates that count.
    s = (n + 3) // 2
    target = (-s) % 3

    divisors = [(1, 1)]
    for p in _factor(s):
        divisors += [(d * p, -mu) for d, mu in divisors]

    def residue_count(limit: int, c: int) -> int:
        cc = c if c != 0 else 3
        return (limit - cc) // 3 + 1 if cc <= limit else 0

    total = 0
    for d, mu in divisors:
        inv = 1 if d % 3 == 1 else 2  # inverse of d mod 3 (s is coprime to 3)
        total += mu * residue_count(s // d, target * inv % 3)
    return total


if __name__ == "__main__":
    print(solve())  # 1209002624
