# Write a Python program for writing and reading in file.


while(1):
    user = int(input("What function do you want to perform:\n1: Read a file\n2: Write a file\n0: To exit the program: "))
    if user == 1:
        print("Read a file")
        my_file = open("assign25.txt","r")
        print(my_file.read())
        my_file.close()
    elif user == 2:
        print("Write a file")
        my_file = open("assign25.txt","w")
        my_file.write(input("Enter text: "))
        my_file.close()
    elif user == 0:
        print("Exit Program")
        break
    else:
        print("INVALID INPUT")