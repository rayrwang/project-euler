def solve(a: int, b: int, c: int, mod: int | None = None) -> int:
    """S(a, b, c) = sum_{n=0}^b F(n) for the crazy function F, assuming a > c.

    For n in (b - a, b] the four nested calls each land above b, giving
    F(n) = n + 4a - 4c; inductively, for n in (b - (k+1)a, b - ka],
    F(n) = n + 4(k+1)a - (3k+4)c. Summing block by block with m = floor(b/a):
    the partial bottom block [0, b - ma] uses k = m, and each full block
    contributes P_k = a*b - a(a-1)/2 + (3k+4)*a*(a-c). All arithmetic is done
    with exact Python integers, so the optional modulus is applied only at the
    end.
    """
    m = b // a
    rem = b - m * a  # top index of the bottom (partial) block
    low = (rem + 1) * (4 * (m + 1) * a - (3 * m + 4) * c) + rem * (rem + 1) // 2
    blocks = (
        m * (a * b - a * (a - 1) // 2)
        + (3 * m * (m - 1) // 2) * a * (a - c)
        + 4 * m * a * (a - c)
    )
    total = low + blocks
    return total % mod if mod is not None else total


if __name__ == "__main__":
    assert solve(50, 2000, 40) == 5204240
    print(solve(21**7, 7**21, 12**7, mod=10**9))  # 291504964
