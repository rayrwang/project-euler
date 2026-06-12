import numba

# Choosing disk (i, j) flips row j and column i, so a multiset of choices s
# flips disk (x, y) exactly R_y + C_x - s(x, y) times (row and column sums
# of s).  Ending all-white needs s(x, y) = b(x, y) xor u_x xor v_y with
# u_x = C_x, v_y = R_y mod 2, and the column-sum consistency conditions.
#
# For even N these force the unique solution u_x = Bcol_x xor B,
# v_y = Brow_y xor B (B the total black parity), so T(N) just counts the
# ones of b(x, y) xor p_x xor q_y with p, q the column and row parities.
# For odd N the u_x cancel and consistency instead demands that all column
# parities agree and all row parities agree (otherwise unsolvable), leaving
# sum u_x and sum v_y fixed mod 2 and everything else free.  Since every
# black column of C_N is far shorter than N/2, any extra flipped column or
# row only adds cost, so the minimum is sum b when the parity is even, and
# otherwise flips exactly the last column and row (the longest arc column,
# with the corner cell white):  T = sum b + 2N - 2 - 4 L_(N-1).  Both
# branches are verified against exhaustive minimisation for N <= 17.
#
# The annulus is handled in O(N): the black cells of column x form the
# interval [lo(x), hi(x)] with both ends nonincreasing in x, so the column
# lengths, their parities q_y, and the windowed sums of q over [lo, hi]
# are all maintained by monotone pointers in amortised constant time.

@numba.jit(cache=True)
def crossflips(n):
    n2 = n * n - 1  # hi(t) = isqrt(n^2 - 1 - t^2)
    m2 = (n - 1) * (n - 1)  # lo(t) = ceil(sqrt(m2 - t^2))

    if n % 2 == 1:
        # parity of every column length must agree
        hi = n - 1
        lo = n - 1
        total = 0
        parity = -1
        l_last = 0
        for t in range(n):
            t2 = t * t
            while hi * hi > n2 - t2:
                hi -= 1
            rem = m2 - t2
            while lo > 0 and (lo - 1) * (lo - 1) >= rem:
                lo -= 1
            length = hi - lo + 1 if hi >= lo else 0
            if parity < 0:
                parity = length & 1
            elif length & 1 != parity:
                return 0
            total += length
            l_last = length
        if parity == 0:
            return total
        return total + 2 * n - 2 - 4 * l_last

    # even N: T = #{(x, y) : b(x, y) xor p_x xor q_y = 1}, accumulated as
    # sum_x sign_x (L_x - 2 W1_x) + N n1 + Wtot (n0 - n1) where W1_x counts
    # odd rows inside the column-x interval and Wtot all odd rows.
    hi = n - 1
    lo = n - 1
    # suffix accumulators S(y) = sum_{y' >= y} q_{y'} at the two window ends
    y_lo = n  # A_lo = S(y_lo), stepped down to lo(x)
    a_lo = 0
    lo_t_hi = 0  # trackers computing L_y for the y_lo evaluator
    lo_t_lo = 0
    y_hi = n  # A_hi = S(y_hi), stepped down to hi(x) + 1
    a_hi = 0
    hi_t_hi = 0
    hi_t_lo = 0
    c1 = 0
    n1 = 0
    for t in range(n):
        t2 = t * t
        while hi * hi > n2 - t2:
            hi -= 1
        rem = m2 - t2
        while lo > 0 and (lo - 1) * (lo - 1) >= rem:
            lo -= 1
        length = hi - lo + 1 if hi >= lo else 0
        while y_lo > lo:  # extend the bottom suffix sum down to lo
            y_lo -= 1
            y2 = y_lo * y_lo
            while (lo_t_hi + 1) * (lo_t_hi + 1) <= n2 - y2:
                lo_t_hi += 1
            r2 = m2 - y2
            while lo_t_lo * lo_t_lo < r2:
                lo_t_lo += 1
            ly = lo_t_hi - lo_t_lo + 1 if lo_t_hi >= lo_t_lo else 0
            a_lo += ly & 1
        while y_hi > hi + 1:  # shrink the top suffix sum down to hi + 1
            y_hi -= 1
            y2 = y_hi * y_hi
            while (hi_t_hi + 1) * (hi_t_hi + 1) <= n2 - y2:
                hi_t_hi += 1
            r2 = m2 - y2
            while hi_t_lo * hi_t_lo < r2:
                hi_t_lo += 1
            ly = hi_t_hi - hi_t_lo + 1 if hi_t_hi >= hi_t_lo else 0
            a_hi += ly & 1
        w1 = a_lo - a_hi
        if length & 1:
            n1 += 1
            c1 -= length - 2 * w1
        else:
            c1 += length - 2 * w1
    wtot = a_lo  # by x = N - 1 the bottom pointer has reached y = 0
    return c1 + n * n1 + wtot * (n - 2 * n1)

@numba.jit(cache=True)
def total():
    assert crossflips(5) == 3
    assert crossflips(10) == 29
    assert crossflips(1000) == 395253
    res = 0
    for i in range(3, 32):
        res += crossflips((1 << i) - i)
    return res

if __name__ == "__main__":
    print(total())  # 467178235146843549
