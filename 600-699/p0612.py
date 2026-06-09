"""Project Euler Problem 612: Friend numbers.

Two numbers are friends if their base-10 representations share at least one digit.
f(n) counts friend pairs (p, q) with 1 <= p < q < n.  Find f(10^18) mod 1000267129.

Count the complement.  For a digit set S (a 10-bit mask) let D[U] be the number of
integers in [1, n) whose digits all lie in U.  Because n = 10^18 is a power of ten,
[1, n) is exactly the positive integers with at most Lmax = 18 digits, so with
a = |U \\ {0}| nonzero allowed digits and b = |U| allowed digits,

    D[U] = sum_{L=1}^{Lmax} a * b^{L-1}.

D is the subset-sum (zeta) transform of cnt[S] = #{x in [1,n): digit set of x = S}, so
cnt is recovered by the Mobius (inverse zeta) transform.  Ordered pairs sharing no
digit number sum_S cnt[S] * D[complement(S)] (this never pairs x with itself, and
counts each unordered pair twice), hence

    f(n) = C(n-1, 2) - (1/2) sum_S cnt[S] * D[~S].

Everything is computed exactly, then reduced mod 1000267129.  Check: f(100) = 1539.
"""

MOD = 1000267129


def f(n: int, lmax: int) -> int:
    D = [0] * 1024
    for U in range(1024):
        b = bin(U).count("1")
        a = bin(U & ~1).count("1")  # nonzero allowed digits
        s = 0
        pw = 1
        for _ in range(lmax):
            s += a * pw
            pw *= b
        D[U] = s

    cnt = D[:]
    for i in range(10):  # inverse zeta transform: recover exact-digit-set counts
        bit = 1 << i
        for S in range(1024):
            if S & bit:
                cnt[S] -= cnt[S ^ bit]

    nf_ordered = 0
    for S in range(1024):
        nf_ordered += cnt[S] * D[1023 ^ S]
    nf_unordered = nf_ordered // 2

    total_pairs = (n - 1) * (n - 2) // 2
    return total_pairs - nf_unordered


def _brute(n: int) -> int:
    c = 0
    sets = [set(str(x)) for x in range(n)]
    for p in range(1, n):
        sp = sets[p]
        for q in range(p + 1, n):
            if sp & sets[q]:
                c += 1
    return c


if __name__ == "__main__":
    assert f(100, 2) == 1539, f(100, 2)
    assert f(1000, 3) == _brute(1000), (f(1000, 3), _brute(1000))
    print(f(10**18, 18) % MOD)  # 819963842
