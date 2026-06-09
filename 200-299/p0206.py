from math import isqrt


def solve() -> int:
    # The square reads 1_2_3_4_5_6_7_8_9_0. It ends in 0 (so n is a multiple of
    # 10) and its hundreds digit is 9, which forces n = 10m with m ending in 3
    # or 7, i.e. n is 30 or 70 mod 100.
    pattern = "1_2_3_4_5_6_7_8_9_0"
    lo = isqrt(1020304050607080900)
    hi = isqrt(1929394959697989990) + 1
    lo -= lo % 100
    for base in range(lo, hi + 1, 100):
        for n in (base + 30, base + 70):
            s = str(n * n)
            if len(s) == 19 and all(p == "_" or p == d for p, d in zip(pattern, s)):
                return n
    raise RuntimeError("no concealed square found")


if __name__ == "__main__":
    print(solve())  # 1389019170
