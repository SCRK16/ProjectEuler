def max_row(r):
    """
    Calculate the maximum for each two consecutive numbers in a row
    Return the resulting list of maximums
    """
    if len(r) == 1:
        return r
    result = []
    for i in range(len(r)-1):
        result.append(max(r[i], r[i+1]))
    return result

with open("67.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
content = [x.split(" ") for x in content]
content = [[int(y) for y in r] for r in content]

triangle = list(reversed(content))

for i in range(len(triangle)-1):
    r = max_row(triangle[i])
    for j in range(len(r)):
        triangle[i+1][j] += r[j]

print(triangle[-1][0])

"""
See 18.py for the explanation of the algorithm.
"""
