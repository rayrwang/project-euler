import numba
import numpy as np

MOD = 10**9 + 7
D = 10**5

@numba.njit(cache=True)
def count_3like(d):
    """f(n) counts substrings of n divisible by 3. With prefix sums S_k mod 3,
    f(n) = sum_r C(c_r, 2) where c_r = #{k : S_k = r}. Since C(c,2) = 1 (mod 3)
    exactly when c = 2 (mod 3), n is 3-like iff the number of residues r with
    c_r = 2 (mod 3) is itself a multiple of 3. So only the c_r mod 3 matter.

    DP over digit positions with state (current residue, c_0 mod 3, c_1 mod 3,
    c_2 mod 3), 3 * 27 = 81 states. A digit congruent to delta mod 3 moves the
    residue and bumps the new residue's count; the leading digit avoids 0 so its
    residue weights are (3, 3, 3) instead of (4, 3, 3).
    """
    vec = np.zeros(81, np.int64)
    # S_0 = 0: current residue 0, counts (1, 0, 0).
    vec[0 * 27 + 1 * 9 + 0 * 3 + 0] = 1
    for k in range(1, d + 1):
        if k == 1:
            w0, w1, w2 = 3, 3, 3
        else:
            w0, w1, w2 = 4, 3, 3
        nv = np.zeros(81, np.int64)
        for cur in range(3):
            for a in range(3):
                for b in range(3):
                    for cc in range(3):
                        st = cur * 27 + a * 9 + b * 3 + cc
                        v = vec[st]
                        if v == 0:
                            continue
                        for delta in range(3):
                            ncur = (cur + delta) % 3
                            na, nb, ncc = a, b, cc
                            if ncur == 0:
                                na = (a + 1) % 3
                            elif ncur == 1:
                                nb = (b + 1) % 3
                            else:
                                ncc = (cc + 1) % 3
                            ns = ncur * 27 + na * 9 + nb * 3 + ncc
                            wt = w0 if delta == 0 else (w1 if delta == 1 else w2)
                            nv[ns] = (nv[ns] + v * wt) % MOD
        vec = nv
    total = 0
    for cur in range(3):
        for a in range(3):
            for b in range(3):
                for cc in range(3):
                    k = (1 if a == 2 else 0) + (1 if b == 2 else 0) + (1 if cc == 2 else 0)
                    if k % 3 == 0:
                        total = (total + vec[cur * 27 + a * 9 + b * 3 + cc]) % MOD
    return total

if __name__ == "__main__":
    print(count_3like(D))  # 884837055
