# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
    
s1 = Student("Pukar Sharma", 100, 90, 80)
print(s1.average())
# The output of the above code is:
# Pukar Sharma You get average of 90.0

