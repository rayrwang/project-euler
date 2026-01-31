
import itertools

if __name__ == "__main__":
    s = 0
    seen = set()
    for perm in itertools.permutations(str(digit) for digit in range(1, 9+1)):
        for mul_split in range(1, 7+1):
            for equal_split in range(mul_split+1, 8):
                multiplier = int("".join(perm[:mul_split]))
                multiplicand = int("".join(perm[mul_split:equal_split]))
                product = int("".join(perm[equal_split:]))
                if multiplier * multiplicand == product:
                    if product not in seen:
                        seen.add(product)
                        s += product
    print(s)  # 45228
