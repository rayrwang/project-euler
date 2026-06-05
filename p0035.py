
from funcs import prime_sieve_bool

def rot(s: str):
    for _ in range(len(s)):
        yield s
        s = s[1:] + s[0]

if __name__ == "__main__":
    primes = prime_sieve_bool(10_000_000)
    s = 0
    for n in range(2, 1_000_000):
        for i in rot(str(n)):
            if not primes[int(i)]:
                break
        else:
            s += 1
    print(s)  # 55
