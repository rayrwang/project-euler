def digit_sum(n: int) -> int:
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def solve(rank: int = 30) -> int:
    # A term equals base^e where base is its own digit sum (base >= 2, e >= 2,
    # value >= 10). A value below 10^16 has digit sum at most 144, bounding base.
    limit = 10**16
    found: set[int] = set()
    for base in range(2, 150):
        p = base * base
        while p <= limit:
            if p >= 10 and digit_sum(p) == base:
                found.add(p)
            p *= base
    return sorted(found)[rank - 1]


if __name__ == "__main__":
    print(solve())  # 248155780267521
