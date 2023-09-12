class A:
    def process(self):
        print("Process in A")


class B:
    def task(self):
        print("Task in B")


class C(A, B):
    pass


obj = C()
obj.process()
obj.task()
