def _num_divisors(m: int, add2: int, add5: int) -> int:
    e2, e5 = add2, add5
    while m % 2 == 0:
        m //= 2
        e2 += 1
    while m % 5 == 0:
        m //= 5
        e5 += 1
    d = (e2 + 1) * (e5 + 1)
    f = 3
    while f * f <= m:
        if m % f == 0:
            c = 0
            while m % f == 0:
                m //= f
                c += 1
            d *= c + 1
        f += 2
    if m > 1:
        d *= 2
    return d


def _count(n: int) -> int:
    # 1/a + 1/b = p/10^n. With a=g*x, b=g*y, gcd(x,y)=1, one gets xy | 10^n and
    # p = (10^n/(xy))(x+y)/g, so the number of valid g (hence solutions) for each
    # coprime pair is d((10^n/(xy))(x+y)). Coprime x,y dividing 10^n split the
    # 2-block and 5-block to one side each.
    sols = 0
    for i in range(n + 1):
        for j in range(n + 1):
            for two_to_y in (0, 1):
                if i == 0 and two_to_y == 1:
                    continue
                for five_to_y in (0, 1):
                    if j == 0 and five_to_y == 1:
                        continue
                    x = (2**i if not two_to_y else 1) * (5**j if not five_to_y else 1)
                    y = (2**i if two_to_y else 1) * (5**j if five_to_y else 1)
                    if x > y:
                        continue
                    sols += _num_divisors(x + y, n - i, n - j)
    return sols


def solve() -> int:
    return sum(_count(n) for n in range(1, 10))


if __name__ == "__main__":
    print(solve())  # 53490
