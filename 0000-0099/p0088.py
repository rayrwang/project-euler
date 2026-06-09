def solve(max_k):
    """Sum of distinct minimal product-sum numbers for set sizes 2..max_k."""
    limit = 2 * max_k                      # the minimal value for any k is at most 2k
    minimal = [limit + 1] * (max_k + 1)

    # Enumerate factorizations into factors >= 2. A product P made of `terms`
    # factors summing to `summ` becomes a product-sum number for
    # k = terms + (P - summ) by padding with (P - summ) ones.
    def dfs(product, summ, terms, start):
        if terms >= 2:
            k = product - summ + terms
            if 2 <= k <= max_k and product < minimal[k]:
                minimal[k] = product
        f = start
        while product * f <= limit:
            dfs(product * f, summ + f, terms + 1, f)
            f += 1

    dfs(1, 0, 0, 2)
    return sum(set(minimal[2:]))

if __name__ == "__main__":
    print(solve(12000))  # 7587457
