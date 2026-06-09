from fractions import Fraction
from math import comb

if __name__ == "__main__":
    # 70 balls: 7 colours, 10 of each. Seven are picked... actually 20 are taken;
    # find the expected number of distinct colours among the 20 chosen balls.
    # By linearity, each colour is present with probability 1 - C(60,20)/C(70,20)
    # (the complement being "none of that colour's 10 balls is chosen"), so the
    # expected count is 7 times that.
    expected = 7 * (Fraction(1) - Fraction(comb(60, 20), comb(70, 20)))
    print(f"{float(expected):.9f}")  # 6.818741802
