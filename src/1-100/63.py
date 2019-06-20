from itertools import count

result = []
for base in range(1, 10): #Bases 10 and above will never produce a 
    for power in count(1):
        n = base ** power
        length = len(str(n))
        if length == power:
            result.append(n)
        elif length < power: #Length can never catch up again
            break            #since base*n < 10*n -> length(base*n) < power+1

print(len(result))
