# FOR LOOPS WITH ELSE

# An optional else can be used with a for loop if the code is to be executed when the loop exhaust.
#EXAMPLE
 
for i in range(10): # it will print up to 9 becoz 0 to n-1
    print(i)   # i will print 1 to 9
else:
    print("now the condition is false") 


# THE BREAK STATEMENT
# Break is used to come out of the loop when encountered.
# It instruct the program to - Exit the loop now

for i in range(10):
    print(i)
    if i == 5: # when i is equal to 5 it will break the loop
        break  # use to exit the loop 


# THE CONTINUE STATEMENT
# Contiune is use to stop the current iteration of the loop and continue with next one
# It instruct the program to "skip" this iteration

for i in range(10):
    if i == 5:
        continue # it will skip the 5 and contiune print from 6
    print(i)


# PASS STATEMENT
# Pass is a null statement in python
# It instruct to  " DO NOTHING"

i = 4
if i>0:
    pass # null 