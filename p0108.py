
import numba

from funcs import inf_range

@numba.jit
def find_n():
    for n in inf_range():
        solutions = 0
        for x in inf_range(start=n+1):
            y = n*x / (x-n)
            if x > y:  # Following already encountered when x was smaller
                break
            if n*x % (x-n) == 0:
                solutions += 1
        if solutions > 1000:
            break
    return n

if __name__ == "__main__":
    print(find_n())  # 180180
