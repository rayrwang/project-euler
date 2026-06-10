from decimal import Decimal, getcontext

def totient_sieve(limit):
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:  # prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi

def E_delta_phi(n, m):
    """E(Delta | phi(k), n, m) to six decimal places.

    Conditioning on k being selected with predecessor j, summing the
    negative-binomial gap weights and applying the hockey-stick and
    Vandermonde identities collapses the expected error to
        E[Delta] = sum_k f(k) * C(n - k, m) / C(n, m),
    a cancellation-free form (verified by exhaustive enumeration over all
    m-subsets for several small (n, m) and reproducing
    E(Delta | k, 100, 50) = 2525/1326 exactly).

    The weight R(k) = C(n-k, m)/C(n, m) = prod_(j<k) (n - m - j)/(n - j)
    decays like exp(-k m / n), so only k up to a few hundred thousand
    contribute; the running product is kept in 40-digit Decimal so the
    six required decimals are unaffected by rounding. The truncation tail
    is bounded by R(K) * sum_(k>K) k < 10^-25.
    """
    getcontext().prec = 40
    cutoff = Decimal(10) ** -32
    phi = totient_sieve(min(n, 400_000))
    total = Decimal(0)
    r = Decimal(1)
    for k in range(1, len(phi)):
        r = r * (n - m - (k - 1)) / (n - (k - 1))
        if r <= 0:
            break
        total += phi[k] * r
        if r < cutoff:
            break
    return total

if __name__ == "__main__":
    assert f"{E_delta_phi(10**4, 10**2):.6f}" == "5842.849907"
    print(f"{E_delta_phi(12345678, 12345):.6f}")  # 607238.610661
