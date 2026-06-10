import numba
import numpy as np

from funcs import prime_sieve_int


@numba.jit(cache=True)
def _total_score(primes: np.ndarray) -> int:
    """Sum over trie nodes of max(#next-bit-0, #next-bit-1).

    A node is a set of primes sharing their low L bits, all known to
    extend past bit L (the game is still running).  The optimal player
    guesses the majority value of bit L; primes whose bit L is their
    leading 1 then leave the game, and the rest split into two children.
    The array segment for a node is partitioned in place.
    """
    arr = primes.copy()
    scratch = np.empty_like(arr)
    total = 0
    # DFS stack of (start, end, bit index)
    stack = np.empty((200, 3), dtype=np.int64)
    stack[0] = (0, len(arr), 0)
    top = 1
    while top:
        top -= 1
        s, e, bit = stack[top]
        c1 = 0
        for i in range(s, e):
            c1 += (arr[i] >> bit) & 1
        c0 = e - s - c1
        total += max(c0, c1)
        # partition: bit-0 primes, then bit-1 primes that continue
        lo = 0
        hi = c0
        for i in range(s, e):
            p = arr[i]
            if (p >> bit) & 1:
                if p >> (bit + 1):  # not the leading bit; game goes on
                    scratch[hi] = p
                    hi += 1
            else:
                scratch[lo] = p
                lo += 1
        arr[s : s + hi] = scratch[:hi]
        if c0:
            stack[top] = (s, s + c0, bit + 1)
            top += 1
        if hi > c0:
            stack[top] = (s + c0, s + hi, bit + 1)
            top += 1
    return total


def e(n: int) -> float:
    primes = prime_sieve_int(n + 1).astype(np.int64)
    return _total_score(primes) / len(primes)


if __name__ == "__main__":
    assert e(10) == 2
    assert e(30) == 2.9
    print(f"{e(10**8):.8f}")  # 14.97696693
