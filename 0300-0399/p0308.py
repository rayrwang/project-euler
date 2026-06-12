import numba
import numpy as np

# Conway's PRIMEGAME.  Writing the state as 2^a 3^b 5^c 7^d times a marker
# in {1, 11, 13, 17, 19, 23, 29}, the fourteen fractions become a tiny
# finite-state machine over the four registers, and its loops batch into
# closed forms: the 13/17 loop subtracts d from c while moving it into a
# and b (2 steps per unit), the 19/23 loop moves a into c, the 11/29 loop
# moves b into d, and the marker-1 phase moves a into b and c and clears d.
#
# Chasing these macros shows the machine performs literal trial division:
# with dividend n in c and divisor d (held in the register 7), one whole
# "compute n mod d" pass costs q (4d + 2) + 2n + 4r + 2 steps with
# q = n div d, r = n mod d, ending with divisor d - 1 and the dividend
# restored; the per-divisor cost collapses to 2 q + 6 n + 2.  A zero
# remainder instead costs q (4d + 2) + 3n + d + 3 and advances to the next
# candidate n + 1 with divisor n; the state is a pure power of 2 exactly
# two steps into that block when d = 1, i.e. when n is prime.  Both levels
# of batching are verified step-for-step against the literal fraction
# machine (powers of two at iterations 19, 69, 281, 710, 2375, ...).
#
# Summing over the divisors d = delta+1 .. n-1 (delta the largest proper
# divisor, where the first zero remainder occurs) needs only the hyperbola
# sums sum floor(n/d), so each candidate costs O(sqrt(n)).

@numba.jit(cache=True)
def phi(n, t):
    # sum of floor(n / d) for d = 1..t (t <= n)
    total = 0
    d = 1
    while d <= t:
        v = n // d
        last = min(t, n // v)
        total += v * (last - d + 1)
        d = last + 1
    return total

@numba.jit(cache=True)
def primegame_steps(index):
    # iterations until the state equals 2^(index-th prime)
    limit = 200_000  # comfortably beyond the 10001st prime
    spf = np.zeros(limit + 1, dtype=np.int64)
    for p in range(2, limit + 1):
        if spf[p] == 0:
            for q in range(p, limit + 1, p):
                if spf[q] == 0:
                    spf[q] = p
    steps = 5  # seed 2 reaches the first division (n = 2 by d = 1) in 5 steps
    seen = 0
    n = 2
    while True:
        delta = n // spf[n]  # largest proper divisor: first zero remainder
        steps += 2 * (phi(n, n - 1) - phi(n, delta))
        steps += (6 * n + 2) * (n - 1 - delta)
        if delta == 1:  # n is prime: power of 2 two steps into the d=1 block
            seen += 1
            if seen == index:
                return steps + 6 * n + 2
        steps += spf[n] * (4 * delta + 2) + 3 * n + delta + 3
        n += 1

if __name__ == "__main__":
    print(primegame_steps(10001))  # 1539669807660924
