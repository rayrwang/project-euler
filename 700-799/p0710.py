MOD = 1_000_000

def solve():
    """Least n > 42 with 10^6 | t(n), where t(n) counts palindromic compositions
    of n that use at least one part equal to 2.

    A palindromic composition is a doubled half plus an optional centre, so the
    generating function for all of them is P(x) = (x + 2x^2) / (1 - 2x^2). The
    ones that avoid the part 2 have Q(x) = (x + x^2 + x^6) / (1 - 2x^2 + x^4 - x^6),
    and t = P - Q. The denominators give the constant-coefficient recurrences
        P_n = 2 P_(n-2),                      n >= 3,
        Q_n = 2 Q_(n-2) - Q_(n-4) + Q_(n-6),  n >= 7,
    which are iterated modulo 10^6 until t(n) vanishes.
    """
    # Seed values (exact, then reduced) for n = 0..6.
    p = [0, 1, 2, 2, 4, 4, 8]
    q = [0, 1, 1, 2, 2, 3, 4]
    n = 6
    while True:
        n += 1
        pn = (2 * p[n - 2]) % MOD
        qn = (2 * q[n - 2] - q[n - 4] + q[n - 6]) % MOD
        p.append(pn)
        q.append(qn)
        if n > 42 and (pn - qn) % MOD == 0:
            return n

if __name__ == "__main__":
    print(solve())  # 1275000
