# Write a Python program that accepts a string from the user and check whether it is a palindrome or not.

x = input("Enter a string: ")

y = x[::-1]

if x == y:
    print("The string is a palindrom")
else:
    print("They are not a palindrom")