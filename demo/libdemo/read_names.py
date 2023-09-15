f = open("names.txt", "rt")

for line in f.readlines():
    print(line.strip())

f.close()
