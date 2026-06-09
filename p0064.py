from math import isqrt

def period_length(n):
    """Period of the continued fraction of sqrt(n), via exact integer recurrence."""
    a0 = isqrt(n)
    if a0 * a0 == n:
        return 0  # perfect square: terminates, no period
    m, d, a = 0, 1, a0
    length = 0
    while a != 2 * a0:           # the period always closes when a term hits 2*a0
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        length += 1
    return length

if __name__ == "__main__":
    print(sum(1 for n in range(2, 10001) if period_length(n) % 2 == 1))  # 1322
