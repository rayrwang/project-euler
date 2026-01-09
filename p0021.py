
def d(n: int, /) -> int:
    """Sum proper divisors"""
    s = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                s += i
            else:
                s += i
                s += n // i
    return s - n

if __name__ == "__main__":
    s = 0
    for a in range(1, 10000):
        b = d(a)
        if b != a and d(b) == a:
            s += a
    print(s)  # 31626
