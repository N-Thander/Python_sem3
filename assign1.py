# Write a Python program to find the maximum number from three given numbers.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

max = num1

if num1 > num2 and num1 > num3:
    max = num1
elif  num2 > num1 and num2 > num3:
    max = num2
elif num3 > num1 and num3 > num2:
    max = num3
elif num1 == num2 == num3:
    max = num1

print(max)