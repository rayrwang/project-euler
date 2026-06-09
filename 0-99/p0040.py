def champernowne_digit(n):
    """The n-th digit (1-indexed) of 0.123456789101112... without building it.

    Numbers with c digits form a block of 9*10^(c-1) numbers contributing
    c*9*10^(c-1) digits. Hop over whole blocks, then locate the exact number
    and the exact digit inside it.
    """
    c = 1
    block_count = 9      # how many c-digit numbers there are
    block_start = 1      # the first c-digit number
    while n > c * block_count:
        n -= c * block_count
        c += 1
        block_count *= 10
        block_start *= 10
    number = block_start + (n - 1) // c
    return int(str(number)[(n - 1) % c])

if __name__ == "__main__":
    product = 1
    for i in range(7):                  # d_1, d_10, ..., d_1000000
        product *= champernowne_digit(10**i)
    print(product)  # 210
