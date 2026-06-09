VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

def parse(s):
    total = 0
    for i, ch in enumerate(s):
        v = VALUES[ch]
        if i + 1 < len(s) and VALUES[s[i + 1]] > v:   # subtractive pair
            total -= v
        else:
            total += v
    return total

def minimal(n):
    out = []
    for value, symbol in TABLE:
        while n >= value:
            out.append(symbol)
            n -= value
    return "".join(out)

if __name__ == "__main__":
    saved = 0
    with open("assets/0089_roman.txt") as f:
        for line in f:
            s = line.strip()
            saved += len(s) - len(minimal(parse(s)))
    print(saved)  # 743
