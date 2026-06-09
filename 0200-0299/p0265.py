# The circular arrangements are exactly the binary de Bruijn sequences
# B(2, n): every n-bit window distinct. Reading each from its unique run of
# n zeros fixes the rotation, so a DFS extends the bit string from n zeros,
# tracking which n-bit windows are used; at full length the n - 1
# wrap-around windows are checked too. S(3) = 52 reproduces the statement.


def solve(n: int = 5) -> int:
    size = 1 << n
    mask = size - 1
    bits = [0] * n
    seen = [False] * size
    seen[0] = True
    total = 0

    def dfs(cur: int, pos: int) -> None:
        nonlocal total
        if pos == size:
            w = cur
            used = []
            for i in range(n - 1):
                w = ((w << 1) | bits[i]) & mask
                if seen[w]:
                    break
                seen[w] = True
                used.append(w)
            else:
                val = 0
                for b in bits:
                    val = (val << 1) | b
                total += val
            for w2 in used:
                seen[w2] = False
            return
        for b in (0, 1):
            w = ((cur << 1) | b) & mask
            if not seen[w]:
                seen[w] = True
                bits.append(b)
                dfs(w, pos + 1)
                bits.pop()
                seen[w] = False

    dfs(0, n)
    return total


if __name__ == "__main__":
    print(solve())  # 209110240768
