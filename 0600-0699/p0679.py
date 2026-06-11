"""Project Euler Problem 679: Freefarea.

Count length-30 words over {A, E, F, R} containing each of the keywords
FREE, FARE, AREA, REEF exactly once.

Build the Aho-Corasick automaton of the four keywords (failure links via
BFS, goto transitions completed so every state has a move on every letter).
All keywords have length 4, so no state can output two keywords at once,
and each transition produces at most one keyword.

Dynamic programming over (automaton state, 4-bit mask of keywords seen so
far): a transition that would produce an already-seen keyword is dropped
(the word can never have each keyword *exactly* once), otherwise the mask
gains that keyword's bit.  After 30 steps, sum the counts with mask 0b1111.

Verified: f(9) = 1, f(15) = 72863, and brute force for n <= 13.
"""

from itertools import product

ALPHABET = "AEFR"
KEYWORDS = ("FREE", "FARE", "AREA", "REEF")


def build_automaton() -> tuple[list[list[int]], list[int]]:
    """Aho-Corasick: per-state transitions and keyword index (-1 if none)."""
    goto: list[list[int]] = [[-1] * 4]
    fail = [0]
    out = [-1]
    for k, word in enumerate(KEYWORDS):
        state = 0
        for ch in word:
            c = ALPHABET.index(ch)
            if goto[state][c] == -1:
                goto.append([-1] * 4)
                fail.append(0)
                out.append(-1)
                goto[state][c] = len(goto) - 1
            state = goto[state][c]
        out[state] = k

    # BFS to set failure links and complete the transitions.
    queue = [c for c in goto[0] if c != -1]
    for c in range(4):
        if goto[0][c] == -1:
            goto[0][c] = 0
    while queue:
        state = queue.pop(0)
        for c in range(4):
            nxt = goto[state][c]
            if nxt == -1:
                goto[state][c] = goto[fail[state]][c]
            else:
                fail[nxt] = goto[fail[state]][c]
                # Keywords all have equal length, so a proper suffix of one
                # keyword is never another whole keyword: out needs no merge.
                assert out[fail[nxt]] == -1 or out[nxt] == -1
                if out[nxt] == -1:
                    out[nxt] = out[fail[nxt]]
                queue.append(nxt)
    return goto, out


def f(n: int) -> int:
    """Words of length n containing each keyword exactly once."""
    goto, out = build_automaton()
    counts = {(0, 0): 1}
    for _ in range(n):
        nxt_counts: dict[tuple[int, int], int] = {}
        for (state, mask), ways in counts.items():
            for c in range(4):
                nxt = goto[state][c]
                k = out[nxt]
                nxt_mask = mask
                if k != -1:
                    if mask >> k & 1:  # Second occurrence: dead end.
                        continue
                    nxt_mask = mask | 1 << k
                key = (nxt, nxt_mask)
                nxt_counts[key] = nxt_counts.get(key, 0) + ways
        counts = nxt_counts
    return sum(ways for (_, mask), ways in counts.items() if mask == 0b1111)


def f_brute(n: int) -> int:
    return sum(
        all(
            sum(
                word[i : i + 4] == kw for i in range(n - 3)
            ) == 1
            for kw in KEYWORDS
        )
        for word in map("".join, product(ALPHABET, repeat=n))
    )


if __name__ == "__main__":
    assert f(9) == 1
    assert f(15) == 72863
    assert all(f(n) == f_brute(n) for n in range(12))
    print(f(30))  # 644997092988678
