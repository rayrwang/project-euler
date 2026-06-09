"""Project Euler 980.

The build operations turn the letters {x, y, z} into the Klein four-group:
inserting "aa" forces a^2 = 1, the replacement x -> yz (and cyclically) forces
x = yz, and the swap makes the product commutative. So a string is reachable
from the empty string iff its letter product is trivial, i.e. the counts
n_x, n_y, n_z all share the same parity.

Requiring an *even* number of steps adds one more Z/2 invariant J that flips on
every operation. It works out to
    J(s) = inv(s) + C(n_x, 2) + C(n_y, 2) + C(n_z, 2)   (mod 2),
where inv(s) is the number of inversions for the order x < y < z. A string is
neutral iff it is reachable AND J(s) is even; this reproduces the given
N(2, 2, 2) = 42 and N(8, 8, 8) = 4732773210.

For a concatenation u v all of this is fixed by the per-string data
(n_x % 2, n_y % 2, n_z % 2, J): counts add, and
    inv(u v)              = inv(u) + inv(v) + sum_{a > b} n_a(u) n_b(v),
    sum_a C(n_a(u)+n_a(v), 2) = (...) + sum_a n_a(u) n_a(v).
Hence every c(i) collapses to one of 16 classes and F(N) is a sum over class
pairs.
"""
from collections import Counter

MOD = 888_888_883

def solve(N):
    tri2 = [(k * (k - 1) // 2) & 1 for k in range(51)]   # C(k, 2) mod 2
    cnt = Counter()
    a = 88_888_888
    first = True
    for _ in range(N):
        s0 = s1 = s2 = 0
        inv = 0
        for _ in range(50):
            if first:
                v = a % 3
                first = False
            else:
                a = (8888 * a) % MOD
                v = a % 3
            if v == 0:
                inv += s1 + s2
                s0 += 1
            elif v == 1:
                inv += s2
                s1 += 1
            else:
                s2 += 1
        J = (inv + tri2[s0] + tri2[s1] + tri2[s2]) & 1
        cnt[(s0 & 1, s1 & 1, s2 & 1, J)] += 1

    def neutral(u, v):
        ux, uy, uz, uJ = u
        vx, vy, vz, vJ = v
        if not ((ux ^ vx) == (uy ^ vy) == (uz ^ vz)):   # counts all same parity
            return False
        cross = (uy & vx) ^ (uz & vx) ^ (uz & vy)        # pairs a > b: yx, zx, zy
        dot = (ux & vx) ^ (uy & vy) ^ (uz & vz)
        return (uJ ^ vJ ^ cross ^ dot) == 0

    cls = list(cnt)
    return sum(cnt[p] * cnt[q] for p in cls for q in cls if neutral(p, q))

if __name__ == "__main__":
    print(solve(10**6))  # 124999683766
