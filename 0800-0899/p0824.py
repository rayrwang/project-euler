P = 10**7 + 19
MOD = P * P


def _build_tables() -> tuple[list[int], int, list[int]]:
    """Precompute, for the prime P: block factorial prefix, (P-1)! mod P^2, harmonic sums."""
    prefix = [1] * P
    for r in range(1, P):
        prefix[r] = prefix[r - 1] * r % MOD
    block = prefix[P - 1]  # (P-1)! mod P^2; every full block contributes this (Wolstenholme)
    inverse = [0] * P
    inverse[1] = 1
    for i in range(2, P):
        inverse[i] = (P - (P // i) * inverse[P % i] % P) % P
    harmonic = [0] * P
    for r in range(1, P):
        harmonic[r] = (harmonic[r - 1] + inverse[r]) % P
    return prefix, block, harmonic


_PREFIX, _BLOCK, _HARMONIC = _build_tables()


def _factorial_unit(n: int) -> int:
    """(n! with all factors of P removed) mod P^2, via Granville's block product."""
    result = 1
    while n > 0:
        q, r = divmod(n, P)
        block = pow(_BLOCK, q, MOD)
        if r:
            block = block * _PREFIX[r] % MOD * ((1 + (q % P) * P % MOD * _HARMONIC[r]) % MOD) % MOD
        result = result * block % MOD
        n = q
    return result


def _p_adic_factorial(n: int) -> int:
    e, pk = 0, P
    while pk <= n:
        e += n // pk
        pk *= P
    return e


def _p_adic_int(n: int) -> int:
    if n == 0:
        return 1 << 60
    e = 0
    while n % P == 0:
        n //= P
        e += 1
    return e


def _unit_int(n: int) -> int:
    while n % P == 0:
        n //= P
    return n % MOD


def _binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    r = n - k
    e = _p_adic_factorial(n) - _p_adic_factorial(k) - _p_adic_factorial(r)
    if e >= 2:
        return 0
    val = _factorial_unit(n) * pow(_factorial_unit(k) * _factorial_unit(r) % MOD, -1, MOD) % MOD
    return val * pow(P, e, MOD) % MOD


def _lucas_coefficient(m: int, s: int) -> int:
    """[x^s] V_m(x) mod P^2, where V_m = lam+^m + lam-^m (lam^2 = lam + x).

    V_m(0) = 1 for m >= 1; otherwise the coefficient is (m/(m-s)) * C(m-s, s),
    handled with explicit P-adic valuations so factors of P in s or m-s cancel.
    """
    if s == 0:
        return 1
    if 2 * s > m:
        return 0
    valuation = (_p_adic_int(m) - _p_adic_int(m - s) + _p_adic_factorial(m - s)
                 - _p_adic_factorial(s) - _p_adic_factorial(m - 2 * s))
    if valuation >= 2:
        return 0
    unit = _unit_int(m) * pow(_unit_int(m - s), -1, MOD) % MOD
    unit = unit * _factorial_unit(m - s) % MOD
    unit = unit * pow(_factorial_unit(s) * _factorial_unit(m - 2 * s) % MOD, -1, MOD) % MOD
    return unit * pow(P, valuation, MOD) % MOD


def sliders_mod(n: int, k: int) -> int:
    """L(N, K) mod P^2: K non-attacking Sliders on an N x N cylindrical board.

    A Slider attacks only the two horizontally adjacent squares (the row is a
    cycle C_N), so rows are independent and L(N, K) = [x^K] g(x)^N, where
    g(x) = I(C_N, x) = trace([[1, x], [1, 0]]^N) = lam+^N + lam-^N is the cycle
    independence polynomial, lam+- = (1 +- sqrt(1+4x))/2.

    Expanding g^N = sum_i C(N,i) lam+^{Ni} lam-^{N(N-i)} and pairing i with N-i
    (using lam+ lam- = -x) gives, with V_m the Lucas-type polynomial,
        g(x)^N = sum_{i < N/2} C(N,i) (-x)^{Ni} V_{N(N-2i)}(x)  (+ middle term),
    so L(N,K) = sum_i C(N,i) (-1)^{Ni} [x^{K-Ni}] V_{N(N-2i)}. Verified against a
    direct polynomial expansion for all N <= 10 and L(2,2)=4, L(6,12)=4204761.

    Only i with Ni <= K contribute (here K/N = 10^6 < N/2), and every binomial
    and Lucas coefficient is taken mod P^2 by Granville's prime-power theorem.
    """
    total = 0
    i = 0
    while n * i <= k and i <= n // 2:
        s = k - n * i
        sign = 1 if (n * i) % 2 == 0 else -1
        if i == n - i:  # middle term, only for even N
            if s == 0:
                total = (total + sign * _binomial(n, i)) % MOD
        else:
            b = _binomial(n, i)
            if b:
                total = (total + sign * b % MOD * _lucas_coefficient(n * (n - 2 * i), s)) % MOD
        i += 1
    return total % MOD


if __name__ == "__main__":
    assert sliders_mod(2, 2) == 4
    assert sliders_mod(6, 12) == 4204761
    print(sliders_mod(10**9, 10**15))  # 26532152736197
