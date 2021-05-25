greeting = "good morning, "
name = "ruu"

c = greeting + name #concatenatng two strings
print(c)
# a string n python can be sliced for gettin a part of the string

name = "rutik"
print(name[2])

print(name[0:4])
'''the index in a string starts from 0 to (length -1)
in python . In order to slice a string we use the following syntax.'''

#print(name[1:4])
#print(name[:4])  #is same as name[0:4]
#print(name[1:])  #is same as name[1:5]
c = name[-4:-1] #is same as name [1:4]
print(c)
''' negative indices: negative indices can also be used as
 shown in the figure -1 correspond to the (length-1), -2 to (length -2)'''

#--------------------------------------------------------
# Slicing With Skip Value #
name = "rutikisgood"
d = name[0::3]
print(d)