"""Project Euler 475: Music Festival.

12n musicians are split into 3n fixed quartets; f(12n) counts the
partitions into 4n trios with no two quartet-mates in a trio.

Mobius inclusion-exclusion over "glue patterns": for each quartet,
independently glue disjoint blocks of its members that are forced into a
common trio. Blocks of size 4 never fit in a trio, so the patterns are:
glue nothing (1 way, weight 1), one pair (6 ways, weight -1), two disjoint
pairs (3 ways, weight +1), one triple (4 ways, weight (-1)^2 2! = +2).
A pattern with P glued pairs and T glued triples leaves s = 12n - 2P - 3T
singles; each triple is a finished trio, each pair grabs one single
(s (s-1) ... (s-P+1) ways), and the s - P remaining singles form trios
freely in q! / (6^(q/3) (q/3)!) ways.
"""

MOD = 10**9 + 7

def solve(m: int, mod: int = MOD) -> int:
    q_total = m // 4
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact = [1] * (m + 1)
    inv_fact[m] = pow(fact[m], mod - 2, mod)
    for i in range(m, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod
    inv6 = pow(6, mod - 2, mod)

    def free_trios(q: int) -> int:
        if q % 3:
            return 0
        return fact[q] * pow(inv6, q // 3, mod) % mod * inv_fact[q // 3] % mod

    total = 0
    for q2 in range(q_total + 1):  # quartets gluing one pair
        for q3 in range(q_total + 1 - q2):  # quartets gluing two pairs
            for q4 in range(q_total + 1 - q2 - q3):  # quartets gluing a triple
                q1 = q_total - q2 - q3 - q4
                pairs = q2 + 2 * q3
                s = m - 2 * pairs - 3 * q4
                if s < pairs or (s - pairs) % 3:
                    continue
                ways = (fact[q_total] * inv_fact[q1] * inv_fact[q2] % mod
                        * inv_fact[q3] * inv_fact[q4] % mod)
                sign = mod - 1 if q2 % 2 else 1
                ways = ways * sign % mod * pow(6, q2, mod) % mod
                ways = ways * pow(3, q3, mod) % mod * pow(8, q4, mod) % mod
                ways = ways * fact[s] % mod * inv_fact[s - pairs] % mod
                total = (total + ways * free_trios(s - pairs)) % mod
    return total

if __name__ == "__main__":
    assert solve(12) == 576
    assert solve(24) == 509089824
    print(solve(600))  # 75780067
