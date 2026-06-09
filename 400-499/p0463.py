def count_bit_set(m: int, k: int) -> int:
    """Count of j in [0, m] whose bit k is set."""
    if m < 0:
        return 0
    period = 1 << (k + 1)
    half = 1 << k
    return (m + 1) // period * half + max(0, (m + 1) % period - half)

def s(n: int) -> int:
    """S(n) = sum_{i=1}^n f(i). The recurrences make f(i) the binary-bit-reversal
    of i (reverse the bits of i's b-bit representation). The b-bit numbers
    [2^{b-1}, 2^b-1] reverse to every b-bit pattern with leading bit set, so their
    reversals sum to 4^{b-1}. For the top (partial) b = bitlength group, sum the
    reversed value bit by bit: bit k of i contributes 2^{b-1-k} times the count of
    in-range i with that bit set."""
    if n <= 0:
        return 0
    bits = n.bit_length()
    total = sum(1 << (2 * (b - 1)) for b in range(1, bits))  # full groups 4^{b-1}
    rest = n - (1 << (bits - 1))  # i - 2^{bits-1} ranges over [0, rest]
    for k in range(bits):
        count = rest + 1 if k == bits - 1 else count_bit_set(rest, k)
        total += (1 << (bits - 1 - k)) * count
    return total

if __name__ == "__main__":
    assert s(8) == 22
    assert s(100) == 3604
    print(s(3**37) % 10**9)  # 808981553
