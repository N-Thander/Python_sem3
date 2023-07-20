# Write a python program to handle exception using multiple except blocks

try:
    my_file = open("Missing.txt", "r")
    print(my_file.read())
    my_file.close()
except FileNotFoundError:
    print("This file does not exit")
except OSError:
    print("Operating system failed")
except:
    print("Something went wrong")


