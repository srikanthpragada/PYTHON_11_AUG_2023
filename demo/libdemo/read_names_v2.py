f = open("names.txt", "rt")

while True:
    line = f.readline()
    if line == "":  # EOF
        break
    print(line.strip())

f.close()
