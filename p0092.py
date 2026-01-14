
import numba

@numba.jit
def sum_square_digits(n):
    s = 0
    while n != 0:
        s += (n % 10)**2
        n //= 10
    return s

@numba.jit
def count_89():
    count = 0
    for n in range(1, 10_000_000):
        while True:
            if n == 1:
                break
            if n == 89:
                count += 1
                break
            n = sum_square_digits(n)
    return count

if __name__ == "__main__":
    print(count_89())  # 8581146
