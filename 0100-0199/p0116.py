
from functools import cache

@cache
def count_tiles(n, size):  # Include empty case
    if n < size:
        return 1
    if n == size:
        return 2
    count = 1  # Empty case
    for start in range(n-size+1):
        count += count_tiles(n-size-start, size)
    return count

def count_tiles_no_empty(n, size):
    return count_tiles(n, size) - 1

if __name__ == "__main__":
    print(count_tiles_no_empty(50, 2)  # 20492570929
        + count_tiles_no_empty(50, 3)
        + count_tiles_no_empty(50, 4))
