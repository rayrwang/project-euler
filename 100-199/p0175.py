def _quotients(x: int, y: int) -> list[int]:
    # Continued-fraction (Euclidean) quotients of x/y; these are the run lengths
    # of the binary expansion of n where f(n)/f(n-1) = x/y.
    res = []
    while y:
        q, x, y = x // y, y, x % y
        res.append(q)
    return res


def solve(p: int = 123456789, q: int = 987654321) -> str:
    # Shortened binary expansion of the smallest n with f(n)/f(n-1) = p/q.
    k = _quotients(p, q)
    if len(k) % 2 == 1:          # make the parity match a run starting on 1s
        k = k[:-1] + [k[-1] - 1, 1]
    runs = [v for v in k if v != 0][::-1]
    return ",".join(map(str, runs))


if __name__ == "__main__":
    print(solve())  # 1,13717420,8
