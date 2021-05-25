# loops make it esy for a programmer to tell the computer,which set of instruction to repeat and how!
'''
Types of Loops in python
primarily there are two type of loop in python
1. While loop
2. For loop  
'''
# While loop
'''In while loop condition is check first. If it evaluate to true, the body of the loop is executed otherwise not!
If the loop is entered, the process of ( condition check & execution ) is continued until the condition becomes false '''

i = 0
while i<10:
    print("yes "+str(i))
    i = i+1
print("done")


i = 0
while i<5:
    print("rutik")
    i =i+1
# NOTE if the condition never becomes false, loop leeps getting executed
