
import numba

from funcs import is_prime

@numba.jit
def count_composites():
    count = 0
    for f1 in range(2, 50_000_000):
        if is_prime(f1):
            for f2 in range(f1, 50_000_000):
                if is_prime(f2):
                    if f1 * f2 < 100_000_000:
                        count += 1
                    else:
                        break
    return count

if __name__ == "__main__":
    print(count_composites())  # 17427258
