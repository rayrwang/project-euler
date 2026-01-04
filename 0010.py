
import numba

@numba.jit
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

s = 0
for n in range(3, 2_000_000, 2):
    if is_prime(n):
        s += n
print(2+s)  # 142913828922
