"""Project Euler 481: Chef Showdown.

n chefs take turns in cyclic number order; on a turn the chef's dish is rated
favorably with probability S(k) = F_k / F_(n+1), in which case the chef must
eliminate one other chef of their choosing. The last chef wins; everyone plays
to maximize their own winning probability, breaking ties among equally good
victims by choosing the one with the next-closest turn. E(n) is the expected
number of dishes cooked; find E(14).

State = (set of remaining chefs, whose turn). When chef c succeeds they pick
the victim v maximizing their own winning probability in the resulting state -
which involves only smaller subsets, so processing subsets in increasing size
makes every elimination choice immediate. Within a fixed subset the failure
transitions form a cycle (turn passes to the next chef), so the win-vector and
expected-dish equations W_i = a_i + b_i W_(i+1 mod m) (with a_i the success
part, b_i = 1 - S) are solved exactly by unrolling once around the loop:
W_0 = (sum_j (prod_(l<j) b_l) a_j) / (1 - prod b), then back-substitution.
"""

import numpy as np

EPS = 1e-12


def solve(n):
    fib = [0, 1, 1]
    while len(fib) < n + 2:
        fib.append(fib[-1] + fib[-2])
    skill = np.array([fib[k + 1] / fib[n + 1] for k in range(n)])

    size = 1 << n
    big_w = np.zeros((size, n, n))  # big_w[mask, current, k] = P(chef k wins)
    big_e = np.zeros((size, n))  # expected dishes still to be cooked

    for mask in sorted(range(1, size), key=lambda v: v.bit_count()):
        chefs = [i for i in range(n) if mask >> i & 1]
        m = len(chefs)
        if m == 1:
            big_w[mask, chefs[0], chefs[0]] = 1.0
            continue
        a = np.zeros((m, n))
        ae = np.zeros(m)
        b = np.zeros(m)
        for i, c in enumerate(chefs):
            s = skill[c]
            best = -1.0
            bw, be = None, 0.0
            for d in range(1, m):  # victims in next-closest-turn order
                v = chefs[(i + d) % m]
                child = mask ^ (1 << v)
                for e in range(1, m + 1):  # successor of c in the child set
                    succ = chefs[(i + e) % m]  # wraps to c itself when m == 2
                    if succ != v:
                        break
                val = big_w[child, succ, c]
                if val > best + EPS:
                    best = val
                    bw = big_w[child, succ]
                    be = big_e[child, succ]
            a[i] = s * bw
            ae[i] = 1.0 + s * be
            b[i] = 1.0 - s
        # unroll the failure cycle once to get position 0, then back-substitute
        acc_w = np.zeros(n)
        acc_e = 0.0
        coeff = 1.0
        for j in range(m):
            acc_w += coeff * a[j]
            acc_e += coeff * ae[j]
            coeff *= b[j]
        wv = np.zeros((m, n))
        ev = np.zeros(m)
        wv[0] = acc_w / (1.0 - coeff)
        ev[0] = acc_e / (1.0 - coeff)
        for j in range(m - 1, 0, -1):
            wv[j] = a[j] + b[j] * wv[(j + 1) % m]
            ev[j] = ae[j] + b[j] * ev[(j + 1) % m]
        for j, c in enumerate(chefs):
            big_w[mask, c] = wv[j]
            big_e[mask, c] = ev[j]

    full = size - 1
    return big_w[full, 0], big_e[full, 0]


if __name__ == "__main__":
    w7, e7 = solve(7)
    expect = [0.08965042, 0.20775702, 0.15291406, 0.14554098, 0.15905291, 0.10261412, 0.14247050]
    assert all(round(w7[k], 8) == expect[k] for k in range(7))
    assert round(e7, 8) == 42.28176050

    _, e14 = solve(14)
    print(f"{e14:.8f}")  # 729.12106947
