def num_to_word(n, numbers, order):
    #Bad implementation of converting a number to a word
    word = ""
    digits = list(reversed([int(x) for x in str(n)]))
    for i in range(len(digits)):
        add = numbers[digits[i]] 
        if digits[i] != 0:
            add += order[i]
        word = add + word
    return word
        

numbers = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine"}
order = {0: "", 1: "ty", 2: "hundredand", 3: "thousand"}

#Because the number is converted to a word in a bad way, mistakes need to be corrected
#See below how -487 is calculated
total = -487

for i in range(1, 1001):
    w = num_to_word(i, numbers, order)
    total += len(w)

print(total)

"""
'and' is done 9 times too many for numbers like:
onehundredand -> onehundred
twohundredand -> twohundred

cont: -27

-----------------------------------
Teens aren't counted correcty: -160

ten: 3
onety: 5
cont: -20

eleven: 6
onetyone: 8:
cont: -20

twelve: 6
onetytwo: 8
cont: -20

thirteen: 8
onetythree: 10
cont: -20

fourteen: 8
onetyfour: 9
cont: -10

fifteen: 7
onetyfive: 9
cont: -20

sixteen: 7
onetysix: 8
cont: -10

seventeen: 9
onetyseven: 10
cont: -10

eighteen: 8
onetyeight: 10
cont: -20

nineteen: 8
onetynine: 9
cont: -10

----------------------------------------------
Multiples or 10 aren't counted correcty: -300 

twenty: 6
twoty: 5
cont: +100

thirty: 6
threety: 7
cont: -100

forty: 5
fourty: 6
cont: -100

fifty: 5
fivety: 6
cont: -100

eighty: 6
eightty: 7
cont: -100

-----------------------------
Total: -27 - 160 - 300 = -487
"""
