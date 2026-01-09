
import numba

from funcs import fact

def sum_fact_digits():
    s = 0
    for i in range(3, 7*fact(9)):  # 8 digits is too long
        if sum([fact(int(digit)) for digit in str(i)]) == i:
            s += i
    return s

if __name__ == "__main__":
    print(sum_fact_digits())  # 40730
