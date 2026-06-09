from collections import Counter

RANKS = "23456789TJQKA"

def hand_key(cards):
    """Collapse a 5-card hand into a single comparable key: (category, tiebreak).

    Card values are ordered by frequency first, then by value, so the cards that
    matter for tie-breaking (quads, trips, pairs) float to the front and plain
    tuple comparison resolves every kicker automatically.
    """
    values = [RANKS.index(c[0]) + 2 for c in cards]
    flush = len({c[1] for c in cards}) == 1
    counts = Counter(values)
    pattern = sorted(counts.values(), reverse=True)
    tiebreak = tuple(sorted(values, key=lambda v: (counts[v], v), reverse=True))

    distinct = sorted(counts)
    straight = len(distinct) == 5 and distinct[-1] - distinct[0] == 4

    if straight and flush:
        category = 8
    elif pattern == [4, 1]:
        category = 7
    elif pattern == [3, 2]:
        category = 6
    elif flush:
        category = 5
    elif straight:
        category = 4
    elif pattern == [3, 1, 1]:
        category = 3
    elif pattern == [2, 2, 1]:
        category = 2
    elif pattern == [2, 1, 1, 1]:
        category = 1
    else:
        category = 0
    return category, tiebreak

if __name__ == "__main__":
    wins = 0
    with open("assets/0054_poker.txt") as f:
        for line in f:
            cards = line.split()
            if hand_key(cards[:5]) > hand_key(cards[5:]):
                wins += 1
    print(wins)  # 376
