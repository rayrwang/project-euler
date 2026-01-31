
from funcs import find_prime_factors_set as find_prime_factors

if __name__ == "__main__":
    consecutive = 0
    for n in range(1, 1<<62):
        if len(find_prime_factors(n)) == 4:
            consecutive += 1
        else:
            consecutive = 0
        if consecutive == 4:
            break
    print(n-3)  # 134043
