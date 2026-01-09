
from funcs import sum_proper_divisors

def is_abundant(n):
    return sum_proper_divisors(n) > n

if __name__ == "__main__":
    s = 0
    for n in range(28123):
        for i in range(n):
            if is_abundant(i) and is_abundant(n-i):
                break
        else:
            s += n
    print(s)  # 4179871
