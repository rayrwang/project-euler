

if __name__ == "__main__":
    terms = set()
    terms_count = 0
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            new_term = a**b
            if new_term not in terms:
                terms_count += 1
                terms.add(new_term)
    print(terms_count)  # 9183
