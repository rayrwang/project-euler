import numba

from funcs import gcd, is_prime, mul_mod_bounded

@numba.jit(cache=True)
def pollard_rho(n: int) -> int:
    """Return a nontrivial factor of composite odd n via Floyd's cycle finding."""
    if n % 2 == 0:
        return 2
    c = 1
    while True:
        x = 2
        y = 2
        d = 1
        while d == 1:
            x = (mul_mod_bounded(x, x, n) + c) % n
            y = (mul_mod_bounded(y, y, n) + c) % n
            y = (mul_mod_bounded(y, y, n) + c) % n
            diff = x - y if x > y else y - x
            d = gcd(diff, n)
        if d != n:
            return d
        c += 1

@numba.jit(cache=True)
def prime_factors(n: int) -> set[int]:
    """Distinct prime factors of n (n >= 1)."""
    fs = {n}
    fs.discard(n)  # typed empty set[int]
    stack = [n]
    while len(stack) > 0:
        m = stack.pop()
        if m <= 1:
            continue
        if is_prime(m):
            fs.add(m)
            continue
        d = pollard_rho(m)
        stack.append(d)
        stack.append(m // d)
    return fs

def g(target: int) -> int:
    """g(target) for g(4)=13, g(n)=g(n-1)+gcd(n, g(n-1))."""
    n = 4
    v = 13
    while n < target:
        c = v - n - 1
        # During a gcd==1 run, g(j-1)-j == c is constant and
        # gcd(j, g(j-1)) == gcd(j, c). The next index that breaks the run is the
        # smallest j>n sharing a prime factor with c.
        jstar = min(p * (n // p + 1) for p in prime_factors(c))
        if jstar > target:
            return v + (target - n)
        v += (jstar - 1 - n) + gcd(jstar, c)
        n = jstar
    return v

if __name__ == "__main__":
    assert g(1000) == 2524
    assert g(10**6) == 2624152
    print(g(10**15))  # 2744233049300770
