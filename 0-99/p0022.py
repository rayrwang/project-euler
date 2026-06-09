
def letter_sum(word):
    return sum([ord(letter) - ord("A") + 1 for letter in word])

if __name__ == "__main__":
    with open("assets/0022_names.txt", "r") as f:
        names = f.read().split(",")
        names = [name[1:-1] for name in names]  # Strip quotes
        names = sorted(names)
    s = 0
    for i, name in enumerate(names, start=1):
        s += i * letter_sum(name)
    print(s)  # 871198282
