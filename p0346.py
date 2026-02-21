
def sum_strong_repunits(n):
    repunits = {}
    # Just under the square root is the highest possible base
    # for a repunit of length 3
    for base in range(2, int(n**0.5)+1):
        rep = 0
        for exp in range(0, 1<<62):
            rep += base**exp
            if rep > n:
                break
            if rep in repunits:
                repunits[rep] += 1
            else:
                repunits[rep] = 1
    # All remaining values above the square root
    # can be expressed as a repunit of length 2
    # k = 1*(k-1) + 1*1
    return sum(k for k, v in repunits.items() if v >= 2 or k > int(n**0.5)+1)

if __name__ == "__main__":
    print(sum_strong_repunits(1_000_000_000_000))  # 336108797689259276
