
from funcs import gcd

if __name__ == "__main__":
    n_prod = 1
    d_prod = 1
    for d in range(10, 100):
        for n in range(10, d):
            common_set = (set(str(n)) & set(str(d)))
            for c in common_set:
                if c != "0":
                    n_reduced = list(str(n))
                    n_reduced.remove(c)
                    n_reduced = int("".join(n_reduced))
                    
                    d_reduced = list(str(d))
                    d_reduced.remove(c)
                    d_reduced = int("".join(d_reduced))
                    # print(n, d, n_reduced, d_reduced)
                    if n_reduced*d == n*d_reduced:
                        n_prod *= n
                        d_prod *= d
    print(d_prod // gcd(n_prod, d_prod))  # 100
