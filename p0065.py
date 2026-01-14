
def e_convergent_value(i):
    if i == 0:
        return 2
    if i % 3 == 2:
        return 2 * ((i+1) // 3)
    else:
        return 1

def e_convergent(n):
    num = e_convergent_value(n-1)
    denom = 1
    for i in range(n-2, 0-1, -1):
        # Reciprocal
        num, denom = denom, num

        # Add new value
        value = e_convergent_value(i)
        num, denom = num + (value*denom), denom
    return num, denom

if __name__ == "__main__":
    print(sum(int(digit) for digit in str(e_convergent(100)[0])))  # 272
