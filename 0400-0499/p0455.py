MOD = 10**9
LAM = 5 * 10**7  # Carmichael lambda(10^9) = lcm(2^7, 4 * 5^8)

def f(n: int) -> int:
    """Largest 0 < x < 10^9 with n^x ending in the 9 digits of x.

    Equivalently the largest solution of n^x = x (mod 10^9). For n a
    multiple of 10 there is none. Otherwise iterating x -> n^x (mod 10^9)
    converges to the value of the power tower n^n^... mod 10^9, the unique
    large fixed point: the result depends on the starting x only through
    the chain lambda(10^9), lambda(lambda(10^9)), ... which collapses to 1.
    The exponent is lifted by lambda so it stays large enough to saturate
    the prime powers 2^9 and 5^9 shared with the modulus.
    """
    if n % 10 == 0:
        return 0
    x = 1
    for _ in range(60):
        new = pow(n, LAM + x % LAM, MOD)
        if new == x:
            break
        x = new
    else:
        raise AssertionError(f"no convergence for {n}")
    assert pow(n, LAM + x % LAM, MOD) == x
    return x

if __name__ == "__main__":
    assert f(4) == 411728896
    assert f(10) == 0
    assert f(157) == 743757
    assert sum(f(n) for n in range(2, 10**3 + 1)) == 442530011399
    print(sum(f(n) for n in range(2, 10**6 + 1)))  # 450186511399999
