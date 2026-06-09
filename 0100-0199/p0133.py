import numpy as np


def is_nonfactor(p: int) -> bool:
    # p divides some R(10^n) iff ord_p(10) divides 10^n for some n, i.e. iff
    # ord_p(10) = 2^a 5^b. Since that order is < p, a,b are small, so testing
    # n up to ~20 settles it. p = 3 is the lone exception (3 | 9), never a factor.
    if p == 3:
        return True
    for n in range(20):
        if pow(10, 10**n, p) == 1:
            return False
    return True


def solve(limit: int = 100_000) -> int:
    sieve = np.ones(limit, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return sum(int(p) for p in np.nonzero(sieve)[0] if is_nonfactor(int(p)))


if __name__ == "__main__":
    print(solve())  # 453647705
