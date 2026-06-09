import numba

from funcs import mod_exp_bounded, prime_sieve_bool

@numba.jit(cache=True)
def unitary_square_sum_factorial(N: int, mod: int, is_pr) -> int:
    """S(N!) mod, where S is the sum of squares of unitary divisors."""
    prod = 1
    for p in range(2, N + 1):
        if not is_pr[p]:
            continue
        # Legendre: exponent of p in N!
        e = 0
        pk = p
        while pk <= N:
            e += N // pk
            pk *= p
        # sigma*_2(p^e) = 1 + p^(2e); S is multiplicative.
        term = (1 + mod_exp_bounded(p, 2 * e, mod)) % mod
        prod = (prod * term) % mod
    return prod

if __name__ == "__main__":
    MOD = 10**9 + 9
    # Check: S(4!) = S(24) = (1+2^6)(1+3^2) = 650
    small = prime_sieve_bool(5)
    assert unitary_square_sum_factorial(4, MOD, small) == 650
    is_pr = prime_sieve_bool(10**8 + 1)
    print(unitary_square_sum_factorial(10**8, MOD, is_pr))  # 98792821
