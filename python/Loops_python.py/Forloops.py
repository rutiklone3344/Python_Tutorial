# FOR LOOPS
''' A for loop is used to iterate through a sequence like ( list, tuple or string).[iterables] '''
 
l = [1, 7, 8] #list print in forloop
for item in l:
    print(item)

# Range Function In Python
''' The range function in python is used to generate a sequence of numbers..
We can also specify the Start,Stop and step-size '''

for i in range(8): #using range fun #(1, 8) if we want to start from 1 or from any number
    print(i)       # i will print upto 7 because 0 to n-1

# range (start, stop, step-size)
#         1      8      2