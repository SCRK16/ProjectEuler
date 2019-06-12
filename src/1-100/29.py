memory = set()

for i in range(2, 101):
    for j in range(2, 101):
        memory.add(i ** j)

print(len(memory))
