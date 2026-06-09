from itertools import product
from math import factorial

if __name__ == "__main__":
    f10 = factorial(10)
    f9 = factorial(9)

    # A double pandigital number has 20 digits (each of 0..9 twice). Split the
    # positions by the parity of their power of ten into two groups of ten. Since
    # 10 ≡ -1 (mod 11), divisibility by 11 needs even_sum - odd_sum ≡ 0 (mod 11);
    # with even_sum + odd_sum = 90 this forces even_sum ≡ 1 (mod 11).
    # k[d] = number of copies of digit d placed in the even-power group.
    total = 0
    leading_zero = 0
    for k in product((0, 1, 2), repeat=10):
        if sum(k) != 10:
            continue
        if sum(d * k[d] for d in range(10)) % 11 != 1:
            continue
        prod_even = 1
        prod_odd = 1
        for d in range(10):
            prod_even *= factorial(k[d])
            prod_odd *= factorial(2 - k[d])
        arr_even = f10 // prod_even
        total += arr_even * (f10 // prod_odd)

        # the leading digit sits in the odd-power group; remove the arrangements
        # that place a 0 there
        zeros_odd = 2 - k[0]
        if zeros_odd >= 1:
            prod_odd9 = factorial(zeros_odd - 1)
            for d in range(1, 10):
                prod_odd9 *= factorial(2 - k[d])
            leading_zero += arr_even * (f9 // prod_odd9)

    print(total - leading_zero)  # 194505988824000
