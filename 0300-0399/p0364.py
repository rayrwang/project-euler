MOD = 100_000_007


def solve(n: int = 1_000_000) -> int:
    """T(N) mod 100000007, where T(N) counts the orders in which N people can fill
    N seats in a row under the rules: prefer a seat with no occupied neighbour,
    else a seat with exactly one occupied neighbour, else any seat.

    The rule-1 people (no occupied neighbour) all sit before any rule-2 person,
    and so on. The rule-1 seats end up as a maximal independent dominating set S
    of size k; since members are pairwise non-adjacent, none ever blocks another,
    so any of the k! orders is valid. Writing the row as
        [end gap L] O [gap g_1] O ... O [gap g_{k-1}] O [end gap R],
    maximality forces L, R in {0, 1} and each interior gap g_i in {1, 2}. Let
    e = L + R (end gaps of size 1, each a rule-2 seat) and g2 = number of interior
    gaps of size 2. Each size-2 gap supplies one rule-2 seat (2 choices for which
    of its two seats goes first) and one rule-3 seat; each size-1 interior gap is a
    single rule-3 seat. So the rule-2 phase has (e + g2) seats in any order and the
    rule-3 phase has (k - 1) seats in any order, giving

        contribution = k! * (k-1)! * (e + g2)! * 2^{g2}.

    The seat count fixes g2 = N - 2k + 1 - L - R, and the C(k-1, g2) chooses which
    interior gaps are the size-2 ones. Summing over k and the four (L, R) cases is
    an O(N) computation; T(1000) mod = 47255094 confirms it.
    """
    size = n + 2
    fact = [1] * (size + 1)
    for i in range(1, size + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (size + 1)
    inv_fact[size] = pow(fact[size], MOD - 2, MOD)
    for i in range(size, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    pow2 = [1] * (size + 1)
    for i in range(1, size + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD

    def choose(a: int, b: int) -> int:
        if b < 0 or b > a:
            return 0
        return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

    total = 0
    for k in range(1, n + 1):
        fk, fk1 = fact[k], fact[k - 1]
        for ends in (0, 1, 1, 2):  # (L, R) in {0,1}^2 -> e = L + R is 0,1,1,2
            g2 = n - 2 * k + 1 - ends
            if g2 < 0 or g2 > k - 1:
                continue
            if k == 1 and g2 != 0:
                continue
            term = choose(k - 1, g2) * fk % MOD * fk1 % MOD * fact[ends + g2] % MOD * pow2[g2]
            total = (total + term) % MOD
    return total


if __name__ == "__main__":
    # T(10) = 61632 and T(1000) mod 100000007 = 47255094.
    assert solve(10) == 61632
    assert solve(1000) == 47255094
    print(solve(1_000_000))  # 44855254
