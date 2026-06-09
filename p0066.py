from math import isqrt

def fundamental_x(d):
    """Smallest x with x^2 - d*y^2 = 1, read off the convergents of sqrt(d)."""
    a0 = isqrt(d)
    m, den, a = 0, 1, a0
    h_prev, h = 1, a0   # convergent numerators h_{-1}, h_0
    k_prev, k = 0, 1    # convergent denominators k_{-1}, k_0
    while h * h - d * k * k != 1:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den
        h_prev, h = h, a * h + h_prev
        k_prev, k = k, a * k + k_prev
    return h

if __name__ == "__main__":
    best_d, best_x = 0, 0
    for d in range(2, 1001):
        r = isqrt(d)
        if r * r == d:           # perfect squares have no solution
            continue
        x = fundamental_x(d)
        if x > best_x:
            best_x, best_d = x, d
    print(best_d)  # 661
