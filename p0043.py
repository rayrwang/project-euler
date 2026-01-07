
import itertools

if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17]
    s = 0
    for number in itertools.permutations(list(range(10))):
        number = "".join([str(digit) for digit in number])
        for i in range(1, 7+1):
            if int(number[i:i+3]) % primes[i-1] != 0:
                break
        else:
            s += int(number)
    print(s)  # 16695334890
