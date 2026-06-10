from math import comb

MOD = 10**9 + 7

def primes_ending_in_7(k):
    out = []
    n = 7
    while len(out) < k:
        if n % 10 == 7 and all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            out.append(n)
        n += 10
    return out

def F(k):
    """Sum of k-Ruff numbers below N_k ending in digit 7, modulo MOD.

    A k-Ruff number below N_k = 10 M (M the product of the k primes ending
    in 7) is an n with gcd(n, N_k) = 1 and n = 7 (mod 10). Inclusion-
    exclusion over the subset T of those primes dividing n writes n = P_T m
    with m = c_T (mod 10), where c_T = 7 * P_T^(-1) = 7 * 3^|T| (mod 10)
    since every prime is 7 mod 10. Each arithmetic progression has exactly
    cnt_T = M / P_T terms below N_k, summing to
    P_T cnt_T (c_T + 5 (cnt_T - 1)). The three pieces factor:
      - P_T cnt_T = M is constant, so the c_T part is
        M * sum_j (-1)^j C(k, j) c_j with c_j cycling through 7,1,3,9;
      - the cnt_T^2 part gives 5 M^2 prod (1 - 1/p) = 5 M phi(M);
      - the remaining part carries sum_T (-1)^|T| = 0.
    Hence F(k) = M A + 5 M phi(M). This reproduces F(3) = 76101452 and was
    verified against brute force for k <= 4.
    """
    ps = primes_ending_in_7(k)
    m = 1
    phi = 1
    for p in ps:
        m = m * p % MOD
        phi = phi * (p - 1) % MOD
    a = sum((-1) ** j * comb(k, j) * (7 * pow(3, j, 10) % 10) for j in range(k + 1))
    return (m * (a % MOD) + 5 * m * phi) % MOD

if __name__ == "__main__":
    assert F(3) == 76101452
    print(F(97))  # 556206950
