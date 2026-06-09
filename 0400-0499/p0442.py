class AhoCorasick:
    """Digit automaton over the forbidden patterns (powers of 11)."""

    def __init__(self, patterns: list[str]):
        self.goto: list[list[int]] = [[-1] * 10]
        self.accept: list[bool] = [False]
        for pat in patterns:
            node = 0
            for ch in pat:
                d = int(ch)
                if self.goto[node][d] == -1:
                    self.goto.append([-1] * 10)
                    self.accept.append(False)
                    self.goto[node][d] = len(self.goto) - 1
                node = self.goto[node][d]
            self.accept[node] = True
        # BFS to fill failure transitions, turning goto into a total function
        fail = [0] * len(self.goto)
        for d in range(10):
            if self.goto[0][d] == -1:
                self.goto[0][d] = 0
        order = [self.goto[0][d] for d in range(10) if self.goto[0][d] != 0]
        head = 0
        seen = set(order)
        while head < len(order):
            u = order[head]
            head += 1
            self.accept[u] = self.accept[u] or self.accept[fail[u]]
            for d in range(10):
                v = self.goto[u][d]
                if v == -1:
                    self.goto[u][d] = self.goto[fail[u]][d]
                else:
                    fail[v] = self.goto[fail[u]][d]
                    if v not in seen:
                        seen.add(v)
                        order.append(v)

def eleven_free_count(x: int, ac: AhoCorasick) -> int:
    """Number of eleven-free integers in [1, x].

    Digit DP over the zero-padded representation: since no power of 11
    starts with 0, leading zeros leave the automaton at the root, so
    every n in [0, x] is scanned correctly; subtract 1 for n = 0.
    """
    if x < 1:
        return 0
    digits = [int(c) for c in str(x)]
    free = [0] * len(ac.goto)  # counts per state, prefix strictly below x
    tight_state = 0
    tight_alive = True
    for d in digits:
        new_free = [0] * len(ac.goto)
        for s, c in enumerate(free):
            if c:
                for nd in range(10):
                    t = ac.goto[s][nd]
                    if not ac.accept[t]:
                        new_free[t] += c
        if tight_alive:
            for nd in range(d):  # branch below the tight prefix
                t = ac.goto[tight_state][nd]
                if not ac.accept[t]:
                    new_free[t] += 1
            tight_state = ac.goto[tight_state][d]
            tight_alive = not ac.accept[tight_state]
        free = new_free
    return sum(free) + (1 if tight_alive else 0) - 1  # -1 removes n = 0

def nth_eleven_free(n: int) -> int:
    patterns = []
    p = 11
    while len(str(p)) <= 20:
        patterns.append(str(p))
        p *= 11
    ac = AhoCorasick(patterns)
    lo, hi = 1, 2 * n + 10  # density > 1/2 by far, so E(n) < 2n
    while lo < hi:
        mid = (lo + hi) // 2
        if eleven_free_count(mid, ac) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

def brute_count(x: int) -> int:
    pats = [str(11**k) for k in range(1, 7)]
    return sum(1 for n in range(1, x + 1)
               if not any(p in str(n) for p in pats))

if __name__ == "__main__":
    assert nth_eleven_free(3) == 3
    assert nth_eleven_free(200) == 213
    assert nth_eleven_free(500_000) == 531563
    patterns_ac = AhoCorasick([str(11**k) for k in range(1, 21)])
    assert eleven_free_count(54321, patterns_ac) == brute_count(54321)
    print(nth_eleven_free(10**18))  # 1295552661530920149
