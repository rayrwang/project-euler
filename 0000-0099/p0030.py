
if __name__ == "__main__":
    s = 0
    for n in range(2, 6*9**5):  # 7 digits is too long
        sum_fifth_pow = sum([int(digit)**5 for digit in str(n)])
        if sum_fifth_pow == n:
            s += n
    print(s)  # 443839
