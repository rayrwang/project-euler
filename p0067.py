
from p0018 import triangle_max_path

if __name__ == "__main__":
    with open("assets/0067_triangle.txt", "r") as f:
        print(triangle_max_path(f.read().split("\n"), slice(-1)))  # 7273
