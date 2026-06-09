from funcs import is_prime, prime_sieve_int

LIMIT = 10_000

def solve():
    primes = [int(p) for p in prime_sieve_int(LIMIT)]
    cache = {}

    def connects(a, b):
        key = (a, b) if a < b else (b, a)
        v = cache.get(key)
        if v is None:
            v = is_prime(int(f"{a}{b}")) and is_prime(int(f"{b}{a}"))
            cache[key] = v
        return v

    best = [float("inf")]

    def extend(clique, csum, group, start):
        if len(clique) == 5:
            best[0] = min(best[0], csum)
            return
        for i in range(start, len(group)):
            p = group[i]
            if csum + p >= best[0]:   # group ascending, so the rest are worse too
                break
            if all(connects(p, c) for c in clique):
                extend(clique + [p], csum + p, group, i + 1)

    # Concatenating two primes p, q gives p*10^k + q == p + q (mod 3), so unless a
    # prime is 3 itself, every prime in the set must share one residue mod 3.
    for residue in (1, 2):
        group = [3] + [p for p in primes if p % 3 == residue]
        extend([], 0, group, 0)
    return best[0]

if __name__ == "__main__":
    print(solve())  # 26033
