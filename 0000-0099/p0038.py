
if __name__ == "__main__":
    max_concat_prod = 0
    for i in range(10_000):  # 10000 and 2*10000 has 10 digits
        concat_prod = ""
        n = 1
        while True:
            concat_prod += str(i*n)
            n += 1
            if len(concat_prod) >= 9:
                digits = set(concat_prod)
                digits.discard("0")
                if len(concat_prod) == 9 and len(digits) == 9:
                    if int(concat_prod) > max_concat_prod:
                        max_concat_prod = int(concat_prod)
                break
    print(max_concat_prod)  # 932718654
