import numba


@numba.njit(cache=True)
def _mod_pow10(e: int, mod: int) -> int:
    """10^e mod `mod` by binary exponentiation (mod < 1.1e8, so products fit i64)."""
    result = 1 % mod
    base = 10 % mod
    while e > 0:
        if e & 1:
            result = result * base % mod
        base = base * base % mod
        e >>= 1
    return result


@numba.njit(cache=True)
def _digit_sum(n: int) -> int:
    """S(n) = sum_{k=1}^n d_n(1/k), the n-th fractional decimal digit of 1/k.

    The n-th digit of 1/k is floor(10^n / k) mod 10. Reducing the numerator
    modulo 10k recovers both the digit and the floor in one shot:
        d_n(1/k) = floor((10^n mod 10k) / k),
    since 10^n mod 10k = (floor(10^n/k) mod 10) * k + (10^n mod k), and the
    bracket is exactly the wanted digit. Each term is one 64-bit modular
    exponentiation (10k <= 1.1e8 for n = 10^7, so all products stay below
    2^63), giving an O(n log n) sweep with no big integers.
    """
    total = 0
    for k in range(1, n + 1):
        total += _mod_pow10(n, 10 * k) // k
    return total


if __name__ == "__main__":
    assert _digit_sum(7) == 10
    assert _digit_sum(100) == 418
    print(_digit_sum(10**7))  # 44967734
