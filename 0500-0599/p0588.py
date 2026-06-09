"""
https://projecteuler.net/problem=588

Q(k) counts the odd coefficients of (x^4 + x^3 + x^2 + x + 1)^k. Find
the sum of Q(10^k) for k = 1..18.

Over GF(2), P(x)^(2^j) = P(x^(2^j)), so writing k in binary,
P^k = prod over set bits j of P(x^(2^j)) (mod 2). The coefficient of
x^e is therefore the parity of the number of ways to write
e = sum c_j 2^j with c_j in {0..4} at set bits of k and c_j = 0
elsewhere -- a carry process in base 2 where position j receives
c_j plus an incoming carry r, emits bit (c_j + r) mod 2 of e, and
passes carry (c_j + r) / 2 onward. Carries never exceed 3 (we allow
0..4 for slack).

The number of e with odd parity is computed by a digit DP whose state,
per exponent prefix, is the vector of representation parities indexed
by pending carry -- a 5-bit class. Processing the bits of k from the
least significant, each prefix splits over the next exponent bit b,
and the class transition XORs contributions over the allowed c and
the live carries. After the last bit of k, a prefix in class v
completes to exactly popcount(v) exponents with an odd coefficient:
appending carry r's binary digits determines the rest of e uniquely,
with parity v[r], and (prefix, r) -> e is injective. Hence
Q(k) = sum over classes of count * popcount.

Verified against direct GF(2) polynomial expansion for all k < 200
and the given Q(3) = 7, Q(10) = 17, Q(100) = 35.
"""

N_CARRIES = 5


def q_direct(k: int) -> int:
    """Literal expansion of P^k over GF(2)."""
    res = [1]
    for _ in range(k):
        new = [0] * (len(res) + 4)
        for i, c in enumerate(res):
            if c:
                for j in range(5):
                    new[i + j] ^= 1
        res = new
    return sum(res)


def q_of(k: int) -> int:
    counts = {1 << 0: 1}  # empty prefix: one representation at carry 0
    for ch in bin(k)[2:][::-1]:
        cs = range(5) if ch == "1" else (0,)
        new: dict[int, int] = {}
        for b in (0, 1):
            for v, cnt in counts.items():
                vp = 0
                for r in range(N_CARRIES):
                    if (v >> r) & 1:
                        for c in cs:
                            t = c + r
                            if t % 2 == b:
                                vp ^= 1 << (t // 2)
                if vp:
                    new[vp] = new.get(vp, 0) + cnt
        counts = new
    return sum(cnt * bin(v).count("1") for v, cnt in counts.items())


if __name__ == "__main__":
    for kk in range(1, 200):
        assert q_of(kk) == q_direct(kk), kk
    assert q_of(3) == 7 and q_of(10) == 17 and q_of(100) == 35

    print(sum(q_of(10**k) for k in range(1, 19)))  # 11651930052
