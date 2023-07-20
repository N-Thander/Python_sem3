# Write a Python program to the square root of n random numbers using Math and Random module.

import random, math

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num = 0

n = int(input("Enter a number: "))


nums = []
sq_nums = []

for i in range(n):
    num = random.choice(num_list)
    nums.append(num)
    sq_nums.append(math.sqrt(num))

print(nums)
print(sq_nums)
