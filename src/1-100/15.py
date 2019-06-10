def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

result = nCk(40, 20)
print(result)
