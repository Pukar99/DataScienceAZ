#Methods 
# Methods are functions that belong to objects.

class Student:
    college = "ABC" # Class Variable
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def hello(self):
        print("Welcome", self.name, "You get",self.marks, "from",Student.college)

s1 = Student("Pukar Sharma", 100)
s1.hello()