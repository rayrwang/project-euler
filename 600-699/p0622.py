"""Project Euler Problem 622: Riffle Shuffles.

A perfect (out) riffle shuffle of an even deck of size n sends the card in
position i (0-indexed) to position 2i mod (n-1) for 0 < i < n-1, fixing the ends.
So the number of shuffles to restore order is the multiplicative order of 2 modulo
(n-1):  s(n) = ord_{n-1}(2).

We want the sum of all n with s(n) = 60.  Writing m = n-1 (odd), we need
ord_m(2) = 60, i.e. m | 2^60 - 1 and m does not divide 2^t - 1 for any maximal
proper divisor t of 60 (t in {30, 20, 12}).  Every divisor m of 2^60 - 1 is odd, so
n = m + 1 is even as required.  We factor 2^60 - 1, enumerate its divisors, keep
those of exact order 60, and sum n = m + 1.  The s(8) = ... sum 412 case checks the
method.
"""


def _factor(x: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


def _divisors(x: int) -> list[int]:
    divs = [1]
    for p, e in _factor(x).items():
        powers = [p**k for k in range(e + 1)]
        divs = [a * b for a in divs for b in powers]
    return divs


def _maximal_proper_divisors(s: int) -> list[int]:
    # s / p for each prime p | s
    out = []
    for p in _factor(s):
        out.append(s // p)
    return out


def shuffle_sum(target: int) -> int:
    base = 2**target - 1
    maximal = _maximal_proper_divisors(target)
    total = 0
    for m in _divisors(base):
        if m == 1:
            continue
        # m | 2^target - 1 holds for every divisor, so ord | target; require exact
        if all(pow(2, t, m) != 1 for t in maximal):
            total += m + 1
    return total


if __name__ == "__main__":
    assert shuffle_sum(8) == 412, shuffle_sum(8)
    print(shuffle_sum(60))  # 3010983666182123972
