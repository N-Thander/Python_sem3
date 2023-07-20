# Write a Python program to find factors of a given number.

#using recrsive 

def fac(num):
    x = num
    if num > 1:
        x = x * fac(x - 1)
    elif x == 1 or x == 0:
        return 1

    return x

num = int(input("Enter the number: "))

val = fac(num)

print("The factorial of", num, "using recusive method is", val)
