def solve(lo: int = 1864, hi: int = 1909) -> int:
    # Each regular S_n contributes edge directions {90 deg + 360 deg * k / n}, so
    # the Minkowski sum's side count is the number of distinct k/n (mod 1) over
    # all n in [lo, hi]. Distinct reduced fractions with denominator d number
    # phi(d), so the answer is the sum of phi(d) over every divisor d of some n.
    divisors: set[int] = set()
    for n in range(lo, hi + 1):
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.add(d)
                divisors.add(n // d)
            d += 1

    limit = hi
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    return sum(phi[d] for d in divisors)


if __name__ == "__main__":
    print(solve())  # 86226
