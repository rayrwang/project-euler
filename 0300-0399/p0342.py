import numpy as np

from funcs import prime_sieve_int


def solve(limit: int) -> int:
    """Sum of n with 1 < n < limit such that phi(n^2) is a cube.

    For n = prod p^a, phi(n^2) = prod p^(2a-1) (p-1). The largest prime p
    of n receives exponent 2a - 1 from its own power and nothing from any
    (q - 1), so 2a - 1 = 0 (mod 3), i.e. a = 2 (mod 3); in particular
    p^2 <= n, so every prime factor of n is below sqrt(limit).

    Build n by depth-first search over primes in *decreasing* order. The
    state tracks, for each smaller prime, the exponent (mod 3) already
    contributed by the (q - 1) factors of the primes used so far. A prime
    with nonzero pending exponent is "obligated": it must appear in n with
    the exponent residue that completes a multiple of three (pending 1
    needs 2a - 1 = 2, a = 0 mod 3, so a >= 3; pending 2 needs a = 1 mod 3,
    a >= 1; pending 0 allows skipping or a = 2 mod 3, a >= 2). Whenever no
    obligation remains, the current n is a solution. The n < limit budget
    keeps the tree small.
    """
    root = int(limit**0.5)
    primes = prime_sieve_int(root + 1)
    # Smallest prime factor table for factorising p - 1 quickly.
    spf = np.zeros(root + 1, dtype=np.int64)
    for p in primes[::-1]:
        spf[p::p] = p

    def factor_residues(m: int) -> dict[int, int]:
        out: dict[int, int] = {}
        while m > 1:
            p = int(spf[m])
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out[p] = e % 3
        return out

    prime_list = [int(p) for p in primes]
    index = {p: i for i, p in enumerate(prime_list)}
    total = 0

    def dfs(n: int, last_index: int, pending: dict[int, int]) -> None:
        nonlocal total
        obligated = [p for p, e in pending.items() if e]
        if not obligated and n > 1:
            total += n
        floor_p = max(obligated, default=2)
        # Next used prime must not skip past any obligated prime.
        for i in range(last_index - 1, index[floor_p] - 1, -1):
            q = prime_list[i]
            if q < floor_p:
                break
            e = pending.get(q, 0)
            a = (2 * (1 - e)) % 3 or 3  # smallest positive valid exponent
            power = q**a
            step = q**3
            while n * power < limit:
                residues = factor_residues(q - 1)
                merged = dict(pending)
                merged[q] = 0  # obligation for q is now consumed
                for r, re in residues.items():
                    merged[r] = (merged.get(r, 0) + re) % 3
                dfs(n * power, i, merged)
                power *= step
                if power >= limit:
                    break

    dfs(1, len(prime_list), {})
    return total


def brute(limit: int) -> int:
    from funcs import totient

    def is_cube(m: int) -> bool:
        c = round(m ** (1 / 3))
        return any((c + d) ** 3 == m for d in (-1, 0, 1))

    return sum(n for n in range(2, limit) if is_cube(n * totient(n)))


if __name__ == "__main__":
    assert brute(10**4) == solve(10**4)
    print(solve(10**10))  # 5943040885644
