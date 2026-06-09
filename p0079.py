from collections import defaultdict

def solve():
    """Shortest passcode consistent with every 3-digit login attempt.

    Each attempt 'abc' says digit a precedes b precedes c, so the attempts are
    precedence edges in a DAG and the passcode is a topological ordering.
    """
    digits = set()
    successors = defaultdict(set)
    with open("assets/0079_keylog.txt") as f:
        for line in f:
            a, b, c = line.strip()
            digits.update((a, b, c))
            successors[a].add(b)
            successors[b].add(c)

    indegree = {d: 0 for d in digits}
    for u in successors:
        for v in successors[u]:
            indegree[v] += 1

    order = []
    ready = sorted(d for d in digits if indegree[d] == 0)
    while ready:
        d = ready.pop(0)
        order.append(d)
        for v in successors[d]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
        ready.sort()
    return "".join(order)

if __name__ == "__main__":
    print(solve())  # 73162890
