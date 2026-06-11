"""Project Euler Problem 674: Solving I-equations.

I(x, y) = (1 + x + y)^2 + y - x is injective on nonnegative integers:
with s = x + y the value lies in [s^2 + s + 1, s^2 + 3s + 1], these
intervals are disjoint (consecutive ones leave the gap (s+1)(s+2)), and
within an interval y - x recovers the pair.  Moreover I(x, y) strictly
exceeds both arguments and is strictly increasing in each.  Hence
e_1 = e_2 has a solution exactly when the two terms unify syntactically
over the constructor I (same-named variables shared across the pair,
occurs check included, since x = I(..x..) would need I's value to not
exceed an argument), and by monotonicity the least simultaneous value
is the unified term evaluated with every free variable set to 0.

All 149 expressions are parsed with hash-consing into one DAG (25k
nodes).  Each of the C(149, 2) pairs runs Robinson unification with a
union-find over node ids and a visited set on representative pairs
(almost linear in DAG size); variables bind to an I-node of their class
when one exists.  Success is followed by an iterative DFS that both
performs the deferred occurs check (cycle detection through bindings)
and evaluates the value mod 10^9 -- the recurrence is polynomial, so
the last nine digits are exact.

Verified: the statement's example values 23, 0 and 3 for the first
three expressions in the file (total 26), with the 23 reproduced by a
brute-force scan over small variable assignments.
"""

from pathlib import Path

MOD = 10**9
DATA = Path(__file__).resolve().parent.parent / "assets"


class Terms:
    def __init__(self) -> None:
        self.intern: dict = {}
        self.left: list[int] = []
        self.right: list[int] = []
        self.vname: list[str | None] = []
        self.zval: list[int] = []
        self.canon_var: dict[str, int] = {}

    def mk(self, key) -> int:
        if key in self.intern:
            return self.intern[key]
        idx = len(self.vname)
        if isinstance(key, tuple):
            _, a, b = key
            self.left.append(a)
            self.right.append(b)
            self.vname.append(None)
            za, zb = self.zval[a], self.zval[b]
            self.zval.append(((1 + za + zb) ** 2 + zb - za) % MOD)
        else:
            self.left.append(-1)
            self.right.append(-1)
            self.vname.append(key)
            self.zval.append(0)
            self.canon_var.setdefault(key, idx)
        self.intern[key] = idx
        return idx

    def parse(self, s: str) -> int:
        stack: list[list] = []
        out = -1

        def emit(node: int) -> None:
            nonlocal out
            while True:
                if not stack:
                    out = node
                    return
                frame = stack[-1]
                if frame[0] is None:
                    frame[0] = node
                    return
                stack.pop()
                node = self.mk(("I", frame[0], node))

        pos, n = 0, len(s)
        while pos < n:
            c = s[pos]
            if c == "I" and pos + 1 < n and s[pos + 1] == "(":
                stack.append([None])
                pos += 2
            elif c.isalpha():
                j = pos
                while j < n and s[j].isalpha():
                    j += 1
                emit(self.mk(s[pos:j]))
                pos = j
            else:
                pos += 1
        return out


def least_simultaneous(t: Terms, r1: int, r2: int) -> int:
    parent: dict[int, int] = {}
    vname, left, right = t.vname, t.left, t.right

    def find(x: int) -> int:
        root = x
        while parent.get(root, root) != root:
            root = parent[root]
        while parent.get(x, x) != root:
            parent[x], x = root, parent[x]
        return root

    def node(u: int) -> int:
        name = vname[u]
        return t.canon_var[name] if name is not None else u

    stack = [(node(r1), node(r2))]
    seen = set()
    while stack:
        u, v = stack.pop()
        u, v = find(u), find(v)
        if u == v or (u, v) in seen:
            continue
        seen.add((u, v))
        if vname[u] is not None:
            parent[u] = v
        elif vname[v] is not None:
            parent[v] = u
        else:
            parent[u] = v
            stack.append((left[u], left[v]))
            stack.append((right[u], right[v]))

    cls_inode: dict[int, int] = {}
    for x in list(parent):
        r = find(x)
        if vname[x] is None:
            cls_inode.setdefault(r, x)
        if vname[r] is None:
            cls_inode.setdefault(r, r)

    def resolve(u: int) -> int:
        r = find(node(u))
        return cls_inode.get(r, r)

    memo: dict[int, int] = {}
    state: dict[int, int] = {}
    todo = [(r1, 0)]
    while todo:
        u, phase = todo.pop()
        w = resolve(u)
        if w in memo:
            continue
        if vname[w] is not None:
            memo[w] = 0
            continue
        if phase == 0:
            if state.get(w) == 1:
                return 0  # cycle: occurs check fails, no solution
            state[w] = 1
            todo.append((w, 1))
            todo.append((left[w], 0))
            todo.append((right[w], 0))
        else:
            a = memo[resolve(left[w])]
            b = memo[resolve(right[w])]
            memo[w] = ((1 + a + b) ** 2 + b - a) % MOD
    return memo[resolve(r1)]


def example_brute() -> int:
    def ival(x: int, y: int) -> int:
        return (1 + x + y) ** 2 + y - x

    best = 0
    for x in range(7):
        for y in range(7):
            for z in range(7):
                for tt in range(7):
                    a = ival(x, ival(z, tt))
                    b = ival(ival(y, z), y)
                    if a == b and (best == 0 or a < best):
                        best = a
    return best


if __name__ == "__main__":
    terms = Terms()
    lines = [
        line.strip()
        for line in (DATA / "0674_i_expressions.txt").open()
        if line.strip()
    ]
    roots = [terms.parse(line) for line in lines]
    assert len(roots) == 149
    assert example_brute() == 23
    first = [
        least_simultaneous(terms, roots[i], roots[j])
        for i, j in ((0, 1), (0, 2), (1, 2))
    ]
    assert first == [23, 0, 3]  # statement examples, total 26

    total = 0
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            total = (total + least_simultaneous(terms, roots[i], roots[j])) % MOD
    print(total)  # 416678753
