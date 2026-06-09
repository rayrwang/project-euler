
from funcs import is_square

def value(word):
    return sum(ord(letter) - ord("A") + 1 for letter in word)

def is_triangle(n):
    return is_square(1 + 8*n)  # Discriminant

if __name__ == "__main__":
    count = 0
    with open("assets/0042_words.txt", "r") as f:
        for word in f.read().split(","):
            if is_triangle(value(word[1:-1])):
                count += 1
    print(count)  # 162
