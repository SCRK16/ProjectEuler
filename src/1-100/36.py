def is_palindrome(l):
    return list(reversed(l)) == l

upper = 1000000
double_palindromes = []

for i in range(upper):
    digits = list(str(i))
    if is_palindrome(digits):
        base2 = list(format(i, 'b'))
        if is_palindrome(base2):
            double_palindromes.append(i)

result = sum(double_palindromes)

print(double_palindromes)
print(result)
