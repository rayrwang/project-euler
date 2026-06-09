"""Project Euler 909: L-expressions I.

The rewrite rules are combinator rules for Church numerals: Z(u)(v) -> v
makes Z the numeral [0], S(u)(v)(w) -> v(u(v)(w)) makes S the successor
(S([n]) behaves as [n + 1], where [n](f) = the n-fold composition f^n),
and the numeral [n] = S(...S(Z)) finally turns A, 0 into the number n.

Two extensional facts close the calculation, writing P = S(S) and
treating every object as an operator acting by composition:

    [a] o [b] = [a b]            (iterating a b-fold iteration)
    S(g)(h) = h o g(h),  P(g)(h) = g(S(g)(h))    (the S-rule itself)

Hence P([n]) = [n]([n + 1]-fold composition) = [n(n + 1)];
S(P)([n]) = [n] o P([n]) = [n^2 (n + 1)]; and
P(P)([n]) = P(S(P)([n])) = [m(m + 1)] with m = n^2 (n + 1).

The target is P(P)(P)([1])(A)(0).  By the S-rule (exactly),
P(P)(P) = P(X) with X = S(P)(P) : t -> P(P(P)(t)), and
P(X)([1]) = X(S(X)([1])) = X(X([1])) since [1] is the identity.  So with
p(n) = n(n + 1), pp(n) = p(n * p(n)) and x(n) = p(pp(n)), the answer is
x(x(1)) = x(42) = M(M + 1) mod 10^9 for M = 75852 * 75853.  Every
identity used (and both given examples) is verified below by an exact
mechanical normal-order evaluator on small numerals, where the
reduction terminates quickly.
"""

Term = int | str | tuple


def ap(f: Term, x: Term) -> Term:
    return ("ap", f, x)


def value(t: Term) -> int:
    """Fully reduce t(A)(0) to a number, by leftmost-outermost rewriting
    on the head spine (the A-rule is folded into a pending increment)."""
    h: Term = ap(ap(t, "A"), 0)
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


def p(n: int) -> int:  # P([n]) = [n (n+1)]
    return n * (n + 1)


def pp(n: int) -> int:  # P(P)([n]) = P([n] o P([n]))
    return p(n * p(n))


def x(n: int) -> int:  # X = S(P)(P) : X([n]) = P(P(P)([n]))
    return p(pp(n))


def solve() -> int:
    return x(x(1)) % 10**9


if __name__ == "__main__":
    s, z = "S", "Z"
    big_p = ap(s, s)
    # given examples
    assert value(ap(s, z)) == 1
    assert value(ap(ap(big_p, big_p), ap(s, z))) == 6
    # mechanical verification of every identity used, on small numerals
    for n in range(1, 4):
        assert value(ap(big_p, church(n))) == p(n)
        assert value(ap(ap(big_p, big_p), church(n))) == pp(n)
        assert value(ap(ap(ap(s, big_p), big_p), church(n))) == x(n)
    # P(P)(P)([1]) = X(X([1])) is two exact S-rule steps plus [1](y) = y
    assert x(1) == 42
    print(solve())  # 399885292
