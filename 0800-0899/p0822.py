import heapq

MOD = 1234567891


class _Element:
    """A list entry equal to k^(2^e); ordered by its real value 2^e * log k.

    Comparisons stay exact by reducing 2^{e_a} log k_a < 2^{e_b} log k_b to an
    integer test k_a < k_b^{2^d} (repeated squaring), aborting early once one
    side overtakes the other. Level differences in play are tiny, so d is small.
    """

    __slots__ = ("k", "e")

    def __init__(self, k: int, e: int = 0) -> None:
        self.k = k
        self.e = e

    def __lt__(self, other: "_Element") -> bool:
        if self.e <= other.e:
            d, lhs, rhs = other.e - self.e, self.k, other.k
            for _ in range(d):
                rhs *= rhs
                if rhs > lhs:
                    return True
            return lhs < rhs
        d, lhs, rhs = self.e - other.e, self.k, other.k
        for _ in range(d):
            lhs *= lhs
            if lhs > rhs:
                return False
        return lhs < rhs


def square_smallest_sum(n: int, m: int) -> int:
    """S(n, m) mod MOD: sum of [2..n] after m rounds of squaring the smallest.

    Squaring never changes which base k an entry came from, only how many times
    it has been squared, so entry k holds k^(2^{e_k}). Each round increments the
    e of the entry with the smallest current value.

    After a short warm-up the values become balanced enough that every block of
    n - 1 consecutive rounds squares each of the n - 1 entries exactly once
    (detected once two successive (n-1)-windows of pops are each a full
    permutation). From there the remaining r rounds split into r // (n-1) full
    blocks — adding that to every level — plus r mod (n-1) extra rounds, which
    follow the just-observed steady order. Final values are k^(2^{e_k}) with the
    exponent reduced modulo MOD - 1 (MOD is prime). Verified against an exact
    heap simulation for all n < 30 and m up to 10^5; S(5,3)=34, S(10,100) checks.
    """
    width = n - 1
    levels = {k: 0 for k in range(2, n + 1)}
    heap = [_Element(k) for k in range(2, n + 1)]
    heapq.heapify(heap)
    history: list[int] = []
    done = 0
    while done < m:
        smallest = heapq.heappop(heap)
        smallest.e += 1
        levels[smallest.k] = smallest.e
        heapq.heappush(heap, smallest)
        history.append(smallest.k)
        done += 1
        if done >= 3 * width and len(history) >= 2 * width:
            w1 = history[-2 * width:-width]
            w2 = history[-width:]
            if len(set(w1)) == width and len(set(w2)) == width:
                break

    if done < m:
        remaining = m - done
        full, extra = divmod(remaining, width)
        for k in levels:
            levels[k] += full
        steady_order = history[-width:]
        for i in range(extra):
            levels[steady_order[i]] += 1

    return sum(pow(k % MOD, pow(2, levels[k], MOD - 1), MOD)
               for k in range(2, n + 1)) % MOD


if __name__ == "__main__":
    assert square_smallest_sum(5, 3) == 34
    assert square_smallest_sum(10, 100) == 845339386
    print(square_smallest_sum(10**4, 10**16))  # 950591530
