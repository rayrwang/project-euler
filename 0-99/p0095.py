import numba

from funcs import proper_divisor_sum_sieve

@numba.jit(cache=True)
def longest_chain_min(sds, N):
    """Smallest member of the longest amicable chain with no element > N.

    Walk the aliquot sequence from each start. A walk that drops below start
    (its true minimum was handled earlier), exceeds N, or fails to return
    within a safe bound is not a valid chain rooted at start. The cap also
    prevents spinning forever inside a foreign cycle whose minimum exceeds
    start; no amicable chain in range is anywhere near this long.
    """
    best_len = 0
    best_min = 0
    for start in range(2, N + 1):
        x = start
        length = 0
        ok = False
        while length < 1000:
            x = sds[x]
            length += 1
            if x > N or x < start:
                break
            if x == start:
                ok = True
                break
        if ok and length > best_len:
            best_len = length
            best_min = start
    return best_min

if __name__ == "__main__":
    N = 1_000_000
    sds = proper_divisor_sum_sieve(N + 1)
    print(longest_chain_min(sds, N))  # 14316
