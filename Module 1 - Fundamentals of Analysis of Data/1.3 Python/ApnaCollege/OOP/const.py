#Constructor in Python
# __init__ Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.    

class Student:
   
    def __init__(self , fullname, marks):
        self.name = fullname
        self.marks = marks
        print("This is the person ")

s1 = Student("Pukar Sharma", 100)
print(s1.name,s1.marks)
s2 = Student("Pukar KAKA", 200)
print(s2.name)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

