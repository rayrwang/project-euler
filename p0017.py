
BELOW_TWENTY = [
    4, 3, 3, 5, 4, 4, 3, 5, 5, 4,  # zero to nine
    3, 6, 6, 8, 8, 7, 7, 9, 8, 8   # ten to nineteen
]
TENS = [None, None, 6, 6, 5, 5, 5, 7, 6, 6]  # twenty to ninety

def count_letters(n):
    if 0 <= n <= 19:
        return BELOW_TWENTY[n]
    if 20 <= n <= 99:
        ones_digit = n % 10
        return TENS[n // 10] \
            + (BELOW_TWENTY[ones_digit] if ones_digit != 0 else 0)
    if 100 <= n <= 999:
        hundreds_digit = n // 100
        tens_and_ones_digits = n % 100
        hundreds_letters = BELOW_TWENTY[hundreds_digit] + 7  # "hundred"
        if tens_and_ones_digits == 0:
            tens_and_ones_letters = 0
        elif 1 <= tens_and_ones_digits <= 19:
            hundreds_letters += 3  # "and"
            tens_and_ones_letters = BELOW_TWENTY[tens_and_ones_digits]
        else:
            hundreds_letters += 3  # "and"
            ones_digit = tens_and_ones_digits % 10
            tens_and_ones_letters = TENS[tens_and_ones_digits // 10] \
                + (BELOW_TWENTY[ones_digit] if ones_digit != 0 else 0)
        return hundreds_letters + tens_and_ones_letters
    if n == 1000:
        return 11

if __name__ == "__main__":
    s = 0
    for n in range(1, 1000+1):
        s += count_letters(n)
    print(s)  # 21124
