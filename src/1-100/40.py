from itertools import count

wanted = [1, 10, 100, 1000, 10000, 100000, 1000000]

constant = []
for i in count():
    digits = [int(x) for x in str(i)]
    constant.extend(digits)
    if len(constant) > wanted[-1]:
        break

result = 1
for w in wanted:
    result *= constant[w]

print(result)
