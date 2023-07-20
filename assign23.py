# Write a Python program to find the max of two given numbers using lamda function with if-else statement.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

y = lambda num1, num2: num1 if num1>num2 else num2

print(y(num1, num2))

