def solve(n: int = 50) -> int:
    # Tiles of length 1 (grey), 2, 3, 4 fill a row of n units.
    # f(n) = f(n-1)+f(n-2)+f(n-3)+f(n-4), f(0)=1, f(<0)=0.
    f = [0, 0, 0, 1]  # represents f(-3..0)
    for _ in range(n):
        f = f[1:] + [sum(f)]
    return f[-1]


if __name__ == "__main__":
    print(solve())  # 100808458960497
