# Write a Python program to find factors of a given number.

#using loop 
num = int(input("Enter the number: "))

fac = 1

for i in range(1,num+1):
    fac = fac*i

print("The factorial of ", num ," using iterative method is", fac)
