TBL = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
LETTERS = "IVXLCDM"
P_LETTER = 0.14
P_HASH = 0.02

def roman(v: int) -> str:
    s = ""
    for val, sym in TBL:
        while v >= val:
            s += sym
            v -= val
    return s

def solve() -> float:
    """Expected value of the random minimal Roman numeral.

    A symbol is drawn each step (each letter 14%, '#' 2%); invalid appends are
    skipped and '#' stops. While only leading M's are written, all 7 letters are
    valid so the draw never skips: stop (value 1000a) with prob 0.02, add another M
    with prob 0.14, or enter the sub-1000 part with one of I,V,X,L,C,D. The thousands
    contribute additively, so E = 1000a + g(s) and H(a) = 1000a + ... is linear in a,
    giving H(0) = (0.14*G6 + 140)/0.86 with G6 = sum of g over the 6 sub-1000 starts.
    Within 0..999, appending a letter strictly increases the value, so the automaton
    is a DAG solved from large s downward:
        g(s) = (0.02*s + 0.14*sum_t g(t)) / (0.02 + 0.14*deg(s)).
    """
    minstr = {v: roman(v) for v in range(1000)}
    str2val = {s: v for v, s in minstr.items()}
    g = [0.0] * 1000
    for s in range(999, -1, -1):
        succ = []
        for letter in LETTERS:
            t = str2val.get(minstr[s] + letter)
            if t is not None and s < t < 1000:
                succ.append(t)
        denom = P_HASH + P_LETTER * len(succ)
        val = P_HASH / denom * s
        for t in succ:
            val += P_LETTER / denom * g[t]
        g[s] = val
    g6 = g[1] + g[5] + g[10] + g[50] + g[100] + g[500]
    return (P_LETTER * g6 + 140) / 0.86

if __name__ == "__main__":
    print(f"{solve():.8f}")  # 319.30207833
