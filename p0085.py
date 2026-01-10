
import math

def count_rectangles(w, h):
    s = min(w, h)
    l = max(w, h)
    count = 0
    for i in range(s):
        for j in range(l):  # TODO too lazy to factor this out
            count += (s-i)*(l-j)
    return count

def find_closest_area():
    closest_area = None
    smallest_difference = float("inf")
    for w in range(1, 1<<62):
        below = None
        for h in range(1, 1<<62):
            count = count_rectangles(w, h)
            if count > 2_000_000:
                above = count
                below_error = math.fabs(2_000_000 - below)
                above_error = math.fabs(2_000_000 - above)
                if below_error < above_error:
                    if below_error < smallest_difference:
                        smallest_difference = below_error
                        closest_area = w * (h-1)
                else:
                    if above_error < smallest_difference:
                        smallest_difference = above_error
                        closest_area = w * h

                if h < w:  # The rest have already been seen in the opposite order
                    return closest_area
                break
            below = count

if __name__ == "__main__":
    print(find_closest_area())  # 2772
