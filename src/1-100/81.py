def in_bounds(pos, bounds):
    return 0 <= pos[0] <= bounds[0] and 0 <= pos[1] <= bounds[1]

def min_next(pos, matrix, bounds):
    right = (pos[0], pos[1]+1)
    down = (pos[0]+1, pos[1])
    possible = []
    if in_bounds(right, bounds):
        possible.append(matrix[right[0]][right[1]])
    if in_bounds(down, bounds):
        possible.append(matrix[down[0]][down[1]])
    return min(possible) if len(possible) > 0 else 0

with open("81.txt") as f:
    content = f.readlines()

content = [row.strip() for row in content[:-1]]
content = [row.split(',') for row in content]
matrix = [[int(y) for y in row] for row in content]

pos = (79, 79)
bounds = (79, 79)

while pos[0] >= 0:
    while pos[1] >= 0:
        m = min_next(pos, matrix, bounds)
        matrix[pos[0]][pos[1]] += m
        pos = (pos[0], pos[1] - 1)
    pos = (pos[0] - 1, bounds[1])

print(matrix[0][0])

"""
Solved in a similar way to 18
See 18.py for a breakdown of the algorithm used
Only change is going from a triangle to a matrix
"""
