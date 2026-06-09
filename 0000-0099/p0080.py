
# Not fun to use `decimal`

from funcs import is_square

def sum_root_digits(n):
    target = n
    guess = int(n**0.5)
    for i in range(99):
        target *= 100  # Only using ints
        guess *= 10
        for next_digit in range(0, 10+1):
            if (guess + next_digit)*(guess + next_digit) > target:
                guess += next_digit - 1
                break
    return sum([int(digit) for digit in str(guess)])

if __name__ == "__main__":
    s = 0
    for n in range(100+1):
        if not is_square(n):
            s += sum_root_digits(n)
    print(s)  # 40886
