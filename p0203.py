
from funcs import is_prime, nCr

def sum_squarefree(rows):
    s = 0
    seen = set()
    for row in range(rows):
        for entry in range((row+1)//2 + 1):  # Left half
            n = nCr(row, entry)
            if n not in seen:
                seen.add(n)
                for i in range(1, int(n**0.5)+1):
                    if is_prime(i):
                        if n % i**2 == 0:
                            break
                else:
                    s += n
    return s

if __name__ == "__main__":
    print(sum_squarefree(51))  # 34029210557338
