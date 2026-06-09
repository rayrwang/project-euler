import numba

N = 1504170715041707
M = 4503599627370517

@numba.jit(cache=True)
def forward_coins(threshold):
    """Eulercoins found by walking n upward until the value drops below threshold.

    value(n) = N*n mod M, tracked incrementally. Record every strict new minimum
    (an Eulercoin); these are the large-valued coins, reached at small n.
    """
    coins = []
    v = 0
    best = M
    n = 0
    while best >= threshold:
        n += 1
        v += N
        if v >= M:
            v -= M
        if v < best:
            best = v
            coins.append(v)
    return coins

@numba.jit(cache=True)
def reverse_coins(threshold, n_inv):
    """Eulercoins with value < threshold, via the step at which a value appears.

    Value c first occurs at step n_c = c * N^{-1} mod M, tracked incrementally as
    c increases. c is an Eulercoin exactly when n_c beats every earlier n_{c'},
    i.e. n_c is a strict new minimum. These are the small-valued coins.
    """
    coins = []
    nc = 0
    best_n = M
    for c in range(1, threshold):
        nc += n_inv
        if nc >= M:
            nc -= M
        if nc < best_n:
            best_n = nc
            coins.append(c)
    return coins

def sum_eulercoins():
    threshold = 20_000_000
    n_inv = pow(N, -1, M)
    values = set(forward_coins(threshold)) | set(reverse_coins(threshold, n_inv))
    return sum(values)

if __name__ == "__main__":
    print(sum_eulercoins())  # 1517926517777556
