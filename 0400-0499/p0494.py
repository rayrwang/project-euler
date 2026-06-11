"""Project Euler 494: Collatz Prefix Families.

A "prefix" is a Collatz trajectory up to (excluding) its first power of two;
two prefixes are in the same family if they are order-isomorphic. f(m)
counts families among length-m prefixes; find f(90).

Theory (Albert, Gudmundsson, Ulfarsson, "Collatz meets Fibonacci",
arXiv:1404.3054): a prefix is encoded by its up/down step type - a word with
no consecutive u's ending in d - and there are Fib(m) types of length m. A
type with k u's is realized exactly at witnesses A = 2^a with a in a single
residue class mod 2 * 3^k, the trace elements being linear functions of A.
Each type yields at most two order types: all witnesses past the first
exceed 2^(2*3^k) > 3^k, which bounds every line-crossing abscissa, so they
share the asymptotic (slope-ordered) permutation. Hence
f(m) = Fib(m) + e_m, where e_m counts "excess" types whose FIRST witness
realization is ordered differently from slope order. A first witness 2^a
with a > 2 * 3^k also exceeds the crossing bound, so excess requires a small
first witness; scanning witnesses 2^6 .. 2^20 finds no excess realizations
(consistent with the paper's observation that the integrality constant is
always 16), leaving the witness A = 16, i.e. traces ending at element 5.

So e_m = number of backward Collatz paths from 5 of length m (predecessors
2v always, and (v-1)/3 when v = 4 mod 6, excluding powers of two) whose
values are NOT ordered like their slopes 2^Q / 3^P (P, Q = suffix step
counts). The slope key Q - P log2(3) is safe in floats: the no-uu constraint
gives P <= 45, where the worst convergent gap |65 - 41 log2 3| ~ 0.0165.
The enumeration (~1.2 * 10^9 paths of length 90, ~5 * 10^9 nodes) runs in
numba with 128-bit values emulated as uint64 pairs, an inversion test
against a Pareto staircase (max value over smaller slope keys) maintained
with an undo log, forced-move fusion (branching only at v = 4 mod 6), and
an O(1) shortcut for v = 0 mod 3 subtrees (eternal doubling chains).

The machinery reproduces the paper's full excess table e_15..e_32
(1,2,3,3,4,6,7,9,12,15,19,24,30,39,49,61,77,96), the given f(5) = 5,
f(10) = 55, f(20) = 6771, and forum-verified f(25), f(30), f(35), f(40).
"""

import numpy as np
from numba import njit

L3 = 1.5849625007211562  # log2(3)
K64 = np.uint64(6148914691236517205)  # (2^64 - 1) // 3
M1 = np.uint64(0xFFFFFFFFFFFFFFFF)


@njit(cache=True)
def run(mmax, root_hi, root_lo):
    """Backward DFS from a root value; per-length path and mismatch counts."""
    cap = mmax + 8
    skap = np.zeros(cap, np.float64)  # staircase: kappa asc, value asc
    svh = np.zeros(cap, np.uint64)
    svl = np.zeros(cap, np.uint64)
    ns = 0
    lop = np.zeros(cap * 4, np.int64)  # undo log
    lloi = np.zeros(cap * 4, np.int64)
    lk = np.zeros(cap * 4, np.int64)
    lpp = np.zeros(cap * 4, np.int64)
    nlog = 0
    pk = np.zeros(cap * 4, np.float64)  # removed-stair payload
    ph = np.zeros(cap * 4, np.uint64)
    pl = np.zeros(cap * 4, np.uint64)
    npay = 0

    f_vh = np.zeros(mmax + 4, np.uint64)  # branch frames
    f_vl = np.zeros(mmax + 4, np.uint64)
    f_kap = np.zeros(mmax + 4, np.float64)
    f_dep = np.zeros(mmax + 4, np.int64)
    f_mm = np.zeros(mmax + 4, np.uint8)
    f_br = np.zeros(mmax + 4, np.int64)
    f_log = np.zeros(mmax + 4, np.int64)
    nframes = 0

    counts = np.zeros(mmax + 2, np.int64)
    mcounts = np.zeros(mmax + 2, np.int64)

    cvh = root_hi
    cvl = root_lo
    ckap = 0.0 - L3
    cdep = 1
    cmm = np.uint8(0)
    mode = 0

    while True:
        if mode == 0:
            while True:
                if cmm == 0 and ns > 0:
                    loi, hii = 0, ns
                    while loi < hii:
                        mid = (loi + hii) // 2
                        if skap[mid] < ckap:
                            loi = mid + 1
                        else:
                            hii = mid
                    if loi > 0 and (
                        svh[loi - 1] > cvh
                        or (svh[loi - 1] == cvh and svl[loi - 1] > cvl)
                    ):
                        cmm = np.uint8(1)
                counts[cdep] += 1
                if cmm:
                    mcounts[cdep] += 1
                if cdep == mmax:
                    mode = 1
                    break
                m3 = (cvh % np.uint64(3) + cvl % np.uint64(3)) % np.uint64(3)
                if m3 == np.uint64(0):
                    # v = 0 mod 3: eternal forced-doubling chain to mmax
                    if cmm == 0 and ns > 0:
                        th = cvh
                        tl = cvl
                        tk = ckap
                        mxh = svh[ns - 1]
                        mxl = svl[ns - 1]
                        for _ in range(cdep + 1, mmax + 1):
                            th2 = (th << np.uint64(1)) | (tl >> np.uint64(63))
                            tl = tl << np.uint64(1)
                            th = th2
                            tk += 1.0
                            if th > mxh or (th == mxh and tl > mxl):
                                break  # above all stairs forever after
                            loi, hii = 0, ns
                            while loi < hii:
                                mid = (loi + hii) // 2
                                if skap[mid] < tk:
                                    loi = mid + 1
                                else:
                                    hii = mid
                            if loi > 0 and (
                                svh[loi - 1] > th
                                or (svh[loi - 1] == th and svl[loi - 1] > tl)
                            ):
                                cmm = np.uint8(1)
                                break
                    for d in range(cdep + 1, mmax + 1):
                        counts[d] += 1
                        if cmm:
                            mcounts[d] += 1
                    mode = 1
                    break
                if cmm == 0:
                    # insert current element into staircase (undo-logged)
                    loi, hii = 0, ns
                    while loi < hii:
                        mid = (loi + hii) // 2
                        if skap[mid] < ckap:
                            loi = mid + 1
                        else:
                            hii = mid
                    if loi == ns:
                        skap[ns] = ckap
                        svh[ns] = cvh
                        svl[ns] = cvl
                        ns += 1
                        lop[nlog] = 0
                        nlog += 1
                    else:
                        k = 0
                        j = loi
                        while j < ns and (
                            svh[j] < cvh or (svh[j] == cvh and svl[j] <= cvl)
                        ):
                            k += 1
                            j += 1
                        lop[nlog] = 1
                        lloi[nlog] = loi
                        lk[nlog] = k
                        lpp[nlog] = npay
                        for t in range(k):
                            pk[npay] = skap[loi + t]
                            ph[npay] = svh[loi + t]
                            pl[npay] = svl[loi + t]
                            npay += 1
                        nlog += 1
                        if k == 0:
                            for t in range(ns, loi, -1):
                                skap[t] = skap[t - 1]
                                svh[t] = svh[t - 1]
                                svl[t] = svl[t - 1]
                            ns += 1
                        elif k > 1:
                            for t in range(loi + k, ns):
                                skap[t - k + 1] = skap[t]
                                svh[t - k + 1] = svh[t]
                                svl[t - k + 1] = svl[t]
                            ns -= k - 1
                        skap[loi] = ckap
                        svh[loi] = cvh
                        svl[loi] = cvl
                if m3 == np.uint64(1) and (cvl & np.uint64(1)) == np.uint64(0):
                    f_vh[nframes] = cvh
                    f_vl[nframes] = cvl
                    f_kap[nframes] = ckap
                    f_dep[nframes] = cdep
                    f_mm[nframes] = cmm
                    f_br[nframes] = 0
                    f_log[nframes] = nlog
                    nframes += 1
                    mode = 1
                    break
                cvh = (cvh << np.uint64(1)) | (cvl >> np.uint64(63))
                cvl = cvl << np.uint64(1)
                ckap += 1.0
                cdep += 1
        else:
            if nframes == 0:
                break
            fi = nframes - 1
            b = f_br[fi]
            target = f_log[fi]
            while nlog > target:  # unwind between siblings and at pop
                nlog -= 1
                if lop[nlog] == 0:
                    ns -= 1
                else:
                    loi = lloi[nlog]
                    k = lk[nlog]
                    pp = lpp[nlog]
                    if k == 0:
                        for t in range(loi, ns - 1):
                            skap[t] = skap[t + 1]
                            svh[t] = svh[t + 1]
                            svl[t] = svl[t + 1]
                        ns -= 1
                    else:
                        if k > 1:
                            for t in range(ns - 1, loi, -1):
                                skap[t + k - 1] = skap[t]
                                svh[t + k - 1] = svh[t]
                                svl[t + k - 1] = svl[t]
                            ns += k - 1
                        for t in range(k):
                            skap[loi + t] = pk[pp + t]
                            svh[loi + t] = ph[pp + t]
                            svl[loi + t] = pl[pp + t]
                    npay = pp
            if b >= 2:
                nframes -= 1
                continue
            f_br[fi] = b + 1
            h = f_vh[fi]
            lo = f_vl[fi]
            if b == 0:
                cvh = (h << np.uint64(1)) | (lo >> np.uint64(63))
                cvl = lo << np.uint64(1)
                ckap = f_kap[fi] + 1.0
            else:
                if lo == np.uint64(0):
                    wh = h - np.uint64(1)
                    wl = M1
                else:
                    wh = h
                    wl = lo - np.uint64(1)
                r = wh % np.uint64(3)
                cvh = wh // np.uint64(3)
                q2 = wl // np.uint64(3)
                rem2 = wl % np.uint64(3)
                cvl = r * K64 + q2 + (r + rem2) // np.uint64(3)
                ckap = f_kap[fi] - L3
                if cvh == np.uint64(0) and cvl < np.uint64(3):
                    continue
            cdep = f_dep[fi] + 1
            cmm = f_mm[fi]
            mode = 0
    return counts, mcounts


def run_root(mmax, root):
    hi, lo = divmod(root, 1 << 64)
    return run(mmax, np.uint64(hi), np.uint64(lo))


if __name__ == "__main__":
    counts, mcounts = run_root(42, 5)
    expect_e = {
        15: 1, 16: 2, 17: 3, 18: 3, 19: 4, 20: 6, 21: 7, 22: 9, 23: 12,
        24: 15, 25: 19, 26: 24, 27: 30, 28: 39, 29: 49, 30: 61, 31: 77,
        32: 96, 33: 122, 34: 155, 35: 194, 36: 244, 37: 311, 38: 394,
        39: 498, 40: 627, 41: 792, 42: 1000,
    }
    for m in range(2, 15):
        assert int(mcounts[m]) == 0
    for m in range(15, 43):
        assert int(mcounts[m]) == expect_e[m]
    fib = [0, 1]
    for _ in range(2, 95):
        fib.append(fib[-1] + fib[-2])
    assert fib[5] + int(mcounts[5]) == 5  # f(5)
    assert fib[10] + int(mcounts[10]) == 55  # f(10)
    assert fib[20] + int(mcounts[20]) == 6771  # f(20)
    assert fib[25] + int(mcounts[25]) == 75044  # f(25), forum-verified
    assert fib[30] + int(mcounts[30]) == 832101
    assert fib[35] + int(mcounts[35]) == 9227659
    assert fib[40] + int(mcounts[40]) == 102334782
    # no excess realizations from witnesses 2^6 .. 2^20
    for a in range(6, 21, 2):
        t_root = (2**a - 1) // 3
        if t_root & (t_root - 1) == 0:
            continue
        _, mc = run_root(40, t_root)
        assert int(mc.sum()) == 0
    _, mcounts90 = run_root(90, 5)
    print(fib[90] + int(mcounts90[90]))  # 2880067194446832666
