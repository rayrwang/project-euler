
def fib():
    x1 = 0
    x2 = 1
    nxt = x2
    while True:
        yield nxt
        x1, x2 = x2, (nxt := x1 + x2)

if __name__ == "__main__":
    for i, f in enumerate(fib()):
        if len(str(f)) >= 1000:
            break
    print(i+1)  # 4782
