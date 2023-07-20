# Write a Python program to convert a given decimal number into corresponding binary number.

def dec2bin(num):
    ans = ""
    if num == 0:
        return 0
    while num:
        ans += str(num&1)
        num = num >> 1

    ans = ans[::-1]

    return ans 


num = int(input("Enter the decimal number: "))

x = dec2bin(num)
print("The binary value of the decimal number", num, "is", x)