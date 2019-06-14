import sys
sys.path.append("..")
from euler import factorial_memory as factorial

result = 0
memory = {0: 1, 1: 1}

for i in range(3, 1000000):
    digits = [int(x) for x in str(i)]
    factorials = [factorial(x, memory) for x in digits]
    if sum(factorials) == i:
        result += i

print(result)


"""
Runtime without memory: 6.095s
Runtime with memory:    2.910s
Reducing search space from 1,000,000 to 100,000 reduces time to: 0.292s
"""
