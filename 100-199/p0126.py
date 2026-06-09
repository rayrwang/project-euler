def solve(target: int = 1000) -> int:
    # Cubes in layer n around an a*b*c cuboid:
    #   2(ab+bc+ca) + 4(n-1)(a+b+c) + 4(n-1)(n-2).
    # Count, for each layer size <= limit, how many (a>=b>=c, n) give it;
    # return the smallest size hit by exactly `target` cuboids.
    limit = 20000
    count = [0] * (limit + 1)
    c = 1
    while 6 * c * c <= limit:           # min layer (a=b=c, n=1) = 6c^2
        b = c
        while 2 * (b * b + 2 * b * c) <= limit:  # min with a=b
            a = b
            while True:
                base = 2 * (a * b + b * c + c * a)
                if base > limit:
                    break
                n = 1
                while True:
                    size = base + 4 * (n - 1) * (a + b + c) + 4 * (n - 1) * (n - 2)
                    if size > limit:
                        break
                    count[size] += 1
                    n += 1
                a += 1
            b += 1
        c += 1
    for size in range(1, limit + 1):
        if count[size] == target:
            return size
    raise ValueError("increase limit")


if __name__ == "__main__":
    print(solve())  # 18522
