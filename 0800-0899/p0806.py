P = 10**9 + 7

# Trivariate generating function for N(a, b, c), the number of indices t in
# the shortest n-disk Hanoi solution (n = a + b + c) whose position puts
# exactly a, b, c disks on pegs 1, 2, 3:
#     sum N(a,b,c) u^a v^b w^c = NUM / (1 - u^2 - v^2 - w^2 - 2uvw).
# NUM maps monomial exponents to coefficients.
NUM = {
    (2, 0, 0): 1, (1, 1, 1): 2, (1, 1, 0): 1, (1, 0, 0): 1,
    (0, 1, 1): 1, (0, 0, 2): 1, (0, 0, 1): 1,
}


def hanoi_nim_losing_sum(n: int) -> int:
    """f(n) mod P: sum of indices of Nim-losing positions in the solution.

    A position with peg counts (a, b, c) is a first-player Nim loss iff
    a XOR b XOR c = 0; with a + b + c = n this forces each binary digit of
    m = n/2 to be held by exactly two of the three counts, so the losing
    count triples are the 3^popcount(m) ways of assigning each bit of m to
    a pair of pegs. Time reversal of the Hanoi solution swaps pegs 1 and 3,
    so t is losing iff 2^n - 1 - t is, pairing the losing indices into
    couples summing to 2^n - 1; hence f(n) = (2^n - 1) * L / 2 with L the
    number of losing positions, and L = sum of N over the losing triples.

    N comes from the run structure of t: maximal runs of equal bits of t
    (n bits, MSB first) are blocks of consecutive disks on a single peg,
    and the run-to-peg automaton yields the rational generating function
    in NUM's comment. Expanding its denominator, N(a,b,c) is a sum of
    multinomials over step sequences from {(2,0,0), (0,2,0), (0,0,2),
    (1,1,1)}, the last taken with weight 2.
    """
    if n % 2 == 1:
        return 0
    m = n // 2

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % P
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], P - 2, P)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % P

    def coefficient(a: int, b: int, c: int) -> int:
        """[u^a v^b w^c] of 1 / (1 - u^2 - v^2 - w^2 - 2uvw), mod P."""
        if min(a, b, c) < 0 or a % 2 != b % 2 or b % 2 != c % 2:
            return 0
        total = 0
        pow2 = pow(2, a % 2, P)
        for d in range(a % 2, min(a, b, c) + 1, 2):  # number of (1,1,1) steps
            i, j, k = (a - d) // 2, (b - d) // 2, (c - d) // 2
            term = fact[i + j + k + d] * inv_fact[i] % P * inv_fact[j] % P
            total = (total + pow2 * term % P * inv_fact[k] % P
                     * inv_fact[d]) % P
            pow2 = pow2 * 4 % P
        return total

    def n_value(a: int, b: int, c: int) -> int:
        return sum(cf * coefficient(a - i, b - j, c - k)
                   for (i, j, k), cf in NUM.items()) % P

    bits = [1 << s for s in range(m.bit_length()) if (m >> s) & 1]
    losing = 0
    for assignment in range(3 ** len(bits)):
        a = b = c = 0
        code = assignment
        for bit in bits:  # give this bit of m to a pair of pegs
            pair = code % 3
            code //= 3
            if pair == 0:
                a, b = a + bit, b + bit
            elif pair == 1:
                a, c = a + bit, c + bit
            else:
                b, c = b + bit, c + bit
        losing = (losing + n_value(a, b, c)) % P

    half = pow(2, P - 2, P)
    return (pow(2, n, P) - 1) * losing % P * half % P


if __name__ == "__main__":
    assert hanoi_nim_losing_sum(4) == 30
    assert hanoi_nim_losing_sum(10) == 67518
    print(hanoi_nim_losing_sum(10**5))  # 94394343
