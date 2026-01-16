
import numba

@numba.jit
def find_p_most():
    p_most = None
    max_count = 0
    for p in range(1, 1000+1):
        print(p)
        count = 0
        for a in range(1, 1000+1):
            for b in range(1, a+1):
                c2 = a**2 + b**2
                c = int(c2**0.5)
                if c**2 == c2:
                    if a + b + c == p:
                        count += 1
        if count > max_count:
            max_count = count
            p_most = p
    return p_most

if __name__ == "__main__":
    print(find_p_most())  # 840
