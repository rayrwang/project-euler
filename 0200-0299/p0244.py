from collections import defaultdict, deque

# The 4x4 board has C(15, 7) * 16 = 102960 states (empty cell plus a
# red/blue colouring), so plain BFS suffices. Move letters name the direction
# the tile slides (the empty square moves opposite). The checksum is
# mod-reduced after each move, but since the final answer is the sum of all
# shortest-path checksums modulo 100000007, a layered DP over the
# shortest-path DAG with all arithmetic mod p is exact: carry (number of
# shortest paths, sum of their checksums) per state. The LULUR example
# reproduces checksum 19761398.

_MOD = 100_000_007
_START = ".RBBRRBBRRBBRRBB"
_TARGET = ".BRBBRBRRBRBBRBR"


def _apply(state: str, letter: str) -> str | None:
    e = state.index(".")
    r, c = divmod(e, 4)
    if letter == "L":  # tile right of the empty square slides left
        t, ok = e + 1, c < 3
    elif letter == "R":
        t, ok = e - 1, c > 0
    elif letter == "U":  # tile below slides up
        t, ok = e + 4, r < 3
    else:
        t, ok = e - 4, r > 0
    if not ok:
        return None
    cells = list(state)
    cells[e], cells[t] = cells[t], "."
    return "".join(cells)


def _bfs(start: str) -> dict[str, int]:
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for ch in "LRUD":
            v = _apply(u, ch)
            if v is not None and v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def solve() -> int:
    dist_s = _bfs(_START)
    dist_t = _bfs(_TARGET)
    total = dist_s[_TARGET]

    def on_path(u: str) -> bool:
        return dist_s[u] + dist_t[u] == total

    layers: dict[int, list[str]] = defaultdict(list)
    for u, d in dist_s.items():
        if u in dist_t and on_path(u):
            layers[d].append(u)
    count: dict[str, int] = defaultdict(int)
    chk: dict[str, int] = defaultdict(int)
    count[_START] = 1
    for d in range(total):
        for u in layers[d]:
            if count[u] == 0:
                continue
            for ch in "LRUD":
                v = _apply(u, ch)
                if v is not None and dist_s.get(v) == d + 1 and on_path(v):
                    count[v] = (count[v] + count[u]) % _MOD
                    chk[v] = (chk[v] + chk[u] * 243 + count[u] * ord(ch)) % _MOD
    return chk[_TARGET]


if __name__ == "__main__":
    print(solve())  # 96356848
