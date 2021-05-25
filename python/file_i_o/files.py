# use open function to read the content of a file!

f = open('typecasting.py', 'r') # to open the file we use open()function and in function we have to put file name and mode(typecasting.py, r) r=read mode
data = f.read() # Read files content
print(data)     # print its content
f.close()   # always remmber yo close the file

# NOTE we can also specify the num remmber of character in read()function: f.read(2)  2=Reads first 2 characters
# NOTE We can also use f.readline() function to read only first line at a time

#read first line
data = f.readline()
print(data)
#read second line
data = f.readline
print(data)

'''NOTE Modes of Opening a file
r -> open for reading
w -> open for writing 
a -> open for appending(add)
+ -> open for updating

'rb' will open for read in binary mode
'rt' will open for read in text mode'''

'''
The random Access memory is volatile and all its content are lost once a program terminates
In order to persist the data forever, we use file'''

''' A file is data stored in a storage device A python program can talk to the file by reading content
from it and writing content to it'''

# RAM = Volatile (don't save data is suddely of pc or exit)
# HDD = NON volatile

'Type of Files'
# 1. Text files (.txt, .c etc)
# 2. Binary files (.jpg, ect)

'Python has a lot of function for reading, updating and deleting files'
