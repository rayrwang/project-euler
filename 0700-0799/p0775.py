from math import isqrt

MOD = 10**9 + 7

def ceil_2sqrt_partial_sum(big):
    """Sum of ceil(2 sqrt(k)) for k = 1..big, in closed form.

    ceil(2 sqrt k) = floor(2 sqrt k) + 1 unless 4k is a perfect square
    (i.e. k is a square), and floor(2 sqrt k) >= j exactly when
    k >= ceil(j^2 / 4), so with j_max = floor(2 sqrt(big)) the floor sum is
    sum_j (big - ceil(j^2/4) + 1); the ceil(j^2/4) sum closes via
    4 ceil(j^2/4) = j^2 + 3 [j odd].
    """
    j = isqrt(4 * big)
    sq = j * (j + 1) * (2 * j + 1) // 6
    csum = (sq + 3 * ((j + 1) // 2)) // 4
    floor_sum = j * (big + 1) - csum
    return floor_sum + big - isqrt(big)

def G(n):
    """Sum of g(m) = 6m - (min surface area of an m-cube polycube), m <= n.

    The optimal polycube grows as a quasi-cube: from the box a*a*a, add a
    layer on an a x a face, then an a x (a+1) face, then an (a+1) x (a+1)
    face, reaching (a+1)^3. A partial layer of k cells is a 2D-optimal
    polyomino (max adjacency 2k - ceil(2 sqrt k), realizable inside the
    near-square face), so with M = number of adjacent cube pairs,
        M(box + k) = M(box) + 3k - ceil(2 sqrt k),
    and g = 2M. Summing M over each layer needs only k-sums of
    ceil(2 sqrt k), done in closed form, so the whole computation is O(1)
    per layer -- about 3 n^(1/3) layers in total.
    """
    msum = 0  # sum over m = 1..n of M(m)
    m_box = 0
    done = 1  # cells placed so far (the 1x1x1 box)
    a = 1
    while done < n:
        for (p, q) in ((a, a), (a, a + 1), (a + 1, a + 1)):
            big = p * q
            k = min(big, n - done)
            msum += k * m_box + 3 * k * (k + 1) // 2 - ceil_2sqrt_partial_sum(k)
            done += k
            m_box += 3 * big - (p + q)
            if done >= n:
                break
        a += 1
    return (2 * msum) % MOD

if __name__ == "__main__":
    assert G(18) == 530
    assert G(10**6) == 951640919
    print(G(10**16))  # 946791106
