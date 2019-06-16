mod = 10000000000 #To get the last 10 digits
result = sum(x ** x for x in range(1, 1001)) % mod
print(result)
