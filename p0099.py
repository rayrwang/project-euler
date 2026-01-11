
import math

if __name__ == "__main__":
    max_line = None
    max_score = 0
    with open("assets/0099_base_exp.txt", "r") as f:
        for i, line in enumerate(f, start=1):
            base, exp = line.split(",")
            base, exp = int(base), int(exp)
            score = exp * math.log(base)
            if score > max_score:
                max_score = score
                max_line = i
    print(max_line)  # 709
