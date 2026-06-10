"""Project Euler Problem 651: Patterned Cylinders.

Stickers tile an infinite cylinder in an a-periodic axial grid with b
stickers around the circumference, so patterns are colourings of the
Z_a x Z_b torus.  The admissible rigid motions -- axial translations,
rotations about the axis, reflections in planes containing or
perpendicular to the axis, and 180-degree flips -- act coordinatewise as
(x, theta) -> (+-x + s, +-theta + t): the group is exactly D_a x D_b of
order 4ab.

Burnside with j labelled colours: cycles of a product permutation pair
according to c(g x h) = sum gcd(|gamma|, |delta|) over cycle pairs, so
grouping by dihedral cycle types (rotations of order d | a with a/d
cycles of length d, phi(d) many; reflections with f fixed points and
(n - f)/2 transpositions) gives B_j in O(d(a) d(b)) exact-integer cycle
counts, with k^cycles done by modular exponentiation and the division by
|G| via a modular inverse (10^9 + 7 is prime).  Exactly m colours then
follows by inclusion-exclusion f(m) = sum (-1)^(m-j) C(m, j) B_j.

Checks: a brute-force orbit enumeration over the full 4ab-element group
for small (a, b, m), the given f(2,2,3) = 11, f(3,2,3) = 56,
f(2,3,4) = 156, and the given residues of f(8,13,21) and f(13,144,233).
"""

from itertools import product
from math import comb, gcd

P = 1_000_000_007


def divisors(n: int) -> list[int]:
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)


def phi(n: int) -> int:
    result = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def cycle_types(n: int) -> list[tuple[int, list[tuple[int, int]]]]:
    """D_n cycle types as (count, [(length, multiplicity), ...])."""
    types = []
    for d in divisors(n):
        types.append((phi(d), [(d, n // d)]))
    if n % 2 == 1:
        types.append((n, [(1, 1), (2, (n - 1) // 2)]))
    else:
        types.append((n // 2, [(1, 2), (2, (n - 2) // 2)]))
        types.append((n // 2, [(2, n // 2)]))
    return types


def burnside(k: int, a: int, b: int) -> int:
    """Orbits of k-colourings of the torus under D_a x D_b, mod P."""
    ta = cycle_types(a)
    tb = cycle_types(b)
    total = 0
    for cnt_g, cyc_g in ta:
        for cnt_h, cyc_h in tb:
            c = 0
            for l1, m1 in cyc_g:
                for l2, m2 in cyc_h:
                    c += m1 * m2 * gcd(l1, l2)
            total = (total + cnt_g * cnt_h * pow(k, c, P)) % P
    return total * pow(4 * a * b, P - 2, P) % P


def f(m: int, a: int, b: int) -> int:
    acc = 0
    for j in range(m + 1):
        term = comb(m, j) % P * burnside(j, a, b) % P
        acc = (acc - term if (m - j) % 2 else acc + term) % P
    return acc % P


def f_brute(m: int, a: int, b: int) -> int:
    """Direct orbit enumeration with exactly m colours."""
    cells = [(x, t) for x in range(a) for t in range(b)]
    group = []
    for s, t, ex, et in product(range(a), range(b), (1, -1), (1, -1)):
        perm = []
        for x, th in cells:
            nx = (ex * x + s) % a
            nt = (et * th + t) % b
            perm.append(cells.index((nx, nt)))
        group.append(perm)
    seen = set()
    count = 0
    for col in product(range(m), repeat=a * b):
        if col in seen or len(set(col)) != m:
            continue
        count += 1
        for perm in group:
            img = tuple(col[perm[i]] for i in range(a * b))
            seen.add(img)
    return count


if __name__ == "__main__":
    assert f(2, 2, 3) == f_brute(2, 2, 3) == 11
    assert f(3, 2, 3) == f_brute(3, 2, 3) == 56
    assert f(2, 3, 4) == f_brute(2, 3, 4) == 156
    assert f(3, 2, 4) == f_brute(3, 2, 4)
    assert f(2, 4, 3) == f_brute(2, 4, 3)
    assert f(8, 13, 21) == 49718354
    assert f(13, 144, 233) == 907081451
    F = [0, 1]
    while len(F) <= 41:
        F.append(F[-1] + F[-2])
    answer = sum(f(i, F[i - 1], F[i]) for i in range(4, 41)) % P
    print(answer)  # 448233151
