import numba

from funcs import is_prime


@numba.jit(cache=True)
def digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


@numba.jit(cache=True)
def total(limit: int) -> int:
    """Sum of strong, right truncatable Harshad primes below `limit`.

    Right truncatable Harshad (RTH) numbers form a tree rooted at 1..9:
    every RTH number is a shorter one with a digit appended.  Grow the tree
    level by level; whenever a node h is strong (h / digitsum(h) prime),
    the primes among its ten extensions 10h + d qualify.
    """
    level = [h for h in range(1, 10)]
    s = 0
    while level:
        nxt = []
        for h in level:
            if is_prime(h // digit_sum(h)):  # h is Harshad, division is exact
                for d in range(10):
                    cand = 10 * h + d
                    if cand < limit and is_prime(cand):
                        s += cand
            for d in range(10):
                child = 10 * h + d
                if child >= limit:
                    break
                if child % digit_sum(child) == 0:
                    nxt.append(child)
        level = nxt
    return s


if __name__ == "__main__":
    assert total(10**4) == 90619
    print(total(10**14))  # 696067597313468
