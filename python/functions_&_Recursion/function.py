# A function is a group of statements performing a specific task.
# A function can be reused by the programmer in a given program any number of time
def func1():
    print("hello")
# The function can be called any number of times anywhere in the program

# FUNCTION CALL
''' Where we want to call a function , we put the name of the function followed by parenthesis as follo
          func1() '''

def percent(marks):
    p = sum(marks)/400*100
    return p

marks1 = [45,78,86,77]
percentage1 = percent(marks1)

marks2 = [98,89,78,88]
percentage2 = percent(marks2)

print(percentage1 , percentage2)