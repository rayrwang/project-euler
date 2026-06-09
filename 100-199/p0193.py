import numpy as np


def solve(limit: int = 1 << 50) -> int:
    # Squarefree count below `limit` is sum_d mu(d) * floor((limit-1)/d^2).
    # Build mu up to sqrt(limit): flip the sign on each prime's multiples and
    # zero the multiples of each prime square.
    root = int((limit - 1) ** 0.5) + 1
    is_prime = np.ones(root + 1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(root**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = False
    mu = np.ones(root + 1, dtype=np.int8)
    for p in np.nonzero(is_prime)[0]:
        mu[p::p] = -mu[p::p]
        if p * p <= root:
            mu[p * p :: p * p] = 0
    d = np.arange(1, root + 1, dtype=np.int64)
    return int((mu[1:].astype(np.int64) * ((limit - 1) // (d * d))).sum())


if __name__ == "__main__":
    print(solve())  # 684465067343069
