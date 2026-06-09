
import math

def circle_int(x):
    return 0.5 * ((1-x**2)**0.5 * x + math.asin(x))

def circle_int_range(a, b):
    """Integrate unit circle centered at the origin from a to b"""
    return circle_int(b) - circle_int(a)

def area(n):
    slope = 1/n
    intersection_x = (-2**0.5 * n**(3/2) + n**2 + n) / (n**2 + 1)
    intersection_y = intersection_x * slope

    triangle_area = 0.5 * intersection_x * intersection_y
    section_area = (1 - intersection_x) - circle_int_range(0, 1-intersection_x)
    concave_triangle_area = triangle_area + section_area
    return concave_triangle_area / L_section_area

if __name__ == "__main__":
    L_section_area = 1 - (math.pi / 4)
    for n in range(1, 1<<62):
        if area(n) < 0.001:
            break
    print(n)  # 2240
