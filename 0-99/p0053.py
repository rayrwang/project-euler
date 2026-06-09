
from funcs import nCr

def count_greater():
    count = 0
    for n in range(1, 100+1):
        for r in range(n+1):
            if nCr(n, r) > 1_000_000:
                count += 1
    return count

if __name__ == "__main__":
    print(count_greater())  # 4075
