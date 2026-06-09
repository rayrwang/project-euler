from collections import defaultdict


def solve(rows: int = 8) -> int:
    # Transfer-matrix DP over the colours of a row's upward triangles. Row k+1 is
    # U0 D0 U1 D1 ... D(k-1) Uk; adjacent triangles differ and each downward Dj
    # also differs from the upward triangle above it. The number of choices for
    # Dj is 3 - |{Uj, U(j+1), above_j}|.
    dp: dict[tuple[int, ...], int] = {(c,): 1 for c in range(3)}
    for k in range(1, rows):
        nxt: dict[tuple[int, ...], int] = defaultdict(int)
        for above, count in dp.items():

            def extend(j: int, new_up: list[int], weight: int,
                       above: tuple[int, ...] = above, count: int = count) -> None:
                if j == k:
                    nxt[tuple(new_up)] += count * weight
                    return
                for nxt_up in range(3):
                    w = 3 - len({new_up[-1], nxt_up, above[j]})
                    if w:
                        extend(j + 1, new_up + [nxt_up], weight * w)

            for first in range(3):
                extend(0, [first], 1)
        dp = nxt
    return sum(dp.values())


if __name__ == "__main__":
    print(solve())  # 10834893628237824
