from collections import Counter

if __name__ == "__main__":
    with open("assets/0059_cipher.txt") as f:
        cipher = [int(x) for x in f.read().strip().split(",")]

    # The 3-letter key cycles, so the text is three streams each XOR-ed by one
    # byte. The commonest character in English is the space (32), so each key
    # byte is (most common byte in its stream) XOR 32 -- no brute force needed.
    key = [Counter(cipher[j::3]).most_common(1)[0][0] ^ 32 for j in range(3)]
    plain = [c ^ key[i % 3] for i, c in enumerate(cipher)]
    print(sum(plain))  # 129448
