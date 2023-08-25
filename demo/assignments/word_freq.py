st = "how do you do now how did you do yesterday"

words = st.split(" ")
for w in set(words):
    print(w, words.count(w))



    