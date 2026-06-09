if __name__ == "__main__":
    # multiplicand x multiplier = product must together use 1-9 exactly once.
    # Only 1-digit x 4-digit and 2-digit x 3-digit give a 9-digit total
    # (both with a 4-digit product), so a < 100 suffices.
    target = set("123456789")
    products = set()
    for a in range(1, 100):
        for b in range(a + 1, 10000 // a + 1):
            c = a * b
            digits = f"{a}{b}{c}"
            if len(digits) == 9 and set(digits) == target:
                products.add(c)
    print(sum(products))  # 45228
