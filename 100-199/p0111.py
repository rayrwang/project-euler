from itertools import combinations, product

from funcs import is_prime


def solve(n: int = 10) -> int:
    total = 0
    for d in range(10):
        # try the largest possible count of digit d first, descending
        for m in range(n, 0, -1):
            free = n - m  # positions holding a digit != d
            found: set[int] = set()
            for pos in combinations(range(n), free):
                for fill in product(range(10), repeat=free):
                    if any(x == d for x in fill):
                        continue
                    digits = [d] * n
                    for p, x in zip(pos, fill):
                        digits[p] = x
                    if digits[0] == 0:
                        continue
                    num = int("".join(map(str, digits)))
                    if is_prime(num):
                        found.add(num)
            if found:
                total += sum(found)
                break
    return total


if __name__ == "__main__":
    print(solve())  # 612407567715
