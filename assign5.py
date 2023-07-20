"""
Write a Python program to print the following pattern using nested for loop.
*
* *
* * *
* *
*

"""

max = int(input("Enter maximum number of stars in the mid rows: "))

for i in range(max + 1):
    for j in range(i):
        print("* ", end="")
    print("\n")

while(i != 0):
    for k in range(0, i - 1):
        print("* ", end = "")
    print("\n")
    i = i - 1