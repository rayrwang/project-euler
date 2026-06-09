def solve(limit: int = 10**9, prime_max: int = 100) -> int:
    # Count "generalised Hamming numbers" <= limit whose prime factors are all
    # at most prime_max, by recursively multiplying in the eligible primes.
    primes = [p for p in range(2, prime_max + 1)
              if all(p % d for d in range(2, int(p**0.5) + 1))]

    def count(index: int, value: int) -> int:
        total = 1
        for i in range(index, len(primes)):
            v = value * primes[i]
            while v <= limit:
                total += count(i + 1, v)
                v *= primes[i]
        return total

    return count(0, 1)


if __name__ == "__main__":
    print(solve())  # 2944730
