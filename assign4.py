#  Write a Python program to compute the greatest common divisor of two given positive integers.

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

if num1 > num2:
    small  = num2
else:
    small = num1

for i in range(1, small + 1):
    if(num1 % i == 0) and (num2 % i == 0):
        gcd = i

print("The gcd of", num1 ,"and", num2, "is", gcd)

