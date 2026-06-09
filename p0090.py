from itertools import combinations

SQUARES = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

def shows(cube, d):
    # A 6 can be flipped to a 9 and vice versa.
    if d in (6, 9):
        return 6 in cube or 9 in cube
    return d in cube

def valid(c1, c2):
    return all(
        (shows(c1, a) and shows(c2, b)) or (shows(c1, b) and shows(c2, a))
        for a, b in SQUARES
    )

if __name__ == "__main__":
    cubes = [frozenset(c) for c in combinations(range(10), 6)]
    count = 0
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):     # unordered pairs of cube configurations
            if valid(cubes[i], cubes[j]):
                count += 1
    print(count)  # 1217
