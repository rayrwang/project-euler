# With F = 1, 2, 3, 5, ... and S(n) = sum of z(i) for 0 < i < n: the
# numbers in [F_k, F_k + j) are F_k plus a smaller Zeckendorf tail
# (valid because j <= F_(k-1)), so
#     S(n) = S(F_k) + (n - F_k) + S(n - F_k)   for F_k < n <= F_(k+1),
# and the table values obey S(F_(k+1)) = S(F_k) + F_(k-1) + S(F_(k-1)).
# Walking the Zeckendorf digits of 10^17 takes O(log n). Verified against
# brute z-summation below 1000 and the given S(10^6) = 7894453.


def solve(n: int = 10**17) -> int:
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    table = [0, 1]
    for k in range(1, len(fib) - 1):
        table.append(table[k] + fib[k - 1] + table[k - 1])
    total = 0
    k = len(fib) - 1
    while n > 1:
        while fib[k] > n - 1:
            k -= 1
        if fib[k] == n:
            return total + table[k]
        total += table[k] + (n - fib[k])
        n -= fib[k]
    return total


if __name__ == "__main__":
    print(solve())  # 2252639041804718029
