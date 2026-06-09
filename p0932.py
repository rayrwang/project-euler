import numba

@numba.jit(cache=True)
def T(max_digits):
    """Sum of N < 10^max_digits with N = (a+b)^2, where a|b is N split so that
    b has some length k (no leading zero) and a is the rest."""
    limit = 10**max_digits
    total = 0
    s = 1
    while s * s < limit:
        # N = a*10^k + b == a + b (mod 9) and N = s^2, so s^2 == s (mod 9).
        if s % 9 <= 1:
            n = s * s
            pw = 10
            while pw < n:                  # pw = 10^k; b occupies k digits
                a = n // pw
                b = n % pw
                if a + b == s and b >= pw // 10:   # b has exactly k digits
                    total += n
                pw *= 10
        s += 1
    return total

if __name__ == "__main__":
    print(T(16))  # 72673459417881349
