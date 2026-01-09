
from funcs import is_prime

def rot(s: str):
    for _ in range(len(s)):
        yield s
        s = s[1:] + s[0]

if __name__ == "__main__":
    s = 0
    for n in range(2, 1_000_000):
        for i in rot(str(n)):
            if not is_prime(int(i)):
                break
        else:
            s += 1
    print(s)  # 55
