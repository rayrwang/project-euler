from funcs import is_palindrome

if __name__ == "__main__":
    LIMIT = 100_000_000
    found = set()
    a = 1
    while a * a + (a + 1) * (a + 1) < LIMIT:   # need at least two terms
        total = a * a
        b = a + 1
        while True:
            total += b * b
            if total >= LIMIT:
                break
            if is_palindrome(total):
                found.add(total)
            b += 1
        a += 1
    print(sum(found))  # 2906969179
