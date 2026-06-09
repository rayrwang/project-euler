MOD = 1234567891


def p_of(n_lim: int) -> int:
    """P(n_lim) = prod of M(p) for p = 1..n_lim, mod MOD.

    The largest n with pi(n) | p is N(p) = gcd(F_p, F_{p+1} - 1), since
    n | F_p and n | F_{p+1} - 1 is exactly the Fibonacci matrix having
    order dividing p mod n. Empirically (verified exactly for p < 1000)
    and provably via Fibonacci/Lucas halving identities:
        N(4k) = F_{2k},  N(4k+2) = L_{2k+1},  N(odd p) = 2 if 3|p else 1.
    M(p) = N(p) when pi(N(p)) = p, which fails only if N(p) = N(p/l) for
    some prime l | p; strict growth of F and L makes that impossible for
    p >= 5 even, leaving M(2) = M(4) = 1, M(3) = 2 and M(p) = 1 for odd
    p >= 5.
    """
    result = 1
    if n_lim >= 3:
        result = 2
    # F_{2k} for 8 <= 4k <= n_lim and L_{2k+1} for 6 <= 4k+2 <= n_lim:
    # multiply F_m (m even, m >= 4) and L_m (m odd, m >= 3) for m <= n_lim/2.
    f0, f1 = 0, 1  # F_m, F_{m+1}
    l0, l1 = 2, 1  # L_m, L_{m+1}
    for m in range(n_lim // 2 + 1):
        if m % 2 == 0 and m >= 4 and 2 * m <= n_lim:
            result = result * f0 % MOD
        if m % 2 == 1 and m >= 3 and 2 * m <= n_lim:
            result = result * l0 % MOD
        f0, f1 = f1, (f0 + f1) % MOD
        l0, l1 = l1, (l0 + l1) % MOD
    return result


if __name__ == "__main__":
    assert p_of(10) == 264
    print(p_of(10**6))  # 29894398
