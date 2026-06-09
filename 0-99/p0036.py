

if __name__ == "__main__":
    s = 0
    for n in range(1, 1_000_000):
        bin_str = bin(n)[2:]
        if str(n) == str(n)[::-1] and bin_str == bin_str[::-1]:
            s += n
    print(s)  # 872187
