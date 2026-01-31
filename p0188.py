
import numba

@numba.jit
def mod_exp(a, b, mod):
    prod = 1
    while b > 0:
        if b % 2 == 1:
            prod = (prod * a) % mod
        b //= 2
        a = (a * a) % mod
    return prod

@numba.jit
def mod_tetr(a, b, mod):
    acc = mod_exp(a, a, mod)
    for _ in range(b-2):
        acc = mod_exp(a, acc, mod)
    return acc

if __name__ == "__main__":
    print(mod_tetr(1777, 1855, 100_000_000))  # 95962097
