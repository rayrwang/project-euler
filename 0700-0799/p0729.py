import numba
import numpy as np

@numba.njit(cache=True)
def solve_rotation(signs, d, x0, nplain):
    """Unique fixed point of the inverse-branch composition
    g_{s_0} o g_{s_1} o ... o g_{s_{d-1}}, where g_+(b) and g_-(b) are the
    positive and negative preimages (b +- sqrt(b^2+4))/2 of Boole's map.
    Both branches are strict contractions, so plain iteration converges
    from anywhere; Newton (using the product of branch derivatives)
    polishes to machine precision."""
    x = x0
    for _ in range(nplain):
        y = x
        for i in range(d - 1, -1, -1):
            rt = (y * y + 4.0) ** 0.5
            y = 0.5 * (y + rt) if signs[i] == 1 else 0.5 * (y - rt)
        x = y
    for _ in range(40):
        y = x
        dphi = 1.0
        for i in range(d - 1, -1, -1):
            rt = (y * y + 4.0) ** 0.5
            if signs[i] == 1:
                dphi *= 0.5 * (1.0 + y / rt)
                y = 0.5 * (y + rt)
            else:
                dphi *= 0.5 * (1.0 - y / rt)
                y = 0.5 * (y - rt)
        f = y - x
        if abs(f) < 1e-13:
            break
        x = x - f / (dphi - 1.0)
    return x

@numba.njit(cache=True)
def S(P):
    """Sum of ranges over all periodic sequences of a_{n+1} = a_n - 1/a_n
    with (minimal) period at most P.

    The map is Boole's transformation: every b has exactly two preimages,
    one positive and one negative, so a periodic orbit is determined by
    its sign itinerary, and orbits of exact period d correspond
    bijectively to primitive binary necklaces of length d (the
    inverse-branch composition along the word is a contraction with a
    unique fixed point; the constant words drift to +-infinity, matching
    the absence of fixed points). Orbit values stay bounded (|a| <= ~7
    for d <= 25, growing like sqrt of the run length), and bounded away
    from 0 (|a| >= 1/8 since |T(a)| <= 8).

    For each Lyndon representative the rotation-0 point is solved from
    scratch; the other d-1 orbit points warm-start from T(previous) and
    need only a couple of Newton steps. Each of the d points of an orbit
    is its own sequence, so an orbit adds d * (max - min). Kahan
    summation keeps the ~6.7e7-term sum accurate to the 4 required
    decimals. Reproduces S(2) = 2 sqrt 2, S(3) ~ 14.6461,
    S(5) ~ 124.1056.
    """
    total = 0.0
    comp = 0.0
    sgn = np.empty(64, dtype=np.int64)
    rot = np.empty(64, dtype=np.int64)
    for d in range(2, P + 1):
        for mask in range(1, (1 << d) - 1):
            ok = True
            primitive = True
            for r in range(1, d):
                rm = ((mask >> r) | (mask << (d - r))) & ((1 << d) - 1)
                if rm < mask:
                    ok = False
                    break
                if rm == mask:
                    primitive = False
                    break
            if not ok or not primitive:
                continue
            for i in range(d):
                sgn[i] = (mask >> i) & 1
            for i in range(d):
                rot[i] = sgn[i]
            x = solve_rotation(rot, d, 0.0, 30)
            mn = x
            mx = x
            prev = x
            for r in range(1, d):
                for i in range(d):
                    rot[i] = sgn[(r + i) % d]
                x = solve_rotation(rot, d, prev - 1.0 / prev, 0)
                mn = min(mn, x)
                mx = max(mx, x)
                prev = x
            term = d * (mx - mn)
            t = total + term
            if abs(total) >= abs(term):
                comp += (total - t) + term
            else:
                comp += (term - t) + total
            total = t
    return total + comp

if __name__ == "__main__":
    assert f"{S(2):.4f}" == "2.8284"
    assert f"{S(3):.4f}" == "14.6461"
    assert f"{S(5):.4f}" == "124.1056"
    print(f"{S(25):.4f}")  # 308896374.2502
