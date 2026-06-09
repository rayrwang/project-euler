from funcs import prime_sieve_bool

def smallest_prime():
    """Smallest prime that is part of an eight-prime family under digit replacement."""
    n_max = 1_000_000
    is_pr = prime_sieve_bool(n_max)
    for n in range(2, n_max):
        if not is_pr[n]:
            continue
        s = str(n)
        length = len(s)
        for mask in range(1, 1 << length):
            # An eight-member family needs the replaced-digit count divisible by
            # 3, otherwise the digit sum (mod 3) cycles and culls too many.
            if bin(mask).count("1") % 3 != 0:
                continue
            start = 1 if mask & (1 << (length - 1)) else 0  # no leading zero
            count = 0
            smallest = -1
            for i in range(start, 10):
                v = 0
                for pos in range(length):
                    d = i if mask & (1 << (length - 1 - pos)) else ord(s[pos]) - 48
                    v = v * 10 + d
                if is_pr[v]:
                    count += 1
                    if smallest < 0:
                        smallest = v
            if count == 8:
                return smallest
    return -1

if __name__ == "__main__":
    print(smallest_prime())  # 121313
