
from funcs import is_prime

if __name__ == "__main__":
    for n in range(1000, 10_000-2*3330):
        if n != 1487:
            n2 = n + 3330
            n3 = n + 2*3330
            str_n = str(n)
            str_n2 = str(n2)
            str_n3 = str(n3)
            if is_prime(n) and is_prime(n2) and is_prime(n3):
                if sorted(str_n) == sorted(str_n2) == sorted(str_n3):
                    concat = str_n + str_n2 + str_n3
                    break
    print(concat)  # 296962999629
