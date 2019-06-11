from itertools import permutations

digits = range(10)
perms = list(permutations(digits))
result = perms[999999] #The one millionth permutation
result = int(''.join([str(x) for x in result]))
print(result)
