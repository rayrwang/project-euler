
from functools import cache

@cache
def count_sums_recurse(n, rem, nxt):
    if rem == 0:  # Found a sum
        return 1
    if nxt > rem:  # No more possible sums
        return 0
    if nxt == n:  # Not allowed sum of length 1
        return 0
        
    count = 0
    for multiple in range(0, (rem//nxt) + 1):
        count += count_sums_recurse(n, rem - multiple*nxt, nxt+1)
    return count

def count_sums(n):
    return count_sums_recurse(n, n, 1)

if __name__ == "__main__":
    print(count_sums(100))  # 190569291
