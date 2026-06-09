import numba

from funcs import is_prime

MOD = 76543217

@numba.jit(cache=True)
def gnomon_count(m: int, n: int, mod: int) -> int:
    """LC(m, n) mod a prime: numberings of the m x m grid minus its
    top-right n x n corner, increasing downward and leftward.

    Rotating the gnomon 180 degrees and complementing the entries turns a
    valid numbering into a standard Young tableau of the straight shape
    lambda = (m repeated m-n times, then m-n repeated n times), so the hook
    length formula applies: LC = N! / prod(hooks) with N = m^2 - n^2.
    Both N and every hook length are below the modulus, so nothing
    vanishes mod p and a single modular inverse finishes the job.
    """
    nn = m * m - n * n
    fact = 1
    for i in range(2, nn + 1):
        fact = fact * i % mod
    hooks = 1
    for i in range(m):  # rows; lengths m for i < m-n, else m-n
        row = m if i < m - n else m - n
        for j in range(row):
            col = m if j < m - n else m - n  # column heights
            h = (row - j) + (col - i) - 1
            hooks = hooks * h % mod
    # modular inverse by Fermat
    inv = 1
    e = mod - 2
    b = hooks
    while e > 0:
        if e & 1:
            inv = inv * b % mod
        b = b * b % mod
        e >>= 1
    return fact * inv % mod

def gnomon_count_exact(m: int, n: int) -> int:
    """Exact LC(m, n) by the same hook length formula, for the checks."""
    from math import factorial
    hooks = 1
    for i in range(m):
        row = m if i < m - n else m - n
        for j in range(row):
            col = m if j < m - n else m - n
            hooks *= (row - j) + (col - i) - 1
    nn = m * m - n * n
    assert factorial(nn) % hooks == 0
    return factorial(nn) // hooks

if __name__ == "__main__":
    assert is_prime(MOD)  # hook formula mod p needs p prime and p > N
    assert gnomon_count_exact(3, 0) == 42
    assert gnomon_count_exact(5, 3) == 250250
    assert gnomon_count_exact(6, 3) == 406029023400
    assert gnomon_count(10, 5, MOD) == 61251715
    print(gnomon_count(10000, 5000, MOD))  # 38788800
