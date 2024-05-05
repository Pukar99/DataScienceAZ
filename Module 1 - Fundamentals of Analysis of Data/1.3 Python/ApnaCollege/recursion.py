#Recursion is a function calling itself
def show(n):
    print(n)
show(5)
# Output: 5
#         5
#         5
#         5
#         5

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    
show(5)
# Output: 5
#         4
#         3
#         2
#         1

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
# Output: 120
#process of the above code:
# fact(5) = 5*fact(4)
# fact(4) = 4*fact(3)
# fact(3) = 3*fact(2)
# fact(2) = 2*fact(1)
# fact(1) = 1

#Q1. write a recursive function to claculate the sum of first n natural numbers.
def sum (n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))
# Output: 15

#Q2. Write a recursive function toprint all elements in a list.
def print_list(lst):
    if len(lst) == 0:
        return
    print(lst[0])
    print_list(lst[1:])

my_list = [1, 2, 3, 4, 5]
print_list(my_list)
# Output: 1
#         2
#         3
#         4
#         5



    