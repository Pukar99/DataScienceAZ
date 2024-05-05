# Class and Instance Attributes in Python

# Class Attributes

class Studnet:
    # Class Attribute
    totalStudents = 20
    classTeacher = "Komal"
    # Instance Attributes
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
s1 = Studnet("Pukar Sharma", 100)
s2 = Studnet("Sagar Sharma", 90)

print(s1.name, s1.marks, s1.totalStudents, s1.classTeacher)
print(s2.name, s2.marks, Studnet.totalStudents, s2.classTeacher)
