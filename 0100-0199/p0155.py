from math import gcd


def solve(n: int = 18) -> int:
    # S[k] = set of capacitances (as reduced (p,q)) from exactly k unit caps.
    # Combine an i-cap network a and a (k-i)-cap network b: parallel a+b and
    # series a*b/(a+b). Answer = number of distinct values over all k <= n.
    sets: list[set[tuple[int, int]]] = [set() for _ in range(n + 1)]
    sets[1].add((1, 1))
    all_values: set[tuple[int, int]] = {(1, 1)}
    for k in range(2, n + 1):
        cur = sets[k]
        for i in range(1, k // 2 + 1):
            for pa, qa in sets[i]:
                for pb, qb in sets[k - i]:
                    # parallel: a + b
                    num = pa * qb + pb * qa
                    den = qa * qb
                    g = gcd(num, den)
                    cur.add((num // g, den // g))
                    # series: a*b/(a+b)
                    num2 = pa * pb
                    den2 = pa * qb + pb * qa
                    g2 = gcd(num2, den2)
                    cur.add((num2 // g2, den2 // g2))
        all_values |= cur
    return len(all_values)


if __name__ == "__main__":
    print(solve())  # 3857447
