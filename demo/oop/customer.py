class Customer:
    # Constructor
    def __init__(self, name, email=None):
        # Object Attributes
        self.name = name
        self.email = email

    # Methods
    def change_email(self, new_email):
        self.email = new_email

    def get_email(self):
        return self.email


c1 = Customer("Scott", "scott@gmail.com")  # Object
print(c1.get_email())

c2 = Customer("Tom")
c2.change_email("tom@yahoo.com")
