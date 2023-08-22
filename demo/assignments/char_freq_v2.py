st = "how do you do"

chars = []
for c in st:
    if c not in chars:
        print(c, st.count(c))
        chars.append(c)

    