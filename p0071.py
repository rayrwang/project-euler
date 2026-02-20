
from funcs import gcd

if __name__ == "__main__":
    target = 3/7
    smallest_diff = float("inf")
    n_smallest = None
    for d in range(2, 1_000_000):
        for n in range(int(d*target), 1-1, -1):
            if gcd(n, d) == 1:
                diff = target - n/d
                if 0 < diff < smallest_diff:
                    smallest_diff = diff
                    n_smallest = n
                break
    print(n_smallest)  # 428570
