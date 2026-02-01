
if __name__ == "__main__":
    s = 1
    for root in range(3, 1001+1, 2):
        dist = root - 1
        s += root**2
        s += root**2 - dist
        s += root**2 - 2*dist
        s += root**2 - 3*dist
    print(s)  # 669171001
