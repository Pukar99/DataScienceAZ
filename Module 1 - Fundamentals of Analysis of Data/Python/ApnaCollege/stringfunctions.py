str = "i am a coder"
print(str.endswith('coder'))
# Output: True
print(str.endswith('i am'))
# Output: False

#The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.

print(str.capitalize())
# Output: I am a coder
#The capitalize() method returns a string where the first character is upper case.

print(str.count('a'))
# Output: 2
#The count() method returns the number of times a specified value appears in the string.

print(str.find('a'))
# Output: 2
#The find() method finds the first occurrence of the specified value.

print(str.replace('coder', 'developer'))
# Output: i am a developer
#The replace() method replaces a specified phrase with another specified phrase.

print(str.find('am'))
# Output: 2
#The find() method finds the first occurrence of the specified value.

print(str.lower())
# Output: i am a coder

#WAP to input user's first name and print its length
name = input("Enter you  first name : ")
print(len(name))
# Output: 5

#WAP to find the occurrence of 's' in the given string
str = "This is a string"
print(str.count('s'))
# Output: 3
