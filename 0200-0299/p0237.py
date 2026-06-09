# T(n) counts Hamiltonian paths on a 4 x n grid from the top-left to the
# bottom-left corner. Brute-force DFS for n = 1..11 gives
# 1, 1, 4, 8, 23, 55, 144, 360, 921, 2329, 5924 (T(10) = 2329 as stated), and
# fitting a minimal linear recurrence yields the order-4 relation
#     T(n) = 2 T(n-1) + 2 T(n-2) - 2 T(n-3) + T(n-4),
# which all of the held-out brute-force terms confirm. (A column-by-column
# transfer-matrix argument guarantees some fixed-order recurrence exists, so
# matching every available term pins this one down.) Then T(10^12) mod 10^8
# falls to 4x4 matrix exponentiation.

_MOD = 10**8


def _mat_mul(x: list[list[int]], y: list[list[int]]) -> list[list[int]]:
    return [
        [sum(x[i][k] * y[k][j] for k in range(4)) % _MOD for j in range(4)]
        for i in range(4)
    ]


def solve(n: int = 10**12) -> int:
    base = [1, 1, 4, 8]  # T(1)..T(4)
    if n <= 4:
        return base[n - 1]
    m = [[2, 2, -2, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    result = [[int(i == j) for j in range(4)] for i in range(4)]
    e = n - 4
    while e:
        if e & 1:
            result = _mat_mul(result, m)
        m = _mat_mul(m, m)
        e >>= 1
    state = [base[3], base[2], base[1], base[0]]  # T(4), T(3), T(2), T(1)
    return sum(result[0][j] * state[j] for j in range(4)) % _MOD


if __name__ == "__main__":
    print(solve())  # 15836928
