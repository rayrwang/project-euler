import numba
import numpy as np

A = 25214903917  # Rand48 multiplier
C = 11  # Rand48 increment
MASK48 = (1 << 48) - 1


def encode(s: str) -> np.ndarray:
    """Map characters to b-values: a..z -> 0..25, A..Z -> 26..51."""
    return np.array(
        [ord(ch) - 97 if ch.islower() else 26 + ord(ch) - 65 for ch in s],
        dtype=np.int64,
    )


@numba.jit(cache=True)
def find_state(target: np.ndarray) -> int:
    """The unique 48-bit Rand48 state whose next 9 outputs equal `target`.

    Writing a = xlo + 2^18 * y with xlo < 2^18, the value (a_k mod 4) of each
    output depends only on bits 16-17 of a_k, hence only on xlo; the nine mod-4
    conditions pin xlo down to (essentially) one value out of 2^18. For each
    surviving xlo the high 30 bits y are searched, with the first output's mod-13
    condition fixing y modulo 13 (since b_0 mod 13 is affine in y), cutting the
    scan by a factor of 13. All products are taken mod 2^48 via uint64 masking,
    which is exact because multiplication mod 2^64 preserves the low 48 bits.
    """
    a_mul = np.uint64(A)
    c_inc = np.uint64(C)
    m18 = np.uint64((1 << 18) - 1)
    mask = np.uint64(MASK48)
    step18 = np.uint64(1 << 18)
    sixteen = np.uint64(16)
    fiftytwo = np.uint64(52)

    for xlo in range(1 << 18):
        a = np.uint64(xlo)
        ok = True
        for k in range(9):
            if int((a >> sixteen) & np.uint64(3)) != (target[k] & 3):
                ok = False
                break
            a = (a_mul * a + c_inc) & m18
        if not ok:
            continue

        w0 = (xlo >> 16) & 3
        y0 = (10 * (target[0] - w0)) % 13  # 10 = inverse of 4 mod 13
        if y0 < 0:
            y0 += 13
        base = np.uint64(xlo)
        y = y0
        while y < (1 << 30):
            state = base + step18 * np.uint64(y)
            a = state & mask
            good = True
            for k in range(9):
                if int((a >> sixteen) % fiftytwo) != target[k]:
                    good = False
                    break
                a = (a_mul * a + c_inc) & mask
            if good:
                return int(state)
            y += 13
    return -1


def _state_after(n: int, a0: int) -> int:
    """State after n Rand48 steps from a0: x -> A x + C iterated, mod 2^48."""
    m, c = 1, 0  # affine map x -> m x + c
    bm, bc = A, C
    while n > 0:
        if n & 1:
            m, c = (m * bm) & MASK48, (bm * c + bc) & MASK48
        bm, bc = (bm * bm) & MASK48, (bm * bc + bc) & MASK48
        n >>= 1
    return (m * a0 + c) & MASK48


def solve_gap(a0: int, astar: int) -> int:
    """Smallest n >= 0 with the n-th Rand48 iterate of a0 equal to astar.

    The affine map x -> A x + C has full period 2^48 (Hull-Dobell), so the step
    count is unique modulo 2^k once states agree modulo 2^k. Lift bit by bit:
    given n mod 2^k, exactly one of n or n + 2^k matches astar modulo 2^(k+1).
    """
    n = 0
    for k in range(48):
        modmask = (1 << (k + 1)) - 1
        cand = n
        if (_state_after(cand, a0) & modmask) != (astar & modmask):
            cand = n + (1 << k)
        n = cand
    return n


def solve() -> int:
    a0 = int(find_state(encode("PuzzleOne")))  # state generating "PuzzleOne..."
    astar = int(find_state(encode("LuckyText")))  # state generating "LuckyText..."
    return solve_gap(a0, astar)


if __name__ == "__main__":
    print(solve())  # 9300900470636
