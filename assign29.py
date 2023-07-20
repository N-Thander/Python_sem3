# Write a python program to handle index-out-of-range exception

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = int(input("Enter a value: "))

try:
  print(num_list[num])
except IndexError:
  print("out of range")
except ValueError:
  print("Enter proper value")