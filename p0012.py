
import numba

@numba.jit
def triangle():
    sum = 0
    next = 1
    while True:
        sum += next
        next += 1
        yield sum

@numba.jit
def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                divisors += 1
            else:
                divisors += 2
    return divisors

if __name__ == "__main__":
    for t in triangle():
        if count_divisors(t) > 500:
            break
    print(t)  # 76576500
