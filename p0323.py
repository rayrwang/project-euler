
def cdf(i):
    """Probability that the sequence will be all one before term i"""
    return ((2**i-1)/(2**i))**32

def p(i):
    """Probability that the sequence will become all one on exactly term i"""
    return cdf(i) - cdf(i-1)

def expectation(terms):
    E = 0
    for i in range(terms):
        E += i * p(i)
    return E

if __name__ == "__main__":
    print(f"{expectation(10000):.10f}")  # 6.3551758451
