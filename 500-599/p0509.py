def grundy_valuation_counts(n: int, v_max: int = 64) -> list[int]:
    """count[v] = #{ k in [1, n] : nu_2(k) = v }."""
    return [n // (1 << v) - n // (1 << (v + 1)) for v in range(v_max)]

def S(n: int, mod: int) -> int:
    """Winning next-player positions among triples (a, b, c), 1 <= a,b,c <= n.

    For a single pile of k stones a move removes a proper divisor of k. The
    Sprague-Grundy value of that pile is nu_2(k) (the 2-adic valuation): odd
    piles are losing (value 0) and 2**a * odd has value a. A triple is winning
    iff the XOR of the three valuations is non-zero.
    """
    v_max = 64
    count = grundy_valuation_counts(n, v_max)
    losing = 0  # triples with XOR of valuations equal to 0
    for v1 in range(v_max):
        if count[v1] == 0:
            continue
        for v2 in range(v_max):
            if count[v2] == 0:
                continue
            losing += count[v1] * count[v2] * count[v1 ^ v2]
    return (n**3 - losing) % mod

if __name__ == "__main__":
    assert S(10, 1234567890) == 692
    assert S(100, 1234567890) == 735494
    print(S(123456787654321, 1234567890))  # 151725678
