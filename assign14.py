# Write a Python program to remove duplicates elements from a given list.

n = int(input("Enter the number of elements in the list: "))

num = []

for i in range(n):
    x = int(input("Enter the value: "))
    num.append(x)

rem_duplicate = []

for k in num:
    if k not in rem_duplicate:
        rem_duplicate.append(k)

print("The original list is: ", num)
print("The list after removal of the original list is: ", rem_duplicate)
    
