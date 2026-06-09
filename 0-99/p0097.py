
import sys

sys.set_int_max_str_digits(3_000_000)

if __name__ == "__main__":
    print((str(28433 * 2**7830457 + 1))[-10:])  # 8739992577
