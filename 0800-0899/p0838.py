"""Project Euler 838: Not Coprime.

f(N) is the cheapest product of primes hitting every n <= N with last
digit 3, where cost is ln, so we need a minimum-weight prime hitting
set.  A prime p = 3 (mod 10) is the only divisor of itself, so all
such primes up to N are mandatory.  Primes p = 1 (mod 10) are never
needed: any n containing one also contains a smaller witness n/p = 3
(mod 10) whose clause is a subset.  What remains are numbers built
from 7-type and 9-type primes with 7^a 9^b = 3 (mod 10), i.e.
(a, b) = (3, 0) or (1, 1) modulo (4, 2); every larger pattern is
subsumed by a sub-product that is itself = 3 (mod 10) and <= N.

An exchange argument (a smaller skipped prime forces all its partners
to be chosen, which then cover every clause of any larger chosen
prime) shows the optimum is downward closed within each residue
class.  Writing a for the smallest excluded 7-type prime, the internal
7-type clauses {p^3}, {p^2 q}, {p q r} all reduce to the single
condition a^3 > N, since a^2 a' and a a' a'' exceed a^3.  The 7 x 9
pair clauses pq <= N form a staircase, forcing every 9-type prime
q <= N/a to be chosen.  Hence

    ln f(N) = C_3 + min_a [ pre7(a) + pre9(N // a) ],

minimised over 7-type primes a with a^3 > N (and a = infinity),
where pre7/pre9 are prefix sums of logarithms and C_3 the mandatory
3-type total.  One sieve and a linear scan give the answer; the code
reproduces ln f(40) = 6.799056 (f = 3 * 13 * 23 = 897) and the given
ln f(2800) = 715.019337.
"""

from __future__ import annotations

import bisect
from math import fsum, log

import numpy as np


def log_f(n: int) -> float:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    primes = np.nonzero(sieve)[0]
    mandatory = fsum(log(int(p)) for p in primes[primes % 10 == 3])
    p7 = [int(p) for p in primes[primes % 10 == 7]]
    p9 = [int(p) for p in primes[primes % 10 == 9]]
    pre7 = [0.0]
    for p in p7:
        pre7.append(pre7[-1] + log(p))
    pre9 = [0.0]
    for q in p9:
        pre9.append(pre9[-1] + log(q))
    best = None
    candidates: list[int | None] = [p for p in p7 if p**3 > n]
    candidates.append(None)
    for a in candidates:
        if a is None:
            cost = pre7[len(p7)]  # choose all 7-types, no 9-types
        else:
            i7 = bisect.bisect_left(p7, a)
            j9 = bisect.bisect_right(p9, n // a)
            cost = pre7[i7] + pre9[j9]
        if best is None or cost < best:
            best = cost
    assert best is not None
    return mandatory + best


def main() -> None:
    assert f"{log_f(40):.6f}" == "6.799056"
    assert f"{log_f(2800):.6f}" == "715.019337"
    print(f"{log_f(10**6):.6f}")  # 250591.442792


if __name__ == "__main__":
    main()
