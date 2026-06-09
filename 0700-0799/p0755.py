from functools import cache

def S(limit):
    """S(limit) = sum_{k <= limit} f(k), where f(k) counts representations of
    k as a sum of distinct Fibonacci numbers {1, 2, 3, 5, 8, ...}.

    Summing f over k <= limit counts exactly the subsets of Fibonacci numbers
    whose total is at most limit (the empty subset covers f(0) = 1). Count
    them greedily from the largest Fibonacci down: with prefix sums P_i =
    F_1 + ... + F_i, the number of subsets of the first i Fibonaccis with
    sum <= cap is 2^i when cap >= P_i, zero when cap < 0, and otherwise
    splits on whether F_i is used. Because F_i > P_(i-1) / 2, the reachable
    caps collapse onto O(i) values per level, so memoisation keeps the
    recursion tiny.
    """
    fibs = [1, 2]
    while fibs[-1] <= limit:
        fibs.append(fibs[-1] + fibs[-2])
    fibs.pop()
    prefix = [0]
    for f in fibs:
        prefix.append(prefix[-1] + f)

    @cache
    def count(i, cap):
        """Subsets of fibs[0..i-1] with sum <= cap."""
        if cap < 0:
            return 0
        if cap >= prefix[i]:
            return 1 << i
        return count(i - 1, cap) + count(i - 1, cap - fibs[i - 1])

    return count(len(fibs), limit)

if __name__ == "__main__":
    assert S(100) == 415
    assert S(10**4) == 312807
    print(S(10**13))  # 2877071595975576960
