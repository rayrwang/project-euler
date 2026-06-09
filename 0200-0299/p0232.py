def solve(target: int = 100) -> str:
    # State (a, b): Player 1 still needs a points, Player 2 needs b.
    # f[a][b] = P(Player 2 wins) with Player 1 about to toss,
    # g[a][b] = the same with Player 2 about to toss.
    # Player 1 scores 1 with probability 1/2, so
    #     f(a,b) = (A + g(a,b)) / 2,  A = g(a-1,b) if a > 1 else 0.
    # Player 2 picks T tosses, succeeding with q = 2^-T for s = 2^(T-1) points:
    #     g(a,b) = max_T [ q W_T + (1-q) f(a,b) ],
    # where W_T = 1 if s >= b else f(a, b-s). Both equations reference the
    # current state (Player 1's tails / Player 2's failure loop back), so for
    # each candidate T solve the 2x2 fixed point in closed form:
    #     y = (q W_T + (1-q) A/2) / (1 - (1-q)/2),
    # and take the best y over T. States are filled with a, then b, ascending,
    # so A and the W_T are always already known. T beyond the first s >= b
    # only lowers q, so the search stops there.
    n = target
    f = [[0.0] * (n + 1) for _ in range(n + 1)]
    g = [[0.0] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            carry = g[a - 1][b] if a > 1 else 0.0
            best = 0.0
            t = 1
            while True:
                s = 1 << (t - 1)
                q = 0.5**t
                w = 1.0 if s >= b else f[a][b - s]
                y = (q * w + (1 - q) * carry / 2) / (1 - (1 - q) / 2)
                best = max(best, y)
                if s >= b:
                    break
                t += 1
            g[a][b] = best
            f[a][b] = (carry + best) / 2
    return f"{f[n][n]:.8f}"


if __name__ == "__main__":
    print(solve())  # 0.83648556
