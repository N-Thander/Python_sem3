"""
Write a Python program that will show the following operations on tuple.
    a) Creating Tuples,             b) Accessing tuple elements,     c) Concatenation of Tuples,
    d) Deleting a Tuple

"""
n = int(input("Enter the no of elements in the tuple: "))

tup = []

#creating a tuple

for i in range(n):
    val = input("Enter value: ")
    tup.append(val) 

print(type(tup))
tup = tuple(tup)
print(tup)
print(type(tup))

while True:
    c = int(input("Enter 1: To Access a tuple Element\nEnter 2: Concatinate an element\nEnter 3:Delete a tuple\nEnter 4: Display"))
    if c == 1:
        #Access tuple element
    elif c == 2:


