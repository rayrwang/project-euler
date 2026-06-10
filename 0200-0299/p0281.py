from math import factorial

# Burnside over the cyclic group of the mn slices: a rotation of order d
# fixes a topping arrangement iff d divides every colour count n, and then
# the fixed arrangements are the multinomial (mn/d; n/d, ..., n/d). Hence
#     f(m, n) = (1/(mn)) sum_(d | n) phi(d) (mn/d)! / ((n/d)!)^m,
# which reproduces f(2,1) = 1, f(3,1) = 2, f(3,2) = 16. f is increasing in
# n for fixed m and f(m, 1) = (m-1)!, so a double loop over m >= 2 and
# n >= 1 with early exits collects every value below 10^15.


def _phi(n: int) -> int:
    r, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            r -= r // p
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        r -= r // x
    return r


def _f(m: int, n: int) -> int:
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += _phi(d) * factorial(m * n // d) // factorial(n // d) ** m
    assert total % (m * n) == 0
    return total // (m * n)


def solve(limit: int = 10**15) -> int:
    answer = 0
    m = 2
    while _f(m, 1) <= limit:
        n = 1
        while True:
            v = _f(m, n)
            if v > limit:
                break
            answer += v
            n += 1
        m += 1
    return answer


if __name__ == "__main__":
    print(solve())  # 1485776387445623
