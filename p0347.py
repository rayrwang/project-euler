
from funcs import find_prime_factors_set

def S(N):
    pq = {}
    for n in range(1, N+1):
        pq_n = tuple(sorted(find_prime_factors_set(n)))
        if len(pq_n) == 2:
            pq[pq_n] = n
    return sum(pq.values())

if __name__ == "__main__":
    print(S(10_000_000))  # 11109800204052
