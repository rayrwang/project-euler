
if __name__ == "__main__":
    s = 0
    for root in range(2, 1_000_000+1):
        print(root)
        square = root**2
        digits = str(square)
        for split_pattern in range(2**(len(digits)-1)):  # len(digits) - 1 possible split locations
            split_pattern = bin(split_pattern)[2:].rjust(len(digits)-1, "0")
            split_sum = 0
            prev_split = 0
            for i, bit in enumerate(split_pattern):
                if bit == "1":
                    split_sum += int(digits[prev_split:i+1])
                    prev_split = i + 1
            split_sum += int(digits[prev_split:])
            if split_sum == root:
                s += square
                break
    print(s)  # 128088830547982
    # TODO very slow (~30 mins)
