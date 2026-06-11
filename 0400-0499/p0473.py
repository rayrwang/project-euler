"""Project Euler 473: Phigital Number Base.

Every positive integer has a unique finite base-phi representation with no
two consecutive 1s. For the digit string (with the phigital point) to be a
palindrome, the point must be the central character, so the digits pair up:
phi^j is used exactly when phi^(-j-1) is, for j ranging over a set S of
non-consecutive positive integers (0 in S would use exponents 0 and -1,
which are consecutive). The single exception is 1 = "1".

In the basis (1, sqrt5)/2, each pair contributes
    2 * (phi^j + phi^(-j-1)) = a_j + b_j sqrt5,
    even j: a_j = -L_(j-1), b_j = +F_(j+2)
    odd  j: a_j = +L_(j+2), b_j = -F_(j-1)
(L Lucas, F Fibonacci). The total is an integer n exactly when the b sum
vanishes, and then n = (sum of a)/2. A DFS over exponents from large to
small prunes on the achievable range of the b sum and on the real value.
"""

from math import sqrt

N = 10**10
SQRT5 = sqrt(5)

FIB = [0, 1]
LUC = [2, 1]
for _ in range(80):
    FIB.append(FIB[-1] + FIB[-2])
    LUC.append(LUC[-1] + LUC[-2])

def pair(j: int) -> tuple[float, int, int]:
    """(real value, a_j, b_j) of the digit pair phi^j + phi^(-j-1)."""
    if j % 2 == 0:
        a, b = -LUC[j - 1], FIB[j + 2]
    else:
        a, b = LUC[j + 2], -FIB[j - 1]
    return (a + b * SQRT5) / 2, a, b

def solve() -> int:
    top = 1
    while pair(top + 1)[0] <= N:
        top += 1
    # bounds on the b sum over exponents <= j (adjacency ignored: still valid)
    pos = [0] * (top + 1)
    neg = [0] * (top + 1)
    for j in range(1, top + 1):
        _, _, b = pair(j)
        pos[j] = pos[j - 1] + max(b, 0)
        neg[j] = neg[j - 1] + min(b, 0)

    results = {1}

    def dfs(j: int, a_sum: int, b_sum: int, val: float) -> None:
        if b_sum == 0 and a_sum > 0:
            assert a_sum % 2 == 0
            results.add(a_sum // 2)
        if j < 1 or b_sum + neg[j] > 0 or b_sum + pos[j] < 0:
            return
        dfs(j - 1, a_sum, b_sum, val)  # skip exponent j
        vy, a, b = pair(j)
        if val + vy <= N + 0.5:  # taking j (then j-1 is excluded)
            dfs(j - 2, a_sum + a, b_sum + b, val + vy)

    dfs(top, 0, 0, 0.0)
    assert sum(r for r in results if r <= 1000) == 4345
    return sum(r for r in results if r <= N)

if __name__ == "__main__":
    print(solve())  # 35856681704365
