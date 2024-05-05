def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_palindrome(s):
    return s == s[::-1]

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def decimal_to_binary_octal_hex(n):
    return bin(n), oct(n), hex(n)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    while True:
        print("\nMENU:")
        print("1. Calculate Sum of Digits")
        print("2. Check if Number is Prime")
        print("3. Find Greatest Common Divisor (GCD)")
        print("4. Check for Palindrome")
        print("5. Generate Fibonacci Sequence")
        print("6. Sort a List of Integers")
        print("7. Convert Decimal to Binary, Octal, and Hexadecimal")
        print("8. Calculate Factorial")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(num))
        elif choice == '2':
            num = int(input("Enter a number: "))
            print("Is prime:", is_prime(num))
        elif choice == '3':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))
        elif choice == '4':
            s = input("Enter a string: ")
            print("Is palindrome:", is_palindrome(s))
        elif choice == '5':
            n = int(input("Enter number of terms: "))
            print("Fibonacci sequence:", fibonacci(n))
        elif choice == '6':
            lst = [int(x) for x in input("Enter space-separated integers: ").split()]
            bubble_sort(lst)
            print("Sorted list:", lst)
        elif choice == '7':
            num = int(input("Enter a decimal number: "))
            binary, octal, hexadecimal = decimal_to_binary_octal_hex(num)
            print("Binary:", binary)
            print("Octal:", octal)
            print("Hexadecimal:", hexadecimal)
        elif choice == '8':
            num = int(input("Enter a number: "))
            print("Factorial:", factorial(num))
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
