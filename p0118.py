from itertools import combinations, permutations
from functools import lru_cache

from funcs import is_prime

def prime_perms(digits):
    """Number of permutations of `digits` (distinct, no zeros) that are prime."""
    if len(digits) == 1:
        return 1 if is_prime(digits[0]) else 0
    # Any arrangement of a digit set whose sum is a multiple of 3 is itself a
    # multiple of 3, hence composite, so the whole subset can be skipped.
    if sum(digits) % 3 == 0:
        return 0
    count = 0
    for perm in permutations(digits):
        if perm[-1] not in (1, 3, 7, 9):  # a prime > 5 can't end in an even digit or 5
            continue
        num = 0
        for d in perm:
            num = num * 10 + d
        if is_prime(num):
            count += 1
    return count

if __name__ == "__main__":
    # f[mask] = number of distinct primes using exactly the digits in `mask`
    # (bit d-1 represents digit d).
    f = {}
    for r in range(1, 9 + 1):
        for combo in combinations(range(1, 9 + 1), r):
            mask = 0
            for d in combo:
                mask |= 1 << (d - 1)
            f[mask] = prime_perms(combo)

    # g[mask] = number of distinct prime sets whose digits are exactly `mask`.
    # Fix the part containing the lowest set bit to count each partition once.
    @lru_cache(maxsize=None)
    def g(mask):
        if mask == 0:
            return 1
        low = mask & (-mask)
        rest = mask ^ low
        total = 0
        sub = rest
        while True:
            part = low | sub
            total += f[part] * g(mask ^ part)
            if sub == 0:
                break
            sub = (sub - 1) & rest
        return total

    print(g((1 << 9) - 1))  # 44680
