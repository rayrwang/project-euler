
def lexical_perm(lst: list):
    if len(lst) == 1:
        yield lst
        return
    for fst in sorted(lst):
        rest = lst.copy()
        rest.remove(fst)
        for rest_perm in lexical_perm(rest):
            rest_perm.insert(0, fst)
            yield rest_perm

if __name__ == "__main__":
    for i, perm in enumerate(lexical_perm(list(map(str, range(10))))):
        if (i+1) == 1_000_000:
            break
    print("".join(perm))  # 2783915460
