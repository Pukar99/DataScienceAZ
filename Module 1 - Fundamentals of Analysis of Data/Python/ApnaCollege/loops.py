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


for i in range (len(nums)):
    print(nums[i])
# Output: 1
#         4
#         9
#         16
#         25
#         36
#         49
#         64
#         81
#         100

ind = 0
while ind < len(nums):
    print(nums[ind])
    ind += 1
# Output: 1
#         4
#         9
#         16
#         25
#         36
#         49
#         64
#         81
#         100
i = 0
while i <=5:
    if (i==3):
        i += 1
        continue
    print(i)
    i += 1

# Output: 0
#         1
#         2
#         4
#         5

#for loops in python
# Loops are used for sequential traversal. Fot tranversing list, string, tuple etc

list = [1,2]
for el in list:
    print(el)
# Output: 1
#         2

# here we get elements el from list and print it.

veg =[ "potato", "tomato", "onion"]
for el in veg:
    print(el[1])
# Output: o
#         o
#         n


tup = (1,2,3)
for num in tup:
    print(num)
# Output: 1
#         2
#         3

    
str = "hello"
for char in str:
    print(char)
# Output: h
#         e
#         l
#         l
#         o
str = "hello"
for char in str:
    print(char)
else:
    print("End of string")
# Output: h
#         e
#         l
#         l
#         o
#         End of string


# Q1 Print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
# Answer:
list = [1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)
# Output: 1
#         4
#         9
#         16
#         25
#         36
#         49
#         64
#         81
#         100

# SEarch for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)
# Answer:
tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
for num in tup:
    if num ==x:
        print("Number found")
        break
else:
    print("Number not found")
# Output: Number found

#finding index as well

idx = 0
for num in tup:
    if num == x:
        print("Number found at index",idx)
        break
    idx += 1
else:
    print("Number not found")
    
# Output: Number found at index 5

# Range function in python
# range(start, stop, step)
# start: starting number of the sequence
# stop: Generate numbers up to this number
# step: difference between each number in the sequence
# range(5) = 0,1,2,3,4

for i in range(5):
    print(i)
# Output: 0
#         1
#         2
#         3
#         4

for i in range(1,6):
    print(i)
# Output: 1
#         2
#         3
#         4
#         5

for i in range (1,6,2):
    print(i)
# Output: 1
#         3
#         5

seq = range(5)
print(seq)
# Output: range(0,5)
print(list(seq))
# Output: [0,1,2,3,4]
for i in seq:
    print(i)
# Output: 0
#         1
#         2
#         3
#         4
for i in range (10):
    print(i)
    #here the range(stop) is given so it will start from 0 and go upto 9
    # if the range (start, stop) is given then it will start from start and go upto stop-1
    # if the range (start, stop, step) is given then it will start from start and go upto stop-1 with step difference
# Output: 0
#         1
#         2
#         3
#         4
#         5
