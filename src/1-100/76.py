def piles(n, min_pile_size, memory):
    if n == 0:
        return 1
    elif (n, min_pile_size) in memory:
        return memory[(n, min_pile_size)]
    s = 0
    for i in range(n, min_pile_size-1, -1):
        n -= i
        s += piles(n, i, memory)
        n += i
        memory[(n, i)] = s
    return s

memory = {(1, 1): 1}

for i in range(101):
    p = piles(i, 1, memory)

print(p - 1)
