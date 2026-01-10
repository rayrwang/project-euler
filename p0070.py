
import numba

from funcs import totient

if __name__ == "__main__":
    min_ratio = float("inf")
    min_ratio_n = None
    for n in range(1, int(1e7)):
        phi = totient(n)
        # If they are permutations of each other
        if sorted(str(phi)) == sorted(str(n)):
            ratio = n / phi
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_n = n
    print(min_ratio_n)  # 8319823
