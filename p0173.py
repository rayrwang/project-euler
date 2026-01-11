
import numba

@numba.jit
def count_square_laminae(n):
    count = 0
    for square_width in range(1<<62):
        if 4*square_width - 4 > n:  # Thinnest shape is still too big
            break 
        for hole_width in range(2 if square_width % 2 == 0 else 1, square_width, 2):
            if square_width**2 - hole_width**2 <= n:
                count += 1
    return count

if __name__ == "__main__":
    print(count_square_laminae(1_000_000))  # 1572729
