from funcs import totient_sieve

def F(N: int) -> int:
    """Maximum lattice points on a strictly convex increasing graph in [0,N]^2.

    Edges between consecutive points are distinct primitive vectors (a,b),
    a,b >= 1, of strictly increasing slope. Maximising their count under
    sum(a) <= N, sum(b) <= N greedily takes them in order of a+b. All primitive
    vectors with a+b = s number phi(s) and cost s*phi(s)/2 to each (symmetric)
    budget; after the last fully affordable level L, the leftover budget R per
    axis admits floor(2R/(L+1)) more (balanced across both axes). Points = edges + 1.
    """
    phi = totient_sieve(3_000_000)
    cost = L = count = 0
    s = 2
    while cost + s * int(phi[s]) // 2 <= N:
        cost += s * int(phi[s]) // 2
        count += int(phi[s])
        L = s
        s += 1
    extra = 2 * (N - cost) // (L + 1)
    return count + extra + 1

if __name__ == "__main__":
    print(F(10**18))  # 1398582231101
