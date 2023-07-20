# Write a Python program to convert a time from 12 hour to 24 hour format. (Hints: Input is 05:23 PM and output is 17:23 )

time = input("Enter the time in the format (HH:MM:AM/PM): ")

seperated = time.split(":")

#print(seperated)

if int(seperated[0]) > 12:
    print("invalid input")
elif seperated[2] == "AM" and int(seperated[0]) == 12:
    print("The time in the 24hr format is: ",  "00" + ":" + seperated[1])
elif seperated[2] == "AM":
    print("The time in 24hr format is: ", seperated[0]+ ":" +seperated[1])
elif seperated[2] == "PM" and int(seperated[0]) != 12:
    print("The time in 24hr format is: ", str(12+int(seperated[0]))+ ":" + seperated[1])


