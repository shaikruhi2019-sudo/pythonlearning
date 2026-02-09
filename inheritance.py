class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def show_details(self):
        print("Branch:", self.branch)


s1 = Student("Ruhi", "CSE")
s1.show_name()
s1.show_details()
