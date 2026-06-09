import numba
import numpy as np

from funcs import prime_sieve_bool

MOD = 1_000_000_007

@numba.jit(cache=True)
def accumulate(is_prime, n, alpha, tau):
    """Single left-to-right pass over the digits of G(N).

    For each digit d the chosen value is a divisor of d, picked uniformly with
    weight alpha[d][a] = [a | d] / tau(d) (mod p). With prefix[a] the running
    sum of alpha over earlier positions, a new digit contributes
    sum_b alpha[d][b] * sum_{a>b} prefix[a] to the order-sensitive expectation E.
    The total over all divided sequences is then T * E, where T = prod tau(d).
    """
    prefix = np.zeros(10, dtype=np.int64)
    expectation = 0
    total = 1  # product of tau over all digits (mod p)
    digits = np.empty(9, dtype=np.int64)
    for value in range(2, n):
        if not is_prime[value]:
            continue
        # Collect digits least-significant first, then read most-significant first.
        m = value
        count = 0
        while m > 0:
            digits[count] = m % 10
            m //= 10
            count += 1
        for k in range(count - 1, -1, -1):
            d = digits[k]
            if d == 0:
                continue
            # suffix[b] = sum_{a>b} prefix[a]; accumulate contribution.
            running = 0
            contrib = 0
            for b in range(9, 0, -1):
                contrib = (contrib + alpha[d, b] * running) % MOD
                running = (running + prefix[b]) % MOD
            expectation = (expectation + contrib) % MOD
            for a in range(1, 10):
                prefix[a] = (prefix[a] + alpha[d, a]) % MOD
            total = (total * tau[d]) % MOD
    return total * expectation % MOD

def F(n):
    tau = np.zeros(10, dtype=np.int64)
    for d in range(1, 10):
        tau[d] = sum(1 for v in range(1, d + 1) if d % v == 0)
    alpha = np.zeros((10, 10), dtype=np.int64)
    for d in range(1, 10):
        inv = pow(int(tau[d]), MOD - 2, MOD)
        for a in range(1, 10):
            if d % a == 0:
                alpha[d, a] = inv
    is_prime = prime_sieve_bool(n)
    return accumulate(is_prime, n, alpha, tau)

if __name__ == "__main__":
    print(F(10**8))  # 480440153
