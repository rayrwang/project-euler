MOD = 10**8


def power_sum(n: int, k: int, mod: int) -> int:
    """S_k = a^k + b^k + c^k mod `mod` for the roots of x^3 - 2^n x^2 + n.

    The power sums satisfy S_k = 2^n S_{k-1} - n S_{k-3} (multiply the
    polynomial relation x^3 = 2^n x^2 - n by x^{k-3} and sum over roots),
    with S_0 = 3, S_1 = 2^n and S_2 = 4^n (from e_1 = 2^n, e_2 = 0).
    Evaluate with a 3x3 matrix power in O(log k).
    """
    t = pow(2, n, mod)

    def mat_mul(x: list[list[int]], y: list[list[int]]) -> list[list[int]]:
        return [
            [sum(x[i][m] * y[m][j] for m in range(3)) % mod for j in range(3)]
            for i in range(3)
        ]

    m = [[t, 0, -n % mod], [1, 0, 0], [0, 1, 0]]
    result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    e = k
    while e:
        if e & 1:
            result = mat_mul(result, m)
        m = mat_mul(m, m)
        e >>= 1
    s2, s1, s0 = pow(4, n, mod), t, 3
    # m advances the window (S_j, S_{j-1}, S_{j-2}) by one, so m^k sends
    # (S_2, S_1, S_0) to (S_{k+2}, S_{k+1}, S_k); the last row yields S_k.
    return (result[2][0] * s2 + result[2][1] * s1 + result[2][2] * s0) % mod


def solve(n_max: int, k: int) -> int:
    """Last eight digits of sum of floor(a_n^k) for odd k.

    Beyond the dominant root a (close to 2^n), the cubic has a root b in
    (0, 1) and a root c in (-1, 0): with x0 = sqrt(n / 2^n), the polynomial
    is positive at 0 and x0 and negative at -x0 and 1. Hence b > x0 > |c|,
    so for odd k the tail t = b^k + c^k lies strictly in (0, 1) and
    floor(a^k) = S_k - t's integer part correction = S_k - 1.
    """
    return sum(power_sum(n, k, MOD) - 1 for n in range(1, n_max + 1)) % MOD


if __name__ == "__main__":
    # Verify floor(a_n^k) = S_k - 1 numerically for small odd powers.
    import numpy as np

    for n in range(1, 6):
        a = max(np.roots([1, -(2**n), 0, n]).real)
        for k in (3, 5, 7):
            assert int(a**k) == power_sum(n, k, 10**15) - 1, (n, k)
    print(solve(30, 987654321))  # 28010159
