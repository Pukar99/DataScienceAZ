#Conditional Statements

age = 18

if (age > 18):
    print("You are eligible to vote")
elif (age == 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
# Other Examples:
color = "red"
if (color == "red"):
    print("stop")
elif (color == "yellow"):
    print("ready to move")
elif (color == "green"):
    print("move")
else:
    print("no signal")
    
# Output: stop

# Example 2:
a = 10
b = 20
if (a > b):
    print("a is greater than b")
elif (a == b):
    print("a is equal to b")
else:
    print("b is greater than a")
    
# Output: b is greater than a

## Nested if-else
a = 10
b = 20
if (a == b):
    print("a is equal to b")
else:
    if (a > b):
        print("a is greater than b")
    else:
        print("b is greater than a")