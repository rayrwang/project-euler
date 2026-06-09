from collections import defaultdict
from math import isqrt

def squares_of_length(length):
    lo = isqrt(10 ** (length - 1) - 1) + 1
    hi = isqrt(10 ** length - 1)
    return [str(i * i) for i in range(lo, hi + 1)]

def derive_mapping(word, digits):
    """Bijective letter<->digit map implied by aligning word with digits, or None."""
    l2d, d2l = {}, {}
    for ch, dg in zip(word, digits):
        if l2d.setdefault(ch, dg) != dg or d2l.setdefault(dg, ch) != ch:
            return None
    return l2d

def solve():
    with open("assets/0098_words.txt") as f:
        words = [w.strip('"') for w in f.read().split(",")]

    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)

    best = 0
    square_cache = {}
    for group in groups.values():
        if len(group) < 2:
            continue
        length = len(group[0])
        if length not in square_cache:
            sqs = squares_of_length(length)
            square_cache[length] = (sqs, set(sqs))
        sqs, sqset = square_cache[length]
        for w1 in group:
            for w2 in group:
                if w1 is w2:
                    continue
                for s1 in sqs:                  # a square supplies the mapping
                    mapping = derive_mapping(w1, s1)
                    if mapping is None:
                        continue
                    s2 = "".join(mapping[ch] for ch in w2)
                    if s2[0] != "0" and s2 in sqset:
                        best = max(best, int(s1), int(s2))
    return best

if __name__ == "__main__":
    print(solve())  # 18769
