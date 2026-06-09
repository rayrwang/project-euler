
from funcs import sum_proper_divisors as d

if __name__ == "__main__":
    s = 0
    for a in range(1, 10000):
        b = d(a)
        if b != a and d(b) == a:
            s += a
    print(s)  # 31626
