

if __name__ == "__main__":
    s = 0
    for n in range(1, 1000+1):
        s += n**n
    print(str(s)[-10:])  # 9110846700
