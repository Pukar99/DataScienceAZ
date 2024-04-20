#String
str1 = "Hello"
str2 = "World"
print(str1 + str2)
# Output: HelloWorld

#String is a sequence of characters enclosed in single or double quotes. In Python, strings are immutable. This means that once a string is created, it cannot be changed. Strings can be concatenated using the + operator.
str3 = 'Hello'
str4 = """World"""
# here we have used triple quotes to define the string. Triple quotes are used to define multi-line strings.

str1 = " this is a string. \n we are learning python"
print(str1)
# Output:  this is a string.
#          we are learning python

# In the above example, we have used the escape character \n to print the string in a new line.

#Basic Operations on Strings
#1. Concatenation
str1 = "Hello"
str2 = "World"
print(str1 + str2)
# Output: HelloWorld

#2. Repetition
str1 = "Hello"
print(str1*3)
# Output: HelloHelloHello

#3. Slicing
str1 = "Hello"
print(str1[0])
# Output: H

print(str1[1:4])
# Output: ell

#4 Length
str1 = "Hello"
print(len(str1))
# Output: 5

len = len(str1)
print(len)
# Output: 5

#5. Membership
str1 = "Hello"
print('H' in str1)
# Output: True

print('H' not in str1)
# Output: False

#6. Iteration
str1 = "Hello"
for i in str1:
    print(i)
# Output: H
#         e
#         l
#         l
#         o

#6. Indexing
str1 = "Hello"
print(str1[0])
# Output: H
#index starts from 0. So, str1[0] will return the first character of the string.
# Negative indexing is also possible in Python. In negative indexing, the index is counted from the right side. The last element of the string will have an index of -1.
print(str1[-1])
# Output: o
