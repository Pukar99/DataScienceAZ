#List
# List is a collection of items. It is a mutable data type. It is defined by square brackets.
# List is a collection which is ordered and changeable. Allows duplicate members.
# List can store the different types of data types i.e. integer, float, string etc.

marks = [45, 78.5, 86, 77, 90]
print(marks)   
print(type(marks))
# Output: [45, 78.5, 86, 77, 90]
#         <class 'list'>
marks[1]
print(marks[1])
# Output: 78.5

print(len(marks))
# Output: 5

student = ['John',33, 11111,"parbat"]
print(student)

# list are mutuable in python.we can change the value 

student[0] = "pukar"
print(student)
# Output: ['pukar', 33, 11111, 'parbat']

#List Methods
list =[1,2,3,4]

list.append(5)

#Output: [1, 2, 3, 4, 5]

list.sort()
#Output: [1, 2, 3, 4, 5]

list.sort(reverse=True)
#Output: [5, 4, 3, 2, 1]

list.reverse()
#Output: [1, 2, 3, 4, 5]

list.insert(1,'apple')
#Output: [1, 'apple', 2, 3, 4, 5]

print(list)
#Output: [1, 'apple', 2, 3, 4, 5]
list.remove(3)
#Output: [1, 'apple', 2, 4, 5]

print(list)