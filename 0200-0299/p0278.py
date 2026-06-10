# For distinct primes p, q, r the Frobenius number of {pq, pr, qr} is
# f(p, q, r) = 2pqr - pq - pr - qr (verified by brute reachability for
# several triples). Summing over all triples p < q < r < 5000:
# sum pqr = e3 and each unordered pair {u, v} appears in K - 2 triples, so
# sum over triples of (pq + pr + qr) = e2 (K - 2). Newton's identities give
# e2 and e3 from the prime power sums.


def solve(limit: int = 5000) -> int:
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                sieve[j] = False
    k = len(primes)
    s1 = sum(primes)
    s2 = sum(p * p for p in primes)
    s3 = sum(p**3 for p in primes)
    e2 = (s1 * s1 - s2) // 2
    e3 = (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
    return 2 * e3 - e2 * (k - 2)


if __name__ == "__main__":
    print(solve())  # 1228215747273908452
