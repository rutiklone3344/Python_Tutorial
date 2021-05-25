#write a prog to find whether a given username contains less than 10 characters or not

name = input("enter a name: ")
if(len(name)<10):
    print("less than 10 characters")
else:
    print("not less than 10 characters")