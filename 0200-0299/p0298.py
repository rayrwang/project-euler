from collections import defaultdict

import numpy as np

# Only the relationship between the two memories matters, not the actual
# numbers: Larry's memory is an LRU queue of slots 1..nL (1 = most recent)
# and Robin's a FIFO tuple whose symbols are either Larry slots ('L', i) or
# canonically-relabelled outside markers ('O', j). Called numbers fall into
# four cases - a Larry element that is/isn't in Robin's memory, a
# Robin-only element, or a fresh number (there are exactly
# 10 - nL - |Robin| + shared of those) - each with probability 1/10 per
# specific element. The score difference D rides along as a distribution
# vector per canonical state (438 reachable states), shifted by +-1 on
# one-sided hits, and E|L - R| is read off after 50 turns. Cross-checked
# by Monte Carlo simulation.


def solve(turns: int = 50) -> str:
    nd = 2 * turns + 1
    off = turns

    def canon(robin: tuple) -> tuple:
        mp: dict = {}
        out = []
        for sym in robin:
            if sym[0] == "O":
                if sym not in mp:
                    mp[sym] = ("O", len(mp))
                out.append(mp[sym])
            else:
                out.append(sym)
        return tuple(out)

    states: dict = {(0, ()): np.zeros(nd)}
    states[(0, ())][off] = 1.0
    p = 0.1
    for _turn in range(turns):
        new: dict = defaultdict(lambda: np.zeros(nd))
        for (n_l, robin), vec in states.items():
            shared = sum(1 for sym in robin if sym[0] == "L")
            fresh = 10 - (n_l + len(robin) - shared)
            for i in range(1, n_l + 1):
                nrobin = tuple(
                    ("L", 1 if s[1] == i else (s[1] + 1 if s[1] < i else s[1]))
                    if s[0] == "L"
                    else s
                    for s in robin
                )
                if ("L", i) in robin:
                    new[(n_l, canon(nrobin))] += p * vec
                else:
                    if len(nrobin) == 5:
                        nrobin = nrobin[1:] + (("L", 1),)
                    else:
                        nrobin = nrobin + (("L", 1),)
                    shifted = np.zeros(nd)
                    shifted[1:] = vec[:-1]
                    new[(n_l, canon(nrobin))] += p * shifted
            for sym in robin:
                if sym[0] != "O":
                    continue

                def conv(x: tuple, called: tuple = sym) -> tuple:
                    if x == called:
                        return ("L", 1)
                    if x[0] == "L":
                        if n_l == 5 and x[1] == 5:
                            return ("O", ("ev",))
                        return ("L", x[1] + 1)
                    return x

                nrobin = tuple(conv(x) for x in robin)
                nn_l = 5 if n_l == 5 else n_l + 1
                shifted = np.zeros(nd)
                shifted[:-1] = vec[1:]
                new[(nn_l, canon(nrobin))] += p * shifted
            if fresh > 0:

                def conv2(x: tuple) -> tuple:
                    if x[0] == "L":
                        if n_l == 5 and x[1] == 5:
                            return ("O", ("ev2",))
                        return ("L", x[1] + 1)
                    return x

                nrobin = tuple(conv2(x) for x in robin)
                nn_l = 5 if n_l == 5 else n_l + 1
                if len(nrobin) == 5:
                    nrobin = nrobin[1:] + (("L", 1),)
                else:
                    nrobin = nrobin + (("L", 1),)
                new[(nn_l, canon(nrobin))] += (p * fresh) * vec
        states = new
    total = np.zeros(nd)
    for vec in states.values():
        total += vec
    expectation = sum(abs(d - off) * total[d] for d in range(nd))
    return f"{expectation:.8f}"


if __name__ == "__main__":
    print(solve())  # 1.76882294
