import numpy as np

J = 40  # number of power sums tracked
L = 5  # digit lengths handled exactly


def allowed(n: int) -> bool:
    s = str(n)
    return all(not (s[i] == s[i + 1] == s[i + 2]) for i in range(len(s) - 2))


def series_sum() -> np.longdouble:
    """Baillie-style summation of sum 1/n over allowed n.

    Track, per digit length k and state (last digit, last two digits equal),
    the power sums S[state][j] = sum n^(-j) over allowed k-digit n.
    Appending digit d maps n to 10 n + d, forbidden only when the state has
    a doubled last digit equal to d, and
        (10 n + d)^(-j) = sum_i binom(j+i-1, i) (-d)^i (10 n)^(-(j+i)),
    so the new power sums are linear images of the old ones.  Lengths up to
    L are summed exactly, making the expansion ratio d / (10 n) < 10^(-L)
    and the truncation error utterly negligible.
    """
    ld = np.longdouble
    total = ld(0)
    s = np.zeros((10, 2, J + 1), dtype=np.longdouble)  # state power sums
    for n in range(1, 10**L):
        if not allowed(n):
            continue
        total += 1 / ld(n)
        if n >= 10 ** (L - 1):
            digits = str(n)
            eq2 = 1 if len(digits) >= 2 and digits[-1] == digits[-2] else 0
            s[int(digits[-1]), eq2] += 1 / ld(n) ** np.arange(J + 1)

    # Transition matrices: m[d][j, jj] maps old power jj to new power j.
    m = np.zeros((10, J + 1, J + 1), dtype=np.longdouble)
    for d in range(10):
        for j in range(1, J + 1):
            coef = ld(1)
            for jj in range(j, J + 1):
                i = jj - j
                if i > 0:
                    coef *= -d * ld(jj - 1) / i
                m[d, j, jj] = coef / ld(10) ** jj

    while True:
        new = np.zeros_like(s)
        for last in range(10):
            for eq2 in range(2):
                src = s[last, eq2]
                if not src.any():
                    continue
                for d in range(10):
                    if eq2 and d == last:
                        continue  # would create three equal digits
                    new[d, 1 if d == last else 0] += m[d] @ src
        s = new
        added = s[:, :, 1].sum()
        total += added
        if added < 1e-16:
            break
    return total


if __name__ == "__main__":
    print(f"{series_sum():.10f}")  # 253.6135092068
