import sys
sys.path.append("..")
from euler import factorial_memory, digits

def digits_factorial(n, fmem):
    df = (factorial_memory(x, fmem) for x in digits(n, convert=True))
    return sum(df)

def chain(n, used, used_list, cmem, fmem):
    """
    Calculate the chain length of n
    cmem is the memory (cache) of the chain function
    fmem is the memory (cache) of the factorial function
    """
    if n in used:
        i = used_list.index(n)
        chain_length = len(used_list) - i
        cmem[n] = chain_length
        return chain_length, chain_length
    if n in cmem:
        return cmem[n], 0
    next = digits_factorial(n, fmem)
    used.add(n)
    used_list.append(n)
    chain_length, loop = chain(next, used, used_list, cmem, fmem)
    if loop > 0:
        loop -= 1
        cmem[n] = chain_length
        return chain_length, loop
    chain_length += 1
    cmem[n] = chain_length
    return chain_length, 0

upper = 1000000
cmem = {}
fmem = {0: 1, 1: 1}
count = 0
for i in range(upper):
    chain_length, _ = chain(i, set(), [], cmem, fmem)
    if chain_length == 60:
        count += 1

print(count)
