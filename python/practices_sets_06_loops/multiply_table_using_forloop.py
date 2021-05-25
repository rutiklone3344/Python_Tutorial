# write a prog to print multiplication table of a given number using for loop

num = int(input("Enter the number: "))
for i in range(1, 11):
   #print(str(num) + "X" + str(i) + "= " + str(i*num))
    print(f"{num}X{i}={i*num}")

# same in while Loop

num1 = int(input("Enter a number: "))
i = 0
while i<=num1: 
   i += 1
   print(num1,'X',i,'=',num1*i)