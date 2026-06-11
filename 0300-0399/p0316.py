import numba


@numba.jit(cache=True)
def g(n: int) -> int:
    """Expected start index of the first occurrence of n's digit string.

    By the fair-casino argument the expected index of the *final* digit is
    sum of 10^|b| over all nonempty borders b of the pattern (strings that
    are both prefix and suffix, the full pattern included); subtract d - 1
    for a d-digit pattern to get the start index.
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    d = len(digits)

    # KMP failure function: fail[i] = length of longest proper border of
    # the prefix of length i + 1.
    fail = [0] * d
    k = 0
    for i in range(1, d):
        while k > 0 and digits[i] != digits[k]:
            k = fail[k - 1]
        if digits[i] == digits[k]:
            k += 1
        fail[i] = k

    # Borders of the whole pattern: d, fail[d-1], fail of that, ...
    total = 0
    length = d
    while length > 0:
        total += 10**length
        length = fail[length - 1]
    return total - (d - 1)


@numba.jit(cache=True)
def total(big: int, limit: int) -> int:
    s = 0
    for n in range(2, limit):
        s += g(big // n)
    return s


if __name__ == "__main__":
    assert g(535) == 1008
    assert total(10**6, 1000) == 27280188
    print(total(10**16, 1_000_000))  # 542934735751917735
