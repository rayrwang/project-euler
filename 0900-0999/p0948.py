"""Project Euler 948: Left vs Right.

Analyzing the game on w[i..j]: with A(i,j) = "Left to move, Left wins" and
B(i,j) = "Right to move, Right wins", the recursions A(i,j) = exists
i' in (i,j]: not B(i',j) and B(i,j) = exists j' in [i,j): not A(i,j') are
monotone in the free endpoint, so A(.,j) and B(i,.) are threshold
sequences: A(i,j) iff i <= t_j and B(i,j) iff j >= u_i. Working out how
t_j evolves as j sweeps right reveals a stack process: an L at position j
sets t_j = j and pushes j; an R pops the most recent unpopped L (if any),
say at m, and sets t_j = m - 1 (no L: t_j = -infinity). This is exactly
greedy bracket matching with L as opener and R as closer. Hence

  Left moving first wins  <=>  w ends in L, or its final R is matched to
                               an L at position >= 1;
  Right moving first wins <=>  the mirror condition - w starts with R, or
                               its first L is matched to an R at position
                               <= n-2 -

and greedy matching is left-right symmetric (the matched pairs of the
reversed, letter-swapped word are the same pairs), so both conditions
reference one matching. F(n) counts words satisfying both, by a DP over
positions whose state is the current stack size s and a flag f marking
whether the position-0 L is still unmatched at the bottom of the stack,
plus (when w starts with L) whether the first L was matched before the
final position. The four (first letter, last letter) cases:

  R...L : always a double first-player win, 2^(n-2) words;
  R...R : need the final R matched - some L unmatched before it;
  L...L : mirror of the previous case;
  L...R : final R matched but not to position 0, and position-0 L matched
          but not by position n-1.

Verified against full game-tree evaluation of every word for n <= 12 and
brute-force counts F(n) for n <= 22, including the given F(3) = 4 and
F(8) = 181.
"""

N = 60


def count_case_RR(n):
    """Words R w[1..n-2] R where the final R is matched.

    Final R matched <=> stack (unmatched L count) nonempty after w[0..n-2].
    Position 0 is R, so any matching L is at position >= 1 automatically.
    """
    # DP over positions 1..n-2 on stack size
    from collections import defaultdict

    dp = {0: 1}  # after position 0 (an R, possibly unmatched): stack 0
    for _ in range(1, n - 1):
        nd = defaultdict(int)
        for s, c in dp.items():
            nd[s + 1] += c  # L
            nd[max(0, s - 1)] += c  # R (pops if possible)
        dp = dict(nd)
    return sum(c for s, c in dp.items() if s >= 1)


def count_case_LR(n):
    """Words L w[1..n-2] R with: final R matched, not to position 0;
    and position-0 L matched by an R at position <= n-2."""
    from collections import defaultdict

    # state: (s, f) with s = stack size, f = 1 if position-0 L still on
    # stack bottom. First-L-matched-early <=> f == 0 before processing the
    # final position (a pop at the last position would match it to n-1).
    dp = {(1, 1): 1}  # after position 0 = L
    for _ in range(1, n - 1):
        nd = defaultdict(int)
        for (s, f), c in dp.items():
            nd[(s + 1, f)] += c  # L
            if s >= 1:
                nf = 0 if (s == 1 and f == 1) else f
                nd[(s - 1, nf)] += c  # R pops
            else:
                nd[(0, 0)] += c  # unmatched R (f already 0 here)
        dp = dict(nd)
    # final char R: matched (s >= 1) and popped L is not position 0
    # (exclude s == 1 and f == 1); plus first L matched earlier (f == 0).
    tot = 0
    for (s, f), c in dp.items():
        if s >= 1 and f == 0:
            tot += c
    return tot


def f_of_n(n):
    if n == 1:
        return 0
    case_RL = 1 << (n - 2)
    case_RR = count_case_RR(n)
    case_LL = case_RR  # mirror symmetry
    case_LR = count_case_LR(n)
    return case_RL + case_RR + case_LL + case_LR


def solve() -> int:
    return f_of_n(N)


if __name__ == "__main__":
    print(solve())  # 1033654680825334184
