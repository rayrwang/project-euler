# A steady square with n digits satisfies x^2 = x (mod 14^n): the
# idempotents mod 14^n = 2^n 7^n. Besides 0 and 1, CRT gives exactly two
# nontrivial idempotents, e1 = (1 mod 2^n, 0 mod 7^n) and its complement
# e2 = 1 - e1; these lift coherently (e mod 14^n is the n-digit truncation
# of e mod 14^N), so computing both idempotents once modulo 14^10000 and
# reading their base-14 digit arrays suffices. An n-digit steady square
# requires a nonzero leading digit, i.e. digit n-1 of the truncation is
# nonzero, in which case the prefix digit sum is added. x = 1 contributes 1
# (for n = 1); 0 is excluded. The statement's check - the total for
# 1 <= n <= 9 is 582 decimal - is asserted.


def _digit_total(num_digits: int) -> int:
    m2, m7 = 2**num_digits, 7**num_digits
    e1 = m7 * pow(m7, -1, m2) % (m2 * m7)
    e2 = m2 * pow(m2, -1, m7) % (m2 * m7)
    total = 1  # x = 1
    for e in (e1, e2):
        digits = []
        x = e
        for _ in range(num_digits):
            digits.append(x % 14)
            x //= 14
        prefix = 0
        for n in range(1, num_digits + 1):
            prefix += digits[n - 1]
            if digits[n - 1] != 0:
                total += prefix
    return total


def solve(num_digits: int = 10000) -> str:
    assert _digit_total(9) == 582
    answer = _digit_total(num_digits)
    out = []
    while answer:
        out.append("0123456789abcd"[answer % 14])
        answer //= 14
    return "".join(reversed(out))


if __name__ == "__main__":
    print(solve())  # 5a411d7b
