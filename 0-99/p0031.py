
import numba

@numba.jit
def count_ways(n, coins):
    if len(coins) == 1:
        return n % coins[0] == 0
    if n == 0:
        return 1
    count = 0
    next_coin = coins[0]
    for n_coins in range(0, n // next_coin+1):
        count += count_ways(n - n_coins*next_coin, coins[1:])
    return count

if __name__ == "__main__":
    print(count_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))  # 73682
