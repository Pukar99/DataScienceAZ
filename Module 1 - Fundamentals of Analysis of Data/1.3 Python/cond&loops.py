#1.	 Write Python code using if-else statements to control the flow of execution based on specific conditions
#code:
# if-else statements
x = 18
if x > 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#2. Write Python code using if-elif-else statements to control the flow of execution based on multiple conditions
    #code:
    # if-elif-else statements
    x = 18
    if x > 18:
        print("you are eligible to vote")
    elif x == 18:
        print("you just turned 18, congratulations!")
    else:
        print("you are not eligible to vote")

    #3. Write Python code using a for loop to iterate over a sequence of elements
    #code:
    # for loop
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    #4. Write Python code using a while loop to repeatedly execute a block of code until a condition is met
    #code:
    # while loop
    count = 0
    while count < 5:
        print("Count:", count)
        count += 1

    #5. Write Python code using a break statement to exit a loop prematurely
    #code:
    # break statement
    count = 0
    while count < 5:
        print("Count:", count)
        if count == 3:
            break
        count += 1
        