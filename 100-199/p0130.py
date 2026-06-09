from funcs import is_prime


def repunit_len(n: int) -> int:
    # A(n): length of the least repunit divisible by n (n coprime to 10).
    x = 1 % n
    k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k


def solve(count: int = 25) -> int:
    # For primes p (not 2,3,5), A(p) | p-1. Find composite n coprime to 10
    # sharing that property and sum the first `count` of them.
    total = 0
    found = 0
    n = 9
    while found < count:
        if n % 2 and n % 5 and not is_prime(n):
            if (n - 1) % repunit_len(n) == 0:
                total += n
                found += 1
        n += 2
    return total


if __name__ == "__main__":
    print(solve())  # 149253
