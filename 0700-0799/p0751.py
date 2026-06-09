from decimal import Decimal, getcontext

PLACES = 24

def concatenation(theta, digits):
    """Concatenate the sequence generated from theta until the fractional
    part has at least `digits` digits, returning tau as a Decimal."""
    b = theta
    a = int(b)
    frac = ""
    while len(frac) < digits:
        b = int(b) * (b - int(b) + 1)
        frac += str(int(b))
    return Decimal(f"{a}.{frac}")

def solve():
    """tau is a contraction of theta: the first terms of the sequence (hence
    the leading digits of tau) only depend on the leading digits of theta, so
    iterating theta <- tau(theta) gains digits each round and converges to
    the unique fixed point starting at a_1 = 2."""
    getcontext().prec = PLACES + 20
    theta = Decimal(2)
    while True:
        tau = concatenation(theta, PLACES + 10)
        if tau == theta:
            break
        theta = tau
    # Round (truncate) to 24 places; the fixed point is stable well past 24.
    s = str(theta)
    head, frac = s.split(".")
    return f"{head}.{frac[:PLACES]}"

if __name__ == "__main__":
    print(solve())  # 2.223561019313554106173177
