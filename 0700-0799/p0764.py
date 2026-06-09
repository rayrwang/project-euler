import numba

MOD = 10**9

@numba.njit(cache=True)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@numba.njit(cache=True)
def S(n):
    """Sum of x + y + z over primitive solutions of 16 x^2 + y^4 = z^2 with
    1 <= x, y, z <= n, modulo 10^9.

    (4x, y^2, z) is a Pythagorean triple whose gcd is a power of 2 (an odd
    common prime would divide x as well, contradicting gcd(x, y, z) = 1).

    y odd: the triple is primitive, so y^2 = m^2 - n^2, 4x = 2mn,
    z = m^2 + n^2. Both m - n and m + n are odd coprime squares s^2 < t^2
    with st = y, giving the family
        x = (t^4 - s^4)/8,  y = s t,  z = (s^4 + t^4)/2,   s < t odd coprime.

    y even: then x is odd and z = 4w, y = 2u with u^4 + x^2 = w^2 primitive;
    x odd forces u even, so u^2 = 2mn with {m, n} = {2p^4-ish}: u = 2pq with
    {m, n} = {2p^2, q^2}, q odd, gcd(p, q) = 1, yielding
        x = |4p^4 - q^4|,  y = 4 p q,  z = 16 p^4 + 4 q^4.

    Both families were verified complete against brute force up to n = 1500
    and reproduce S(10^4) = 112851 with 26 solutions. Within each family the
    parameters are recoverable from (y, z), and the families have opposite
    y parity, so no solution is generated twice. z is always the binding
    constraint apart from x >= 1, which holds automatically.
    """
    total = 0
    # Family A: y odd.
    t = 3
    while 1 + t**4 <= 2 * n:
        t4 = t**4
        s = 1
        while s < t and s**4 + t4 <= 2 * n:
            if gcd(s, t) == 1:
                x = (t4 - s**4) // 8
                y = s * t
                z = (s**4 + t4) // 2
                total = (total + x + y + z) % MOD
            s += 2
        t += 2
    # Family B: y even.
    p = 1
    while 16 * p**4 + 4 <= n:
        p4 = 4 * p**4
        q = 1
        while 4 * p4 + 4 * q**4 <= n:
            if gcd(p, q) == 1:
                x = p4 - q**4 if p4 > q**4 else q**4 - p4
                y = 4 * p * q
                z = 4 * p4 + 4 * q**4
                total = (total + x + y + z) % MOD
            q += 2
        p += 1
    return total

if __name__ == "__main__":
    assert S(10**2) == 81
    assert S(10**4) == 112851
    assert S(10**7) == 248876211
    print(S(10**16))  # 255228881
