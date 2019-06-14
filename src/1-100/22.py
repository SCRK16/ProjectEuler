import html5lib
import urllib
import sys
sys.path.append("..")
from euler import wordscore

#Read text from link
link = "https://projecteuler.net/project/resources/p022_names.txt"
f = urllib.request.urlopen(link)
text = f.read()
words = str(text)[2:-1].split(",")
words = [x[1:-1] for x in words]

#Sort words
words = sorted(words)

#Calculate scores
result = sum(wordscore(name) * (i+1) for i, name in enumerate(words))

print(result)
