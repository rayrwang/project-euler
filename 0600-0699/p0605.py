MOD = 10**8

def last8_M(n: int, k: int) -> int:
    """Last 8 digits of M_n(k) = (reduced numerator) * (reduced denominator).

    Relabel each round by whether the player shared with the next round wins;
    this is an i.i.d. fair bit s_r, and the game ends at the first "10" pattern.
    The first such pattern is at position r with probability r * 2^-(r+1), and
    player k wins iff r == k-1 (mod n). Summing the geometric/arithmetic series
    gives, with m = k-1 and D = 2^n - 1,
        P_n(k) = 2^(n-m-1) (m D + n) / D^2.
    Here n = 10^8 + 7 is prime, so gcd(n, D) = 1 and (since any common prime of
    numerator and denominator must divide that gcd) the fraction is already in
    lowest terms. Thus M = 2^(n-m-1) (m D + n) D^2, taken mod 10^8.
    """
    m = k - 1
    D = (pow(2, n, MOD) - 1) % MOD
    num = pow(2, n - m - 1, MOD) * ((m * D + n) % MOD) % MOD  # reduced numerator
    den = D * D % MOD  # reduced denominator
    return num * den % MOD

if __name__ == "__main__":
    print(last8_M(10**8 + 7, 10**4 + 7))  # 59992576
