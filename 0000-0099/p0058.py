
from funcs import is_prime

if __name__ == "__main__":
    prime_count = 0
    for side_length in range(3, 1<<62, 2):
        square = side_length**2
        side_diff = side_length - 1

        bottom_left = square - side_diff
        top_left = square - 2*side_diff
        top_right = square - 3*side_diff

        prime_count += is_prime(bottom_left)
        prime_count += is_prime(top_left)
        prime_count += is_prime(top_right)

        diagonal_count = 2*side_length - 1
        ratio = prime_count / diagonal_count
        if ratio < 0.1:
            break
    print(side_length)  # 26241
