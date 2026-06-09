
def fib():
    x1 = 1
    x2 = 2
    while True:
        x1, x2 = x2, (nxt := x1 + x2)
        yield nxt

if __name__ == "__main__":
    s = 0
    for i in fib():
        if i > 4_000_000:
            break
        if i % 2 == 0:
            s += i
    print(2+s)  # 4613732
