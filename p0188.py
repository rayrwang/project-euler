
import numba

from funcs import mod_exp_bounded as mod_exp

@numba.jit
def mod_tetr(a, b, mod):
    acc = mod_exp(a, a, mod)
    for _ in range(b-2):
        acc = mod_exp(a, acc, mod)
    return acc

if __name__ == "__main__":
    print(mod_tetr(1777, 1855, 100_000_000))  # 95962097
