import numpy as np
import numba

from funcs import totient_sieve

@numba.jit(cache=True)
def search(phi):
    N = phi.shape[0]
    best_n = -1
    best_num = 1   # best ratio so far = best_num / best_den
    best_den = 0   # a zero denominator stands in for +infinity
    cnt = np.zeros(10, dtype=np.int64)
    for n in range(2, N):
        ph = phi[n]
        # A permutation preserves digit sum, so n == phi(n) (mod 9) is necessary.
        if (n - ph) % 9 != 0:
            continue
        for d in range(10):
            cnt[d] = 0
        a = n
        while a > 0:
            cnt[a % 10] += 1
            a //= 10
        b = ph
        while b > 0:
            cnt[b % 10] -= 1
            b //= 10
        is_perm = True
        for d in range(10):
            if cnt[d] != 0:
                is_perm = False
                break
        if is_perm:
            # n/ph < best_num/best_den  <=>  n*best_den < best_num*ph
            if best_den == 0 or n * best_den < best_num * ph:
                best_num = n
                best_den = ph
                best_n = n
    return best_n

if __name__ == "__main__":
    N = 10**7
    phi = totient_sieve(N)
    print(search(phi))  # 8319823
