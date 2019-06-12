from itertools import count

pentagonals = []
for k in range(1, 100000):
    pentagonals.append((k*(3*k-1) // 2, k % 2 != 0))
    pentagonals.append(((-k)*(-3*k-1) // 2, k % 2 != 0))

partitions = [1, 1]
for i in count(2):
    s = 0
    for pent, add in pentagonals:
        if pent > i:
            break
        p = partitions[i-pent]
        if add:
            s += p
        else:
            s -= p
    partitions.append(s)
    if s % 1000000 == 0:
        break

print(i)
