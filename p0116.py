
from functools import cache

@cache
def count_tiles(n, size):
    """For n contiguous squares"""
    if n < size:
        return 0
    if n == size:
        return 1
    count = 0
    for start in range(n-size+1):
        count += 1 + count_tiles(n-size-start, size)
    return count

if __name__ == "__main__":
    print(count_tiles(50, 2) + count_tiles(50, 3) + count_tiles(50, 4))  # 20492570929
