with open("13.txt") as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

s = sum(content)

digits = str(s)[:10]

print(digits)
