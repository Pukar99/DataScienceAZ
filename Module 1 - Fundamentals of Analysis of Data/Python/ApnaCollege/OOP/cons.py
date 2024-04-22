class Studnet:
    def __init__(self): # Default Constructor
        print("Studnet Database")
    def __init__(self, fullname, marks): # Parameterized Constructor
        self.name = fullname
        self.marks = marks
        print("This is the Student")

s1 = Studnet("Pukar Sharma", 100)
print(s1.name,s1.marks)

