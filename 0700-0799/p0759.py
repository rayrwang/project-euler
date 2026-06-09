MOD = 10**9 + 7

BINOM = ((1, 0, 0), (1, 1, 0), (1, 2, 1))

def S(n):
    """S(n) = sum_{i <= n} f(i)^2 mod MOD, where f satisfies f(1) = 1,
    f(2m) = 2 f(m), f(2m+1) = 2m + 1 + 2 f(m) + f(m)/m.

    Induction shows f(m) = m * b(m) with b the binary digit sum: the even
    case is immediate, and the odd case gives (2m+1) + (2m+1) b(m) =
    (2m+1)(b(m) + 1) = (2m+1) b(2m+1). (Verified directly for m < 20000.)

    So S(n) = sum m^2 b(m)^2, computed by a binary digit DP. For k-bit
    blocks define the joint moments
        M_k[a][c] = sum_{s < 2^k} s^a b(s)^c,   a, c in {0, 1, 2},
    built up by splitting on the top bit h: the h = 1 half contributes
    sum_{i <= a, j <= c} C(a,i) C(c,j) (2^(k-1))^(a-i) M_(k-1)[i][j].
    Walking the bits of n from the top, every position with a set bit
    contributes a block of 2^k consecutive integers sharing the prefix
    (value A, digit sum B):
        sum_{s < 2^k} (A + s)^2 (B + b(s))^2
          = sum_{i, j} C(2,i) C(2,j) A^(2-i) B^(2-j) M_k[i][j],
    and finally n itself is added.
    """
    bits = n.bit_length()
    # moments[k][a][c]
    moments = [[[0] * 3 for _ in range(3)] for _ in range(bits + 1)]
    moments[0][0][0] = 1  # s = 0 only: s^0 b^0 = 1 (0^0 taken as 1)
    for k in range(1, bits + 1):
        w = pow(2, k - 1, MOD)
        prev = moments[k - 1]
        cur = moments[k]
        for a in range(3):
            for c in range(3):
                total = prev[a][c]  # h = 0 half
                for i in range(a + 1):
                    for j in range(c + 1):
                        total += (
                            BINOM[a][i] * BINOM[c][j]
                            * pow(w, a - i, MOD) * prev[i][j]
                        )
                cur[a][c] = total % MOD

    answer = 0
    prefix_count = 0
    for k in range(bits - 1, -1, -1):
        if not n >> k & 1:
            continue
        a_val = ((n >> (k + 1)) << (k + 1)) % MOD
        b_val = prefix_count
        m = moments[k]
        for i in range(3):
            for j in range(3):
                answer += (
                    BINOM[2][i] * BINOM[2][j]
                    * pow(a_val, 2 - i, MOD) * pow(b_val, 2 - j, MOD)
                    * m[i][j]
                )
        answer %= MOD
        prefix_count += 1
    # n itself
    answer = (answer + n % MOD * (n % MOD) % MOD * prefix_count**2) % MOD
    return answer

if __name__ == "__main__":
    assert S(10) == 1530
    assert S(10**2) == 4798445
    print(S(10**16))  # 282771304
