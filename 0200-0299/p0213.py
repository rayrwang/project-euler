import numpy as np


def solve(side: int = 30, turns: int = 50) -> float:
    # Each flea does an independent random walk; flea starting at s sits at cell c
    # after `turns` with probability (T^turns)[s, c]. Expected number of empty
    # squares = sum over cells c of product over starting cells s of (1 - that prob).
    n = side * side
    trans = np.zeros((n, n))
    for r in range(side):
        for c in range(side):
            i = r * side + c
            nb = []
            if r > 0:
                nb.append((r - 1) * side + c)
            if r < side - 1:
                nb.append((r + 1) * side + c)
            if c > 0:
                nb.append(r * side + c - 1)
            if c < side - 1:
                nb.append(r * side + c + 1)
            for j in nb:
                trans[i, j] = 1.0 / len(nb)

    power = np.eye(n)
    base = trans
    e = turns
    while e:
        if e & 1:
            power = power @ base
        base = base @ base
        e >>= 1
    return round(float(np.prod(1.0 - power, axis=0).sum()), 6)


if __name__ == "__main__":
    print(solve())  # 330.721154
