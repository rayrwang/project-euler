import numba
import numpy as np

_GUESSES = [
    ("5616185650518293", 2), ("3847439647293047", 1), ("5855462940810587", 3),
    ("9742855507068353", 3), ("4296849643607543", 3), ("3174248439465858", 1),
    ("4513559094146117", 2), ("7890971548908067", 3), ("8157356344118483", 1),
    ("2615250744386899", 2), ("8690095851526254", 3), ("6375711915077050", 1),
    ("6913859173121360", 1), ("6442889055042768", 2), ("2321386104303845", 0),
    ("2326509471271448", 2), ("5251583379644322", 2), ("1748270476758276", 3),
    ("4895722652190306", 1), ("3041631117224635", 3), ("1841236454324589", 3),
    ("2659862637316867", 2),
]


@numba.njit(cache=True)
def _error(state: np.ndarray, guess: np.ndarray, correct: np.ndarray) -> int:
    total = 0
    for i in range(guess.shape[0]):
        m = 0
        for p in range(guess.shape[1]):
            if state[p] == guess[i, p]:
                m += 1
        total += abs(m - correct[i])
    return total


@numba.njit(cache=True)
def _search(guess: np.ndarray, correct: np.ndarray, seed: int) -> np.ndarray:
    # Steepest-descent local search with random restarts: minimise the total
    # deviation between achieved and required match counts until it reaches 0.
    np.random.seed(seed)
    length = guess.shape[1]
    while True:
        state = np.random.randint(0, 10, length)
        err = _error(state, guess, correct)
        while err != 0:
            best_gain, bp, bd = 0, -1, -1
            for p in range(length):
                old = state[p]
                for d in range(10):
                    if d != old:
                        state[p] = d
                        gain = err - _error(state, guess, correct)
                        if gain > best_gain:
                            best_gain, bp, bd = gain, p, d
                state[p] = old
            if bp == -1:
                break  # local minimum: restart
            state[bp] = bd
            err -= best_gain
        if err == 0:
            return state


def solve() -> int:
    guess = np.array([[int(c) for c in g] for g, _ in _GUESSES], dtype=np.int64)
    correct = np.array([n for _, n in _GUESSES], dtype=np.int64)
    state = _search(guess, correct, 12345)
    return int("".join(str(int(x)) for x in state))


if __name__ == "__main__":
    print(solve())  # 4640261571849533
