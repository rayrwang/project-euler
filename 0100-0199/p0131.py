from funcs import is_prime


def solve(limit: int = 1_000_000) -> int:
    # n^3 + n^2 p = n^2(n+p) is a cube. Taking n = k^3 gives
    # k^6 (k^3 + p); this is a cube exactly when k^3 + p = (k+1)^3, i.e.
    # p = (k+1)^3 - k^3 = 3k^2 + 3k + 1. So count primes of that form.
    count = 0
    k = 1
    while True:
        p = 3 * k * k + 3 * k + 1
        if p >= limit:
            break
        if is_prime(p):
            count += 1
        k += 1
    return count


if __name__ == "__main__":
    print(solve())  # 173
