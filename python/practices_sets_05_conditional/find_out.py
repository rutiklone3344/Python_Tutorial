#write a prog to fing out whether a given post is talking about "rutik" or not.
post = input("enter a post: ")
if("HARRY" in post):
    find = True
elif("harry" in post):
    find = True
else:
    find = False

if(find):
    print("yes")
else:
    print("no")