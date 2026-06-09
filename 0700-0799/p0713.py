N = 10**7

def solve(n):
    """T(N, m) is the least number of fuse pairs to test so that, whichever m
    fuses work, some tested pair is all-working. Equivalently it is the minimum
    number of edges on N vertices meeting every m-subset, i.e. the Turan-type
    covering number: split N into k = m - 1 almost-equal parts and sum C(s_i, 2)
    over the parts. With q = floor(N / k) this collapses to
        T = q * N - k * q * (q + 1) / 2,
    so L(N) = sum_{k=1}^{N-1} (q*N - k*q*(q+1)/2) is evaluated over the O(sqrt N)
    blocks on which q = floor(N / k) is constant.
    """
    total = 0
    k = 1
    while k <= n - 1:
        q = n // k
        khi = n // q
        if khi > n - 1:
            khi = n - 1
        cnt = khi - k + 1
        sum_k = (k + khi) * cnt // 2
        total += q * n * cnt - q * (q + 1) // 2 * sum_k
        k = khi + 1
    return total

if __name__ == "__main__":
    print(solve(N))  # 788626351539895
