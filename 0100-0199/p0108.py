import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def min_n_with_div_count(target, prime_idx=0, max_exp=None):
    """Smallest n whose square n^2 has at least `target` divisors.

    For n = prod p_i^a_i we have d(n^2) = prod (2*a_i + 1). The value of n is
    minimised by giving the largest exponents to the smallest primes, so the
    search keeps the exponents non-increasing across primes in ascending order.
    """
    if target <= 1:
        return 1
    if prime_idx >= len(primes):
        return math.inf
    p = primes[prime_idx]
    best = math.inf
    power = 1
    a = 0
    while max_exp is None or a < max_exp:
        a += 1
        power *= p
        remaining = -(-target // (2 * a + 1))  # ceil(target / (2a+1))
        sub = min_n_with_div_count(remaining, prime_idx + 1, a)
        if sub != math.inf:
            best = min(best, power * sub)
        if remaining <= 1:  # this prime alone already meets the target
            break
    return best

if __name__ == "__main__":
    # (x - n)(y - n) = n^2, so the number of unordered (x, y) solutions is
    # (d(n^2) + 1) / 2. Requiring this to exceed 1000 means d(n^2) >= 2001.
    print(min_n_with_div_count(2 * 1000 + 1))  # 180180
