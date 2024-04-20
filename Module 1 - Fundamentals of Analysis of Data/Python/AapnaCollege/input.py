input("Enter your name:")
if input("Enter your name:")=="Pukar":
    print("You are legend")
else:
    print("You are not legend")
# Output: Enter your name:Pukar
#         You are legend
#         Enter your name:Raj
#         You are not legend

# In the above example, the input() function takes input from the user and stores it in the variable name.
input() # always takes input in string format
input(float()) # always takes input in float format
input(int()) # always takes input in integer format
input(bool()) # always takes input in boolean format
input(str()) # always takes input in string format

#Q1. Write a Program to input 2 numbers and print their sum and difference.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = a + b
print(sum)
# Output: Enter first number:10
#         Enter second number:20
#         30

sub = a - b
print(sub)
# Output: Enter first number:10
#         Enter second number:20
#         -10

#Q2. Write a Program to input 2 int nubers a and b print true if a is greater than or equal to b. if not print false.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a>=b:
    print("True")
else:
    print("False")
    
# Output: Enter first number:10
#         Enter second number:20
#         False
#         Enter first number:20
#         Enter second number:10
#         True

