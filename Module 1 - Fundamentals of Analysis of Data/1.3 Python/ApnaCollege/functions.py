#Function in Python
# Functions are used to group the code and reuse it.

# find the sum of two numerbs using function.
def add(a,b):
    return a+b
print(add(5,4))
# Output: 9

# find the maximum of two numbers using function.
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(5,4))
# Output: 5

sum(3,4) # Output: 7
max(3,4) # Output: 4

# Redudent code is bad. So, we use functions to avoid redudent code.

def sigmoid(x):
    return 1/(1+math.exp(-x))
print(sigmoid(0))
# Output: 0.5

def relu(x):
    return max(0,x)
print(relu(-3))
# Output: 0

def leaky_relu(x):
    return max(0.1*x,x)
print(leaky_relu(-3))
# Output: -0.3

def tanh(x):
    return math.tanh(x)
print(tanh(0))
# Output: 0.0

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))
print(softmax([1,2,3]))
# Output: [0.09003057 0.24472847 0.66524096]
sum(softmax([1,2,3])) # Output: 1.0

def cal_sum(a,b):
    s = a+b
    return s
def cal_sum(a,b,c):
    s = a+b-c
    return s
print(cal_sum(5,4,3))
# Output: 6
print(cal_sum(5,4))
# Output: 9


def print_hello():
    print("Hello")
print_hello()
# Output: Hello

#Q1. Write a function to find the factorial of a number.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
# Output: 120

#Statistics Functions:
#1. Mean
def mean(arr):
    return sum(arr)/len(arr)
print(mean([1,2,3,4,5]))
# Output: 3.0

#2. Median
def median(arr):
    arr.sort()
    n = len(arr)
    if n%2 == 0:
        return (arr[n//2]+arr[n//2-1])/2
    return arr[n//2]
print(median([1,2,3,4,5]))
# Output: 3


def avg_of_3(a,b,c):
    return (a+b+c)/3
print(avg_of_3(1,2,3))
# Output: 2.0


#BUilt-in Functions:
#1. print()
#2. input()
#3. len()
#4. type()
#5. range()
#6. sum()

#User Defined Functions:
# these function are written by the user to perform a specific task.
def calc_prod(a,b):
    print(a*b)
    return a*b
calc_prod(3,4)
# Output: 12


#Practice Questions:
#WAP to print the length of list. list is the paramenter.
def length_of_list(arr):
    return len(arr)
print(length_of_list([1,2,3,4,5]))
# Output: 5

#WAF to print the elemetnst of a list in a simgle line (list in the parameter   )
def print_list(arr):
    for i in arr:
        print(i,end=" ")
print_list([1,2,3,4,5])
# Output: 1 2 3 4 5

#WAF to find the factorial of n . n is the parameter. 
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

#WAF to conver the nepali currency to dollar. n is the parameter.
n=int(input("Enter the amount in Nepali Currency: "))
def convert_to_dollar(n):
    return n/118.5
print(convert_to_dollar(n))
# Output: 0.08438818565400844

