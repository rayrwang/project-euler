# A(m, n) = 2 (up-arrow)^(m-2) (n + 3) - 3 for m >= 2 (checked against the
# recursive definition for small arguments). So A(0..3, same) = 1, 3, 7, 61
# exactly, A(4, 4) = 2^^7 - 3, while A(5, 5) = 2^^^8 - 3 and
# A(6, 6) = 2^^^^9 - 3 are both 2^^h - 3 for astronomically large h - and
# 2^^h mod M is eventually constant in h, because each level of the
# phi-chain of M = 14^8 collapses to 1 within ~35 steps. The tetration is
# computed with the generalised Euler theorem, 2^T = 2^(T mod phi + phi)
# (valid since the exponents here are at least 65536 > log2 M), exactly for
# heights <= 4. Stability is verified by comparing heights 50 and 60.


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


def _tower_mod(h: int, mod: int) -> int:
    if mod == 1:
        return 0
    if h <= 4:
        return (2, 4, 16, 65536)[h - 1] % mod
    ph = _phi(mod)
    return pow(2, _tower_mod(h - 1, ph) + ph, mod)


def solve(mod: int = 14**8) -> int:
    stable = _tower_mod(50, mod)
    assert stable == _tower_mod(60, mod)
    small = 1 + 3 + 7 + 61  # A(0,0) .. A(3,3)
    return (small + (_tower_mod(7, mod) - 3) + 2 * (stable - 3)) % mod


if __name__ == "__main__":
    print(solve())  # 1098988351
