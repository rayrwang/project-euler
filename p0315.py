
import numba

from funcs import is_prime

segments = (
    (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 1, 0, 0, 1, 0),  # 1
    (1, 0, 1, 1, 1, 0, 1),  # 2
    (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 1, 1, 0, 1, 0),  # 4
    (1, 1, 0, 1, 0, 1, 1),  # 5
    (1, 1, 0, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 1, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)   # 9
)

empty = (0,)*10

@numba.jit
def digital_root(n):
    while n >= 10:
        digital_sum = 0
        while n != 0:
            digital_sum += n % 10
            n = n // 10
        n = digital_sum
        yield digital_sum

@numba.jit
def sam_transitions(n1, n2):
    transitions = 0
    while n1 != 0:
        digit = n1 % 10
        transitions += sum(segments[digit])
        n1 //= 10
    while n2 != 0:
        digit = n2 % 10
        transitions += sum(segments[digit])
        n2 //= 10
    return transitions

def max_transitions(n1, n2):
    transitions = 0
    while n1 != 0 or n2 != 0:
        if n1 == 0:
            segs1 = empty
        else:
            segs1 = segments[n1 % 10]
        if n2 == 0:
            segs2 = empty
        else:
            segs2 = segments[n2 % 10]
        transitions += sum([s1 ^ s2 for s1, s2 in zip(segs1, segs2)])
        n1 //= 10
        n2 //= 10
    return transitions

def dr_transitions(n, f):
    transitions = 0
    transitions += f(0, n)
    curr = n
    for nxt in digital_root(n):
        transitions += f(curr, nxt)
        curr = nxt
    transitions += f(nxt, 0)
    return transitions

if __name__ == "__main__":
    sam_total = 0
    max_total = 0
    for n in range(int(1e7), int(2e7)):
        if is_prime(n):
            sam_total += dr_transitions(n, sam_transitions)
            max_total += dr_transitions(n, max_transitions)
    print(sam_total-max_total)  # 13625242
