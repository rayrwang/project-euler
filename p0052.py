
if __name__ == "__main__":
    for n in range(1, 1<<62):
        digits = set(str(n))
        for multiple in range(2, 6+1):
            if set(str(multiple*n)) != digits:
                break
        else:
            break
    print(n)  # 142857
