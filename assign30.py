# Write a python program to handle division-by-zero exception.

num = int(input("Enter a num:"))

try:
    print(num//0)
except ZeroDivisionError:
   print("divison by zero is undefined")