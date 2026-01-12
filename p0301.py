
import numba

@numba.jit
def X(n1, n2, n3):
    return n1 ^ n2 ^ n3

@numba.jit
def count_X_zero():
    count = 0
    for n in range(1, int(2**30)+1):
        if X(n, 2*n, 3*n) == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(count_X_zero())  # 2178309
