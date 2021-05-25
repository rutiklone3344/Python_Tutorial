# Write a recursive function to calculate the sum of first n natural numbers
#1 + 2 + 3 + 4..........n

def recur_sum(n):
    if n <= 1: 
        return n
    else:
        return n + recur_sum(n-1)
  
num = int(input("Enter the number: "))
if num < 0:
    print("Enter A Positive Number")
else:
    print("The Sum is", recur_sum(num))