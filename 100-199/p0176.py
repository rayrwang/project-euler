_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def _min_value(tau: int, first_prime: int) -> int:
    # Smallest integer M with tau(M^2) = tau, i.e. prod(2 e_i + 1) = tau.
    # Factor tau into odd parts >= 3 (each = 2 e_i + 1) and assign the largest
    # exponents to the smallest available primes.
    found: list[int] = []

    def recurse(remaining: int, max_factor: int, idx: int, value: int) -> None:
        if remaining == 1:
            found.append(value)
            return
        for d in range(min(max_factor, remaining), 2, -1):
            if remaining % d == 0:
                recurse(remaining // d, d, idx + 1, value * _PRIMES[idx] ** ((d - 1) // 2))

    recurse(tau, tau, first_prime, 1)
    return min(found)


def solve(triangles: int = 47547) -> int:
    # Right triangles with leg n number (tau(N^2) - 1) / 2 with N = n (n odd) or
    # N = n/2 (n even). Find the smallest n giving exactly `triangles` triangles.
    tau = 2 * triangles + 1
    even_candidate = 2 * _min_value(tau, 0)   # n = 2M, any M
    odd_candidate = _min_value(tau, 1)        # n = N, odd (primes from 3)
    return min(even_candidate, odd_candidate)


if __name__ == "__main__":
    print(solve())  # 96818198400000
