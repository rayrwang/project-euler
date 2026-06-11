from collections import Counter
from fractions import Fraction
from functools import cache
from math import factorial

PHRASE = "thereisasyetinsufficientdataforameaningfulanswer"
MAXLEN = 15
LETTERS = sorted(set(PHRASE))

@cache
def continuations(counts: tuple[int, ...], length: int) -> int:
    """Number of words of length <= `length` (including the empty word)
    formed from a letter multiset with the given (sorted) count profile.

    The count of length-k words is k! [x^k] prod_i sum_(j<=c_i) x^j / j!.
    """
    poly = [Fraction(1)] + [Fraction(0)] * length
    for c in counts:
        new = [Fraction(0)] * (length + 1)
        for j in range(min(c, length) + 1):
            fj = factorial(j)
            for k in range(length + 1 - j):
                if poly[k]:
                    new[k + j] += poly[k] / fj
        poly = new
    return sum(int(poly[k] * factorial(k)) for k in range(length + 1))

def words_below(counts: Counter, length: int) -> int:
    """Words of length <= `length` from `counts`, empty word included."""
    return continuations(tuple(sorted(c for c in counts.values() if c)), length)

def position(word: str) -> int:
    """P(word): 1-based rank of `word` in the alphabetical list."""
    counts = Counter(PHRASE)
    rank = 0
    for i, letter in enumerate(word):
        for c in LETTERS:
            if c >= letter:
                break
            if counts[c]:
                counts[c] -= 1
                rank += words_below(counts, MAXLEN - i - 1)
                counts[c] += 1
        rank += 1  # the prefix word[:i+1] itself
        assert counts[letter] > 0
        counts[letter] -= 1
    return rank

def word_at(rank: int) -> str:
    """W(rank): the word at the given 1-based position."""
    counts = Counter(PHRASE)
    word: list[str] = []
    while True:
        if word:  # the current prefix is itself a word in the list
            if rank == 1:
                break
            rank -= 1
        for c in LETTERS:
            if not counts[c]:
                continue
            counts[c] -= 1
            n = words_below(counts, MAXLEN - len(word) - 1)
            if rank <= n:
                word.append(c)
                break
            counts[c] += 1
            rank -= n
        else:
            raise AssertionError("rank out of range")
    return "".join(word)

if __name__ == "__main__":
    assert word_at(10) == "aaaaaacdee"
    assert position("aaaaaacdee") == 10
    assert position("euler") == 115246685191495243
    assert word_at(115246685191495243) == "euler"
    p = (position("legionary") + position("calorimeters") - position("annihilate")
         + position("orchestrated") - position("fluttering"))
    print(word_at(p))  # turnthestarson
