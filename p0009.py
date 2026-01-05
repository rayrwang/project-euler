
import itertools

def find_ptriplet_prod():
    for a in itertools.count():
        for b in range(a):
            c_est = round((a**2 + b**2)**0.5)
            if a+b+c_est == 1000 and a**2 + b**2 == c_est**2:
                return a*b*c_est

if __name__ == "__main__":
    print(find_ptriplet_prod())  # 31875000
