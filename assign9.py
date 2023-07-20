# Write a Python program that takes your name as input, removes all vowels from your name and display the resultant string.

name = input("Enter your name: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

new = ""

for i in name:
    if i  not in vowels:
        new = new+i

print(new)