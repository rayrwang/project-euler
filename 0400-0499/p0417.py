import numba
import numpy as np

@numba.jit(cache=True)
def spf_sieve(n: int) -> np.ndarray:
    """Smallest prime factor for every integer up to n."""
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    return spf

@numba.jit(cache=True)
def mod_pow32(a: int, b: int, p: int) -> int:
    r = 1
    a %= p
    while b > 0:
        if b & 1:
            r = r * a % p
        a = a * a % p
        b >>= 1
    return r

@numba.jit(cache=True)
def gcd64(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

@numba.jit(cache=True)
def cycle_length_sum(n_max: int) -> int:
    """Sum of L(n) for 3 <= n <= n_max, where L(n) is the recurring-cycle
    length of 1/n (zero when n has no prime factors besides 2 and 5).

    L(n) is the multiplicative order of 10 modulo n with all factors of 2
    and 5 removed, which is the lcm of the orders modulo the prime powers
    of n. So: for every prime p (not 2 or 5), get ord_p(10) by starting
    from p - 1 and dividing out prime factors (via an SPF sieve) while 10
    to the reduced exponent stays 1; lift to ord_{p^k}(10), which is the
    previous order times 1 or p; and for each prime power q = p^k fold the
    order into L[m] by lcm for every m exactly divisible by q. Numbers of
    the form 2^a 5^b keep the initial value 1 and are corrected at the end.
    """
    spf = spf_sieve(n_max)
    cyc = np.ones(n_max + 1, dtype=np.int32)
    for p in range(3, n_max + 1):
        if spf[p] != p or p == 5:
            continue
        # multiplicative order of 10 mod p: reduce p - 1 prime by prime
        e = p - 1
        rem = p - 1
        while rem > 1:
            q = spf[rem]
            while rem % q == 0:
                rem //= q
            while e % q == 0 and mod_pow32(10, e // q, p) == 1:
                e //= q
        o = e
        pk = p
        while True:
            # fold ord(10 mod p^k) into every m with p^k exactly dividing m
            for m in range(pk, n_max + 1, pk):
                if (m // pk) % p != 0:
                    g = gcd64(cyc[m], o)
                    cyc[m] = cyc[m] // g * o
            if pk > n_max // p:
                break
            pk *= p
            if mod_pow32(10, o, pk) != 1:
                o *= p  # order grows by exactly a factor p per level
    total = 0
    for m in range(3, n_max + 1):
        total += cyc[m]
    # remove the placeholder 1 for terminating fractions n = 2^a 5^b
    two = 1
    while two <= n_max:
        five = two
        while five <= n_max:
            if five >= 3:
                total -= 1
            if five > n_max // 5:
                break
            five *= 5
        if two > n_max // 2:
            break
        two *= 2
    return total

if __name__ == "__main__":
    assert cycle_length_sum(10) == 1 + 0 + 1 + 6 + 0 + 1 + 0  # L(3..10)
    assert cycle_length_sum(10**6) == 55535191115  # given in the problem
    print(cycle_length_sum(10**8))  # 446572970925740
