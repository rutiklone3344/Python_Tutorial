# Write a python function to print multiplaction take of a given number 

num = int(input("Enter the number: "))
# using for loop to iterate multiplication 10 times
print("Multiplication Table of: ")
for i in range(1,11):
    print(num,'X',i,'=',num*i)