
import itertools

bouncy = 0
for i in itertools.count(start=1):
    i_str = str(i)
    i_sorted = ''.join(sorted(i_str))
    if i_str not in [i_sorted, i_sorted[::-1]]:
        bouncy += 1
    if bouncy / i >= 0.99:
        break
print(i)  # 1587000
