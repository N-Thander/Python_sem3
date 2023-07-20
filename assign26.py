# Write a Python program to write names and roll numbers of your friends in a file, then print names of your friends for a given range of roll numbers.

while(1):
    choice = int(input("1: To read student details\n2: To Enter new data\n0: Exit program: "))
    if choice == 1: #read student details
        my_file = open("assign26.txt", "r")
        lower_roll_no = input("Enter the lower index value : ")
        upper_roll_no = input("Enter the upper index value: ")
        name = None 
        for line in my_file:    
            words = line.split(",")
            if lower_roll_no <= words[1].strip() <= upper_roll_no:
                print(words[0])
        my_file.close()
    elif choice == 2: #new details
        my_file = open("assign26.txt", "a")
        my_file.write(input("Enter name,roll no: ")+"\n")
        my_file.close()        
    elif choice == 0: #exit code
        break
    else:
        print("Invalid Input")
    

           




