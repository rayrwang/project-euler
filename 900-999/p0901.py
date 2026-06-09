"""Project Euler 901.

The driller picks an increasing sequence of depths 0 = d_0 < d_1 < d_2 < ...;
drilling to depth d_i costs d_i hours and is only reached when every earlier
drill failed, i.e. with probability P(X > d_{i-1}) = e^{-d_{i-1}}. Hence the
expected total time is

    E = sum_{i>=1} d_i * e^{-d_{i-1}}.

Setting dE/dd_j = 0 gives e^{-d_{j-1}} = d_{j+1} e^{-d_j}, i.e. the optimal
depths satisfy d_{j+1} = exp(d_j - d_{j-1}). With d_0 = 0 this is a two-point
boundary value problem (d_0 = 0, d_N -> infinity); forward shooting is unstable
because the recurrence amplifies error, so we solve the whole stationary system
at once with Newton's method, pinning d_N at a large L (the tail beyond depth L
contributes < e^{-L}). The result is 2.364497769 hours.
"""
import numpy as np

def solve(n: int, large: float) -> float:
    # Unknowns d[1..n-1]; fixed d[0] = 0 and d[n] = large.
    # Residual F_j = d_{j+1} - exp(d_j - d_{j-1}) = 0 for j = 1..n-1.
    d = np.linspace(0.0, large, n + 1)
    for _ in range(200):
        dm, dj, dp = d[0:n - 1], d[1:n], d[2:n + 1]
        ex = np.exp(dj - dm)
        f = dp - ex
        m = n - 1
        jac = np.zeros((m, m))
        for j in range(m):
            jac[j, j] += -ex[j]
            if j - 1 >= 0:
                jac[j, j - 1] += ex[j]
            if j + 1 < m:
                jac[j, j + 1] += 1.0
        step = np.linalg.solve(jac, -f)
        d[1:n] += step
        if np.max(np.abs(step)) < 1e-15:
            break
    return float(np.sum(d[1:n + 1] * np.exp(-d[0:n])))

if __name__ == "__main__":
    print(f"{solve(20, 42.0):.9f}")  # 2.364497769
