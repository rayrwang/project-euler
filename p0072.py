
import numba

from funcs import find_prime_factors_set, lcm

@numba.jit
def count_fractions():
    count = 0
    for d in range(2, 1_000_000+1):
        prime_factors = sorted(find_prime_factors_set(d))
        if len(prime_factors) == 1:
            possibilities = (d-1) - (d-1)//(prime_factors[0])
        elif len(prime_factors) == 2:
            possibilities = (d-1) \
                - (d-1)//prime_factors[0] \
                - (d-1)//prime_factors[1] \
                + (d-1)//lcm(prime_factors[0], prime_factors[1])
        else:  # TODO better way?
            possibilities = (d-1) \
                - (d-1)//prime_factors[0] \
                - (d-1)//prime_factors[1] \
                + (d-1)//lcm(prime_factors[0], prime_factors[1])
            multiples = set()
            for f in prime_factors[2:]:
                for n in range(f, d, f):
                    if n % prime_factors[0] != 0 and n % prime_factors[1] != 0:
                        multiples.add(n)
            possibilities -= len(multiples)
        count += possibilities
    return count

if __name__ == "__main__":
    print(count_fractions())  # 303963552391
