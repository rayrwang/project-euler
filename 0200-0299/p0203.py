from math import comb

if __name__ == "__main__":
    ROWS = 51
    # Every prime factor of C(n, k) with n <= 50 is at most n, so squarefreeness
    # only needs checking against primes up to 50.
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    seen = set()
    total = 0
    for n in range(ROWS):
        for k in range((n + 1) // 2 + 1):  # left half; C(n,k) = C(n,n-k)
            c = comb(n, k)
            if c in seen:
                continue
            seen.add(c)
            if all(c % (p * p) != 0 for p in primes):
                total += c
    print(total)  # 34029210557338
