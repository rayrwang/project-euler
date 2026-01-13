
import numba

from funcs import fact_bounded as fact

@numba.jit
def digit_fact_sum(n):
    s = 0
    while n != 0:
        s += fact(n % 10)
        n //= 10
    return s

@numba.jit
def count_60():
    count = 0
    for start in range(1_000_000):
        terms = []
        t = start
        while t not in terms:
            terms.append(t)
            t = digit_fact_sum(t)
        non_repeating = len(terms)
        if non_repeating == 60:
            count += 1
    return count

if __name__ == "__main__":
    print(count_60())  # 402
