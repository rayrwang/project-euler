from itertools import permutations

def solve():
    """Maximum 16-digit string for a magic 5-gon ring using 1..10.

    A 16- (not 17-) digit string forces the two-digit 10 onto an outer node
    (outer nodes appear once, inner nodes twice). To maximise the string, which
    starts at the smallest outer node, the outer ring must be the five largest
    numbers {6,7,8,9,10} and the inner pentagon {1,2,3,4,5}. The line total is
    then fixed: (sum outer) + 2*(sum inner) = 40 + 30 = 70 = 5 * 14, so each line
    sums to 14, which makes every outer value a function of the inner pentagon:
    outer[j] = 14 - inner[j] - inner[j+1].
    """
    best = ""
    for inner in permutations((1, 2, 3, 4, 5)):
        outer = [14 - inner[j] - inner[(j + 1) % 5] for j in range(5)]
        if sorted(outer) != [6, 7, 8, 9, 10]:
            continue
        start = outer.index(min(outer))          # begin at the lowest outer node
        s = "".join(
            f"{outer[(start + k) % 5]}{inner[(start + k) % 5]}{inner[(start + k + 1) % 5]}"
            for k in range(5)
        )
        if s > best:
            best = s
    return best

if __name__ == "__main__":
    print(solve())  # 6531031914842725
