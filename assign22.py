# Write a Python function to find an element from a given list using recursive binary search technique.

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l+(r -1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1
        



num_list = [1, 3, 25, 67, 89, 64, 21, 100, -18, 19]
num_list.sort()
x = int(input("Enter the element to search for: "))

result = binarySearch(num_list, 0, len(num_list)-1, x)

if result != -1:
    print("The element is present at index", result , "after sorting")
else:
    print("The element is not present in array")