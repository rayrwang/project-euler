"""Project Euler Problem 520: Simbers.

A simber is a positive integer in which each odd digit present occurs an odd number
of times and each even digit present occurs an even number of times.  Q(n) counts
simbers with at most n digits.  Find (sum_{u=1}^{39} Q(2^u)) mod 1000000123.

Counting strings (including leading zeros) of length L with each even digit having
an even count and each odd digit a 0-or-odd count uses exponential generating
functions: even digits contribute cosh(x), odd digits contribute 1+sinh(x).  With
five of each kind, the count is

    T(L) = L! [x^L] cosh(x)^5 (1+sinh(x))^5 = (1/2^10) sum_j a_j j^L,

where, putting z = e^x, a_j = [z^{j+10}] (z^2+1)^5 (z^2+2z-1)^5 for j in [-10,10].
Strings of length L that *start* with a 0 and are simbers fix one 0 in front, so the
remaining L-1 digits need digit 0 to have odd count: that count is
Z(L-1) = (1/2^10) sum_j b_j j^{L-1} with b_j = [z^{j+10}] (z^2-1)(z^2+1)^4(z^2+2z-1)^5.
Then the number of L-digit simbers (no leading zero) is T(L) - Z(L-1), and

    Q(n) = sum_{L=1}^n (T(L) - Z(L-1))
         = (1/2^10) [ sum_j a_j * PA_j(n) - sum_j b_j * RB_j(n) ],

with PA_j(n) = sum_{L=1}^n j^L and RB_j(n) = sum_{t=0}^{n-1} j^t evaluated as
geometric series modulo 1000000123.
"""

MOD = 1_000_000_123


def _polymul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
    return out


def _polypow(a: list[int], e: int) -> list[int]:
    out = [1]
    for _ in range(e):
        out = _polymul(out, a)
    return out


# z^2+1, z^2+2z-1, z^2-1  (index = power of z)
A2 = [1, 0, 1]
B = [-1, 2, 1]
C2 = [-1, 0, 1]

# a_j = [z^{j+10}] (z^2+1)^5 (z^2+2z-1)^5
P = _polymul(_polypow(A2, 5), _polypow(B, 5))
# b_j = [z^{j+10}] (z^2-1)(z^2+1)^4 (z^2+2z-1)^5
QP = _polymul(C2, _polymul(_polypow(A2, 4), _polypow(B, 5)))

INV2_10 = pow(2**10, -1, MOD)


def _geom(j: int, n: int, include_zeroth: bool) -> int:
    """sum_{t=s}^{n-1+s} j^t reductions, mod MOD.

    include_zeroth False -> PA = sum_{L=1}^n j^L
    include_zeroth True  -> RB = sum_{t=0}^{n-1} j^t
    """
    if include_zeroth:
        if j == 0:
            return 1  # only t=0 term, 0^0 = 1
        if j % MOD == 1:
            return n % MOD
        jm = j % MOD
        return (pow(jm, n, MOD) - 1) * pow(jm - 1, -1, MOD) % MOD
    # PA
    if j == 0:
        return 0
    if j % MOD == 1:
        return n % MOD
    jm = j % MOD
    return jm * (pow(jm, n, MOD) - 1) % MOD * pow(jm - 1, -1, MOD) % MOD


def Q(n: int) -> int:
    total = 0
    for idx in range(21):  # j+10 = 0..20  -> j = -10..10
        j = idx - 10
        a_j = P[idx]
        b_j = QP[idx]
        total += a_j * _geom(j, n, False)
        total -= b_j * _geom(j, n, True)
    return total % MOD * INV2_10 % MOD


if __name__ == "__main__":
    assert Q(7) == 287975, Q(7)
    assert Q(100) % MOD == 123864868, Q(100)
    print(sum(Q(2**u) for u in range(1, 40)) % MOD)  # 238413705
