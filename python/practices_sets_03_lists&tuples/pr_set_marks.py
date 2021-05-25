# write a prog to accept marks of 6 students and display them in a sorted manner.
s1 = int(input("Enter marks for student number 1: "))
s2 = int(input("Enter marks for student number 2: "))
s3 = int(input("Enter marks for student number 3: "))
s4 = int(input("Enter marks for student number 4: "))
s5 = int(input("Enter marks for student number 5: "))
s6 = int(input("Enter marks for student number 6: "))

mymarkslist = [s1, s2, s3, s4, s5, s6]
mymarkslist.sort()
print(mymarkslist)