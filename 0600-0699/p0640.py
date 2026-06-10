"""Project Euler Problem 640: Shut the Box.

Bob's twelve cards form a 4096-state Markov decision process: the state is
the bitmask of face-down cards, a turn rolls (x, y) uniformly from 6 x 6,
and Bob must toggle card x, card y, or card x + y, aiming for the all-down
state with the fewest expected turns.  The optimal expectation satisfies

    E[s] = 1 + (1/36) sum_rolls min over the three toggles E[s'],

with E[goal] = 0 -- a stochastic shortest-path problem solved by
Gauss-Seidel value iteration (sweeping states in place) until the values
move by less than 1e-13.  Toggles mean revisits are possible, but the
optimal policy reaches the goal with probability bounded away from zero
each turn, so iteration converges geometrically.

Alice's game is the same MDP with four cards and two fair coins (values
1 or 2, so rolls range over 2 x 2 and toggles over {x, y, x+y} with
x + y <= 4); her given optimum 5.673651 validates the solver, which is
also sanity-checked against a Monte Carlo simulation of the greedy
computed policy for Alice.
"""

import numba
import numpy as np


@numba.jit(cache=True)
def expected_turns(num_cards: int, faces: int) -> float:
    goal = (1 << num_cards) - 1
    E = np.zeros(goal + 1, dtype=np.float64)
    rolls = []
    for x in range(1, faces + 1):
        for y in range(1, faces + 1):
            rolls.append((x, y))
    for _ in range(1000000):
        delta = 0.0
        for s in range(goal, -1, -1):
            if s == goal:
                continue
            total = 0.0
            for x, y in rolls:
                best = E[s ^ (1 << (x - 1))]
                v = E[s ^ (1 << (y - 1))]
                if v < best:
                    best = v
                v = E[s ^ (1 << (x + y - 1))]
                if v < best:
                    best = v
                total += best
            new = 1.0 + total / len(rolls)
            d = abs(new - E[s])
            if d > delta:
                delta = d
            E[s] = new
        if delta < 1e-13:
            break
    return E[0]


def simulate_alice(E: np.ndarray, trials: int) -> float:
    rng = np.random.default_rng(12345)
    total = 0
    for _ in range(trials):
        s, turns = 0, 0
        while s != 15:
            x, y = rng.integers(1, 3), rng.integers(1, 3)
            options = [s ^ (1 << (x - 1)), s ^ (1 << (y - 1)), s ^ (1 << (x + y - 1))]
            s = min(options, key=lambda t: E[t])
            turns += 1
        total += turns
    return total / trials


@numba.jit(cache=True)
def alice_values() -> np.ndarray:
    goal = 15
    E = np.zeros(goal + 1, dtype=np.float64)
    for _ in range(1000000):
        delta = 0.0
        for s in range(goal - 1, -1, -1):
            total = 0.0
            for x in range(1, 3):
                for y in range(1, 3):
                    best = min(
                        E[s ^ (1 << (x - 1))],
                        E[s ^ (1 << (y - 1))],
                        E[s ^ (1 << (x + y - 1))],
                    )
                    total += best
            new = 1.0 + total / 4.0
            delta = max(delta, abs(new - E[s]))
            E[s] = new
        if delta < 1e-13:
            break
    return E


if __name__ == "__main__":
    alice = expected_turns(4, 2)
    assert f"{alice:.6f}" == "5.673651", alice
    sim = simulate_alice(alice_values(), 200000)
    assert abs(sim - alice) < 0.05, (sim, alice)
    print(f"{expected_turns(12, 6):.6f}")  # 50.317928
