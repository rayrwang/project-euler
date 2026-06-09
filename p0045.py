from funcs import is_square

def is_pentagonal(p):
    # p = n(3n-1)/2  =>  n = (1 + sqrt(1 + 24p)) / 6 must be a positive integer
    disc = 1 + 24 * p
    return is_square(disc) and (1 + int(disc**0.5)) % 6 == 0

if __name__ == "__main__":
    # Every hexagonal number H_n = n(2n-1) = T_{2n-1} is already triangular,
    # so only check hexagonals (starting past H_143 = 40755) for pentagonality.
    n = 144
    while True:
        h = n * (2 * n - 1)
        if is_pentagonal(h):
            print(h)  # 1533776805
            break
        n += 1
