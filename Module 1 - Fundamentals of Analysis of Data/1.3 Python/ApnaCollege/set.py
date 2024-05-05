#Set in Python
# A built in data type that lets us store a collection of data.
# They are unordered, unindexed and do not allow duplicate values.

# Set is defined by curly brackets.


# set = {1,2,3,4,5}
# print(set)
# # Output: {1, 2, 3, 4, 5}

set = {"apple", "banana", "cherry"}
print(set)
# Output: {'apple', 'banana', 'cherry'}

print(type(set))
# Output: <class 'set'>

#list and dictionary are not allowed in set

collection = {1,2,"pukar",3.5}
print(collection)
# Output: {1, 2, 3.5, 'pukar'}
print(type(collection))
# Output: <class 'set'>

# set = {1,2,3,4,5,1,2,3,4,5}
# print(set)
# # Output: {1, 2, 3, 4, 5}
# # Duplicate values are not allowed in set.It reduce the duplicate values.

# set methods

set = {1,2,3,4,5}
set.add("apple")
print(set)
# Output: {1, 2, 3, 4, 5, 'apple'}

set.remove(3)
print(set)
# Output: {1, 2, 4, 5, 'apple'}
set.add((1,2,3))
print(set)
# Output: {1, 2, 4, 5, 'apple', (1, 2, 3)}
set.add([1,2,3])
print(set)
# Output: TypeError: unhashable type: 'list'

set.add({1,2,3})
print(set)
# Output: TypeError: unhashable type: 'set'

set.add({1:2,3:4})
print(set)
# Output: TypeError: unhashable type: 'dict'
set.pop()
print(set)
# Output: {2, 4, 5, 'apple', (1, 2, 3)}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2))
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

set1.intersection(set2)
# Output: {4, 5}


#Practice Questions
#1. Store following word meaning in python dictionary:
#table:"a piece of furtniture", "list of facts and figures"
#cat:"a domestic animal"

dict = {"table":["a piece of furniture","list of facts and figures"], "cat":"a domestic animal"}
print(dict)
# Output: {'table': ['a piece of furniture', 'list of facts and figures'], 'cat': 'a domestic animal'}

# You are given a list of subjects for students. assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#"python", "java", "c", "c++", "java", "python", "c", "java", "c++"

list = ["python", "java", "c", "c++", "java", "python", "c", "java", "c++"]
set= set(list)
print(len(set))
# Output: 4

# WAP to enter marks of 3 subject form the user and store them in a dictionary. Start with an empty dictionary and add none by one . Use subject name as key and marks as value.

dict = {}
subject1 = input("Enter the name of the subject: ")
marks1 = int(input("Enter the marks: "))
dict[subject1] = marks1
subject2 = input("Enter the name of the subject: ")
# marks2 = int(input("Enter the marks: ")
# dict[subject2] = marks2
subject3 = input("Enter the name of the subject: ")
mark3 = int(input("Enter the marks: "))
dict[subject3] = mark3
print(dict)
# Output: Enter the name of the subject: python
#         Enter the marks: 90
#         Enter the name of the subject: java
#         Enter the marks: 80
#         Enter the name of the subject: c++
#         Enter the marks: 70
#         {'python': 90, 'java': 80, 'c++': 70}

#figure out a way to store 9,9.0 as separeate vales int he set. (you can take help of built in data types )
set = {9,9.0}
print(set)
# Output: {9}
# 9 and 9.0 are same value so it will be stored as a single value in the set.

set = {9,9.1,8,8.0}
print(set)
# Output: {8, 9, 9.1}
# 8 and 8.0 are same value so it will be stored as a single value in the set. 9 and 9.1 are different values so it will be stored as a separate value in the set.