_RULE = {"a": "aRbFR", "b": "LFaLb"}
_DX = (1, 0, -1, 0)
_DY = (0, 1, 0, -1)  # directions E, N, W, S; 'L' turns +1 (CCW), 'R' turns -1


def _rotate(x: int, y: int, d: int) -> tuple[int, int]:
    if d == 0:
        return x, y
    if d == 1:
        return -y, x
    if d == 2:
        return -x, -y
    return y, -x


def _build(depth: int):
    # For each symbol/level, the F-step count and the net (dx, dy, turn) when
    # the block is entered facing East, so a whole block can be skipped at once.
    count = {"a": [0] * (depth + 1), "b": [0] * (depth + 1)}
    trans = {"a": [(0, 0, 0)] * (depth + 1), "b": [(0, 0, 0)] * (depth + 1)}
    for level in range(1, depth + 1):
        for sym in ("a", "b"):
            x = y = d = c = 0
            for ch in _RULE[sym]:
                if ch == "F":
                    x += _DX[d]
                    y += _DY[d]
                    c += 1
                elif ch == "L":
                    d = (d + 1) % 4
                elif ch == "R":
                    d = (d - 1) % 4
                else:
                    ex, ey, ed = trans[ch][level - 1]
                    rx, ry = _rotate(ex, ey, d)
                    x += rx
                    y += ry
                    d = (d + ed) % 4
                    c += count[ch][level - 1]
            count[sym][level] = c
            trans[sym][level] = (x, y, d)
    return count, trans


def solve(steps: int = 10**12, depth: int = 50) -> str:
    count, trans = _build(depth)
    state = {"x": 0, "y": 0, "d": 1, "rem": steps}  # start facing North

    def apply_block(sym: str, level: int) -> None:
        ex, ey, ed = trans[sym][level]
        rx, ry = _rotate(ex, ey, state["d"])
        state["x"] += rx
        state["y"] += ry
        state["d"] = (state["d"] + ed) % 4
        state["rem"] -= count[sym][level]

    def walk(sym: str, level: int) -> None:
        if state["rem"] <= 0 or level == 0:
            return
        for ch in _RULE[sym]:
            if state["rem"] <= 0:
                return
            if ch == "F":
                state["x"] += _DX[state["d"]]
                state["y"] += _DY[state["d"]]
                state["rem"] -= 1
            elif ch == "L":
                state["d"] = (state["d"] + 1) % 4
            elif ch == "R":
                state["d"] = (state["d"] - 1) % 4
            elif count[ch][level - 1] <= state["rem"]:
                apply_block(ch, level - 1)
            else:
                walk(ch, level - 1)

    walk("a", depth)
    return f"{state['x']},{state['y']}"


if __name__ == "__main__":
    print(solve())  # 139776,963904
