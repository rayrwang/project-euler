
from funcs import count_digits

if __name__ == "__main__":
    count = 0
    for n_digits in range(1, 21+1):  # 9^22 only has 21 digits
        for base in range(1, 10):  # 10 is already too large as 10^1 has 2 digits
            power_digits = count_digits(base**n_digits)
            if power_digits == n_digits:
                count += 1
            elif power_digits > n_digits:
                break
    print(count)  # 49
