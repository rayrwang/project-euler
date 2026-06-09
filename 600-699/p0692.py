"""Project Euler Problem 692: Siegbert and Jo.

This is Fibonacci Nim.  With the Fibonacci numbers F_1=1, F_2=2, F_3=3, F_4=5, ...,
the smallest first move that still guarantees a win, H(N), equals the smallest
Fibonacci number in the Zeckendorf representation of N.  We need G(n) = sum_{k=1}^n
H(k) for n = 23416728348467685.

Let S(n) = sum_{k=1}^n H(k).  If F_m is the largest Fibonacci number <= n, then the
k in [F_m, n] are F_m + r with 0 <= r <= n - F_m < F_{m-1}: for r = 0 the smallest
part is F_m, and for r >= 1 the smallest part of k equals that of r.  Hence

    S(n) = A(m) + F_m + S(n - F_m),   where A(m) = S(F_m - 1),

and A(m) itself satisfies A(m) = A(m-1) + F_{m-1} + A(m-2).  Both recurrences are
O(log n).  Check: G(13) = 43.
"""

import sys


def _fibs(limit: int) -> list[int]:
    F = [1, 2]  # F[0] = F_1 = 1, F[1] = F_2 = 2
    while F[-1] <= limit:
        F.append(F[-1] + F[-2])
    return F


def G(n: int) -> int:
    F = _fibs(n)
    # Aval[m] = S(F_m - 1); A(1) = S(0) = 0, A(2) = S(1) = H(1) = 1.
    Aval = {1: 0, 2: 1}
    for m in range(3, len(F) + 1):
        Aval[m] = Aval[m - 1] + F[m - 2] + Aval[m - 2]  # F_{m-1} = F[m-2]

    def S(x: int) -> int:
        if x <= 0:
            return 0
        m = len(F)
        while F[m - 1] > x:
            m -= 1
        Fm = F[m - 1]
        return Aval[m] + Fm + S(x - Fm)

    return S(n)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    assert G(13) == 43, G(13)
    print(G(23416728348467685))  # 842043391019219959
