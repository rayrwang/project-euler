P = 982451653  # the 50-millionth prime, the required modulus


def solve(n_max: int) -> int:
    """sum of f(n) * m(n) for 1 <= n <= n_max, modulo P.

    f(n) is the maximum product of a partition of n into distinct parts and
    m(n) the number of parts achieving it. The optimal partition is built
    from the consecutive block {2, 3, ..., k} for the largest k with
    S_k = 2 + 3 + ... + k <= n, then the surplus r = n - S_k (which ranges
    over 0..k) is absorbed:
        r = 0            -> {2, ..., k},                product k!
        1 <= r <= k - 1  -> drop (k+1-r), add (k+1),    product k!(k+1)/(k+1-r)
        r = k            -> drop 2, add (k+2),          product k!(k+2)/2
    In every case the count of parts is m = k - 1 (verified against a
    brute-force search). The block for a given k therefore covers the k+1
    consecutive values n = S_k .. S_k + k, with S_k = k(k+1)/2 - 1.

    Summing f*m over a whole block collapses to a closed form. The middle
    cases give k!(k+1) * sum_{j=2}^{k} 1/j = k!(k+1)(H_k - 1) with H_k the
    harmonic number, so maintaining k! and H_k modulo P incrementally makes
    the whole computation O(sqrt(n_max)). Modular inverses are precomputed
    in one linear pass. Only the final block can be partial, where the sum
    is taken over r = 0..(n_max - S_k) directly.

    n = 1 is the lone exception (f(1) = m(1) = 1), and the block k = 2
    cleanly accounts for n = 2, 3, 4.
    """
    # Largest k with S_k <= n_max, where S_k = k(k+1)/2 - 1.
    k_max = int((2 * n_max) ** 0.5) + 2
    while k_max * (k_max + 1) // 2 - 1 > n_max:
        k_max -= 1

    # inv[i] = i^{-1} mod P for i = 1..k_max+2 via inv[i] = -(P//i) inv[P%i].
    inv = [0] * (k_max + 3)
    inv[1] = 1
    for i in range(2, k_max + 3):
        inv[i] = (P - (P // i) * inv[P % i]) % P

    total = 1 % P  # the n = 1 term
    fact = 2 % P  # k! for the current k, starting at 2! = 2
    harm = inv[2]  # H_k - 1 = sum_{j=2}^{k} 1/j, here for k = 2
    inv2 = inv[2]
    k = 2
    while True:
        s_k = k * (k + 1) // 2 - 1
        if s_k > n_max:
            break
        rmax = min(k, n_max - s_k)
        if rmax == k:
            block = fact  # r = 0
            block += fact * (k + 1) % P * harm  # middle cases
            block += fact * inv2 % P * (k + 2)  # r = k
        else:
            block = fact  # r = 0
            for r in range(1, rmax + 1):
                block += fact * (k + 1) % P * inv[k + 1 - r] % P
        total = (total + block % P * ((k - 1) % P)) % P
        k += 1
        fact = fact * k % P
        harm = (harm + inv[k]) % P
    return total % P


if __name__ == "__main__":
    # sum_{1<=n<=100} f(n)*m(n) = 1683550844462 (given), reduced mod P.
    assert solve(100) == 1683550844462 % P
    print(solve(10**14))  # 334420941
