
import numba

from funcs import inf_range, is_prime

@numba.jit
def find_prod():
    most_primes = 0
    a_most = None
    b_most = None
    for a in range(-999, 1000):
        for b in range(-1000, 1000+1):
            for n in inf_range():
                if is_prime(n**2 + a*n + b):
                    if n > most_primes:
                        most_primes = n
                        a_most = a
                        b_most = b
                else:
                    break
    if a_most is not None and b_most is not None:
        return a_most * b_most

if __name__ == "__main__":
    print(find_prod())  # -59231
