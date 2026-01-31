
from funcs import is_prime

if __name__ == "__main__":
    count = 0
    seen = set()
    rem = 50_000_000
    for fourth_root in range(84+1):
        if is_prime(fourth_root):
            rem4 = rem - fourth_root**4
            for cube_root in range(368+1):
                if is_prime(cube_root):
                    rem3 = rem4 - cube_root**3
                    if rem3 <= 0:
                        break
                    for square_root in range(7071+1):
                        if is_prime(square_root):
                            rem2 = rem3 - square_root**2
                            if rem2 <= 0:
                                break
                            if rem2 not in seen:
                                seen.add(rem2)
                                count += 1
    print(count)  # 1097343
