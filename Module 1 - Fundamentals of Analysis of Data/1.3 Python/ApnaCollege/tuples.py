#Tuples in Python
# A built in data types that lets us create immutable ordered sequence of elements
tuple = (1,2,3,4,5)
print(type(tuple))
# Output: <class 'tuple'>

print(tuple[1])
# Output: 2

# tuple[1] = 5
# Output: TypeError: 'tuple' object does not support item assignment

tup =()
print(tup)
# Output: ()

tup = (1)
print(tup)
# Output: 1
print(type(tup))
# Output: <class 'int'>

tup = (1,)
print(tup)
# Output: (1,)
print(type(tup))
# Output: <class 'tuple'>

tup = (1,2,3,4,5)
print(tup[:3])
# Output: (1, 2, 3)

tup.index(1)
# Output: 0

tup.count(1)
# Output: 1

tup.index(2)
# Output: 1

# WAP to ask the user to enter names of their 3 favourite movies and store them in a list.

movie1 = input("Enter the name of your favourite movie: ")
movie2 = input("Enter the name of your favourite movie: ")
movie3 = input("Enter the name of your favourite movie: ")
list = [movie1, movie2, movie3]
print(list)
# Output: Enter the name of your favourite movie: Titanic
#         Enter the name of your favourite movie: Inception
#         Enter the name of your favourite movie: Avatar
#         ['Titanic', 'Inception', 'Avatar']


#WAP to check if a list contains a palindrome of elements. (hint use copy() method)

list = [1,2,3,4,5,4,3,2,1]
list2 = list.copy()
list2.reverse()
if list == list2:
    print("Palindrome")
else:
    print("Not a palindrome")
# Output: Palindrome

#WAP to count the number of student with the "A" grade inthe following tuple.
#['A','B','C','A','D','A','B','A','C]

tup = ('A','B','C','A','D','A','B','A','C')
print(tup.count('A'))
# Output: 4

#WAP to remove the duplicate elements from the following tuple.
#(1,2,3,4,5,4,3,2,1)
tuple = (1,2,3,4,5,4,3,2,1)
print(set(tuple))
# Output: {1, 2, 3, 4, 5}

# Store the above value in a list and sort them from "A to D"
# ['A','B','C','A','D','A','B','A','C]

tup= ['A','B','C','A','D','A','B','A','C']
tup.sort()
print(tup)
# Output: ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
