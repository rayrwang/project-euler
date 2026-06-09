
if __name__ == "__main__":
    largest = float("-inf")
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                if prod > largest:
                    largest = prod
    print(largest)  # 906609
