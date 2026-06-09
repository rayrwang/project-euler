import numba

from funcs import prime_sieve_bool


@numba.jit(cache=True)
def sum_s(is_prime) -> int:
    """Sum of S(p) = (sum_{k=1}^5 (p-k)!) mod p over primes 5 <= p < len.

    By Wilson's theorem (p-1)! == -1 (mod p), and dividing successively gives
    (p-k)! == (-1)^k / (k-1)! (mod p). Hence
        S(p) == -1 + 1 - 1/2 + 1/6 - 1/24 == -3/8 (mod p).
    Solving 8x == -3 (mod p) gives a closed form depending on p mod 8:
        p==1: (3p-3)/8,  p==3: (p-3)/8,  p==5: (7p-3)/8,  p==7: (5p-3)/8.
    """
    total = 0
    for p in range(5, len(is_prime)):
        if is_prime[p]:
            r = p & 7
            if r == 1:
                m = 3
            elif r == 3:
                m = 1
            elif r == 5:
                m = 7
            else:  # r == 7
                m = 5
            total += (m * p - 3) // 8
    return total


def solve(limit: int) -> int:
    return int(sum_s(prime_sieve_bool(limit)))


if __name__ == "__main__":
    assert solve(100) == 480
    print(solve(10**8))  # 139602943319822
