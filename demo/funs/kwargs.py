def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def showall(*args, **kwargs):
    pass


show(a=10, b=20, msg="Hi")
show(name="Abc", age=20)
showall(10, 20, a=10, b=20)
