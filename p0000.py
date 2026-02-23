
if __name__ == "__main__":
    s = 0
    FIRST_N_SQUARES = 213_000
    for i in range(1, FIRST_N_SQUARES, 2):
        s += i**2
    print(s)  # 1610599499964500
