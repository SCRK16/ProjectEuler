def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

f = factorial(100)
digits = [int(i) for i in str(f)]
result = sum(digits)
print(result)
