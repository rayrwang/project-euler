
from functools import cache

@cache
def F(m, n):
    if n <= m-1:
        return 1
    if n == m:
        return 2
    count = 1
    for start in range(n-m+1):
        for length in range(m, n-start+1):
            count += F(m, n-start-length-1)
    return count

if __name__ == "__main__":
    for n in range(1<<62):
        if F(50, n) > 1_000_000:
            break
    print(n)  # 168
