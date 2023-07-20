# Write a Python function to find the factorial of a given number using recursion.

def factorial(n):
    while n >= 1:
        if n>1:
            return n*factorial(n-1)
        elif n == 1:
            return 1



num = int(input("Enter number: "))
x = factorial(num)
print("The factorial of", num ,"is: ", x)