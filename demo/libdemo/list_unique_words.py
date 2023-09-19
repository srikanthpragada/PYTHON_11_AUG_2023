import re

with open("story.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for w in sorted(set(words)):
    print(w)

