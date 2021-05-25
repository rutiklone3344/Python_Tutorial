# Write a program to convert inch into cm

def convert(cm):
    return cm * 2.54

length = int(input("Enter the length value: "))
f = convert(length)
print("converted value of inchs into cm " + str(f))