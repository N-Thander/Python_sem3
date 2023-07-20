# Write a Python program to compute sum of digits of a given number.

num = int(input("Enter a number: "))

n = num
sum = 0

while(n != 0):
    sum = sum + (n%10)
    n = n // 10

print("The sum of the digits of the ", num, "is", sum)

