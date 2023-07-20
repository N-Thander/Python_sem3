# Write a Python program to find the second largest number from a given list.

n = int(input("Enter the number of elements in the list: "))

num_list = []

for i in range(n):
    x = int(input("Enter value: "))
    num_list.append(x)

num_list.sort()
num_list.reverse()

for i in num_list:
    if num_list[0] > i:
        break

print("The second largest number in the list is: ", i)
    