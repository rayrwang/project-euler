import numba
import numpy as np

from funcs import mul_mod_bounded

MOD = 10**18

@numba.jit(cache=True)
def perm_table() -> np.ndarray:
    """For each zero-pattern of the four sorted-digit gaps (bit i set means
    gap u_{i+1} = 0, i.e. two adjacent sorted digits are equal), the number
    of orderings 120 / prod(run!), runs being maximal blocks of equal digits."""
    fact = np.array([1, 1, 2, 6, 24, 120], dtype=np.int64)
    out = np.zeros(16, dtype=np.int64)
    for mask in range(16):
        denom = 1
        run = 1
        for i in range(4):
            if mask & (1 << i):
                run += 1
            else:
                denom *= fact[run]
                run = 1
        denom *= fact[run]
        out[mask] = 120 // denom
    return out

@numba.jit(cache=True)
def pair_count(s: int, z_left: bool, z_right: bool) -> int:
    """#(u, v) with u + v = s where a flagged variable must be 0 and an
    unflagged one must be >= 1."""
    if z_left and z_right:
        return 1 if s == 0 else 0
    if z_left or z_right:
        return 1 if s >= 1 else 0
    return s - 1 if s >= 2 else 0

@numba.jit(cache=True)
def s_of_base(b: int, perms: np.ndarray, mod: int) -> int:
    """S(b) mod `mod` for base b = 6t + 3.

    Sorting digits ascending d1 <= ... <= d5, one Kaprekar step gives
    D = x (b^4 - 1) + y (b^3 - b) with x = d5 - d1, y = d4 - d2 — the step
    depends only on (x, y). So sb(i) = 1 + F(x, y) for every non-repdigit
    i except i = C_b itself (where it is 0), with F(x, y) = 0 if
    D(x, y) = C_b and otherwise 1 + F applied to D's own statistics.
    F is filled over the O(b^2) states by path-following with memoisation.

    N(x, y), the number of i < b^5 in each class, factors over the
    zero-patterns of the sorted-digit gaps (u1, u2, u3, u4): u2 + u3 = y,
    u1 + u4 = x - y, b - x translates, and the orderings from perm_table.
    """
    t = (b - 3) // 6
    cb = ((4 * t + 2) * b**4 + (2 * t) * b**3 + (6 * t + 2) * b**2
          + (4 * t + 1) * b + (2 * t + 1))
    b4m1 = b**4 - 1
    b3mb = b**3 - b
    f = np.full(b * b, -1, dtype=np.int32)
    stack = np.empty(b * b + 8, dtype=np.int64)
    digits = np.empty(5, dtype=np.int64)
    total = 0
    for x in range(1, b):
        for y in range(x + 1):
            # --- fill F(x, y) by following the chain ---
            cur = x * b + y
            depth = 0
            base_val = -1
            while f[cur] == -1:
                f[cur] = -2  # on-stack marker (a cycle would assert below)
                stack[depth] = cur
                depth += 1
                d_val = (cur // b) * b4m1 + (cur % b) * b3mb
                if d_val == cb:
                    base_val = 0
                    break
                v = d_val
                for j in range(5):
                    digits[j] = v % b
                    v //= b
                for j in range(1, 5):  # insertion sort, 5 elements
                    key = digits[j]
                    m = j - 1
                    while m >= 0 and digits[m] > key:
                        digits[m + 1] = digits[m]
                        m -= 1
                    digits[m + 1] = key
                cur = (digits[4] - digits[0]) * b + (digits[3] - digits[1])
            if base_val == -1:
                assert f[cur] >= 0  # -2 would mean a cycle: cannot happen
                base_val = f[cur] + 1  # last pushed state is one step before
            while depth > 0:
                depth -= 1
                f[stack[depth]] = base_val
                base_val += 1
            # --- count the class and accumulate ---
            n_class = 0
            for mask in range(16):
                c_mid = pair_count(y, mask & 2 != 0, mask & 4 != 0)
                if c_mid == 0:
                    continue
                c_out = pair_count(x - y, mask & 1 != 0, mask & 8 != 0)
                if c_out != 0:
                    n_class += perms[mask] * c_mid * c_out
            n_class *= b - x
            steps = 1 + f[x * b + y]
            if n_class < (1 << 62) // steps:
                total = (total + n_class * steps) % mod
            else:  # rare: avoid int64 overflow in the product
                total = (total + mul_mod_bounded(n_class, steps, mod)) % mod
    return (total - 1) % mod  # i = C_b itself contributes 0, not 1

@numba.jit(cache=True)
def kaprekar_sum(k_lo: int, k_hi: int, mod: int) -> int:
    perms = perm_table()
    total = 0
    for k in range(k_lo, k_hi + 1):
        total = (total + s_of_base(6 * k + 3, perms, mod)) % mod
    return total

def brute_s(b: int) -> int:
    def step(i: int) -> int:
        ds = sorted((i // b**j) % b for j in range(5))
        asc = sum(d * b**j for j, d in enumerate(reversed(ds)))
        dsc = sum(d * b**j for j, d in enumerate(ds))
        return dsc - asc

    # find the constant: iterate from a non-repdigit number
    c = step(1)
    while step(c) != c or c == 0:
        c = step(c)
    steps_of = {c: 0}
    total = 0
    for i in range(1, b**5):
        ds = {(i // b**j) % b for j in range(5)}
        if len(ds) == 1:
            continue
        chain = []
        v = i
        while v not in steps_of:
            chain.append(v)
            v = step(v)
        s = steps_of[v]
        for v in reversed(chain):
            s += 1
            steps_of[v] = s
        if i != c:
            total += steps_of[i]
    return total

if __name__ == "__main__":
    perms = perm_table()
    assert s_of_base(15, perms, 10**18) == 5274369  # given
    assert brute_s(15) == 5274369
    assert s_of_base(111, perms, 10**18) == 400668930299  # given
    print(kaprekar_sum(2, 300, MOD))  # 552506775824935461
