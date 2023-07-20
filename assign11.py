# Write a Python that accepts your full name and display in short form. (Hints: Input is “Sachin Ramesh Tendulkar” and output is “S. R. Tendulkar”.)

name = input("Enter your name: ")

parts = name.split(" ")

#print(parts)
for i in parts:
    if i != parts[-1]:
        print(i[0]+". ", end="")
    else:
        print(i)