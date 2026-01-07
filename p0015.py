
def fact(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

def nCr(n, r):
    # n! / (r!(n-r)!)
    prod = 1
    for i in range(max(r, n-r)+1, n+1):
        prod *= i
    return int(prod / fact(min(r, n-r)))

if __name__ == "__main__":
    # print(int(fact(40) / (fact(20)*fact(20))))  # 137846528820
    print(nCr(40, 20))  # 137846528820
