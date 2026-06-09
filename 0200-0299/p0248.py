from math import factorial

from funcs import is_prime

# phi(n) = prod p^(e-1) (p - 1) over the prime powers of n, so every prime
# factor p of a solution satisfies (p - 1) | 13!. Collect those candidate
# primes (459 of them, from the 1584 divisors of 13!), then DFS over strictly
# increasing primes: choosing p with exponent e consumes a factor
# (p - 1) p^(e-1) of the target. Each n with phi(n) = 13! is produced exactly
# once; sort the 182752 solutions and take the 150000th.


def _divisors(n: int) -> list[int]:
    fac: dict[int, int] = {}
    d, m = 2, n
    while d * d <= m:
        while m % d == 0:
            fac[d] = fac.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        fac[m] = fac.get(m, 0) + 1
    divs = [1]
    for p, e in fac.items():
        divs = [d0 * p**i for d0 in divs for i in range(e + 1)]
    return sorted(divs)


def solve(rank: int = 150_000) -> int:
    target = factorial(13)
    candidates = [d + 1 for d in _divisors(target) if is_prime(d + 1)]
    solutions: list[int] = []

    def dfs(idx: int, remaining: int, n: int) -> None:
        if remaining == 1:
            solutions.append(n)
            return
        for i in range(idx, len(candidates)):
            p = candidates[i]
            if p - 1 > remaining:
                break
            if remaining % (p - 1):
                continue
            t = remaining // (p - 1)
            pe = p
            while True:
                dfs(i + 1, t, n * pe)
                if t % p:
                    break
                t //= p
                pe *= p

    dfs(0, target, 1)
    solutions.sort()
    return solutions[rank - 1]


if __name__ == "__main__":
    print(solve())  # 23507044290
