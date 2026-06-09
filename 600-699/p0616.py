def _primes(n: int) -> list[int]:
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(2, n + 1) if sieve[i]]

def solve(n: int) -> int:
    """Sum of creative integers <= n.

    An integer is creative iff it is a perfect power a^b (a, b > 1) that is not a
    dead end. Writing it via its primitive root, the only non-creative perfect powers
    are p^q with p, q both prime (a list {p, q} of two unsplittable primes that merely
    oscillates) and the single value 16 = 2^4: its splits only ever yield the elements
    2 and 4, and three 2s cannot be assembled into 256, so it can never expose an odd
    factor. Every other perfect power (e.g. 256 = 2^8 -> {2, 8}, 8 = 2^3 -> {2, 3})
    can reach an odd prime and grow without bound, hence reaches every m > 1.

    So the answer is (sum of distinct perfect powers) - (sum of p^q) - 16.
    """
    powers: set[int] = set()
    k = 2
    while 2**k <= n:
        m = 2
        while m**k <= n:
            powers.add(m**k)
            m += 1
        k += 1
    total = sum(powers)

    primes = _primes(int(n**0.5) + 1)
    bad = 0
    for q in primes:
        if 2**q > n:
            break
        for p in primes:
            v = p**q
            if v > n:
                break
            bad += v
    return total - bad - 16

if __name__ == "__main__":
    print(solve(10**12))  # 310884668312456458
