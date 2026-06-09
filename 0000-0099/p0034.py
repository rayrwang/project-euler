
import numba

from funcs import fact_bounded as fact

@numba.jit
def sum_fact_digits(n):
    s = 0
    while n != 0:
        s += fact(n % 10)
        n //= 10
    return s

@numba.jit
def sum_sfd():
    s = 0
    for i in range(3, 7*fact(9)):  # 8 digits is too long
        if sum_fact_digits(i) == i:
            s += i
    return s

if __name__ == "__main__":
    print(sum_sfd())  # 40730
