def next(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def solve(n, memory):
    if n in memory:
        return memory[n]
    solution = solve(next(n), memory) + 1
    memory[n] = solution
    return solution

upper = 1000000
memory = {1:0}
longest_start = 0
longest_length = 0

for i in range(1, upper):
    length = solve(i, memory)
    if length > longest_length:
        longest_length = length
        longest_start = i
print(longest_length)
print(longest_start)

