def A(m):
    """sum_{k=1}^{m} floor(log2 k).

    floor(log2 k) = j for the 2^j values k in [2^j, 2^(j+1)); the final block
    [2^L, m] is partial, where L = floor(log2 m).
    """
    if m <= 0:
        return 0
    length = m.bit_length() - 1
    total = sum(j * (1 << j) for j in range(length))
    total += length * (m - (1 << length) + 1)
    return total

def B(m):
    """sum_{k=1}^{m} v2(k) = v2(m!) = m - popcount(m) by Legendre's formula."""
    return m - bin(m).count("1")

def S(n):
    """sum_{k=1}^{n} F(k).

    By Kummer's theorem g(n, m) = v2(C(n, m)) is the number of carries when
    adding m and n - m in base 2, equal to s(m) + s(n-m) - s(n) for the binary
    digit sum s. Maximising over m gives F(n) = (high bit) - (low bit) of n + 1,
    i.e. F(n) = floor(log2(n+1)) - v2(n+1). Re-indexing k = n + 1 turns the sum
    into A(N+1) - B(N+1).
    """
    return A(n + 1) - B(n + 1)

if __name__ == "__main__":
    print(S(10**16))  # 501985601490518144
