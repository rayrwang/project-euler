import numba

from funcs import prime_sieve_bool

@numba.jit(cache=True)
def total(N, is_pr):
    s = 1  # n = 1 qualifies: its only divisor pair (1, 1) gives 1 + 1 = 2, prime
    for n in range(2, N + 1, 2):       # n + 1 must be prime, so n is even
        if not is_pr[n + 1]:           # divisor pair (1, n)
            continue
        ok = True
        d = 2
        while d * d <= n:
            if n % d == 0 and not is_pr[d + n // d]:
                ok = False
                break
            d += 1
        if ok:
            s += n
    return s

if __name__ == "__main__":
    N = 100_000_000
    is_pr = prime_sieve_bool(N + 2)
    print(total(N, is_pr))  # 1739023853137
