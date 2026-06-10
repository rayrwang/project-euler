"""Project Euler 910: L-expressions II.

As in Problem 909, the rules are Church-numeral combinators, with
C_i = [i] and D_i = C_i(S)(S) = S^i(S), so D_i = S(D_{i-1}) and the
S-rule gives, for any objects h, w,

    D_i(h)(w) = h(h(...h(S(h)(w))...))        (h object-applied i times).

In F(a, b, c, d, e) = D_a(D_b)(D_c)(C_d)(A)(e) every application chain
bottoms out on numerals, where object application of an operator V with
numeral action v ([m] -> [v(m)]) is just arithmetic, and
S(V)([m]) = [m] o V([m]) = [m * v(m)].  Peeling the layers:

    f(m)  = (m + 1) m^c                  D_c on numerals
    w1(m) = f^(b)(m f(m))                D_b(D_c)
    v0(m) = f(w1(m))                     U0 = S(D_b)(D_c) = D_c o D_b(D_c)
    vk(m) = v_{k-1}^(b)(m v_{k-1}(m))    V_k = D_b(V_{k-1}),  k = 1..a
    F     = e + v_a(d)                   since D_a(D_b)(D_c) = V_a

(superscripts denote function iteration).  This arithmetic semantics is
verified below against exact mechanical reduction of the L-expressions
(with D_i built literally as C_i(S)(S)) on dozens of small parameter
tuples.

Every operation is a ring operation with *fixed* exponent c and *fixed*
iteration count b, so the whole computation descends to Z_M for any
modulus M.  Tabulating each v_k over Z_M and forming b-fold iterates by
binary lifting (log2 b table compositions) costs O(M log b) per level.
Computing modulo 2^9 and 5^9 separately and combining by CRT gives the
last nine digits.
"""

import numpy as np

Term = int | str | tuple


def ap(f: Term, x: Term) -> Term:
    return ("ap", f, x)


def value(t: Term, e: int) -> int:
    """Fully reduce t(A)(e) to a number by head-spine rewriting."""
    h: Term = ap(ap(t, "A"), e)
    stack: list[Term] = []
    pending = 0
    while True:
        while isinstance(h, tuple):
            stack.append(h[2])
            h = h[1]
        if h == "A":
            pending += 1
            h = stack.pop()
        elif h == "Z":
            stack.pop()
            h = stack.pop()
        elif h == "S":
            u = stack.pop()
            v = stack.pop()
            w = stack.pop()
            h = ap(v, ap(ap(u, v), w))
        else:
            assert isinstance(h, int) and not stack
            return h + pending


def church(n: int) -> Term:
    t: Term = "Z"
    for _ in range(n):
        t = ap("S", t)
    return t


def f_mech(a: int, b: int, c: int, d: int, e: int) -> int:
    def big_d(i: int) -> Term:
        return ap(ap(church(i), "S"), "S")

    return value(ap(ap(ap(big_d(a), big_d(b)), big_d(c)), church(d)), e)


def f_exact(a: int, b: int, c: int, d: int, e: int) -> int:
    def f(m):
        return (m + 1) * m**c

    def it(fn, n, x):
        for _ in range(n):
            x = fn(x)
        return x

    v = lambda m: f(it(f, b, m * f(m)))  # noqa: E731
    for _ in range(a):
        prev = v
        v = lambda m, p=prev: it(p, b, m * p(m))  # noqa: E731
    return e + v(d)


def _pow_table(c: int, mod: int) -> np.ndarray:
    r = np.ones(mod, dtype=np.int64)
    base = np.arange(mod, dtype=np.int64)
    e = c
    while e:
        if e & 1:
            r = r * base % mod
        base = base * base % mod
        e >>= 1
    return r


def _iterate_table(t: np.ndarray, b: int, mod: int) -> np.ndarray:
    res = np.arange(mod, dtype=np.int64)
    base = t.copy()
    while b:
        if b & 1:
            res = base[res]
        base = base[base]
        b >>= 1
    return res


def f_mod(a: int, b: int, c: int, d: int, e: int, mod: int) -> int:
    x = np.arange(mod, dtype=np.int64)
    tf = (x + 1) % mod * _pow_table(c, mod) % mod
    fb = _iterate_table(tf, b, mod)
    v = tf[fb[x * tf % mod]]
    for _ in range(a):
        v = _iterate_table(v, b, mod)[x * v % mod]
    return int((e + v[d % mod]) % mod)


def solve(a: int, b: int, c: int, d: int, e: int) -> int:
    m1, m2 = 2**9, 5**9
    r1 = f_mod(a, b, c, d, e, m1)
    r2 = f_mod(a, b, c, d, e, m2)
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2)


if __name__ == "__main__":
    # given examples of the rewriting system
    assert value(ap("S", "Z"), 0) == 1
    assert value(ap(ap(ap("S", "S"), ap("S", "S")), ap("S", "Z")), 0) == 6
    # arithmetic semantics == exact mechanical reduction on small cases
    # (the call-by-name reducer re-evaluates duplicated subterms, so only
    # cases with small values terminate quickly), and the modular
    # pipeline agrees with the exact values at several moduli
    small = [
        (0, 0, 1, 2, 0), (0, 1, 1, 1, 0), (0, 1, 1, 2, 5), (0, 2, 1, 1, 0),
        (1, 0, 0, 2, 0), (1, 1, 0, 2, 4), (1, 0, 1, 2, 0), (2, 0, 1, 1, 5),
        (0, 0, 2, 2, 0), (0, 1, 2, 1, 0), (2, 0, 0, 2, 1), (2, 0, 0, 3, 0),
    ]
    for case in small:
        exact = f_exact(*case)
        assert exact < 10**5 and f_mech(*case) == exact
        for mod in (512, 1000, 5**6):
            assert f_mod(*case, mod) == exact % mod
    assert f_mod(0, 1, 1, 2, 5, 5**9) == f_exact(0, 1, 1, 2, 5) % 5**9
    print(solve(12, 345678, 9012345, 678, 90))  # 547480666
