MOD = 1_000_000_007
N = 12_345_678


def solve(n):
    """S(N) = sum of all m <= 2^N for which Eric forces a win.

    The game gives Oscar and Eric a budget of m to split into a composition;
    Eric wins when the total number of 1-bits (including those of m itself) is
    even. Solving the parity minimax and reading off the outcomes shows that
    whether Eric wins depends only on the binary string of m:

      * even bit-length: Eric wins only for the all-ones number 2^L - 1;
      * odd  bit-length L = 2j + 1: write the L - 1 bits after the leading 1 as
        j pairs (most-significant pair first) with values 0..3, and run the DFA
        F -0-> F, F -1-> N3, F -3-> A3,  N3 -0-> F, N3 -1-> N3,  A3 -3-> A3
        (pair value 2 and any other edge is dead). Eric wins iff the run ends in
        F or A3.

    Summing the winning m <= 2^N then splits into the odd-length contribution
    (a digit-DP over the pair DFA tracking both count and value-sum), the
    even-length contribution (one all-ones winner per length), and the single
    boundary value 2^N.
    """
    # Odd-length contribution via the pair DFA. State order: F, N3, A3.
    cf, cn, ca = 1, 0, 0  # counts; j = 0 starts a single empty run in F
    vf, vn, va = 0, 0, 0  # sums of the partial values built so far
    pow4 = 1              # 4^j = 2^(L-1) for L = 2j + 1
    total = 0
    j = 0
    while 2 * j + 1 <= n:
        # Accepting states are F and A3; each run contributes 2^(L-1) + X.
        total = (total + (cf + ca) * pow4 + vf + va) % MOD
        # Append one pair (advance j -> j + 1): new partial value = old*4 + digit.
        nf_c = cf + cn
        nf_v = (vf + vn) * 4
        nn_c = cf + cn
        nn_v = (vf + vn) * 4 + cf + cn
        na_c = cf + ca
        na_v = (vf + va) * 4 + 3 * (cf + ca)
        cf, cn, ca = nf_c % MOD, nn_c % MOD, na_c % MOD
        vf, vn, va = nf_v % MOD, nn_v % MOD, na_v % MOD
        pow4 = pow4 * 4 % MOD
        j += 1

    # Even-length contribution: sum over even L in [2, n] of (2^L - 1).
    m = n // 2
    inv3 = pow(3, MOD - 2, MOD)
    sum_pow = 4 * (pow(4, m, MOD) - 1) % MOD * inv3 % MOD  # sum_{i=1}^m 4^i
    total = (total + sum_pow - m) % MOD

    # Boundary value 2^N has bit-length N + 1; it wins iff that length is odd.
    if n % 2 == 0:
        total = (total + pow(2, n, MOD)) % MOD

    return total % MOD


if __name__ == "__main__":
    print(solve(N))  # 541510990
