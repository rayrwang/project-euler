"""Project Euler Problem 666: Polymorphic Bacteria.

Species S_{k,m} has k types; a type-i bacterium picks j uniform in
[0, m), reads q = r_{i m + j} mod 5 (r_0 = 306, r_{n+1} = r_n^2 mod
10007), and then: q=0 die; q=1 clone (-> two type i); q=2 mutate (->
one type 2i mod k); q=3 split into three of type i^2+1 mod k; q=4 spawn
(-> type i plus type i+1 mod k).  P_{k,m} is the extinction probability
starting from one alpha_0; find P_{500,10}.

This is a multitype branching process.  Let x_i be the probability that
a lineage seeded by a single type-i bacterium eventually dies out.  By
first-step analysis over the m equally likely choices,

    x_i = (1/m) sum_{j<m} g_q(x),   q = r_{i m + j} mod 5,

    g_0 = 1,            g_1 = x_i^2,        g_2 = x_{2i mod k},
    g_3 = x_{i^2+1}^3,  g_4 = x_i x_{i+1}.

The required extinction probability is the minimal nonnegative fixed
point of this monotone system, obtained by iterating from x = 0 (the
iterates increase monotonically to the minimal root).  Convergence is
linear, so a couple thousand sweeps -- accelerated by in-place Gauss
-Seidel updates -- pin down eight decimals; types feeding only into the
q=0/clone structure converge fastest and the rest follow.

Checks: a Monte-Carlo-free exact match against the given P_{2,2} =
0.07243802, P_{4,3} = 0.18554021, P_{10,5} = 0.53466253, plus the single
-type sanity that S_{2,2} reproduces the stated 0.07243802 for alpha.
"""


def r_table(n: int) -> list[int]:
    r = [306]
    for _ in range(n):
        r.append(r[-1] * r[-1] % 10007)
    return r


def extinction(k: int, m: int) -> float:
    r = r_table(k * m + 1)
    # precompute, for each type i, the list of q-actions over j
    actions = [[r[i * m + j] % 5 for j in range(m)] for i in range(k)]
    x = [0.0] * k
    inv_m = 1.0 / m
    for _ in range(200000):
        diff = 0.0
        for i in range(k):
            s = 0.0
            xi = x[i]
            for q in actions[i]:
                if q == 0:
                    s += 1.0
                elif q == 1:
                    s += xi * xi
                elif q == 2:
                    s += x[(2 * i) % k]
                elif q == 3:
                    t = x[(i * i + 1) % k]
                    s += t * t * t
                else:
                    s += xi * x[(i + 1) % k]
            new = s * inv_m
            d = new - x[i]
            if d > diff:
                diff = d
            x[i] = new  # Gauss-Seidel: use updated values immediately
            xi = new
        if diff < 1e-13:
            break
    return x[0]


if __name__ == "__main__":
    assert round(extinction(2, 2), 8) == 0.07243802
    assert round(extinction(4, 3), 8) == 0.18554021
    assert round(extinction(10, 5), 8) == 0.53466253
    print(f"{extinction(500, 10):.8f}")  # 0.48023168
