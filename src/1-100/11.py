def step_possible(current, direction, bounds):
    row = current[0] + direction[0]
    col = current[1] + direction[1]
    if (row < bounds[0][0] or 
        row > bounds[0][1] or 
        col < bounds[1][0] or 
        col > bounds[1][1]):
        return False
    return True

def product(l):
    result = 1
    for x in l:
        result *= x
    return result

with open("11.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
content = [x.split(" ") for x in content]
content = [[int(y) for y in r] for r in content]

#First: Vertical (Down = -1, Up = 1), Second: Horizontal (Left = -1, Right = 1)
directions = [(-1, 0), (0, 1), (-1, 1), (1, 1)]

#Bounds of the 20x20 grid (start counting from 0)
bounds = [[0, 19], [0, 19]]

maximum_product = 0

for row in range(20):
    for col in range(20):
        for direction in directions:
            adjacent_numbers = []
            adjacent_numbers.append(content[row][col])
            position = [row, col]
            #We are looking for 4 adjacent numbers, so take 3 steps from the start
            steps_allowed = 3
            while steps_allowed > 0:
                if step_possible(position, direction, bounds):
                    position[0] += direction[0]
                    position[1] += direction[1]
                    steps_allowed -= 1
                    adjacent_numbers.append(content[position[0]][position[1]])
                else: #Step takes us out of bounds
                    steps_allowed = 0
            p = product(adjacent_numbers)
            if len(adjacent_numbers) == 4 and p > maximum_product:
                maximum_product = p

print(maximum_product)
