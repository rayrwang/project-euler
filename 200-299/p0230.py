_A = (
    "14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
)
_B = (
    "82148086513282306647093844609550582231725359408128"
    "48111745028410270193852110555964462294895493038196"
)


def _fibword_letter(counts: list[int], q: int) -> str:
    # Which block (A or B) is at 0-indexed position q of the infinite Fibonacci
    # word with F1 = A, F2 = B, F_n = F_{n-2} F_{n-1}.
    n = 1
    while counts[n] <= q:
        n += 1
    while n > 2:
        if q < counts[n - 2]:
            n -= 2
        else:
            q -= counts[n - 2]
            n -= 1
    return "A" if n == 1 else "B"


def solve() -> int:
    block = len(_A)
    positions = [(127 + 19 * n) * 7**n for n in range(18)]
    max_block = max((p - 1) // block for p in positions)
    counts = [0, 1, 1]
    while counts[-1] <= max_block + 1:
        counts.append(counts[-1] + counts[-2])

    def digit(p: int) -> int:
        q, i = (p - 1) // block, (p - 1) % block
        return int(_A[i] if _fibword_letter(counts, q) == "A" else _B[i])

    return sum(10**n * digit(positions[n]) for n in range(18))


if __name__ == "__main__":
    print(solve())  # 850481152593119296
