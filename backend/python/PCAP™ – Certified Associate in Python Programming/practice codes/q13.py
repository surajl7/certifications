class Person:
    def __init__(self, name, age, dob=None):
        self.name = name
        self.age = age
        self.dob = dob

    @classmethod
    def print_name(cls, name):
        print(name)

    def save(self, destination):
        destination.write(str(self))

person = Person('Jose', 26)

person.print_name('Alex')