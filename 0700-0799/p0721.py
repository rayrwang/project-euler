import numba

MOD = 999_999_937

@numba.njit(cache=True)
def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result

@numba.njit(cache=True)
def f(a, n):
    """floor((ceil(sqrt a) + sqrt a)^n) mod MOD.

    If a = s^2 the base is the integer 2s. Otherwise let c = ceil(sqrt a) and
    y = c - sqrt(a), which lies strictly in (0, 1). The conjugate sum
    (c + sqrt(a))^n + (c - sqrt(a))^n is an integer (symmetric in the two
    roots of t^2 - 2ct + (c^2 - a)), and 0 < y^n < 1, so the floor is that
    integer minus one. Compute (c + sqrt(a))^n = u + v sqrt(a) by binary
    exponentiation in Z_p[sqrt(a)]; the conjugate sum is 2u.
    """
    s = int(a ** 0.5)
    while s * s > a:
        s -= 1
    while (s + 1) * (s + 1) <= a:
        s += 1
    if s * s == a:
        return pow_mod(2 * s, n, MOD)
    c = s + 1
    # (u + v sqrt(a))^n mod MOD
    u, v = 1, 0
    bu, bv = c % MOD, 1
    am = a % MOD
    e = n
    while e > 0:
        if e & 1:
            u, v = (u * bu + v * bv % MOD * am) % MOD, (u * bv + v * bu) % MOD
        bu, bv = (bu * bu + bv * bv % MOD * am) % MOD, 2 * bu * bv % MOD
        e >>= 1
    return (2 * u - 1) % MOD

@numba.njit(cache=True)
def G(n):
    total = 0
    for a in range(1, n + 1):
        total = (total + f(a, a * a)) % MOD
    return total

if __name__ == "__main__":
    assert f(5, 2) == 27
    assert f(5, 5) == 3935
    assert G(1000) == 163861845
    print(G(5_000_000))  # 700792959
