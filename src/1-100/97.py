base = 2
exponent = 7830457
mult = 28433
add = 1
mod = 10000000000

#Calculate the last 10 digits of mult * base^exponent + 1

number = 1
while exponent >= 1:
    number *= base
    number %= mod #Take last 10 digits
    exponent -= 1

const = number
while mult > 1:
    number += const
    number %= mod
    mult -= 1

number += add
number %= mod

print(number)
