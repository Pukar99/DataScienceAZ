# Type conversion 
# Type conversion is the process of converting the value of one data type (integer, string, float, etc.) to another data type.  

a = 10
b = 20.5

sum = a + b #Type conversion of a to float where float is superior value
print(sum)
# Output: 30.5 This is implicit type conversion

a = "10"
b = 20
print(type(a))
# Output: <class 'str'>
print(type(b))
# Output: <class 'int'>

sum = int(a) + b #Type conversion of a to int where int is superior value
print(sum)
# Output: 30 This is explicit type conversion