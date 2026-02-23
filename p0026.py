
def reciprocal(d):
    rem = 10
    while True:
        if rem == 0:
            return
        if d <= rem:
            yield rem // d, rem
            rem = rem % d
            rem *= 10
        else:
            yield 0, rem
            rem *= 10

if __name__ == "__main__":
    len_max = 0
    d_max = None
    for d in range(2, 1000):
        rems = []
        for length, (_, rem) in enumerate(reciprocal(d)):
            if rem in rems:  # Found cycle
                break
            rems.append(rem)
        else:  # Terminates, no cycle
            length = 0
        if length > len_max:
            len_max = length
            d_max = d
    print(d_max)  # 983
