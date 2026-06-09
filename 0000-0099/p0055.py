
from funcs import reverse, is_palindrome

if __name__ == "__main__":
    count = 0
    for n in range(10_000):
        for _ in range(50):
            n += reverse(n)
            if is_palindrome(n):
                break
        else:
            count += 1
    print(count)  # 249
