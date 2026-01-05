
def find_prime_factors(n: int) -> set[int]:
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return find_prime_factors(i) | find_prime_factors(n//i)
    return {n}

if __name__ == "__main__":
    print(max(find_prime_factors(600851475143)))  # 6857
