#loops in Python
# Loops are used to repear instructions.
#while loop
count = 1
while count<=5:
    print("Hello")
    count = count + 1
# Output: Hello
#         Hello
#         Hello
#         Hello
#         Hello

# for loop
for i in range(5):
    print("Hello")
# Output: Hello
#         Hello
#         Hello
#         Hello
#         Hello

# for loop with range
for i in range(1,6):
    print("Hello")
# Output: Hello
#         Hello
#         Hello
#         Hello
#         Hello

# for loop with step
for i in range(1,6,2):
    print("Hello")
# Output: Hello
#         Hello
#         Hello

#Print the table of 10 using for loop

n = input("Enter the number: ")
for i in range(1,11):
    print(n,"X",i,"=",n*i)
# Enter the number: 10
# Output: 10 X 1 = 10
#         10 X 2 = 20
#         10 X 3 = 30
#         10 X 4 = 40
#         10 X 5 = 50
#         10 X 6 = 60
#         10 X 7 = 70
#         10 X 8 = 80
#         10 X 9 = 90
#         10 X 10 = 100

nums = [1,4,9,16,25,36,49,64,81,100]
print(nums[1])
# Output: 4

count = len(nums)
for i in range(1,count):
    print(nums[i])
# Output: 4
#         9
#         16
#         25
#         36
#         49
#         64
#         81
#         100




    
