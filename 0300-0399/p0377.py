import numpy as np

MOD = 10**9


def mat_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    # int64 entries < 10^9 -> products < 10^18, summed over 18 terms via
    # object dtype would overflow int64; use Python ints through object.
    return (a @ b) % MOD


def f(n: int) -> int:
    """Sum (mod 10^9) of zero-free positive integers with digit sum n.

    With c(n) the count and f(n) the sum of such integers, appending a final
    digit d in 1..9 to every integer of digit sum n - d (or to nothing,
    via c(0) = 1) gives
        c(n) = sum_{d=1}^{9} c(n - d),
        f(n) = sum_{d=1}^{9} (10 f(n - d) + d c(n - d)).
    Encode the last nine values of f and c in a vector and raise the 18x18
    transition matrix to the n-th power.
    """
    m = np.zeros((18, 18), dtype=object)
    # State: [f(k-1), ..., f(k-9), c(k-1), ..., c(k-9)]
    for d in range(1, 10):
        m[0, d - 1] = 10  # f(k) += 10 f(k-d)
        m[0, 9 + d - 1] = d  # f(k) += d c(k-d)
        m[9, 9 + d - 1] = 1  # c(k) += c(k-d)
    for r in range(1, 9):
        m[r, r - 1] = 1
        m[9 + r, 9 + r - 1] = 1

    # Start at k = 1: f(0) = 0, c(0) = 1, negative indices empty.
    vec = np.zeros(18, dtype=object)
    vec[9] = 1
    power = n
    while power:
        if power & 1:
            vec = mat_mul(m, vec)
        m = mat_mul(m, m)
        power >>= 1
    return int(vec[0]) % MOD  # after n steps, vec[0] = f(n)


if __name__ == "__main__":
    assert f(5) == 17891
    print(sum(f(13**i) for i in range(1, 18)) % MOD)  # 732385277
