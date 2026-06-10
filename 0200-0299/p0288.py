# Legendre's formula: the exponent of p in N! is (N - s_p(N))/(p - 1) with
# s_p the base-p digit sum - and N(p, q) = sum T_n p^n has exactly the T_n
# as its base-p digits since 0 <= T_n < p. So NF(p, q) mod p^k is
# ((N - sum T_n) mod (p-1) p^k) / (p - 1), needing only N modulo
# (p - 1) p^k, accumulated alongside the BBS-style generator. The given
# check NF(3, 10000) mod 3^20 = 624955285 is asserted.


def _nf_mod(p: int, q: int, mod: int) -> int:
    big = (p - 1) * mod
    s = 290797
    n_mod = 0
    pw = 1
    digit_sum = 0
    for _ in range(q + 1):
        t = s % p
        n_mod = (n_mod + t * pw) % big
        digit_sum += t
        pw = pw * p % big
        s = s * s % 50515093
    diff = (n_mod - digit_sum) % big
    assert diff % (p - 1) == 0
    return diff // (p - 1)


def solve() -> int:
    assert _nf_mod(3, 10000, 3**20) == 624955285
    return _nf_mod(61, 10**7, 61**10)


if __name__ == "__main__":
    print(solve())  # 605857431263981935
