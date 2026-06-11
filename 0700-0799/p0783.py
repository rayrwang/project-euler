def E(n, k):
    """Expectation of sum of B_t^2, where B_t is the number of black balls
    removed on turn t.

    Track e1 = E[X_t] and e2 = E[X_t^2] for X_t, the number of black balls
    in the urn at the start of turn t. With K = X_t + k black among
    N = k(n - t + 2) balls after the k black balls are added, the draw of
    m = 2k balls is hypergeometric, so conditionally on K:
        E[B] = mK/N,  E[B(B-1)] = m(m-1) K(K-1) / (N(N-1)),
        E[KB] = m K^2 / N,
    and X_{t+1} = K - B_t closes the recursion on the first two moments.
    """
    m = 2 * k
    e1 = 0.0  # E[X_t]
    e2 = 0.0  # E[X_t^2]
    total = 0.0
    for t in range(1, n + 1):
        size = float(k * (n - t + 2))
        k1 = e1 + k  # E[K]
        k2 = e2 + 2 * k * e1 + k * k  # E[K^2]
        b1 = m * k1 / size  # E[B_t]
        b2 = m * (m - 1) * (k2 - k1) / (size * (size - 1)) + b1  # E[B_t^2]
        total += b2
        # X_{t+1} = K - B_t
        kb = m * k2 / size  # E[K B_t]
        e1 = k1 - b1
        e2 = k2 - 2 * kb + b2
    return total

if __name__ == "__main__":
    assert abs(E(2, 2) - 9.6) < 1e-12
    print(round(E(10**6, 10)))  # 136666597
