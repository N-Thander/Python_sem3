# Write a Python program to check a given string contains all unique characters or not.

sentence = input("Enter a string: ")

count = 0
flag = 0

for i in sentence:
    count = count + 1
    for j in sentence[count:]:
        if i == j:
            flag = 1
            break

if flag == 0:
    print("The string contains all unique charecters")
else:
    print("The string does not contain all unique charecters")