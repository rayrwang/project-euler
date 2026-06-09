from p0103 import is_special

if __name__ == "__main__":
    total = 0
    with open("assets/0105_sets.txt") as f:
        for line in f:
            nums = [int(x) for x in line.split(",")]
            if is_special(nums):
                total += sum(nums)
    print(total)  # 73702
