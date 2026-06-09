from fractions import Fraction
from itertools import combinations

def reachable(nums):
    """All values obtainable from these numbers via + - * / and parentheses."""
    if len(nums) == 1:
        return {nums[0]}
    out = set()
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = nums[i], nums[j]
            rest = [nums[k] for k in range(n) if k != i and k != j]
            combined = [a + b, a - b, a * b]
            if b != 0:
                combined.append(a / b)
            for value in combined:
                out |= reachable(rest + [value])
    return out

def run_length(digits):
    values = reachable([Fraction(d) for d in digits])
    ints = {v.numerator for v in values if v.denominator == 1 and v.numerator >= 1}
    n = 1
    while n in ints:
        n += 1
    return n - 1   # length of the unbroken run 1, 2, ..., n-1

if __name__ == "__main__":
    best_len, best = 0, ()
    for digits in combinations(range(10), 4):
        length = run_length(digits)
        if length > best_len:
            best_len, best = length, digits
    print("".join(map(str, best)))  # 1258
