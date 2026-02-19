
from functools import cache

@cache
def count_tiles(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2
    count = 1
    for start in range(n-3+1):
        for length in range(3, n-start+1):
            count += count_tiles(n-start-length-1)
    return count

if __name__ == "__main__":
    print(count_tiles(50))  # 16475640049
