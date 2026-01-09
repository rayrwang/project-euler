
import numba

from funcs import count_divisors

@numba.jit
def triangle():
    sum = 0
    next = 1
    while True:
        sum += next
        next += 1
        yield sum

if __name__ == "__main__":
    for t in triangle():
        if count_divisors(t) > 500:
            break
    print(t)  # 76576500
