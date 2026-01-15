
from funcs import is_prime

from functools import cache

def next_prime(n):
    for i in range(n+1, 1<<62):
        if is_prime(i):
            return i

@cache
def count_prime_sums_recurse(n, rem, nxt):
    if rem == 0:  # Found a sum
        return 1
    if nxt > rem:  # No more possible sums
        return 0
    if nxt == n:  # Not allowed sum of length 1
        return 0
        
    count = 0
    for multiple in range(0, (rem//nxt) + 1):
        count += count_prime_sums_recurse(n, rem - multiple*nxt, next_prime(nxt))
    return count

def count_prime_sums(n):
    return count_prime_sums_recurse(n, n, 2)

if __name__ == "__main__":
    for n in range(10, 1<<62):
        if count_prime_sums(n) > 5_000:
            break
    print(n)  # 71
