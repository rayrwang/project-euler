
from funcs import inf_range, is_prime

if __name__ == "__main__":
    prime_i = 1
    for n in inf_range(start=3, step=2):
        if is_prime(n):
            prime_i += 1
        if prime_i == 10_001:
            break
    print(n)  # 104743
