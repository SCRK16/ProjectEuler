upper = 389045

equal = []

for i in range(2, upper):
    digits = [int(x) for x in str(i)]
    powers = [x ** 5 for x in digits]
    s = sum(powers)
    if s == i:
        equal.append(i)

print(equal)
print(sum(equal))

"""
Reasoning for stopping at 389045:
We know that the smallest number with n digits is 10^(n-1)
The maximum sum of fifth powers is n*(9^5)
Calculate 10^(n-1) == n*(9^5)
Result: n = 6.59
10^(6.59 - 1) = 389045
"""
