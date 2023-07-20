# Write a Python program to put Even and Odd numbers in separate lists.

num = int(input("Enter the number of elements in the list: "))

num_list = []

for i in range(num):
    x = int(input("Enter value: "))
    num_list.append(x)

even_list = []
odd_list = []

for j in num_list:
    if j%2 == 0:
        even_list.append(j)
    else:
        odd_list.append(j)

print("The odd number in the list are: ", odd_list)
print("The even number in the list are: ", even_list)