MOD = 10**9
SIZE = 7  # alphabet {c, e, j, o, p, r, t}

def transition_matrix() -> list[list[int]]:
    """M[j][i] = number of letters taking a string whose maximal
    pairwise-distinct suffix has length i+1 to one with length j+1.

    From suffix length k: a letter equal to the one i positions back
    (1 <= i <= k) gives new suffix length i (one way each); any of the
    7 - k unused letters extends to k + 1. Length 7 is forbidden, so
    states are 1..6 and the 7 - 6 = 1 letter completing a permutation
    from state 6 is simply dropped.
    """
    m = [[0] * (SIZE - 1) for _ in range(SIZE - 1)]
    for k in range(1, SIZE):  # current suffix length
        for i in range(1, k + 1):  # duplicate i positions back
            m[i - 1][k - 1] += 1
        if k + 1 < SIZE:
            m[k][k - 1] += SIZE - k
    return m

def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) % MOD for j in range(n)]
        for i in range(n)
    ]

def count_safe_strings(n: int) -> int:
    """T(n) mod 10^9: strings of length n over 7 letters with no window of
    7 consecutive, pairwise-distinct letters."""
    vec = [0] * (SIZE - 1)
    vec[0] = SIZE  # after the first letter: suffix length 1, 7 ways
    m = transition_matrix()
    e = n - 1
    while e > 0:  # vec <- M^(n-1) vec
        if e & 1:
            vec = [sum(m[i][k] * vec[k] for k in range(SIZE - 1)) % MOD
                   for i in range(SIZE - 1)]
        m = mat_mul(m, m)
        e >>= 1
    return sum(vec) % MOD

def brute(n: int) -> int:
    total = 0
    for s in range(SIZE**n):
        word = []
        x = s
        for _ in range(n):
            word.append(x % SIZE)
            x //= SIZE
        ok = True
        for i in range(n - SIZE + 1):
            if len(set(word[i:i + SIZE])) == SIZE:
                ok = False
                break
        if ok:
            total += 1
    return total % MOD

if __name__ == "__main__":
    assert count_safe_strings(7) == (7**7 - 5040) % MOD
    assert count_safe_strings(8) == brute(8)
    print(count_safe_strings(10**12))  # 423341841
