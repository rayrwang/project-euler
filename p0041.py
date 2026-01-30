
import itertools

from funcs import is_prime

if __name__ == "__main__":
    largest = 0
    for n in range(1, 9+1):
        for num in itertools.permutations(tuple(str(i) for i in range(1, n+1))):
            # print(num)
            num = int("".join(num))
            if is_prime(num) and num > largest:
                largest = num
    print(largest)  # 7652413
