
import sys

sys.set_int_max_str_digits(1_000_000)

def fib():
    x1 = 0
    x2 = 1
    nxt = x2
    while True:
        yield nxt
        x1, x2 = x2, (nxt := x1 + x2)

def fib_tail():
    x1 = 0
    x2 = 1
    nxt = x2
    while True:
        yield nxt
        x1, x2 = x2, (nxt := (x1 + x2) % 1_000_000_000)

def find_fib():
    for k, (f, ft) in enumerate(zip(fib(), fib_tail()), start=1):
        ft_str = str(ft)
        if len(ft_str) == 9:
            last_nine = set(ft_str)
            last_nine.discard("0")
            if len(last_nine) == 9:
                f_str = str(f)
                first_nine = set(f_str[:9])
                first_nine.discard("0")
                if len(first_nine) == 9:
                    break
    return k

if __name__ == "__main__":
    print(find_fib())  # 329468
