from funcs import totient_sieve

if __name__ == "__main__":
    N = 1_000_000
    # A reduced proper fraction n/d (n < d, gcd(n, d) = 1) exists for each n
    # coprime to d, so denominator d contributes exactly phi(d) fractions.
    # The answer is therefore sum_{d=2}^{N} phi(d).
    phi = totient_sieve(N + 1)
    print(int(phi[2:].sum()))  # 303963552391
