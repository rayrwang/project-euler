import heapq

MOD = 123454321

def _odd_primes(n: int) -> list[int]:
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(3, n + 1) if sieve[i]]

def _seeds(limit: int, primes: list[int]) -> list[tuple[int, int]]:
    """All odd u with base(u) = u / 2^Omega(u) <= limit, as (u, Omega(u))."""
    out: list[tuple[int, int]] = []
    np_ = len(primes)

    def dfs(u: int, om: int, idx: int) -> None:
        out.append((u, om))
        cap = limit << (om + 1)
        for i in range(idx, np_):
            nu = u * primes[i]
            if nu <= cap:
                dfs(nu, om + 1, i)
            else:
                break

    dfs(1, 0, 0)
    return out

def solve(k: int, target: int, limit: int) -> int:
    """The target-th smallest n with Omega(n) >= k, modulo 123454321.

    Writing n = 2^a * u (u odd), Omega(n) >= k means a >= k - Omega(u), so
    n / 2^k = u * 2^(a-k) = base(u) * 2^t with base(u) = u / 2^Omega(u) and t >= 0.
    The numbers with Omega >= k therefore correspond order-preservingly to the values
    base(u) * 2^t. Seeding every odd u with base(u) <= limit and merging the geometric
    chains base(u), 2 base(u), ... with a heap yields them in order; the target-th one,
    n = 2^(k + E) * u (E = t - Omega(u)), is reduced modulo 123454321. The choice of
    limit is valid because the target-th ratio comes out <= limit (so no u was missed).
    """
    primes = _odd_primes(2 * limit)
    off = 64
    heap = [(u << (-om + off), u, -om) for u, om in _seeds(limit, primes)]
    heapq.heapify(heap)
    u = e = 0
    for _ in range(target):
        _, u, e = heapq.heappop(heap)
        heapq.heappush(heap, (u << (e + 1 + off), u, e + 1))
    return pow(2, k + e, MOD) * (u % MOD) % MOD

if __name__ == "__main__":
    print(solve(10**6, 10**6, 200000))  # 108424772
