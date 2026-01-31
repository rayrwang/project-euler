
from itertools import permutations

from funcs import is_prime

def count_sets():
    count = 0
    sets = set()
    for perm in permutations(range(1, 9+1)):
        for split_pattern in range(2**8):
            # Right to left
            prev_split = 0
            new_set = []  # Set can't be added to set
            for i in range(1, 9+1):
                bit = split_pattern % 2
                if bit == 1:
                    n = int("".join(str(digit) for digit in perm[9-i: 9-prev_split]))
                    if not is_prime(n):
                        break
                    new_set.append(n)
                    prev_split = i
                split_pattern //= 2
            else:
                # Still need to check left most number
                n = int("".join(str(digit) for digit in perm[0: 9-prev_split]))
                new_set.append(n)
                new_set = ",".join(str(num) for num in sorted(new_set))
                if is_prime(n) and new_set not in sets:
                    sets.add(new_set)
                    count += 1
    return count

if __name__ == "__main__":
    print(count_sets())  # 44680
