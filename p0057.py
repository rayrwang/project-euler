
import math

from funcs import count_digits

if __name__ == "__main__":
    # Starting term is 1 + 1/2
    num_recurse = 1
    denom_recurse = 2

    more_digits = 0
    for _ in range(1000):
        # 1 + num_recurse/denom_recurse
        num = num_recurse + denom_recurse
        denom = denom_recurse
        if count_digits(num) > count_digits(denom):
            more_digits += 1
        # new = 1 / (2 + old)
        num_recurse, denom_recurse = denom_recurse, (2*denom_recurse + num_recurse)
    print(more_digits)  # 153
