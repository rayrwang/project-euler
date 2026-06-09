if __name__ == "__main__":
    # d2d3d4 .. d8d9d10 (sliding 3-digit windows) divisible by 2,3,5,7,11,13,17.
    # Build from the right: start with 3-digit multiples of 17, then prepend a
    # digit at a time so each new leading window is divisible by the next prime.
    primes = (13, 11, 7, 5, 3, 2)
    cands = [f"{m:03d}" for m in range(0, 1000, 17) if len(set(f"{m:03d}")) == 3]
    for p in primes:
        nxt = []
        for s in cands:
            for d in "0123456789":
                if d not in s and int(d + s[:2]) % p == 0:
                    nxt.append(d + s)
        cands = nxt
    total = 0
    for s in cands:                       # s is now d2..d10 (9 distinct digits)
        for d in "0123456789":
            if d not in s:                # prepend the remaining digit as d1
                total += int(d + s)
    print(total)  # 16695334890
