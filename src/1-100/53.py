import sys
sys.path.append("..")
from euler import factorial_memory

def nCr(n, r, memory):
    return factorial_memory(n, memory) // (factorial_memory(r, memory) * factorial_memory(n - r, memory))

memory = {}
count = 0
for n in range(1, 101):
    for r in range(0, n+1):
        if nCr(n, r, memory) > 1000000:
            count += 1

print(count)
