# Write a Python program using a function to print all prime factors of a given number.

def primeFactors(n):

    c = 2
    while(n > 1):
        if(n % c == 0):
            print(c, end = ' ')
            n = n/c
        else:
            c = c + 1

num = int(input("Enter a number: "))
primeFactors(num)