def wish(msg, name):
    print(msg, name)


wish('Hi', "Scott")  # Positional
wish(name='Joe', msg="Hello")  # Keyword
wish("Hello", name="Scott")  # Mixed
