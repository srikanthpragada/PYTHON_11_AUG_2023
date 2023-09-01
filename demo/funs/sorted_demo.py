names = ['SQL', 'Python', 'C', 'Java', 'Cobol']

# for n in sorted(names):
#     print(n)

for n in sorted(names, key=len):
    print(n)
