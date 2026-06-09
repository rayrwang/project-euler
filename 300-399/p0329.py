from math import gcd

CROAKS = "PPPPNNPPPNPPNPN"
N_SQUARES = 500


def sieve(n: int) -> list[bool]:
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return is_p


def solve() -> str:
    """Probability of hearing CROAKS over the frog's first 15 croaks.

    Track an integer weight per square so the result stays exact. A croak on
    square s contributes numerator 2 (matching label) or 1 (mismatching),
    each over a factor of 3. A jump contributes 1/2 to each neighbour; at the
    two ends the move is forced (probability 1 = 2 * 1/2), so a forced jump
    carries numerator 2. Every path then shares the denominator
        500 * 3^15 * 2^14,
    and the total numerator is the path-weight sum, obtained by a forward
    sweep over the 15 croaks.
    """
    prime = sieve(N_SQUARES)

    def chance(t: int, s: int) -> int:
        prime_croak = CROAKS[t] == "P"
        # numerator out of 3: 2 if the croak matches the square's prime-ness
        return 2 if prime[s] == prime_croak else 1

    # dp[s] = summed path weight for the frog currently on square s.
    dp = [0] * (N_SQUARES + 1)
    for s in range(1, N_SQUARES + 1):
        dp[s] = chance(0, s)
    for t in range(1, len(CROAKS)):
        new = [0] * (N_SQUARES + 1)
        for k in range(1, N_SQUARES + 1):
            inc = 0
            if k - 1 >= 1:  # arrived from the left (source jumped right)
                inc += dp[k - 1] * (2 if k - 1 == 1 else 1)
            if k + 1 <= N_SQUARES:  # arrived from the right (source jumped left)
                inc += dp[k + 1] * (2 if k + 1 == N_SQUARES else 1)
            new[k] = chance(t, k) * inc
        dp = new

    numerator = sum(dp)
    denominator = N_SQUARES * 3 ** len(CROAKS) * 2 ** (len(CROAKS) - 1)
    g = gcd(numerator, denominator)
    return f"{numerator // g}/{denominator // g}"


if __name__ == "__main__":
    print(solve())  # 199740353/29386561536000
