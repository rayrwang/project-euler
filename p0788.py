
from funcs import nCr, mod_add

modulus = 1_000_000_007

if __name__ == "__main__":
    count = 0
    for n_digits in range(1, 2022+1):
        for repeat in range(n_digits//2 + 1, n_digits + 1):
            # Not replacing first digit
            if repeat < n_digits:
                count = mod_add(
                    count,
                    9 * 9 * nCr(n_digits-1, repeat) * 9**(n_digits-1-repeat),
                    modulus)
                #   ^ first digit can be 1 to 9   
                #       ^ repeating digits can't be same as first digit
                #           ^ possibilities for where repeating digits are
                #                                     ^ remaining digits

            # Replacing first digit
            count = mod_add(
                count,
                9 * nCr(n_digits-1, repeat-1) * 9**((n_digits-1) - (repeat-1)),
                modulus)
            #   ^ repeating digits can be 1 to 9
            #       ^ possibilities for repeating digits, given one of them is first digit
            #                                   ^ remaining digits
    print(count)  # 471745499
