# Write a python program to handle exception using raise command.

x = input("Enter a word: ")

try:
    print(int(x))
except:
    raise ValueError("String cannot be changed to integer")  


