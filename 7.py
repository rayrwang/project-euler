
import itertools

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_i = 1
for n in itertools.count(start=3, step=2):
    if is_prime(n):
        prime_i += 1
    if prime_i == 10_001:
        break
print(n)  # 104743
