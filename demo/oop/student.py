class AmountError(Exception):
    def __init__(self, amount):
        super().__init__(f"Invalid amount : {amount}. It must be > 0")

class Student:
    # static or class attributes
    javafee = 10000
    pythonfee = 15000

    @staticmethod
    def get_total_fee(course):
        return Student.javafee if course == 'java' else Student.pythonfee

    def __init__(self, name, course, feepaid = 0):
        # Object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        if amount <= 0:
            raise AmountError(amount)

        if amount > self.get_due():
            raise ValueError("Excess amount being paid!")

        self.feepaid += amount

    def get_due(self):
        return self.total_fee() - self.feepaid

    def total_fee(self):
        return Student.javafee if self.course == 'java' else Student.pythonfee

    def change_course(self, newcourse):
        self.course = newcourse


print(Student.get_total_fee('python'))

s1 = Student("Larry", "java")
s1.payment(-5000)
s1.payment(2000)
print(s1.get_due())
