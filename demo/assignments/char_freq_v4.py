st = "how are you doing today"

chars = {}
for c in sorted(set(st)):
    chars[c] = st.count(c)

print(chars)




    