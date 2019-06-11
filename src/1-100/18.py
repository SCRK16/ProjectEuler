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

with open("18.txt") as f:
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
Reasoning:
Start at the row second to last from the bottom.
You only have to choose between two numbers at the very bottom of the triangle.
Pick the bigger one! This will result in a higher score.

If we were going to pick that number anyway when choosing the number on the bottom row,
we may as well add it to the number in the row above it.

We now have a pyramid with one fewer row.

Repeat until there is only 1 row left.
The pyramid now contains the maximum score attainable.

Example:

   3               3            3           23
  7 4            7  4         20 19   
 2 4 6         10 13 15
8 5 9 3

This is the maximum attainable score: 3 + 7 + 4 + 9 = 23
"""
