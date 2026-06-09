"""Project Euler 981.

Same "neutral string" setup as Problem 980. A string over {x, y, z} is neutral
iff its letter counts share a common parity AND
    inv(s) + C(n_x, 2) + C(n_y, 2) + C(n_z, 2)   is even,
where inv(s) counts inversions for the order x < y < z.

So among the multiset permutations with X, Y, Z copies (all of one parity, else
N = 0), neutral ones are those of a fixed inversion parity. With
    T = multinomial(X+Y+Z; X, Y, Z)            (total arrangements)
    S = sum over arrangements of (-1)^inv       (signed count)
the neutral count is (T + eps*S) / 2 with eps = +1 when C(X,2)+C(Y,2)+C(Z,2) is
even and -1 otherwise.

S is the Gaussian multinomial at q = -1, which factors into q-binomials:
    S = qbin(X | Y+Z)_{-1} * qbin(Y | Z)_{-1},
and a q-binomial at -1 obeys the q = -1 phenomenon:
    [m+n choose n]_{-1} = C(floor((m+n)/2), floor(n/2))  unless m, n are both odd
    (in which case it is 0).

Everything is needed only modulo the prime 888888883, and the largest argument
3 * 87^3 stays below the modulus, so plain factorial tables suffice.
"""
P = 888_888_883

def solve():
    NMAX = 3 * 87 ** 3
    fact = [1] * (NMAX + 1)
    for i in range(1, NMAX + 1):
        fact[i] = fact[i - 1] * i % P
    inv_fact = [1] * (NMAX + 1)
    inv_fact[NMAX] = pow(fact[NMAX], P - 2, P)
    for i in range(NMAX, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % P
    inv2 = pow(2, P - 2, P)

    def C(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % P * inv_fact[n - k] % P

    def qbin_m1(n, m):                       # [m+n choose n] at q = -1
        if (n & 1) and (m & 1):
            return 0
        return C((m + n) // 2, n // 2)

    def Nmod(X, Y, Z):
        if not (X % 2 == Y % 2 == Z % 2):
            return 0
        T = fact[X + Y + Z] * inv_fact[X] % P * inv_fact[Y] % P * inv_fact[Z] % P
        S = qbin_m1(X, Y + Z) * qbin_m1(Y, Z) % P
        cs = ((X * (X - 1) // 2) + (Y * (Y - 1) // 2) + (Z * (Z - 1) // 2)) & 1
        val = (T + S) if cs == 0 else (T - S)
        return val % P * inv2 % P

    cubes = [i ** 3 for i in range(88)]
    total = 0
    for X in cubes:
        for Y in cubes:
            for Z in cubes:
                total += Nmod(X, Y, Z)
        total %= P
    return total % P

if __name__ == "__main__":
    print(solve())  # 794963735
