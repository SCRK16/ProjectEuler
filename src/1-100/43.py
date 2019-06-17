from itertools import permutations

def satisfy_property(n):
    n = ''.join(n)
    #Reverse order is faster (-0.7s): Not many numbers are divisible by 17
    if int(n[7:10]) % 17 != 0: 
        return False
    if int(n[6:9]) % 13 != 0:
        return False
    if int(n[5:8]) % 11 != 0:
        return False
    if int(n[4:7]) % 7 != 0:
        return False
    if int(n[3:6]) % 5 != 0:
        return False
    if int(n[2:5]) % 3 != 0:
        return False
    if int(n[1:4]) % 2 != 0:
        return False
    return True

pandigital = "0123456789"
perms = permutations(pandigital)
perms = filter(lambda x: x[0] != '0', perms)
valid = filter(satisfy_property, perms)
result = [int(''.join(x)) for x in valid]

print(sum(result))
