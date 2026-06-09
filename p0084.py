import numba
import numpy as np

@numba.jit(cache=True)
def simulate(turns, sides):
    np.random.seed(1)
    counts = np.zeros(40, dtype=np.int64)
    pos = 0
    doubles = 0
    for _ in range(turns):
        d1 = np.random.randint(1, sides + 1)
        d2 = np.random.randint(1, sides + 1)
        doubles = doubles + 1 if d1 == d2 else 0
        if doubles == 3:                       # three doubles in a row -> jail
            pos = 10
            doubles = 0
            counts[pos] += 1
            continue
        pos = (pos + d1 + d2) % 40
        if pos == 30:                          # Go To Jail
            pos = 10
        elif pos == 2 or pos == 17 or pos == 33:   # Community Chest
            c = np.random.randint(0, 16)
            if c == 0:
                pos = 0
            elif c == 1:
                pos = 10
        elif pos == 7 or pos == 22 or pos == 36:    # Chance
            c = np.random.randint(0, 16)
            if c == 0:
                pos = 0
            elif c == 1:
                pos = 10
            elif c == 2:
                pos = 11
            elif c == 3:
                pos = 24
            elif c == 4:
                pos = 39
            elif c == 5:
                pos = 5
            elif c == 6 or c == 7:             # next railway
                pos = 15 if pos == 7 else (25 if pos == 22 else 5)
            elif c == 8:                       # next utility
                pos = 28 if pos == 22 else 12
            elif c == 9:                       # go back three
                pos = (pos - 3) % 40
                if pos == 33:                  # landed on Community Chest
                    c2 = np.random.randint(0, 16)
                    if c2 == 0:
                        pos = 0
                    elif c2 == 1:
                        pos = 10
        counts[pos] += 1
    return counts

if __name__ == "__main__":
    counts = simulate(20_000_000, 4)
    top3 = np.argsort(counts)[::-1][:3]
    print("".join(f"{int(s):02d}" for s in top3))  # 101524
