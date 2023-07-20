# Write a Python function that will return the Nth largest element from a list.

m = int(input("Enter the number of elements in the list: "))

num_list = []

for i in range(m):
    x = int(input("Enter value: "))
    num_list.append(x)

N = int(input("Enter the postion till which you want to find the largest value:"))

large = -999

for k in range(0, N+1):
    for j in range(k+1, N+1):
        if num_list[k] > num_list[j]:
            large = num_list[k]

print("The Nth largest number is: ", large)