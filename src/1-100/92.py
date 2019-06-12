def next(n):
    return sum([int(x) ** 2 for x in str(n)])

def square_digit_chain(n, memory):
    if n in memory:
        return memory[n]
    memory[n] = square_digit_chain(next(n), memory)
    return memory[n]
    

upper = 10000000

memory = {1: False, 89: True}

count = 0

for i in range(1, upper):
    sorted_i = int(''.join(sorted(str(i)))) #Notice: next(i) == next(sorted_i)
    if sorted_i in memory:
        memory[i] = memory[sorted_i]
    if square_digit_chain(i, memory):
        count += 1

print("Count: ", count)

"""
Original dynamic programming solution:
37 sec
Using next(i) == next(sorted_i):
17 sec
"""
