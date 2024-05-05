age =25

#nesting
if (age>= 20):
    if (age<30):
        print("Age is between 20 and 30")
    else:
        print("Age is greater than 30")
else:
    print("Age is less than 20")
    
# Output: Age is between 20 and 30

#WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if (num%2 == 0):
    print("Even number")
else: 
    print("Odd number")
    
# Output: Enter a number: 5
#         Odd number

# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >num2):
    if (num1 > num3):
        print(num1, "is the greatest number")
    else:
        print(num3, "is the greatest number")
else:
    if (num2 > num3):
        print(num2, "is the greatest number")
    else:
        print(num3, "is the greatest number")

# Output: Enter first number: 10
#         Enter second number: 20
#         Enter third number: 30

#         30 is the greatest number


# WAP to check if a number is a mulitple of 7 or not.

num = int(input("Enter a number: "))
if (num%7 == 0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")
    
# Output: Enter a number: 14
#         14 is a multiple of 7


