
if __name__ == "__main__":
    digits = {}
    for root in range(1<<62):
        new_digits = tuple(sorted(str(root**3)))
        if new_digits not in digits:
            digits[new_digits] = (root**3,)
        else:
            digits[new_digits] = (*digits[new_digits], root**3)
            if len(digits[new_digits]) == 5:
                break
    print(digits[new_digits][0])  # 127035954683
