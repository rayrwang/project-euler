import numba
import numpy as np

@numba.jit(cache=True)
def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    comp = np.zeros(n + 1, dtype=np.bool_)
    for p in range(2, n + 1):
        if not comp[p]:
            for j in range(p, n + 1, p):
                if j > p:
                    comp[j] = True
                mu[j] = -mu[j]
            pp = p * p
            for j in range(pp, n + 1, pp):
                mu[j] = 0
    mu[1] = 1
    return mu

@numba.jit(cache=True)
def count_nondominated(order: np.ndarray, vrank: np.ndarray,
                       nranks: int) -> int:
    """Pairs p before q in `order` with vrank[p] <= vrank[q], via a BIT."""
    bit = np.zeros(nranks + 1, dtype=np.int64)
    total = 0
    for t in range(len(order)):
        r = vrank[order[t]] + 1
        i = r
        while i > 0:  # count previous with rank <= r
            total += bit[i]
            i -= i & (-i)
        i = r
        while i <= nranks:
            bit[i] += 1
            i += i & (-i)
    return total

def balanced_interval_pairs(n: int) -> int:
    """C(n): pairs 1 <= a <= b <= n with 99 N(a,b) <= 100 P(a,b) and
    99 P(a,b) <= 100 N(a,b), where P/N count mu = +1 / -1 in [a, b].

    With prefix counts P_k, N_k, both conditions become the dominance
    U_{a-1} <= U_b and V_{a-1} <= V_b for U = 100P - 99N, V = 100N - 99P.
    Since U_k + V_k = P_k + N_k never decreases, any dominating pair of
    distinct (U, V) values automatically has the earlier index first, and
    equal (U, V) groups contribute each unordered pair once. So C(n) is
    the number of pairs p before q with V_p <= V_q after sorting the n+1
    prefix points lexicographically by (U, V) — a BIT count over V ranks.
    """
    mu = mobius_sieve(n)
    u = np.zeros(n + 1, dtype=np.int64)
    v = np.zeros(n + 1, dtype=np.int64)
    p_cnt = n_cnt = 0
    for k in range(1, n + 1):
        if mu[k] == 1:
            p_cnt += 1
        elif mu[k] == -1:
            n_cnt += 1
        u[k] = 100 * p_cnt - 99 * n_cnt
        v[k] = 100 * n_cnt - 99 * p_cnt
    order = np.lexsort((v, u)).astype(np.int64)
    uniq_v = np.unique(v)
    vrank = np.searchsorted(uniq_v, v).astype(np.int64)
    return count_nondominated(order, vrank, len(uniq_v))

def brute(n: int) -> int:
    mu_list = [0, 1]
    for k in range(2, n + 1):
        m = 1
        kk = k
        d = 2
        ok = True
        while d * d <= kk:
            if kk % d == 0:
                kk //= d
                if kk % d == 0:
                    ok = False
                    break
                m = -m
            d += 1
        if not ok:
            mu_list.append(0)
        else:
            if kk > 1:
                m = -m
            mu_list.append(m)
    total = 0
    for a in range(1, n + 1):
        pc = nc = 0
        for b in range(a, n + 1):
            if mu_list[b] == 1:
                pc += 1
            elif mu_list[b] == -1:
                nc += 1
            if 99 * nc <= 100 * pc and 99 * pc <= 100 * nc:
                total += 1
    return total

if __name__ == "__main__":
    assert balanced_interval_pairs(10) == brute(10) == 13
    assert balanced_interval_pairs(500) == brute(500) == 16676
    assert balanced_interval_pairs(10**4) == 20155319  # given
    print(balanced_interval_pairs(2 * 10**7))  # 198775297232878
