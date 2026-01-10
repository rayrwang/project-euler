
from funcs import totient

if __name__ == "__main__":
    max_ratio_n = None
    max_ratio = 0
    for n in range(2, 1_000_000+1):
        if n / totient(n) > max_ratio:
            max_ratio = n / totient(n)
            max_ratio_n = n
    print(max_ratio_n)  # 510510
