import numba
import numpy as np

@numba.jit(cache=True)
def divisor_count_sieve(u: int) -> np.ndarray:
    """d[j] = number of divisors of j, for 0 <= j <= u (d[0] unused)."""
    d = np.zeros(u + 1, dtype=np.int16)  # d(j) < 800 for j <= 10^8
    for i in range(1, u + 1):
        for j in range(i, u + 1, i):
            d[j] += 1
    return d

@numba.jit(cache=True)
def s(u: int, k: int) -> int:
    """S(u,k) = sum over n=1..u-k+1 of M(n,k), where M(n,k)=max d(j) on the
    length-k window [n, n+k-1]. A monotonic deque (kept in a circular buffer of
    capacity k+1) yields each window maximum in amortised O(1)."""
    d = divisor_count_sieve(u)
    cap = k + 1
    dq = np.empty(cap, dtype=np.int64)  # indices with strictly decreasing d
    head = 0
    tail = 0  # logical counters; current size = tail - head <= k
    total = 0
    for j in range(1, u + 1):
        while tail > head and d[dq[(tail - 1) % cap]] <= d[j]:
            tail -= 1
        dq[tail % cap] = j
        tail += 1
        if dq[head % cap] <= j - k:  # drop the index that left the window
            head += 1
        if j >= k:  # a full window now ends at j
            total += d[dq[head % cap]]
    return total

if __name__ == "__main__":
    assert s(1000, 10) == 17176
    print(s(10**8, 10**5))  # 51281274340
