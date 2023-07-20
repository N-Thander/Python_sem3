# Write a Python program to count total number of words in a given string.

sentence = input("Enter a string: ")
parts = sentence.split(" ")
count = 0

for i in parts:
    count = count + 1

print("The number of words in parts is: ", count)