# Each 72-degree arc has a displacement that is an integer combination of four
# irrational basis terms (two for x, two for y); the robot returns to its start
# exactly when all four integer coordinates are zero. State = (facing direction,
# the four coordinates). Anticlockwise move when facing direction d adds the
# table entry; a clockwise move negates the x-part and the direction index.
_ACW = ((0, -1, 0, 1), (-1, 0, 1, -1), (0, 0, -2, 0), (1, 0, 1, -1), (0, 1, 0, 1))


def solve(arcs: int = 70) -> int:
    def move(state: tuple[int, int, int, int, int], sign: int):
        e = _ACW[state[0] * sign % 5]
        return (
            (state[0] + sign) % 5,
            state[1] + e[0] * sign,
            state[2] + e[1] * sign,
            state[3] + e[2],
            state[4] + e[3],
        )

    reach = {(0, 0, 0, 0, 0): 1}
    for _ in range(arcs):
        nxt: dict[tuple[int, int, int, int, int], int] = {}
        for state, ways in reach.items():
            for sign in (1, -1):
                ns = move(state, sign)
                nxt[ns] = nxt.get(ns, 0) + ways
        reach = nxt
    return sum(reach.get((d, 0, 0, 0, 0), 0) for d in range(5))


if __name__ == "__main__":
    print(solve())  # 331951449665644800
